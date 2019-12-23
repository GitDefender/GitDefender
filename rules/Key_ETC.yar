rule yml_
{

    meta:
        description0 = "User stored API key!"

    strings:
        $yml_0 = "secrets.yml"

    condition:
        $yml_0

}

