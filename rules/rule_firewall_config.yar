rule Little_Snitch_firewall
{

    meta:
        description0 = "리틀 스니치는 macOS용 호스트 기반 애플리케이션 방화벽이다. 응용프로그램을 감시하는 데 사용할 수 있으며, 고급 규칙을 통해 연결된 네트워크에 접속하는 것을 방지하거나 허용한다. 오스트리아의 확고한 목표 개발 소프트웨어 GmbH에 의해 생산되고 유지된다."

    strings:
        $Little_Snitch_firewall0 = "configuration.user.xpl"

    condition:
        $Little_Snitch_firewall0

}

