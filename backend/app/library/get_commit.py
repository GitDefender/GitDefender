import requests
from .crawl_tool_base import CrawlTool

class crawl_commit(CrawlTool):

    def __init__(self):
        super().__init__(self)

    def get_commit(self,gitdefender_tok,repo_name,repo_branch):
        commit_data = dict()
        commit_data['commit'] = list()

        self.user_token = gitdefender_tok
        repo_user = self.github_username(self.user_token)

        self.api_route = "/repos/" + repo_user + "/" + repo_name + "/branches/" + repo_branch

        headers = {'Content-Type': 'application/json; charset=utf-8',
            'Authorization': self.user_token,
            'Accept': 'application/vnd.github.machine-man-preview+json',
            'User-Agent': self.user_agent
        }

        params = {
            'client_id':self.client_id,
            'client_secret': self.client_secret,
        }

        response = requests.get(self.github_api_root + self.api_route, headers=headers, params=params)
        json_data = response.json()

        value = dict(sha=json_data["commit"]["sha"], message=json_data["commit"]["commit"]["message"])
        commit_data['commit'].append(value)

        return commit_data
        

if __name__ == "__main__":
    commit = crawl_commit()
