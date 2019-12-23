rule docker
{

    meta:
        description0 = "Docker configuration file"

    strings:
        $docker0 = /\.?dockercfg/

    condition:
        $docker0

}
