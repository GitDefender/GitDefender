rule Git
{

    meta:
        description0 = "git 설정에대한 username, password가 있음"

    strings:
        $Git0 = /^\.?gitconfig$/

    condition:
        $Git0

}

rule GitHub_Hub_command-line_client__GitHub_API_access_token
{

    meta:
        description0 = "git 설정에대한 username, password가 있음"

    strings:
        $GitHub_Hub_command-line_client__GitHub_API_access_token0 = "config/hub$"

    condition:
        $GitHub_Hub_command-line_client__GitHub_API_access_token0

}

