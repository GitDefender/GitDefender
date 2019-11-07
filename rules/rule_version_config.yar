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
        description0 = ""GitHub Hub CLI 클라이언트 구성 파일,GitHub API 액세스 토큰을 포함할 수 있음 port, userid, pwd 등 도 노출""

    strings:
        $GitHub_Hub_command-line_client__GitHub_API_access_token0 = "config/hub$"

    condition:
        $GitHub_Hub_command-line_client__GitHub_API_access_token0

}
