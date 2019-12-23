import requests
import json


# repo_변수 부분은 입력을 받는걸로 변경가능
repo_user = "u0jin"
repo_name = "test-server"

repo_key = "?client_id=d220f1ce704075b77610&client_secret=a811f2c99f77d0632404aaae6f0058dff3b7c0b5"


REPO_URL = "https://api.github.com/repos/" + repo_user + "/" + repo_name + "/commits"

response = requests.get(REPO_URL + repo_key)
json_data = response.json()

# list안에 sha 만 뽑아 내기
sha_list = list()
for data in json_data:
    sha_list.append(data['sha'])

# sha하나당 commit 하나씩 불러옴
for a in sha_list:
    response = requests.get(REPO_URL + "/" + a + repo_key)
    json_data = response.json()
    print(json_data)

 #   commit msg 만 보여주기    
 #   print(json_data['commit']['message']) 
    