class Account:
    def __init__(self, user, pwd, pri):
        self._user= user
        self._pwd = pwd
        self._pri = pri

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user

    @property
    def pwd(self):
        return self._pwd
    @pwd.setter
    def pwd(self, pwd):
        self._pwd = pwd

    @property
    def pri(self):
        return self._pri
    @pri.setter
    def pri(self, pri):
        self._pri = pri