import requests
from .crawl_tool_base import CrawlTool

class crawl_commit(CrawlTool):

    def __init__(self):
        super().__init__(self)

    def get_commit(self,gitdefender_tok,repo_name):

        self.user_token = gitdefender_tok
        repo_user = self.github_username(self.user_token)

        repo_url = "https://api.github.com/repos/" + repo_user + "/" + repo_name + "/commits"

        repo_key = "?client_id="+ str(self.client_id) + "&client_secret=" + str(self.client_secret)

        response = requests.get(repo_url + repo_key)
        json_data = response.json()
    
        commit_sha = list()
        for data in json_data:
            commit_sha.append(data['sha'])

  
        commit_data = dict()
        commit_data['commits'] = list()
        
        for a in commit_sha:
            response = requests.get(repo_url + "/" + a + repo_key)
            json_data = response.json()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", json_data)
            value = dict(sha=json_data["sha"], message=json_data["commit"]["message"])

            commit_data['commits'].append(value)

        return commit_data

if __name__ == "__main__":
    commit = crawl_commit()
