import requests

def get_repo():
    """
    param: /user/repos json 
    return: repository_list
    """
    GITHUB_API_URL = "https://api.github.com"
    GITHUB_API_TOKEN = "token <YOUR TOKEN>"
    REPO_SEARCH_URL = "/user/repos"
    # 따로 파일 만들어서 관리할 것

    headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': GITHUB_API_TOKEN,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': 'GitDefender'
                }

    params = {
        'client_id':'<CLIENT ID>',
        'client_secret': '<CLIENT SECRET>'
    }

    res = requests.get(GITHUB_API_URL + REPO_SEARCH_URL , headers=headers, params=params)

    def get_repository_name(data):
        """
        param: {'name': ~ , 'clone_url': ~ , 'commits_url': ~}
        return: 
        """
        repository_info = dict(
            name=data['name'],
            clone_url=data['clone_url'],
            commits_url=str(data['commits_url']).replace('{/sha}', '')
        )

        return repository_info

    try:
        repo_list = list(map(get_repository_name, res.json()))
        # get repository_list

        return dict(
            status=200,
            repository_list=repo_list
        ) 
    except Exception as e:
        print(e)
        return dict(
            status=404,
            repository=[]
        )
        
    #TODO jsonify   


if __name__ == "__main__":
    res = get_repo()
    print(res)

