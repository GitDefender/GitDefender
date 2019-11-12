rule PHP_config
{

    meta:
        description0 = "php configuration file!"

    strings:
        $PHP_config0 = /config(\.inc)?\.php/
        $PHP_config1 = /configuration.php/


    condition:
        $PHP_config0 or $PHP_config1

}