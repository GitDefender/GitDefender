rule shell_history
{

    meta:
        description0 = "shell_history-Allows logging of args and directory locations of commands not recorded in aact / pacct files"

    strings:
        $shell_history0 = ".history"
        $shell_history1 = ".sh_history"

    condition:
        $shell_history0 or $shell_history1

}

rule Bash_Zsh_history : need_config
{

    meta:
        description0 = "need_config - log args or directory locations of commands not recorded in aact / pacct files."

    strings:
        $Bash_Zsh_history0 = /\\A\\.?(bash_|zsh_|z)?history\\z/
        $Bash_Zsh_history1 = /^\.?(bash_|zsh_|sh_|z)?history$/

    condition:
        $Bash_Zsh_history0 or $Bash_Zsh_history1

}

