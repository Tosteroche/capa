import bottle
import os
import cgi


@bottle.route('/')
def hello():
    out = bottle.request.environ.get('REMOTE_ADDR')
    return out


bottle.run(host="192.168.1.1")
