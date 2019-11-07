rule Shell_config
{

    meta:
        description0 = "쉘 환경설정 파일 부분"
        description1 = "쉘 환경설정 파일 부분 "
        description2 = "쉘 환경설정 파일 부분"
        description3 = "쉘 환경설정 파일로서 password, API key등 각종 credential한 키가 노출되어 있을 수 있다.  C shell reouce 파일_cshrc에서 PATH, setenv 등을 설정할 수 있음. 하나의 shell이 열릴 때(window open) 마다 ~/.cshrc를 읽어 사용자의 환경을 설정한다."

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
        description0 = "쉘 환경설정 파일로서 password, API key등 각종 credential한 키가 노출되어 있을 수 있다."

    strings:
        $Shell_command_alias0 = /^\.?(bash_|zsh_)?aliases$/

    condition:
        $Shell_command_alias0

}

rule Shell_profile
{

    meta:
        description0 = "쉘 환경설정 파일로서 password, API key등 각종 credential한 키가 노출되어 있을 수 있다."

    strings:
        $Shell_profile0 = /^\.?(bash_|zsh_)?profile$/

    condition:
        $Shell_profile0

}

rule Potential_MSBuild_publish_profile
{

    meta:
        description0 = "쉘 환경설정 파일로서 password, API key등 각종 credential한 키가 노출되어 있을 수 있다."

    strings:
        $Potential_MSBuild_publish_profile0 = /\\A*\\.pubxml(\\.user)?\\z/

    condition:
        $Potential_MSBuild_publish_profile0

}

