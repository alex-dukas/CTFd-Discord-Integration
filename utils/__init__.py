from json import dump, load

class jsonio():
    def __init__(self, file):
        self.f = file

    def __write(self, data):
        with open(self.f, "w") as f:
            dump(data, f, indent=4)

    def __read(self):
        with open(self.f) as e:
            return load(e)

    def new_token(self, userid, token):
        all = self.__read()
        all.update({str(userid): str(token)})
        self.__write(all)

    def is_reg(self, userid):
        for i in self.__read():
            if str(i) == str(userid):
                return True
        return False

    def get_user_token(self, userid):
        all = self.__read()
        return str(all.get(str(userid), None))

class dataio():
    def __init__(self, file):
        self.f = file

    def __write(self, data):
        with open(self.f, "w") as f:
            dump(data, f, indent=4)

    def read(self):
        with open(self.f) as e:
            return load(e)

    def update_pos(self, data):
        all = self.read()
        all["pos_data"] = data
        self.__write(all)

    def update_chal(self, data):
        all = self.read()
        all["chal_data"] = data
        self.__write(all)

    def add_one_msg(self, userid):
        all = self.read()
        if all.get("user_msgs").get(str(userid)) is None:
            all.get("user_msgs").update({str(userid): 1})
        else:
            msg_now = int(all.get("user_msgs").get(str(userid)))
            all.get("user_msgs").update({str(userid): msg_now + 1})
        self.__write(all)

    def get_msgs(self, userid):
        all = self.read()
        return all.get("user_msgs").get(str(userid)) or 0
    