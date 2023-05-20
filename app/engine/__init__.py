import time, requests, logging
from engine import config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Engine:
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

    def finish(self, e):
        logging.info('Inizio esperimento. experiment_id: %d' %(e['experiment_id']))
        requests.get(config.finish(e['experiment_id'])).json()

    def run(self):
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
