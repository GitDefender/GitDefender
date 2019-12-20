import re
import requests
import json
from library.crawl_tool_base import CrawlTool


class KeywordAnalyze(CrawlTool):
    def __init__(self):
        pass

    def keyword_analyze(self, files_list):
        """
        param: ['./home~~/a.txt, ~, ~]
        return: [{'keyword': , 'start': ,'end': }]
        """
        result = list(map(self._scan_file, files_list))
        return result

    def _scan_file(self, source_code):
        with open(source_code, 'r') as f:
            scan_data = re.finditer('rule_set', f.read())
            #TODO iter 할때 json화시켜서 리턴시키기
        
        data = []
        
        for iter_data in scan_data:
            data.append(dict(
                file_name = source_code,
                keyword = iter_data.group(),
                start = iter_data.start(),
                end = iter_data.end()
            ))
        return data

    def api_commit_regex(self, files):
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
                'Authorization': self.user_token,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': self.user_agent
                }
    
        req = requests.get("https://api.github.com/repos/roharon/HUFormation-kakao/commits").content
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

            #TODO api commit analyze 분석



        
    
"""
if __name__ == "__main__":
    data = [
        '/home/aaronroh/projects/crawltool/library/files_keyword_analyze/files_keyword_analyze.py',
        '/home/aaronroh/projects/crawltool/library/files_keyword_analyze/__init__.py'
    ]

    res = files_keyword_analyze(data)
    print(res)

"""