rule Ruby_On_Rails
{

    meta:
        description0 = "Web framework written in ruby configration file of potential database-exposing database credentials information ip, port, username, pw, mac address, etc.
"

    strings:
        $Ruby_On_Rails0 = "database.yml"

    condition:
        $Ruby_On_Rails0

}

rule Django
{

    meta:
        description0 = "Configuration file of django framework-reveals secret key exposure, databases configuration information, debug mode on off"

    strings:
        $Django0 = "settings.py"

    condition:
        $Django0

}

rule Drupal
{

    meta:
        description0 = "Drupal Bulletin Database Configuration File"

    strings:
        $Drupal0 = "databases password"

    condition:
        $Drupal0

}
