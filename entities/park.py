class Park:
    def __init__(self, ID, bsx, day, timein, timeout, link_img, link_img_out, flag):
        self._ID= ID
        self._bsx = bsx
        self._timein = timein
        self._timeout = timeout
        self._link_img = link_img
        self._flag = flag
        self._day = day
        self._link_img_out = link_img_out

    @property
    def ID(self):
        return self._ID
    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def bsx(self):
        return self._bsx
    @bsx.setter
    def bsx(self, bsx):
        self._bsx = bsx

    @property
    def timein(self):
        return self._timein
    @timein.setter
    def timein(self, timein):
        self._timein = timein

    @property
    def timeout(self):
        return self._timeout
    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout

    @property
    def link_img(self):
        return self._link_img
    @link_img.setter
    def link_img(self, link_img):
        self._link_img = link_img

    @property
    def flag(self):
        return self._flag
    @flag.setter
    def flag(self, flag):
        self._flag = flag

    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, day):
        self._day = day

    @property
    def link_img_out(self):
        return self._link_img_out
    @link_img_out.setter
    def link_img_out(self, link_img_out):
        self._link_img_out = link_img_out