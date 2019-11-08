rule Jenkins
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $Jenkins0 = "credentials.xml"

    condition:
        $Jenkins0

}

