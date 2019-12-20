rule Filezilla
{

    meta:
        description0 = "FileZilla exposes the host & port number of a free software cross-platform FTP application sever consisting of a FileZilla client and FileZilla server."
        description1 = "FileZilla FTP recent servers file Can contain credentials for FTP servers-expose sever's hsot url, port, protocal, user id, password"

    strings:
        $Filezilla0 = "filezilla.xml"
        $Filezilla1 = "recentservers.xml "

    condition:
        $Filezilla0 or $Filezilla1

}

rule Generic_file
{

    meta:
        description0 = "server.cfg is a server configuration file that can change all kinds of settings of the sa-mp server."


    strings:
        $Generic_file0 = "server.cfg"

    condition:
        $Generic_file0

}

rule SSH
{

    meta:
        description0 = "Information about the openssh server-including various information such as root login information and authentication file location"

    strings:
        $SSH0 = "sshd_config"

    condition:
        $SSH0

}

rule Web
{

    meta:
        description0 = "This file specifies the schema for the web server properties."

    strings:
        $Web0 = "WebServers.xml"

    condition:
        $Web0

}

rule DHCP
{

    meta:
        description0 = "The dhcpd.conf file contains configuration information for dhcpd, the Internet System Consortium DHCP server."

    strings:
        $DHCP0 = "dhcpd.conf"

    condition:
        $DHCP0

}

rule Environment_config
{

    meta:
        description0 = "Environment variable setting part. Contains settings for the server environment."

    strings:
        $Environment_config0 = /\.?env/

    condition:
        $Environment_config0

}

rule Ventrilo_server
{

    meta:
        description0 = "Ventrilo server configuration file"

    strings:
        $Ventrilo_server_0 = "ventrilo_srv.ini"

    condition:
        $Ventrilo_server_0

}

rule properties_configration_file
{

    meta:
        description0 = "The deployment.config file is used to specify system level deployment.properties in your infrastructure."

    strings:
        $properties_configration_file0 = "deployment-config.json"

    condition:
        $properties_configration_file0

}

