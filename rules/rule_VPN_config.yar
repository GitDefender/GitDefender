rule OpenVPN
{

    meta:
        description0 = "키가 들어있는 경우 가능성은 적지만 암호화를 풀수 있고, 복호화 키를 가져올수 있다면 해킹이 가능하다."

    strings:
        $OpenVPN0 = "ovpn"

    condition:
        $OpenVPN0

}

rule Tunnelblick
{

    meta:
        description0 = "키가 들어있는 경우 가능성은 적지만 암호화를 풀수 있고, 복호화 키를 가져올수 있다면 해킹이 가능하다."

    strings:
        $Tunnelblick0 = "tblk"

    condition:
        $Tunnelblick0

}

