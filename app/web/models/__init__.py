import sqlalchemy, enum, os
from flask import flash
from web import db

def existImg(img, folder):
    if os.path.exists("app/web/static/%s/%s" %(folder, img)):
        return img
    else:
        flash("image (static/%s/%s) not found. Rplaced my (none.png)" %(folder, img), category='yellow')
        return 'none.png'

def tr(*values):
    txt = "<tr>"
    for value in values:
        txt += "<td>%s</td>" % str(value)
    return txt + "</tr>"

sourceMount = db.Table('source_mount',
    db.Column('id', db.Integer),
    db.Column('source_id', db.Integer, db.ForeignKey('source.id', ondelete="CASCADE")),
    db.Column('mount_id', db.Integer, db.ForeignKey('mount.id', ondelete="CASCADE"))
)

from .ElementQ import ElementQ
from .Experiment import Experiment
from .Mount import Mount
from .Platform import Platform
from .Room import Room
from .Source import Source
from .User import User, UserStatus