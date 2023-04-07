from wtforms_alchemy import ModelForm
from .models import *

class MyModelForm(ModelForm):
    def __init__(self, action, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)
        self.action = action
        if action == 'new':
            self.icon = 'plus'
        elif action == 'edit':
            self.icon = 'edit'
    
    def get_title(self):
        return self.action + " " + self._name 

    title = property(get_title)

class PlatformForm(MyModelForm):
    _name = 'Platform'
    class Meta:
        model = Platform

class RoomForm(MyModelForm):
    _name = 'Room'
    class Meta:
        model = Room

class ExperimentForm(MyModelForm):
    _name = 'Experiment'
    class Meta:
        model = Experiment
        exclude = ('minutes', )
