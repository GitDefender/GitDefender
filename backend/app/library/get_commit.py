import requests
from library.crawl_tool_base import CrawlTool
from library.get_repository import GetRepository


class GetCommit(GetRepository):

    def __new__(cls, parent):
        parent.__class__ = GetCommit
        return parent

    def __init__(self, parent):
        pass

    def get_commit(self):
        """
        param: {'commits_url':'github.com/sfjif/fda/~~~/commits}
        return: 각 레포별 commits history
        """
        data = self.repositories

        #TODO 웹에서 불러올때
        # 저장소만 클릭해서 하나만 불러오니
        # repositories를 dict로 해야 덜 호출하지 않는가
        
        commit_list = requests.get(data['commits_url']).json()
        commit_history = list(map(self._parse_history, commit_list))

        try:
            return dict(
                commits_history=commit_history
                )

        except:
            return dict(
                commits_history=[]
                )

    def _parse_history(self, da):

        try:
            commit_content = dict(
                commit=da['commit'],
                url=da['url'],
                html_url=da['html_url'],
                comments_url=da['comments_url'],
                parents=da['parents']
                )
            return commit_content

        except:
            return dict()


# "commits_url": "https://api.github.com/repos/roharon/HUFormation-kakao/commits{/sha}",

"""
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

"""