import json


class CrawlTool:
    def __init__(self, tok=None):
        self.__github_api_root = "https://api.github.com"
        self.__user_token = tok
        self.__api_route = None
        with open("./secret.json", 'r') as secret:
            secret = json.loads(secret.read())
            self.__client_id = secret['CLIENT_ID']
            self.__client_secret = secret['CLIENT_SECRET']
            self.__user_agent = secret['USER_AGENT']

    @property
    def github_api_root(self):
        return self.__github_api_root

    @github_api_root.setter
    def github_api_root(self, root_url):
        self.__github_api_root = root_url

    @property
    def api_route(self):
        return self.__api_route

    @api_route.setter
    def api_route(self, route_url):
        self.__api_route = route_url

    @property
    def user_token(self):
        return self.__user_token

    @user_token.setter
    def user_token(self, tok):
        self.__user_token = tok

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, id_info):
        self.__client_id == id_info

    @property
    def client_secret(self):
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, secret_data):
        self.__client_secret == secret_data

    @property
    def user_agent(self):
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, agent_name):
        self.__user_agent = agent_name
