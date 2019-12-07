import requests
from .crawl_tool_base import CrawlTool

class crawl_commit(CrawlTool):

    def __init__(self):
        super().__init__(self)

    #repo 가져오기 user name , repo name 가져와야함
    def get_commit(self,repo_user,repo_name):

        repo_url = "https://api.github.com/repos/" + repo_user + "/" + repo_name + "/commits"

        repo_key = "?client_id="+ str(self.client_id) + "&client_secret=" + str(self.client_secret)

        response = requests.get(repo_url + repo_key)
        json_data = response.json()
       # return print(json_data)

        commit_sha = list()
        for data in json_data:
            commit_sha.append(data['sha'])
        #return print(commit_sha)
  

        commit_data = dict()
        commit_data['commits'] = list()
        
        for a in commit_sha:
            response = requests.get(repo_url + "/" + a + repo_key)
            json_data = response.json()
            value = dict(sha=json_data["sha"], message=json_data["commit"]["message"])

            commit_data['commits'].append(value)
 
        return commit_data

if __name__ == "__main__":
    commit = crawl_commit()
    print(commit.get_commit("u0jin","data_go_kr_api"))