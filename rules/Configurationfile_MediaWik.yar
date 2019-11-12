rule MediaWiki_config
{

    meta:
        description0 = "DB access information related to media wiki, user group view / edit information can be checked, file uploadable extension can be identified."

    strings:
        $MediaWiki_config0 = "LocalSettings.php"

    condition:
        $MediaWiki_config0

}

