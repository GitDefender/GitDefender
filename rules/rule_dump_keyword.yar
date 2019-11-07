rule dump_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $dump_0 = "dump"

    condition:
        $dump_0

}

