rule Rubygems
{

    meta:
        description0 = ""Rubygems credentials file""

    strings:
        $Rubygems0 = /credentials/

    condition:
        $Rubygems0

}

