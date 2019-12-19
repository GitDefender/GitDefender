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

GET_COMMIT_STATUS_200 = ResponseCollection(
    message = "HTTP_200_OK",
    data ={
        'commit': [
            {'sha': '123133010b97571286b568432f63395d18a49e05', 
            'message': 'fix : remove comments and fix code'}, 
            {'sha': '312313fc750cdea348e23145948d2ee58e29f483b', 
            'message': 'Update : korea_api crawling and yara convert  Update : korea_api crawling and yara rule convert'}, 
            {'sha': '464d238123137e8502a455f97dca165cb2d28612', 'message': 'Initial commit'}]
        
    }
)


GET_CODE_DETECT_STATUS_200 = ResponseCollection(
    message = "HTTP_200_OK",
    data = {
        "Repository_name": "mymyproject",
        "branch": "master",
        "commit": "qef88u3qo4t8y12h",

        "key": [
            {
                "filename": "/daa.sh",
                "Line": 239,
                "code": "~~~~<CODE>~~~~~~~~"
            },
            {
                "filename": "/~~/~~~.py",
                "Line": 7,
                "code": "Google_API_KEY = 19u429012u5few"
            }
        ],
        "Token": [
            {
                "filename": "/da.sh",
                "Line": 432,
                "code": "~~~~<CODE>~~~~~~~~"
            },
        ],
        "Config": [
            {
                "filename": "/~~/~~~.java",
                "Line": 3159,
                "code": "~~~~<CODE>~~~~"
            },
            {
                "filename": "/~~/~~~.sh",
                "Line": 2341,
                "code": "~~~~<CODE>~~~~"
            },
        ],
        "URL": [
                        {
                "filename": "",
                "Line": 2,
                "code": "~~~~<CODE>~~~~"
            },
            {
                "filename": "/~~/~~~.sh",
                "Line": 2341,
                "code": "~~~~<CODE>~~~~"
            },
        ]
    }
)