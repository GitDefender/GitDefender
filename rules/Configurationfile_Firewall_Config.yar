rule Little_Snitch_firewall
{

    meta:
        description0 = "MacOS host base application firewall configuration file."

    strings:
        $Little_Snitch_firewall0 = "configuration.user.xpl"

    condition:
        $Little_Snitch_firewall0

}

