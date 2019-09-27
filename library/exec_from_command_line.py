from get_commit.get_commit import *
from get_repository.get_repository import *

def exec_from_command_line():
    res = get_commit(get_repo()['repository_list'][0])
        

if __name__ == "__main__":
    exec_from_command_line()