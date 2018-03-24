import telnetlib
from IPProxies import IPProxie

class TelnetTest(object):

    def __init__(self):
        pass

    def telnetTest(self, proxie, timeout):
        result = True
        try:
            tn = telnetlib.Telnet(proxie.ip, port=proxie.port, timeout=timeout)
        except Exception as e:
            result = False
        finally:
            print('test telnet !!!  ip : %s   port : %s   result : %s' % (proxie.ip, proxie.port, result))
        return result