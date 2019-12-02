rule Microsoft_BitLocker
{

    meta:
        description0 = "facebook api를 사용할때 쓰는 key"

    strings:
        $Microsoft_BitLocker0 = "bek"

    condition:
        $Microsoft_BitLocker0

}

