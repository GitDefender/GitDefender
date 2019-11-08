rule Apache_htpasswd_file
{

    meta:
        description0 = "인증할 사용자의 ID와 password가 들어있는 파일이다.)"

    strings:
        $Apache_htpasswd_file0 = /^\.?htpasswd$ \\A\\.?htpasswd\\z/

    condition:
        $Apache_htpasswd_file0

}

