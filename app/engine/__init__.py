import time, requests

class Engine:
    def __init__(self):
        self.run()

    def experiment(self, e):
        minutes = e['minutes']
        print('aspetto', minutes, 'secondi')
        time.sleep(minutes)
        self.finish(e)

    def finish(self, e):
        print("RISULTATI")
        print("VADO SU", 'http://localhost:8000/engine/finish/' + e['id'])
        requests.get('http://localhost:8000/engine/finish/' + e['id']).json()
    def run(self):
        self.running = True
        while self.running == True:
            try:
                response = requests.get('http://localhost:8000/engine/next').json()
                if response['status'] == 'experiment':
                    self.experiment(response)
                elif response['status'] == 'wait':
                    print("Nessun esperimento da runnare. riprovo tra poco")
                    time.sleep(5)
            except:
                print("Fallito")
                time.sleep(2)
            print("VADO SU", 'http://localhost:8000/engine/next')
