import requests
from .crawl_tool_base import CrawlTool

class crawl_commit(CrawlTool):

    def __init__(self):
        super().__init__(self)

    def get_commit(self,param_github_tok,repo_name,repo_branch):
        
        self.user_token = param_github_tok

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': self.user_token,
            'Accept': 'application/vnd.github.machine-man-preview+json',
            'User-Agent': "GitDefender"
            }

        params = {
            'sha' : repo_branch,
            'client_id' : self.client_id,
            'client_secret': self.client_secret
            }
            
        repo_user = self.github_username(self.user_token)

        repo_url = "https://api.github.com/repos/" + repo_user + "/" + repo_name + "/commits"

        response = requests.get(repo_url, headers=headers, params=params)
        json_data = response.json()

        commit_data = dict()
        commit_data['commit'] = list()
        
        for i in json_data :
            value = dict(sha=i["sha"], message=i["commit"]["message"])
            commit_data['commit'].append(value)

        return commit_data

if __name__ == "__main__":
    commit = crawl_commit()