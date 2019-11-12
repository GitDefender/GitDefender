#all_need_config

rule Git
{

    meta:
        description0 = "git configuration - username, password "

    strings:
        $Git0 = /\.?gitconfig/

    condition:
        $Git0

}

rule GitHub_Hub_command_line_client__GitHub_API_access_token
{

    meta:
        description0 = "GitHub Hub CLI client configuration file, can include GitHub API access tokens Expose port, userid, pwd, etc."

    strings:
        $GitHub_Hub_command_line_client__GitHub_API_access_token0 = "config/hub"

    condition:
        $GitHub_Hub_command_line_client__GitHub_API_access_token0

}
