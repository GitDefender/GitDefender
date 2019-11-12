rule Potential_Linux_Passwd_file
{

    meta:
        description0 = "Potential Linux passwd file"

    strings:
        $Potential_Linux_Passwd_file0 = "etc/passwd$"

    condition:
        $Potential_Linux_Passwd_file0

}

rule Potential_Linux_shadow_file
{

    meta:
        description0 = "Contains encrypted passwords and user account information."

    strings:
        $Potential_Linux_shadow_file0 = "etc/shadow$"

    condition:
        $Potential_Linux_shadow_file0

}

