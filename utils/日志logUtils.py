import socket
import os

import sys
import socket


class LogBase(object):
    @staticmethod
    def get_host_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    @staticmethod
    def get_file_name():
        return os.path.realpath(sys.argv[0])

    @staticmethod
    def get_call_method_name():
        str = " \nmethod_name: \n"
        # str +=  sys._getframe().f_code.co_name + " \\ "
        if sys._getframe().f_back:
            str += sys._getframe().f_back.f_code.co_name + " \\ "
            if sys._getframe().f_back.f_back:
                str += sys._getframe().f_back.f_back.f_code.co_name + " \\ "
                if sys._getframe().f_back.f_back.f_back:
                    str += sys._getframe().f_back.f_back.f_back.f_code.co_name + " \\ "
        str += " _(:з」∠)_   \n "
        return str

    @staticmethod
    def get_host_name():
        return socket.getfqdn(socket.getfqdn())


class log(LogBase):

    def sent_msg(self):
        str = ""
        str += self.get_host_ip() + "\n"
        str += self.get_call_method_name() + "\n"
        str += self.get_file_name() + "\n"
        str += self.get_host_name() + "\n"

        return str


if __name__ == '__main__':
    print(LogBase.get_host_ip())
    print(LogBase.get_file_name())
    print(LogBase.get_call_method_name())
    print(LogBase.get_host_name())

    a = log()
    print(a.sent_msg())
