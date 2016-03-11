import bottle
import cgi

capa = bottle.Bottle()


@capa.get('/')
def hello():
    out = bottle.template('index')
    return out


@capa.get('/access')
def access():
    out = bottle.template('acc_form')
    return out


@capa.post('/access')
def get_access():
    phone = bottle.request.forms.get('phone')
    phone = cgi.escape(phone)

    out = ''

    if not phone:   # TODO: create function valid(phone) -> True or False
        out = bottle.template('err_access')
    else:
        out = 'OK!'

    return out

if __name__ == '__main__':
    bottle.run(app=capa, host='192.168.1.1', reloader=True)
