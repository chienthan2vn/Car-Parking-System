class Car:
    def __init__(self, bsx, user, name, cmt, ndk, hsd, type):
        self._name = name
        self._user = user
        self._cmt  = cmt
        self._bsx  = bsx
        self._ndk  = ndk
        self._hsd  = hsd
        self._type = type

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def cmt(self):
        return self._cmt
    @cmt.setter
    def cmt(self, cmt):
        self._cmt = cmt

    @property
    def bsx(self):
        return self._bsx
    @bsx.setter
    def bsx(self, bsx):
        self._bsx = bsx

    @property
    def ndk(self):
        return self._ndk
    @ndk.setter
    def ndk(self, ndk):
        self._ndk = ndk

    @property
    def hsd(self):
        return self._hsd
    @hsd.setter
    def hsd(self, hsd):
        self._hsd = hsd

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user