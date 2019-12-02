rule Filezilla
{

    meta:
        description0 = "FileZilla는 FileZilla 클라이언트와 FileZilla 서버로 구성된 무료 소프트웨어 교차 플랫폼 FTP 애플리케이션  sever의 호스트& 포트 번호가 노출되어있으므로 공격시나리오를 작성할때 고려 대상이 될수있다."
        description1 = "FileZilla FTP recent servers file  FTP 서버에 대한 자격 증명을 포함할 수 있음  sever의 hsot url, port, protocal, user id, password 노출  >대신 개수가 적음"

    strings:
        $Filezilla0 = "filezilla.xml"
        $Filezilla1 = "recentservers.xml "

    condition:
        $Filezilla0 or $Filezilla1

}

rule Generic_file
{

    meta:
        description0 = "server.cfg는 sa-mp 서버의 모든 종류의 설정을 변경할 수 있는 서버 구성 파일이다. 이 파일은 모든 서버에 필요하며 서버 응용프로그램(samp-server.exe) 옆의 서버 디렉토리에 위치해야 한다."

    strings:
        $Generic_file0 = "server.cfg"

    condition:
        $Generic_file0

}

rule SSH
{

    meta:
        description0 = "openssh 서버에대한 정보를 알 수 있음 + root 로그인정보, 인증파일 위치등 다양한 정보 포함"

    strings:
        $SSH0 = "sshd_config"

    condition:
        $SSH0

}

rule Web
{

    meta:
        description0 = "https://docs.pushtechnology.com/docs/6.1.0/manual/html/administratorguide/configuration/WebServer.html"

    strings:
        $Web0 = "WebServers.xml"

    condition:
        $Web0

}

rule DHCP
{

    meta:
        description0 = " dhcpd.conf 파일에는 인터넷 시스템 컨소시엄 DHCP 서버인 dhcpd에 대한 구성 정보가 포함되어 있다.  server ip, port 노출   dhcpd.conf 파일은 자유형 ASCII 텍스트 파일이다. 그것은 dhcpd에 내장된 재귀적 설계 분석기에 의해 구문 분석된다. 파일에는 포맷을 위한 추가 탭과 새 라인이 포함될 수 있다. 파일의 키워드는 대소문자를 구분하지 않는다. 코멘트는 파일 내 어디에나 배치할 수 있다(따옴표 내 제외). 코멘트는 # 문자로 시작해서 줄의 끝에서 끝난다."

    strings:
        $DHCP0 = "dhcpd.conf"

    condition:
        $DHCP0

}

rule Environment_config
{

    meta:
        description0 = "환경변수 설정부분이다. 서버 환경에 대한 설정이 포함되어 있음"

    strings:
        $Environment_config0 = /^\.?env$/

    condition:
        $Environment_config0

}

rule _Ventrilo_server_
{

    meta:
        description0 = "Ventrilo server configuration file  서버설정 파일이기때문에 포트번호를 확인할수 있고 공격시나리오를 작성할 근거로 사용될수 있다."

    strings:
        $_Ventrilo_server_0 = "ventrilo_srv.ini"

    condition:
        $_Ventrilo_server_0

}

rule properties_configration_file
{

    meta:
        description0 = "Ventrilo server configuration file  서버설정 파일이기때문에 포트번호를 확인할수 있고 공격시나리오를 작성할 근거로 사용될수 있다."

    strings:
        $properties_configration_file0 = "deployment-config.json"

    condition:
        $properties_configration_file0

}

