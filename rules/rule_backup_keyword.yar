rule backup_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $backup_0 = "backup"

    condition:
        $backup_0

}

