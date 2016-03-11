import bottle
import cgi
import syswork


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
    if phone:
        ip = syswork.getIp()
        mac = syswork.getMac(ip)
        check = syswork.userCheck(mac, phone)
        if check == 0:
            passkode = syswork.userStart(mac, phone)
            out = bottle.template('get_access', ip=ip, mac=mac, passkode=passkode, phone=phone)
            return out
        elif check == 1:
            return 'you have passkode, we working'
        elif check == 2:
            return 'you from eother phone? work on this'
        elif check == 3:
            return 'Somthng wrong'
        else:
            return 'UFO'


@capa.post('/go/<phone>')
def go(phone):
    passkode = bottle.request.forms.get('passkode')
    out = 'enter passkode %s' % passkode
    if syswork.passCheck(phone=phone, passkode=passkode):
        return out + ' All gut'
    else:
        return out + ' Wrong passkode'



if __name__ == '__main__':
    bottle.run(app=capa, host='192.168.1.1', reloader=True)
