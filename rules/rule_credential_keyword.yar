rule credential_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $credential_0 = "credentials"

    condition:
        $credential_0

}

