import pprint

class ErrorResponseCollection(object):
    def __init__(self, status, message, param = "message"):
        self.status = status
        self.message = message
        self.param = param

    def as_md(self):
        return '\n\n> **%s**\n\n```\n{\n\n\t"%s": "%s"\n\n}\n\n```' % \
               (self.message, self.param, self.message)

GET_401 = ErrorResponseCollection(
    status= 401,
    message = "Authentication credentials were not provided.",
    param = "detail"
)

GET_REPO_STATUS_404 = ErrorResponseCollection(
    status = 404,
    message = "NOT FOUND"
)



class ResponseCollection(object):
    def __init__(self, message=None, data=None):
        self.message = message
        self.data = data
        if self.message == None:
            self.message = " "
    def as_md(self):
        return '\n\n> **%s**\n\n```json\n%s\n\n```' % \
               (self.message, pprint.pformat(self.data, width=20, indent=4))

GET_BRANCH_STATUS_200 = ResponseCollection(
    message = "HTTP_200_OK",
    data = dict(branches=[
        'master',
        'develop',
        'feature/get_repo'
    ])
)

GET_REPO_STATUS_200 = ResponseCollection(
    message = "HTTP_200_OK",
    data = {
	"repositories": [
		{
			"name": "dogproject",
			"url": "https://github.com/<user>~~~~~~.git",
			"latest_commit": "2019-09-12",
			"latest_scan": "2019-09-15",
			
		},
		{
			"name": "catproject1234533",
			"url": "https://github.com/<user>~~~~~~.git",
			"latest_commit": "2019-10-11",
			"latest_scan": "2019-10-11",
		},
        
	],
    "repository_size": 31
    }
)


GET_CODE_DETECT_STATUS_200 = ResponseCollection(
    message = "HTTP_200_OK",
    data = {
        "category": [
            "log_",
            "Token",
            "룰추가따라 늘어남",
            "..."
        ],

        "log_": [
            {
                "file_name": ".gitignore",
                "line_number": 1,
                "strings": "a",
                "line1": "",
                "line2": "# Created by https://www.gitignore.io/api/git,python,django,pycharm+all",
                "line3": "## HUFORMATION ##"
            }
        ],
        "Token": [
            {
                "file_name": "파일이름",
                "line_number": 10,
                "strings": "ddddd",
                "line1": "탐지 줄 앞",
                "line2": "탐지된 줄",
                "line3": "탐지줄 다음"
            },
            {
                "file_name": ".gitignore",
                "line_number": 1,
                "strings": "a",
                "line1": "",
                "line2": "# Created by https://www.gitignore.io/api/git,python,django,pycharm+all",
                "line3": "## HUFORMATION ##"
            }
        ],
        "룰추가따라 늘어남": [
            {
                "file_name": "파일이름",
                "line_number": 302,
                "strings": "ddddd",
                "line1": "탐지 줄 앞",
                "line2": "탐지된 줄",
                "line3": "탐지줄 다음"
            },
            {
                "file_name": ".gitignore",
                "line_number": 1,
                "strings": "a",
                "line1": "aa",
                "line2": "~~a~~~",
                "line3": "다음줄"
            },
            {
                "file_name": ".gitignore",
                "line_number": 1,
                "strings": "a",
                "line1": "aa",
                "line2": "~~a~~~",
                "line3": "다음줄"
            },
        ],
        "...": [
            {
                "file_name": ".gitignore",
                "line_number": 1,
                "strings": "a",
                "line1": "aa",
                "line2": "~~a~~~",
                "line3": "다음줄"
            },
        ]
    }
)