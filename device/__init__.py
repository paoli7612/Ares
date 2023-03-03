from . import template
from random import randint
import os

class Ares:
    def __init__(self):
        pass

    @staticmethod
    def form(form):
        source = template.build(form['setup'], form['loop'])
        Ares.newProject(source)

    def newProject(source, name=None):
        os.chdir('/home/alberto/Repository/Ares/ares')
        if name is None:
            name = "%d.experiment" % randint(1, 100000)
        with open('./src/main.cpp', 'w') as f:
            f.write(source)
        os.system("pwd")
        print("platformio run --environment esp1")
        os.system('platformio run --environment esp1')



