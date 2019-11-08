rule log_
{

    meta:
        description0 = "모든 사용내역을 저장하고 있는 파일이다."

    strings:
        $log_0 = "log"

    condition:
        $log_0

}

