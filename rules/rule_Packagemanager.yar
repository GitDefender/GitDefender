rule Rubygems
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $Rubygems0 = /\.?gem/credentials$/

    condition:
        $Rubygems0

}

