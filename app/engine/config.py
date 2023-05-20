host = 'http://localhost:8000'
app = 'engine'
base_url = host + '/' + app + '/'

def next():
    return base_url + 'next'

def finish(id):
    return base_url + 'finish/' + str(id) 