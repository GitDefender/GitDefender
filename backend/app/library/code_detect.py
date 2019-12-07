import os
import yara
import time
import git
#from .crawl_tool_base import CrawlTool
#from app.library.yara_detect.detect_core import DetectCore

class GetCodeDetect():
    def __init__(self, param_gdf_token, param_repo_name, param_commit_sha, param_path):
        #super().__init__(self)
        #self.username = self.github_username(self.user_token)
        self.path = param_path
        self.file_list = list()
        self.now_file = None

        self._get_file_list()
        self._config_yara()

        self._git_clone()

    def _git_clone(self):
        pass
    
    def _get_file_list(self):
        for top, dirs, files in os.walk('./yara_detect'):
            for nm in files:    
                print(top,nm)
                self.file_list.append(os.path.join(top, nm))

    def _config_yara(self):
        rules = yara.compile(filepaths={
            "log": "./yara_detect/Log_Keyword.yar",
        })

        rules.save("./yara_detect/Log_Keyword")

    def yara_callback(self, data):
        if data['matches'] == True:
            print(self.now_file)
            #print(data)
            print(data['strings'])
            with open(self.now_file) as f:
                count = 0
                print("count",count)
                try:
                    file_offset = list(map(lambda x:int(x[0]), data['strings']))
                    file_line = f.readlines()
                    for index, fl in enumerate(file_line):
                        count += len(fl)
                        min_offset = min(file_offset)
                        print("offset", file_offset)
                        print("min_offset", min(file_offset))
                        if count > min_offset:

                            print(file_line[index-1])
                            print(fl)
                            print(file_line[index+1])

                            file_offset.remove(min_offset)
                            if len(file_offset) == 0:
                                break
                        
                except Exception as e:
                    print("--FAIL", e)
                    pass
            #158을 검출하면 log__log가 나온다
            # 이런식으로 찾을까
            print("count", count)
        return yara.CALLBACK_ALL

    def detect(self, target_folder):
        rules = yara.load(target_folder)

        for sourcefile in self.file_list:
            self.now_file = sourcefile
            matches = rules.match(sourcefile, callback=self.yara_callback)

if __name__ == "__main__":
    start_time = time.time()
    gcd_instance = GetCodeDetect(None, 'huformation', None, '../../')
    
    end1 = time.time()

    result = gcd_instance.detect('./yara_detect/Log_Keyword')

    end2 = time.time()

    print("#1 : ", end1-start_time)
    print("#2 : ", end2-start_time)

    #print(result)

        

