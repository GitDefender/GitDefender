import requests
import json
from .crawl_tool_base import CrawlTool

class GetBranch(CrawlTool):
    """
    >>> GetBranch.
    """
    def __init__(self, param_github_tok, username, reponame):
        CrawlTool.__init__(self)
        self.user_token = param_github_tok
        self.api_route = "/repos/" + str(username) + "/" + str(reponame) + "/branches"
        
        

if __name__ == "__main__":
    pass