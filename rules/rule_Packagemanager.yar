rule Rubygems : need_config
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $Rubygems0 = /credentials/

    condition:
        $Rubygems0

}

