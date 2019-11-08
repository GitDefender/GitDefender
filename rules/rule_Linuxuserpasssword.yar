rule Potential_Linux_Passwd_file
{

    meta:
        description0 = "Potential Linux passwd file 사용자의 로그인 쉘, id 값을 알 수 있음 (보통 깃플젝에 없음)"

    strings:
        $Potential_Linux_Passwd_file0 = "etc/passwd$"

    condition:
        $Potential_Linux_Passwd_file0

}

rule Potential_Linux_shadow_file
{

    meta:
        description0 = "암호화된 패스워드와 사용자 계정정보가 들어있다. 암호화가 되어있긴하지만 crack과 같은 툴로 패스워드를 알아낼수 있으며, 누구나 읽을수 있기때문에 암호를 해독하고 사용하는것이 어렵지않다.)"

    strings:
        $Potential_Linux_shadow_file0 = "etc/shadow$"

    condition:
        $Potential_Linux_shadow_file0

}

