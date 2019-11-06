rule Windows_BitLocker_full_volume_encrypted_data_file
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $Windows_BitLocker_full_volume_encrypted_data_file0 = "fve"

    condition:
        $Windows_BitLocker_full_volume_encrypted_data_file0

}

