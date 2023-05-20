import time, requests

class Engine:
    def __init__(self):
        self.run()

    def experiment(self, e):
        minutes = e['minutes']
        print('aspetto', minutes, 'secondi')
        time.sleep(minutes)

    def run(self):
        self.running = True
        while self.running == True:
            response = requests.get('http://localhost:8000/engine/next').json()
            if response['status'] == 'experiment':
                self.experiment(response)
            elif response['status'] == 'wait':
                print("Nessun esperimento da runnare. riprovo tra poco")
                time.sleep(5)
