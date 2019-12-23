rule secret_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $secret_0 = "secret"

    condition:
        $secret_0

}

