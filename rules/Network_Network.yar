rule Network_traffic_capture_file
{

    meta:
        description0 = "Network Packet file"

    strings:
        $Network_traffic_capture_file0 = "pcap"

    condition:
        $Network_traffic_capture_file0

}

