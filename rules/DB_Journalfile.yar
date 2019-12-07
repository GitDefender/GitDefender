rule Dayone
{

    meta:
        description0 = "gitrob : Day One journal file"

    strings:
        $Dayone0 = "dayone"

    condition:
        $Dayone0

}

rule Potential_jrml_journal_file
{

    meta:
        description0 = "Potential jrnl journal file"

    strings:
        $Potential_jrml_journal_file0 = "journal.txt"

    condition:
        $Potential_jrml_journal_file0

}

