import os
import yara
import time
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
        if(data['matches'] == True):
            print(self.now_file)
            print(data['strings'])
        return yara.CALLBACK_ALL

    def detect(self):
        rules = yara.load('./yara_detect/Log_Keyword')

        for sourcefile in self.file_list:
            self.now_file = sourcefile
            matches = rules.match(sourcefile, callback=self.yara_callback)

if __name__ == "__main__":
    start_time = time.time()
    gcd_instance = GetCodeDetect(None, 'huformation', None, '../../')
    
    end1 = time.time()

    result = gcd_instance.detect()

    end2 = time.time()

    print("#1 : ", end1-start_time)
    print("#2 : ", end2-start_time)

    #print(result)

        

