rule log_
{

    meta:
        description0 = "log file"

    strings:
        $log_0 = "log"

    condition:
        $log_0

}

