rule Pidgin
{

    meta:
        description0 = "Pidgin > OTR 프로토콜을 사용하는 채팅 프로그램   OTR> 비밀 메신저 프로토콜  // OTF 프로토콜의 private key 가 노출되는 케이스"

    strings:
        $Pidgin0 = /\\.?purple\\/accounts\\.xml\\z \.?purple/accounts\.xml$/

    condition:
        $Pidgin0

}

rule Hexchat/XChat
{

    meta:
        description0 = "IRC 는 실시간 채팅 프로토콜 이다. Xchat 은 IRC 를 통해 통신을 하는 메신저 프로그램이다. 해당 프로그램의 설정 파일이다. 권한, userid, password, port, logfile 경로 등 다수 정보가 노출된다"

    strings:
        $Hexchat/XChat0 = /\\.?xchat2?\\/servlist_?\\.conf\\z \.?xchat2?/servlist_?\.conf$/

    condition:
        $Hexchat/XChat0

}

rule Irssi
{

    meta:
        description0 = "IRC 는 실시간 채팅 프로토콜 이다. irssi는 위의 은 IRC 를 통해 통신을 하는 메신저 프로그램이다. 해당 프로그램의 설정 파일이다. 권한, url, port, 등의 정보가 존재한다"

    strings:
        $Irssi0 = / \\.?irssi\\/config\\z \.?irssi/config$/

    condition:
        $Irssi0

}

rule IRC_Config
{

    meta:
        description0 = "IRC 는 실시간 채팅 프로토콜 이다. irssi는 위의 은 IRC 를 통해 통신을 하는 메신저 프로그램이다. 해당 프로그램의 설정 파일이다. 권한, url, port, 등의 정보가 존재한다"

    strings:
        $IRC_Config0 = "config"

    condition:
        $IRC_Config0

}

