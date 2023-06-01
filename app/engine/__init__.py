import time, requests, logging, os, subprocess
from engine import config, email

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Engine:
    def __init__(self, room, id):
        self.room = room
        self.id_room = id
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path_project = os.path.join(self.path, self.room)
        self.path_src = os.path.join(self.path_project, 'src')
        self.path_log = os.path.join(self.path_project, 'log')
        self.path_main = os.path.join(self.path_src, 'main.cpp')

        os.chdir(self.path_project)
        self.loop()

    def get_next(self):
        r = requests.get(config.next(self.id_room))
        return r.json()
    
    def get_finish(self, id):
        r = requests.get(config.finish(id))
        return r.json()

    def loop(self):
        self.running = True
        while self.running:
            response = self.get_next()
            if response['status'] == 'experiment':
                self.experiment(response)
            elif response['status'] == 'wait':
                self.wait(response)

    def experiment(self, response):
        logging.info('Start experiment [%s]' %str(response['experiment_id']))
        try:
            import shutil
            shutil.rmtree(self.path_log)
            os.mkdir(self.path_log)
        except: pass
        
        for source in response['sources']:
            # main.cpp = source['content']
            with open(self.path_main, 'w') as f:
                f.write(source['content'])

            # platformio run -e source['mount_name'] --target upload     
            for mount_name in source['mounts']:
                attempts = 4
                while attempts and not os.path.exists(os.path.join('log', mount_name)):
                    subprocess.run('platformio run -e %s -t upload && echo ok > log/%s.txt' %(mount_name, mount_name), shell=True)
                    attempts -= 1
            
        
        time.sleep(response['minutes'] * 60)
        email.send_confirm(response['email'], response['experiment_id'])
        self.finish(response)

    def finish(self, response):
        logging.info('Finish experiment [%s]' %str(response['experiment_id']))
        experiment_id = response['experiment_id']
        self.get_finish(experiment_id)

    def wait(self, response):
        logging.debug("I'm waiting")
        time.sleep(2)

