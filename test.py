import bottle
import os
import cgi


@bottle.route('/')
def hello():
    out = ''

    for i in os.environ:
        out = out + str(i) + '\t' + str(os.environ[i]) + '<br>'
    return out


bottle.run(host="192.168.1.1")
