rule PHP_config
{

    meta:
        description0 = "php configuration file!"

    strings:
        $PHP_config0 = /config(\.inc)?\.php$/

    condition:
        $PHP_config0

}

