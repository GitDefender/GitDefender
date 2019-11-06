rule docker
{

    meta:
        description0 = "git 설정에대한 username, password가 있음"

    strings:
        $docker0 = /^\.?dockercfg$/

    condition:
        $docker0

}

