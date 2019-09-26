import requests

def get_repo():
    """
    param: /user/repos json 
    return: repository_list
    """
    GITHUB_API_URL = "https://api.github.com"
    GITHUB_API_TOKEN = "token 16395dbb7594f1bb54ae89796283e02170bb8613"
    REPO_SEARCH_URL = "/user/repos"
    # 따로 파일 만들어서 관리할 것

    headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': GITHUB_API_TOKEN,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': 'GitDefender'
                }

    params = {
        'client_id':'d220f1ce704075b77610',
        'client_secret': 'a811f2c99f77d0632404aaae6f0058dff3b7c0b5'
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


