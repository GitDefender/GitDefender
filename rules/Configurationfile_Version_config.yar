rule Git
{

    meta:
        description0 = "git configuration - username, password "

    strings:
        $Git0 = /\.?gitconfig/

    condition:
        $Git0

}

rule GitHub_Hub_CLI_Client
{

    meta:
        description0 = "GitHub Hub CLI client configuration file, can include GitHub API access tokens Expose port, userid, pwd, etc."

    strings:
        $GitHub_Hub_CLI_Client0 = "config/hub"

    condition:
        $GitHub_Hub_CLI_Client0

}
