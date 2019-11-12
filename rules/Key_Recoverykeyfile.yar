rule Microsoft_BitLocker
{

    meta:
        description0 = "BitLocker Encryptfile"

    strings:
        $Microsoft_BitLocker0 = "bek"

    condition:
        $Microsoft_BitLocker0

}

