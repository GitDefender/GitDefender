import yara
from os import walk

#if __name__=="__main__":
#    filepath = '../rule_accesskeyID.yar'
#    match_file = 'test_case1'
#    rules = yara.compile(filepath)
#    print(rules.match(match_file))

#filepath = ['', '', '', '', '', '', '']
match_file = 'test_case'
filepath = [] 
mypath = '/home/tuuna/gitdefender/rules/'
for (dirpath, dirnames, filenames) in walk(mypath):
    filepath.extend(filenames)
    break;

filepath.remove('file')
filepath.remove('rule_encrypt_decrypt_key.yar')
filepath.remove('rule_CMDCLI_config.yar')
filepath.remove('rule_APIKey.yar')
filepath.remove('rule_git.yar')
filepath.remove('rule_Accesstoken.yar')
filepath.remove('rule_OauthKey.yar')
filepath.remove('rule_secretKey.yar')
filepath.remove('rule_version_config.yar')
filepath.remove('rule_shell.yar')
filepath.remove('rule_Packagemanager.yar')
filepath.remove('rule_SSH_config.yar')

for i in range(0, 27):
   # print("filename : " + filepath[i])
    rule_file = '../'+filepath[i]
    rules = yara.compile(rule_file)
    print(rules.match(match_file))
