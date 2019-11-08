rule Gitrob
{

    meta:
        description0 = "git 설정에대한 username, password가 있음l"

    strings:
        $Gitrob0 = /\\A\\.?gitrobrc\\z ^\.?gitrobrc$/

    condition:
        $Gitrob0

}

