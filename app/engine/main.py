import time, requests

class Boss:
    def __init__(self):
        pass

    def run(self):
        self.running = True
        while self.running == True:
            print(requests.get('http://localhost:8000/engine/next').json())
            time.sleep(3)

if __name__ == '__main__':
    b = Boss()
    b.run()