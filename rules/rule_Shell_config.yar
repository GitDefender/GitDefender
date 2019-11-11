rule Shell_config
{

    meta:
        description0 = "Shell configuration file"
        description1 = "Shell configuration file"
        description2 = "Shell configuration file"
        description3 = "Shell configuration file-various credential keys such as password, API key & You can set PATH, setenv, etc. in the C shell reouce file_cshrc. Each time a shell is opened, it reads ~ / .cshrc to set the user's environment."

    strings:
        $Shell_config0 = "exports"
        $Shell_config1 = "functions"
        $Shell_config2 = "extra"
        $Shell_config3 = /^\.?(bash|zsh|csh)rc$ .cshrc/

    condition:
        $Shell_config0 or $Shell_config1 or $Shell_config2 or $Shell_config3

}

rule Shell_command_alias
{

    meta:
        description0 = "Shell configuration file-various credential keys such as password, API key"

    strings:
        $Shell_command_alias0 = /^\.?(bash_|zsh_)?aliases$/

    condition:
        $Shell_command_alias0

}

rule Shell_profile
{

    meta:
        description0 = "Shell configuration file-various credential keys such as password, API key"

    strings:
        $Shell_profile0 = /^\.?(bash_|zsh_)?profile$/

    condition:
        $Shell_profile0

}

rule Potential_MSBuild_publish_profile
{

    meta:
        description0 = "repo - scanner : Potential MSBuild publish profile"

    strings:
        $Potential_MSBuild_publish_profile0 = /\\A*\\.pubxml(\\.user)?\\z/

    condition:
        $Potential_MSBuild_publish_profile0

}

