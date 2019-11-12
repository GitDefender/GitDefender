rule Wordpress_configuration_file : filename
{

    meta:
        description0 = "This is a configuration file for WordPress that contains administrator-return passwords and databases manager information. In addition, multiple secure keys can be exposed."

    strings:
        $Wordpress_configuration_file0 = "wp-config.php"

    condition:
        $Wordpress_configuration_file0

}

