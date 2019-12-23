import os
import yara
import subprocess
from app.library.crawl_tool_base import CrawlTool

#from app.library.yara_detect.detect_core import DetectCore
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class GetCodeDetect(CrawlTool):
    def __init__(self, param_gdf_token, param_repo_name, param_branch, param_commit_sha):
        #super().__init__(self)
        #self.username = self.github_username(self.user_token)
        self.gdf_token = str(param_gdf_token)
        self.repo_name = str(param_repo_name)
        self.branch_name = str(param_branch)
        self.commit_sha = str(param_commit_sha)
        self.file_list = list()
        
        self.result = dict()
        self.result['category'] = list()
        # yara_callback 에서 결과데이터 담음

        self.now_file = None
        # callback에서 사용

        self.root_directory = BASE_DIR + '/app/library/yara_detect/' + self.repo_name + '/'

        self.yara_rule_file = BASE_DIR + "/app/library/yara_detect/Log_Keyword.yar"
        #야라 룰셋 위치
        self.yara_compield_rule_file = BASE_DIR + "/app/library/yara_detect/Log_Keyword"
        #야라 룰 컴파일 된파일 저장위치
        self.detect_path = BASE_DIR + '/app/library/yara_detect/'

        self._git_clone()
        # repository clone job

        self._get_file_list()
        # get repository files with path

        self._config_yara()
        # compile yara rule

    def _git_clone(self):
        #추후 commit url전달통한 https replace to https token 가능
        response = subprocess.call(["git", "clone", "https://" + self.github_token(self.gdf_token) + "@github.com/"
            + self.github_username(self.gdf_token) + "/" + self.repo_name + ".git"], 
                cwd=self.detect_path)
        response_2 = subprocess.call(["git", "reset", "--soft", self.commit_sha], cwd=self.detect_path+self.repo_name)
        
        if (response != 0) or (response_2 != 0):
            return -1
        return 0


    def _get_file_list(self):
        for top, dirs, files in os.walk(self.detect_path + self.repo_name):
            for nm in files:    
                #print(top,nm)
                self.file_list.append(os.path.join(top, nm))

    def _config_yara(self):
        rules = yara.compile(filepaths={
            "log": self.yara_rule_file,
        })
        # yara rule 위치

        rules.save(self.yara_compield_rule_file)
        

    def yara_callback(self, data):
        #print(data['matches'])
        #print(self.file_list)
        if data['matches'] == True:
            print(self.now_file)
            #print(data['strings'])

            self.result[data['rule']] = list()
            self.result['category'].append(data['rule'])
            
            self.file_show_name = self.now_file.replace(self.root_directory, '')

            with open(self.now_file) as f:
                count = 0
                #print("count",count)
                try:
                    file_offset = list(map(lambda x:int(x[0]), data['strings']))
                    file_line = f.readlines()
                    file_line_size = len(file_line)
                    for index, fl in enumerate(file_line):
                        count += len(fl)
                        min_offset = min(file_offset)
                        #print("offset", file_offset)
                        #print("min_offset", min(file_offset))
                        if count > min_offset:
                            try:
                                self.result[data['rule']].append(
                                    dict(
                                        file_name=self.file_show_name,
                                        line_number=index,
                                        strings=data['strings'][0][2],
                                        line1=file_line[index-1].replace('\t', '').replace('\n', ''),
                                        line2=file_line[index].replace('\t', '').replace('\n', ''),
                                        line3=file_line[index+1].replace('\t', '').replace('\n', ''),
                                    )
                                )

                            except Exception as e:
                                try:
                                    self.result[data['rule']].append(
                                        dict(
                                            file_name=self.file_show_name,
                                            line_number=index,
                                            strings=data['strings'][0][2],
                                            line1=file_line[index-2].replace('\t', '').replace('\n', ''),
                                            line2=file_line[index-1].replace('\t', '').replace('\n', ''),
                                            line3=file_line[index].replace('\t', '').replace('\n', ''),
                                        )
                                    )
                                except Exception as e:
                                    try:
                                        self.result[data['rule']].append(
                                            dict(
                                                file_name=self.file_show_name,
                                                line_number=index,
                                                strings=data['strings'][0][2],
                                                line1=file_line[index].replace('\t', '').replace('\n', ''),
                                                line2=file_line[index+1].replace('\t', '').replace('\n', ''),
                                                line3=file_line[index+2].replace('\t', '').replace('\n', ''),
                                            )
                                        )
                                    except Exception as e:
                                        pass

                            file_offset.remove(min_offset)

                            if len(file_offset) == 0:
                                break
                            
                except Exception as e:
                    pass

        return yara.CALLBACK_ALL

    def detect(self):
        rules = yara.load(self.yara_compield_rule_file)
        # 룰 파일

        for sourcefile in self.file_list:
            #print('-')
            self.now_file = sourcefile
            matches = rules.match(sourcefile, callback=self.yara_callback)
            return self.result


"""
gcd_instance = GetCodeDetect("<GitDefender User Token>", 'Repository Name', None)
result = gcd_instance.detect()

"""     

