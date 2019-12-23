import yara

rule = yara.compile(filepath='/home/hyunjae/gitdefender/crawltool/rules/rule_Packagemanager.yar')


maches = rule.match('/home/hyunjae/gitdefender/crawltool/rules/yara_test/test_case')

print (maches)


