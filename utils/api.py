import requests
from config import Config
import json
import urllib.parse

class Api():
    @staticmethod
    def __send_req(token, endpoint, v=True):
        if v:
            return requests.get(endpoint, headers={'Authorization': f'Token {token}', "Content-Type": "application/json"}) 
        else:
            return requests.get(endpoint, headers={"Content-Type": "application/json"}) 

    def get_top_10(self, token):
        req = self.__send_req(token, Config.CTFD_BASE_URL + "/api/v1/scoreboard")
        return json.loads(req.content.decode("utf-8"))

    def get_user(self, token):
        req = self.__send_req(token, Config.CTFD_BASE_URL + "/api/v1/users/me")
        return json.loads(req.content.decode("utf-8"))

    def get_challenges(self, token, name=None):
        if name is None:
            req = self.__send_req(token, Config.CTFD_BASE_URL + "/api/v1/challenges")
        else:
            req = self.__send_req(token, Config.CTFD_BASE_URL + f"/api/v1/challenges?name={urllib.parse.quote(name)}")
        return json.loads(req.content.decode("utf-8"))

    def see_who_solved(self, token):
        req = self.__send_req(token, Config.CTFD_BASE_URL + "/api/v1/scoreboard/top/999")
        return json.loads(req.content.decode("utf-8"))