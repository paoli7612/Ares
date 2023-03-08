from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from device import Ares
from .models import Experiment

comunity = Blueprint('comunity', __name__)

@comunity.route('/')
def welcome():
    return render_template('comunity/home.html')

@comunity.route('/forum')
def forum():
    return render_template('comunity/forum.html')