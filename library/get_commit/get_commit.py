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

if __name__ == "__main__":
    get_commit()

#"commits_url": "https://api.github.com/repos/roharon/HUFormation-kakao/commits{/sha}",