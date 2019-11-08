rule Microsoft_BitLocker
{

    meta:
        description0 = "BitLocker는 Windows Vista에서 시작하는 Microsoft Windows(Pro 및 Enterprise 전용) 버전에 포함된 전체 볼륨 암호화 기능이다"

    strings:
        $Microsoft_BitLocker0 = "bek"

    condition:
        $Microsoft_BitLocker0

}

