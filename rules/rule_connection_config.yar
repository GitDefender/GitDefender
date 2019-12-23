rule ftp
{

    meta:
        description0 = "ftp와 sftp에 접속하기 위한 username, password가 들어있음"
        description1 = "cPanel backup ProFTPd credentials file > github에 존재하는 코드 개수가 적고, 파일 내용만 봐서는 정확히 어떤 내용을 포함하는지 보이기힘듬 > 중요정보가 포함된 url 느낌 (인증 token이나 경로나 그런 ?)   >> FTP 서버에 접속하기 위한 connection 관련 설정 파일로 보임 /   >cPanel은 cPanel & WHM. cPanel & WHM을 구축한 회사로, 웹사이트 소유자 또는 end user에게 웹 사이트 호스팅 과정을 단순화하도록 설계된 그래픽 인터페이스(GUI)와 자동화 도구를 제공하는 온라인 Linux 기반 웹 호스팅 제어판이다.   >ProFTPD(Pro FTP 데몬의 줄임말)는 FTP 서버다. ProFTPD는 무료 오픈 소스 소프트웨어로 유닉스 유사 시스템 및 마이크로소프트 윈도(사이그윈을 통해)와 호환된다. vsftpd 및 Pure-FTPd와 함께, ProFTPD는 오늘날 Unix와 유사한 환경에서 가장 인기 있는 FTP 서버 중 하나이다. 단순성, 속도 또는 보안에 초점을 맞추는 것에 비해, ProFTPD의 주요 설계 목표는 사용자에게 많은 구성 옵션을 노출시키는 고도로 기능이 풍부한 FTP 서버가 되는 것이다."

    strings:
        $ftp0 = "ftpconfig"
        $ftp1 = "proftpdpasswd"

    condition:
        $ftp0 or $ftp1

}

rule Autologin
{

    meta:
        description0 = "자동 로그인 프로세스를 위한 구성 파일  사용자 이름과 암호를 포함할 수 있음.  유닉스 시스템은 오랫동안 사용자가 원격 FTP 서버의 사용자 이름과 암호를 저장할 수 있는 방법을 제공해 왔다. ftp 클라이언트는 수십 년 동안 이를 지원했으며, 이러한 방법으로 사용자는 매번 수동으로 자격 증명을 다시 입력하지 않고도 알려진 서버에 신속하게 로그인할 수 있었다. .netrc 파일은 일반적으로 사용자의 홈 디렉토리에 저장된다(Windows에서는 curl이 _netrc라는 이름으로 검색한다).  널리 사용되고 잘 사용되는 개념인 컬은 또한 그것을 지원한다. 만약 당신이 요청한다면 컬은 이 기능을 FTP로 제한하지 않지만, 이것과 함께 어떤 프로토콜에 대해서도 기계에 대한 자격 증명을 얻을 수 있다. 자세한 내용은 아래를 참조하십시오. https://ec.haxx.se/usingcurl-netrc.html"

    strings:
        $Autologin0 = /^(\.|_)netrc$/

    condition:
        $Autologin0

}

rule SFTP_connection
{

    meta:
        description0 = "sftp연결에 대한 username, pasword가 포함되어 있음"

    strings:
        $SFTP_connection0 = /`^sftp-config(\.json)?$/

    condition:
        $SFTP_connection0

}

rule vscode_SFTP_connection_config
{

    meta:
        description0 = "sftp연결에 대한 username, pasword가 포함되어 있음"

    strings:
        $vscode_SFTP_connection_config0 = ".vscode/sftp.json"

    condition:
        $vscode_SFTP_connection_config0

}

rule Remote_Desktop_connection_file
{

    meta:
        description0 = "RDP 통신에 대한 password, username, ip등의 노출 가능성"

    strings:
        $Remote_Desktop_connection_file0 = ".rdp"

    condition:
        $Remote_Desktop_connection_file0

}

rule esmtp_
{

    meta:
        description0 = "SMTP 의 hostname, username, password,starttls 를 알수 있다,"

    strings:
        $esmtp_0 = ".esmtprc"

    condition:
        $esmtp_0

}

rule 일반적인_설정파일
{

    meta:
        description0 = "응용프로그램의 appname, store,logger,port 가 저장되어있다."

    strings:
        $일반적인_설정파일0 = "config.json"

    condition:
        $일반적인_설정파일0

}

rule atom_editer_server_connection_
{

    meta:
        description0 = "아톰의 원격서버에 자동으로 접속할때 필요한 동기화 설정 파일이다. username, IP, password를 알 수 있음"

    strings:
        $atom_editer_server_connection_0 = ".remote-sync.json"

    condition:
        $atom_editer_server_connection_0

}

rule CCcam_"IP_camera_application__configuration_file"
{

    meta:
        description0 = "아톰의 원격서버에 자동으로 접속할때 필요한 동기화 설정 파일이다. username, IP, password를 알 수 있음"

    strings:
        $CCcam_"IP_camera_application__configuration_file"0 = "CCCam.cfg"

    condition:
        $CCcam_"IP_camera_application__configuration_file"0

}

