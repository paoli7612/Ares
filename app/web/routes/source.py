from flask import Blueprint, render_template, request, redirect, flash, url_for, abort
from flask_login import current_user
from werkzeug.utils import secure_filename

from web.models import Source
from web import db

source = Blueprint('source', __name__)

def exist_mine(id):
    """
        If there aren't source with this id raise 404
        If it is not your source raise 403
    """
    s = Source.query.get(id)
    if not s: # source exist
        abort(404)
    if not s.experiment.user == current_user: # source is mine
        abort(403)
    return s

@source.route('/<int:id>')
def single(id):
    """
        /source/<int:id>
    """
    s = exist_mine(id)
    return render_template('source/single.html',
                           source=s,
                           text=s.content(),
                           experiment_id=s.experiment_id
    )

@source.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    """
        /source/delete/<int:id>
    """
    s = exist_mine(id)
    if request.method == 'POST':
        experiment_id = s.experiment_id
        Source.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('experiment.single', id=experiment_id))
    return render_template('pages/ask.html', title='Deleting experiment', question='Are you sure?', icon='trash')

# __POST_________________________________________________________________________________________________________________________
"""@source.route("/save", methods=['POST'])
def save():
    print("it's me mario")
    for field in request.form:
        if "devices" in field:
            source = Source.query.get(field.split('_')[0])
            source.devices = request.form[field]
            db.session.add(source)
    db.session.commit()
    return redirect(request.referrer)
"""