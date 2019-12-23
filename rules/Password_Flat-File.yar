rule Apache_htpasswd_file
{

    meta:
        description0 = "Contain User ID and Password"

    strings:
        $Apache_htpasswd_file0 = ".htpasswd" nocase

    condition:
        $Apache_htpasswd_file0

}

