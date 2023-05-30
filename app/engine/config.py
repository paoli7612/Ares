host = 'http://localhost:8000'
app = 'engine'
base_url = host + '/' + app + '/'

def next(room):
    return base_url + 'next/' + str(room)

def finish(id):
    return base_url + 'finish/' + str(id) 