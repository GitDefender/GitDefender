import requests
import json
import os
from .crawl_tool_base import CrawlTool

class GetRepository(CrawlTool):
    def __init__(self, param_github_tok, param_github_agent="GitDefender", page=1, per_page=10):
        super().__init__(self)
        self.user_token = param_github_tok
        self.user_agent = param_github_agent
        self.__repositories = None
        self.__repositories_index = None
        self.api_route = '/user/repos'
        self.repo_page = page
        self.repo_per_page = per_page

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
            'client_secret': self.client_secret,
            'sort': 'updated',
            'visibility': 'all',
            'page' : self.repo_page,
            'per_page' : self.repo_per_page
            }

        res = requests.get(self.github_api_root + self.api_route, \
            headers=headers, params=params)
        
        try:
            if res.status_code == 401:
                raise Exception("Unvalid User Token")
            elif res.status_code == 403:
                raise Exception("API rate limit exceeded")
            
            repo_list = list()

            for data in res.json():
                commits_url = str(data['commits_url']).replace('{/sha}', '')
                headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': self.user_token,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': self.user_agent
                    }

                params = {
                'client_id':self.client_id,
                'client_secret': self.client_secret,
                }

                try:
                    repo_commit_data = requests.get(commits_url, headers=headers, params=params).json()
                    recent_commit_message = repo_commit_data[0]['commit']['message']
                except:
                    recent_commit_message = ''
                repository_info = dict(
                    name=str(data['name']),
                    url=str(data['clone_url']),
                    commits_url=str(commits_url),
                    recent_commit_date=str(data['pushed_at']),
                    recent_commit_message=str(recent_commit_message),
                    secure_level=str("low") # ['low', 'middle', 'high'] 추후 기능구현 예정
                )

                repo_list.append(repository_info)

            # get repository_list

            self.repositories = repo_list
            return dict(
                repositories=repo_list,
                repository_size = str(len(repo_list))
                )

        except Exception as e:
            return dict(
                repository=[],
                error_message=str(e)
                )

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

