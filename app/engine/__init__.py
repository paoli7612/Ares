import time, requests, logging
from engine import config

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Engine:
    def __init__(self):
        self.loop()

    def get_next(self):
        r = requests.get(config.next())
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
        logging.info(response)
        time.sleep(2)
        self.finish(response)

    def finish(self, response):
        logging.info('__FINISH__')
        experiment_id = response['experiment_id']
        print(self.get_finish(experiment_id))
        time.sleep(1)

    def wait(self, response):
        logging.debug("Nessun esperimento in coda. Aspetto 2 secondi")
        time.sleep(2)







a = """
    def __init__(self):
        self.run()

    def experiment(self, e):
        logging.info('Inizio esperimento. experiment_id: %d' %(e['experiment_id']))
        minutes = e['minutes']
        for m in minutes:
            print("Sto eseguendo", e['name'])
            time.sleep(m)
        time.sleep(minutes)
        self.finish(e)

    def start(self):
        response = requests.get(config.next()).json()
        if response['status'] == 'experiment':
            self.experiment(response)
        elif response['status'] == 'wait':
            print("Nessun esperimento da runnare. riprovo tra poco")
            time.sleep(5)

    def finish(self, e):
        logging.info('Inizio esperimento. experiment_id: %d' %(e['experiment_id']))
        requests.get(config.finish(e['experiment_id'])).json()

    def run(self):
        e = None
        while True:
            s = input("1) next\n2)finish\n3)exit")
            if s == '1':
                e = self.start()
            elif s == '2':
                e = {'experiment_id': 2}
                self.finish(e)
            else:
                break

        self.running = True
        while self.running == True:
            try:
                response = requests.get(config.next()).json()
                if response['status'] == 'experiment':
                    self.experiment(response)
                elif response['status'] == 'wait':
                    print("Nessun esperimento da runnare. riprovo tra poco")
                    time.sleep(5)
                raise Exception('campo \'status\' non valido')
            except Exception as e:
                logging.error(e)
                time.sleep(2)
"""
