import sys
sys.path.append("..")
import requests
from models import *
def get_github_username(data):
    
    


    """
    >>> get_username(data.user_token='Token ffbaf6f93cbf9c8cccda6a45042383309784709a')
    roharon
    """

    user_token = data.user_token
    obj = GdfUser.objects.get(github_token=user_token)
    return obj.username

if __name__ == "__main__":
    data.user_token = "Token ffbaf6f93cbf9c8cccda6a45042383309784709a"
    get_github_username()