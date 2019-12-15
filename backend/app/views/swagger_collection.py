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
   "name": "master",
    "commit": {
        "sha": "956425010b97571286b568432f63395d18a49e05",
        "node_id": "MDY6Q29tbWl0MjI1NDI1ODAwOjk1NjQyNTAxMGI5NzU3MTI4NmI1Njg0MzJmNjMzOTVkMThhNDllMDU=",
        "commit": {
            "author": {
                "name": "youjin",
                "email": "yujin5836@gmail.com",
                "date": "2019-12-02T17:30:29Z"
            },
            "committer": {
                "name": "youjin",
                "email": "yujin5836@gmail.com",
                "date": "2019-12-02T17:30:29Z"
            },
            "message": "fix : parse.py ",
            "tree": {
                "sha": "2ef8605db9b2cfef0215549acd14f52723450562",
                "url": "https://api.github.com/repos/u0jin/data_go_kr_api/git/trees/2ef8605db9b2cfef0215549acd14f52723450562"
            },
            "url": "https://api.github.com/repos/u0jin/data_go_kr_api/git/commits/956425010b97571286b568432f63395d18a49e05",
            "comment_count": 0,
            "verification": {
                "verified": "false",
                "reason": "unsigned",
                "signature": "null",
                "payload": "null"
            }
        }
    }
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