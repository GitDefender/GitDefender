rule log_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $log_0 = "log"

    condition:
        $log_0

}

