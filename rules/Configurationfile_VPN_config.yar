rule OpenVPN : filename
{

    meta:
        description0 = "OpenVPN provides flexible VPN solutions for businesses to secure all data communications and extend private network services while maintaining security."

    strings:
        $OpenVPN0 = "ovpn"

    condition:
        $OpenVPN0

}

rule Tunnelblick : filename
{

    meta:
        description0 = "Tunnelblick is open source software that can be used to connect to any VPN network that supports OpenVPN."

    strings:
        $Tunnelblick0 = "tblk"

    condition:
        $Tunnelblick0

}