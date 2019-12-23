#from get_repository import get_repo
import requests
import json

def api_commit_regex(files):
    """
    param: files:list - [raw_url]
    return: {
    	[
            'file_name': "./디렉토리구조/파일명.확장자":str,
            'line_number': 숫자:int,
            'keyword': 해당코드줄:str,
            'start': 키워드시작인덱스,
            'end' : 키워드끝인덱스,
            'category': 카테고리분류:str - 룰셋을 통해 나온 결과기반,
            '
        ]    
    }
    """

    headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': "",
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': "Gitdefender"
                }
    
    req = requests.get("https://api.github.com/repos/roharon/HUFormation-kakao/commits").content
    # [{}] 로 짜여진 구조이므로 json 화 시키기 위해 string 에서 [1:-1]통해 제거
    
    json_data_list = json.loads(req)

    data_list = []
    for data in json_data_list:
        data_list.append(dict(
            sha = data['sha'],
            commit = data['commit'],
            url = data['url']
        ))

    
    for data in data_list:
        url_req = requests.get(data['url']).content
        files_data = json.loads(url_req['files'])

        for d in files_data:
            raw_data = requests.get(d['raw_url']).content
            # ~~()
            # regex 검사실행



if __name__ == "__main__":
    headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': "",
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': "Gitdefender"
                }
    
    req = requests.get("https://api.github.com/repos/roharon/HUFormation-kakao/commits").content
    # [{}] 로 짜여진 구조이므로 json 화 시키기 위해 string 에서 [1:-1]통해 제거
    
    json_data_list = json.loads(req)

    data_list = []
    for data in json_data_list:
        data_list.append(dict(
            sha = data['sha'],
            commit = data['commit'],
            url = data['url'],
        ))