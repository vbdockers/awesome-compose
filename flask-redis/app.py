from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    
    donkey_art = """
<pre>
     |\    /|
     | \__/ |
     |      |
     |      |  ___
     |   __/  |   \\
     |  |      \\   \\
     |  |       |___|
</pre>
"""
    return "I am playing with Docker compose.<br>" + \
           "This webpage has been viewed " + counter + " time(s)<br>" + \
           donkey_art

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

