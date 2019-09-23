import requests, json

def get_repo():

    GITHUB_API_URL = "https://api.github.com"
    GITHUB_API_TOKEN = "token 342deef2cc1bedda15bf050280d893f31a874b24"

    REPO_SEARCH_URL = "/user/repos"
    
    headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': GITHUB_API_TOKEN,
                'Accept': 'application/vnd.github.machine-man-preview+json'}


    params = {

    }

    res = requests.get(GITHUB_API_URL + REPO_SEARCH_URL, headers=headers, params=params)

    for json_result in res.json():
        print(json.dumps(json_result['full_name'], indent=4))
        print(json.dumps(json_result['clone_url'], indent=4))
        print(json.dumps(json_result['commits_url'], indent=4))
        print()
    
    #TODO jsonify


if __name__ == "__main__":
    get_repo()

#"commits_url": "https://api.github.com/repos/roharon/HUFormation-kakao/commits{/sha}",
