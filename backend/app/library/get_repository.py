import requests
import json
import os
from crawl_tool_base import CrawlTool

class GetRepository(CrawlTool):
    def __init__(self, param_github_tok, param_github_agent="GitDefender"):
        CrawlTool.__init__(self)
        self.user_token = param_github_tok
        self.user_agent = param_github_agent
        self.__repositories = None
        self.__repositories_index = None
        self.api_route = '/user/repos'

    def test(self):
        print("---test start----")
        print("api root : " + self.github_api_root)
        print("api route : " + self.api_route)
        print("result : " + str(self.get_repo()))
        print("----test End ----")

    def get_repo(self):
        headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': self.user_token,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': self.user_agent
            }

        params = {
            'client_id':self.client_id,
            'client_secret': self.client_secret
            }

        res = requests.get(self.github_api_root + self.api_route, \
            headers=headers, params=params)

        try:
            if res.status_code == 401:
                raise Exception("Unvalid User Token")
            elif res.status_code == 403:
                raise Exception("API rate limit exceeded")
            repo_list = list(map(self._get_repo_name, res.json()))
            # get repository_list

            self.repositories = repo_list
            return dict(
                repositories=repo_list,
                repository_size = len(repo_list)
                )

        except Exception as e:
            return dict(
                repository=[],
                error_message=str(e)
                )

    def _get_repo_name(self, data):
        """
        param: {'name': ~ , 'clone_url': ~ , 'commits_url': ~}
        return:

        data for repositories
        """

        try:
            commits_url = str(data['commits_url']).replace('{/sha}', '')
            headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': self.user_token,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': self.user_agent
                }

            params = {
                'client_id':self.client_id,
                'client_secret': self.client_secret
                }

            repo_commit_data = requests.get(commits_url, headers=headers, params=params).json()
            recent_commit_message = repo_commit_data[0]['commit']['message']

            repository_info = dict(
                name=data['name'],
                url=data['clone_url'],
                commits_url=commits_url,
                recent_commit_date=data['pushed_at'],
                recent_commit_message=recent_commit_message,
                secure_level='low' # ['low', 'middle', 'high'] 추후 기능구현 예정
            )
            return repository_info

        except Exception as e:
            return e

    def _get_recent_commit(self, commits_url):

        headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': self.user_token,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': self.user_agent
            }

        params = {
            'client_id':self.client_id,
            'client_secret': self.client_secret
            }

        res = requests.get(commits_url, headers=headers, params=params).json()
        return res[0]['sha']

    @property
    def repositories(self):
        return self.__repositories

    @repositories.setter
    def repositories(self, repo_list):
        self.__repositories = repo_list

    @property
    def repositories_index(self):
        return self.__repositories_index

    @repositories_index.setter
    def repositories_index(self, repo_ind):
        self.__repositories_index = repo_ind


if __name__ == "__main__":
    data = GetRepository("Token 44371dca090a3794c560427d26931a19f46d5155")
    data.test()