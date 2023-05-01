from . import template
import os, re, subprocess, shutil

class MyPIO:
    def test(esp, control_file):
        os.system('platformio run -e test' + esp + ' && echo "OK" > ' + control_file)

class Ares:
    """
        -- ares
            -- inis
                files ini delle rooms
            -- sources
                sorgenti caricati dagli utenti chiamati per id.source
            -- platormio
                cartella dove mettiamo i file da lavorare con platformio
                -- platformio.ini
                    file di configurazione dei mount della room
            -- src
                cartella contenente i file da caricare sulle platform
                -- main.cpp
                    file principale da caricare
    """
    class Path:
        """
            Contain all stati path required from this app
            - platformio.ini file
            - src folder
            - sources folder
            - init folder
        """
        ares = os.path.dirname(__file__)
        inis = os.path.join(ares, 'inis')
        sources = os.path.join(ares, 'sources')
        platformio = os.path.join(ares, 'platformio')
        platformioFile = os.path.join(platformio, 'platformio.ini')
        platformioMain = os.path.join(platformio, 'src/main.cpp')

    class Ini:
        def path(id):
            return os.path.join(Ares.Path.inis, '%d.ini'%id)
        def use(id):
            path = Ares.Ini.path(id)
            shutil.copy(path, Ares.Path.platformioFile)
        def build(id, content):
            with open(Ares.Ini.path(id), 'w') as f:
                f.write(content)

    class Source:
        def path(id):
            return os.path.join(Ares.pathSources, "%d.source"%id)
        def use(id):
            path = Ares.Source.path(id)
            shutil.copy(path, Ares.pathPlatformioMain)

        def load(sourceId, mountName):
            print("Carico il file ", sourceId, " sul mountName ", mountName)

        def build(id, content):
            with open(Ares.Source.path(id), 'w') as f:
                f.write(content)

        def buildByForm(id, form):
            content = template.build(form['setup'], form['loop'], form['platform'])
            Ares.Source.build(id, content)

    @staticmethod
    def test(form):
        id = Ares.randomId()
        Ares.Source.buildByForm(id, form)
        Ares.Source.use(id)

    def read(path):
        return open(path, 'r').read()
    
    @staticmethod
    def testbed(room, mounts):
        Ares.Ini.use(room)
    
    @staticmethod
    def parse(form, esp):
        print("BUILD " , esp)
        return template.build(form['setup'], form['loop'], form['esp'])
    
    #########################################


    @staticmethod
    def newProject(source):
        with open('./src/main.cpp', 'w') as f:
            f.write(source)
        print("platformio run --environment esp1")
        subprocess.run('platformio run -t upload', shell=True)

    @staticmethod
    def randomId():
        used = list()
        for fname in os.listdir(Ares.pathSources):
            n = re.findall(r'\d+', fname)
            if n:
                used.append(int(n[0]))
        id = 1
        while id in used:
            id += 1
        return id
    
    @staticmethod
    def control(path, esp):
        esp = esp[3:]
        fname = path.split("/")[-1]
        os.rename(path, os.path.join(Ares.platformio_src_folder, 'main.cpp'))
        os.chdir(Ares.platformio_folder)
        if os.path.exists(Ares.control_file):
            os.remove(Ares.control_file)
        MyPIO.test(esp, Ares.control_file)
        return os.path.exists(Ares.control_file)
    
if __name__ == '__main__':
    Ares.Ini.build()
    Ares.Source.buildByForm(1, {
        'setup': "int a = 10;",
        'loop': "int b = 20;",
        'platform': 'esp8266'
    })

    Ares.testbed(room=1, mounts=[1, 1, None, 1])