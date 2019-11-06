rule shell_history
{

    meta:
        description0 = "시스템 해킹이 가능할 경우, 사용자의 행위를 모두 볼수있다는 점에서 위험하다. 또한 aact/pacct파일에서 기록되지 않는 명령어의 arg나 디렉토리 위치까지 기록이 가능하므로 해킹에 유용한 정보를 제공해줄수 있다."
        description1 = "시스템 해킹이 가능할 경우, 사용자의 행위를 모두 볼수있다는 점에서 위험하다. 또한 aact/pacct파일에서 기록되지 않는 명령어의 arg나 디렉토리 위치까지 기록이 가능하므로 해킹에 유용한 정보를 제공해줄수 있다."

    strings:
        $shell_history0 = ".history"
        $shell_history1 = ".sh_history"

    condition:
        $shell_history0 or $shell_history1

}

rule Bash/Zsh_history
{

    meta:
        description0 = "시스템 해킹이 가능할 경우, 사용자의 행위를 모두 볼수있다는 점에서 위험하다. 또한 aact/pacct파일에서 기록되지 않는 명령어의 arg나 디렉토리 위치까지 기록이 가능하므로 해킹에 유용한 정보를 제공해줄수 있다."

    strings:
        $Bash/Zsh_history0 = /\\A\\.?(bash_|zsh_|z)?history\\z ^\.?(bash_|zsh_|sh_|z)?history$/

    condition:
        $Bash/Zsh_history0

}

