from django.core.exceptions import ObjectDoesNotExist
from doctest
import requests
import json

from crawl_tool_base import CrawlTool

class GetBranch(CrawlTool):
    """
    doctest
    >>> data = GetBranch("GITHUBTOKEN_WITHOUT_-Token -_prefix", 'Huformation')
    >>> print(data.branch)
    """
    def __init__(self, github_tok, reponame):
        CrawlTool.__init__(self)
        self.branches = list()
        self.branch_list = None
        self.user_token = github_tok
        
        username = self.github_username
        self.api_route = "/repos/" + str(username) + "/" + str(reponame) + "/branches"
        self.branches = self._get()

    def _get(self):
        result = requests.get(self.github_api_root + self.api_route)
        data = result.json()

        try:
            branch_list = list(map(lambda x:x['name'], data))
            return branch_list
        except ObjectDoesNotExist:
            return list()

    @property
    def branch(self):
        return self.branches

if __name__ == "__main__":
    doctest.testmod()