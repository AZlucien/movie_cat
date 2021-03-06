import random
import string
import hashlib,base64


class UserService():
    @staticmethod
    def genePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()


    @staticmethod
    def geneSalt(length=16):
        key_list = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return "".join(key_list)
