import requests

def get_commit(data):
    """
    param: {'commits_url':'github.com/sfjif/fda/~~~/commits}
    return: 각 레포별 commits history
    """
    commit_list = requests.get(data['commits_url']).json()

    def parse_history(da):
        try:
            commit_content = dict(
            commit = da['commit'],
            url = da['url'],
            html_url = da['html_url'],
            comments_url = da['comments_url'],
            parents = da['parents']
        )
            return commit_content

        except:
            return dict()
    commit_history = list(map(parse_history, commit_list))

    try:
        return dict(
            commits_history = commit_history
            )

    except:
        return dict(
            commits_history = []
            )

# "commits_url": "https://api.github.com/repos/roharon/HUFormation-kakao/commits{/sha}",


if __name__ == "__main__":
    json_object = {
        'status': 200,
        'repository_list':
            [{'name': '006975',
              'clone_url': 'https://github.com/roharon/006975.git',
              'commits_url': 'https://api.github.com/repos/roharon/006975/commits'

            }]}

    res = get_commit(json_object['repository_list'][0])
    print(res)