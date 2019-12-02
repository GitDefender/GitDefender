rule Apache_htpasswd_file
{

    meta:
        description0 = "Potential Linux passwd file 사용자의 로그인 쉘, id 값을 알 수 있음 (보통 깃플젝에 없음)"

    strings:
        $Apache_htpasswd_file0 = /^\.?htpasswd$ \\A\\.?htpasswd\\z/

    condition:
        $Apache_htpasswd_file0

}

