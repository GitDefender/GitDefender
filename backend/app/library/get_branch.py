from django.core.exceptions import ObjectDoesNotExist
import doctest
import requests
import json

from app.library.crawl_tool_base import CrawlTool

class GetBranch(CrawlTool):
    """
    doctest
    >>> data = GetBranch("GITHUBTOKEN_WITHOUT_-Token -_prefix", 'Huformation')
    >>> print(data.branch)
    """
    def __init__(self, gitdefender_tok, reponame):
        super().__init__(self)
        self.branches = list()
        self.branch_list = None
        self.user_token = gitdefender_tok
        username = self.github_username(self.user_token)

        self.api_route = "/repos/" + str(username) + "/" + str(reponame) + "/branches"
        self.branches = self._get()

    def _get(self):
        headers = {'Content-Type': 'application/json; charset=utf-8',
            'Authorization': self.user_token,
            'Accept': 'application/vnd.github.machine-man-preview+json',
            'User-Agent': self.user_agent
        }

        params = {
            'client_id':self.client_id,
            'client_secret': self.client_secret,
            }
        result = requests.get(self.github_api_root + self.api_route
            ,headers=headers, params=params)
        data = result.json()

        try:
            print(data)
            branch_list = list(map(lambda x:x['name'], data))
            return branch_list
        except ObjectDoesNotExist:
            return list()

    @property
    def get_branch(self):
        return dict(branches=self.branches)

if __name__ == "__main__":
    doctest.testmod()