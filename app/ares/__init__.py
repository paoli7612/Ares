from . import template
import os, re, subprocess

class MyPIO:
    def test(esp, control_file):
        os.system('platformio run -e test' + esp + ' && echo "OK" > ' + control_file)
        
    def test32(control_file):
        MyPIO.test('32', control_file)

    def test8266(control_file):
        MyPIO.test('8266', control_file)

class Ares:
    source_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources')
    platformio_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'platformio')
    platformio_src_folder = os.path.join(platformio_folder, 'src')
    control_file = 'asd.control'
    
    @staticmethod
    def path(id):
        return os.path.join(Ares.source_folder, "%d.source" % id)
    
    @staticmethod
    def read(path):
        return open(path, 'r').read()

    @staticmethod
    def newFile(source, id):
        path = Ares.path(id)
        with open(path, 'w') as file:
            file.write(source)
        return path

    @staticmethod
    def parse(form, esp):
        print("BUILD " , esp)
        return template.build(form['setup'], form['loop'], esp)

    @staticmethod
    def newProject(source):
        with open('./src/main.cpp', 'w') as f:
            f.write(source)
        print("platformio run --environment esp1")
        subprocess.run('platformio run -t upload', shell=True)

    @staticmethod
    def randomId():
        used = list()
        for fname in os.listdir(Ares.source_folder):
            n = re.findall(r'\d+', fname)
            if n:
                used.append(int(n[0]))
        id = 1
        while id in used:
            id += 1
        return id

    @staticmethod
    def test(form):
        source = Ares.parse(form, form['esp'])
        id = Ares.randomId()
        path = Ares.newFile(source, id)
        return Ares.control(path, form['esp'])
    
    @staticmethod
    def control(path, esp):
        esp = esp[3:]
        fname = path.split("/")[-1]
        os.rename(path, os.path.join(Ares.platformio_src_folder, 'main.cpp'))
        os.chdir(Ares.platformio_folder)
        try:
            os.remove(Ares.control_file)
        except:
            print("amen")
        MyPIO.test(esp, Ares.control_file)
        return os.path.exists(Ares.control_file)