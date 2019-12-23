rule Gitrob
{

    meta:
        description0 = "Contain git configuration User ID and Password"

    strings:
        $Gitrob0 = /.gitrobrc/

    condition:
        $Gitrob0

}

