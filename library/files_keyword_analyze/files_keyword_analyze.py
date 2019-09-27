import re

def files_keyword_analyze(files_list):
    """
    param: ['./home~~/a.txt, ~, ~]
    return: [{'keyword': , 'start': ,'end': }]
    """
    
    def scan_file(source_code):
        with open(source_code, 'r') as f:
            scan_data = re.finditer('App', f.read())
            #TODO iter 할때 json화시켜서 리턴시키기
        
        data = dict()

        for iter_data in scan_data:
            data = dict(
                keyword= iter_data.group(),
                start=iter_data.start(),
                end=iter_data.end()
            )
        return data
    
    result = list(map(scan_file, files_list))
    return result

if __name__ == "__main__":
    data = [
        '/home/aaronroh/projects/project-Oechul-front/yarn.lock',
        '/home/aaronroh/projects/project-Oechul-front/src/App.js',
        '/home/aaronroh/projects/project-Oechul-front/src/index.js',
    ]

    res = files_keyword_analyze(data)
    print(res)