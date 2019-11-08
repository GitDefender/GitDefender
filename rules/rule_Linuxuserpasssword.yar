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
        description0 = "Potential Linux passwd file 사용자의 로그인 쉘, id 값을 알 수 있음 (보통 깃플젝에 없음)"

    strings:
        $Potential_Linux_shadow_file0 = "etc/shadow$"

    condition:
        $Potential_Linux_shadow_file0

}

