rule IntelliJ_IDEA_14
{

    meta:
        description0 = "jetbrain java IDE LICENSE key"

    strings:
        $IntelliJ_IDEA_140 = /\.?idea14.key/

    condition:
        $IntelliJ_IDEA_140

}

rule avastlic
{

    meta:
        description0 = "Virus Vaccine LICENSE key"

    strings:
        $avastlic0 = "avastlic"

    condition:
        $avastlic0

}

