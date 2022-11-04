import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
def get_hit_count():
    retries = 5
    while True:
        return cache.incr('hits')
            
@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hola! Este sitio se ha visitado {} veces.\n'.format(count)