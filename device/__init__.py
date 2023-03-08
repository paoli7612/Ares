from . import template
from random import randint
import os, subprocess

class Ares:
    def __init__(self):
        pass

    @staticmethod
    def form(form):
        source = template.build(form['setup'], form['loop'])
        Ares.newProject(source)

    def newProject(source, name=None):
        os.chdir('/home/alberto/Repository/Ares/device')
        with open('./src/main.cpp', 'w') as f:
            f.write(source)
        print("platformio run --environment esp1")
        subprocess.run('platformio run -t upload', shell=True)



