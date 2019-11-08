rule Network_traffic_capture_file
{

    meta:
        description0 = "각종 네트워크 상에 흘러다니는 정보를 캐치할 수 있디."

    strings:
        $Network_traffic_capture_file0 = "pcap"

    condition:
        $Network_traffic_capture_file0

}

