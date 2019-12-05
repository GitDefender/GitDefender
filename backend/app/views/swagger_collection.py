import pprint

class ErrorResponseCollection(object):
    def __init__(self, status, message, param = "message"):
        self.status = status
        self.message = message
        self.param = param

    def as_md(self):
        return '\n\n> **%s**\n\n```\n{\n\n\t"%s": "%s"\n\n}\n\n```' % \
               (self.message, self.param, self.message)

GET_REPO_STATUS_404 = ErrorResponseCollection(
    status = 404,
    message = "NOT FOUND"
)

GET_REPO_STATUS_403 = ErrorResponseCollection(
    status= 403,
    message = "Authentication credentials were not provided.",
    param = "detail"
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


GET_DETECT_STATUS_200 = ResponseCollection(
    message = "HTTP_200_OK",
    data = {
        ""
    }
)