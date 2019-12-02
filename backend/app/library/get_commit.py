import requests
from crawl_tool_base import CrawlTool

class crawl_commit(CrawlTool):

    def __init__(self):
        CrawlTool.__init__(self)

    #repo 가져오기
    def _get_repository(self):
        repo_user = "u0jin"
        repo_name = "test-server"

        repo_url = "https://api.github.com/repos/" + repo_user + "/" + repo_name + "/commits"

        repo_key = "?client_id="+ str(self.client_id) + "&client_secret=" + str(self.client_secret)

        response = requests.get(repo_url + repo_key)
        json_data = response.json()
       # return print(json_data)

        commit_sha = list()
        for data in json_data:
            commit_sha.append(data['sha'])
        #return print(commit_sha)
  
        for a in commit_sha:
            response = requests.get(repo_url + "/" + a + repo_key)
            json_data = response.json()
            
            return print(json_data)


if __name__ == "__main__":
    commit = crawl_commit()
    commit._get_repository()