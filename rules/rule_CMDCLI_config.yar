#need all config 

rule Twitter_client
{

    meta:
        description0 = "T command-line Twitter client configuration file 트위터 와 관련된 CLI 도구인것 같음, 예시를보면 key 위주로 노출됨 "

    strings:
        $Twitter_client0 = /\\A\\.?trc\\z ^\.?trc$/

    condition:
        $Twitter_client0

}

rule tugboat
{

    meta:
        description0 = "repo - scanner : Tugboat DigitalOcean management tool configuration  Tugboat  :A command line tool for interacting with your DigitalOcean droplets. // "

    strings:
        $tugboat0 = /\\A\\.?tugboat\\z ^\.?tugboat$/

    condition:
        $tugboat0

}

rule NPM
{

    meta:
        description0 = "npm register에 대한 크리덴셜한 정보가 포함될 수 있다  npm은 명령줄, 환경 변수 및 npmrc 파일에서 구성 설정을 얻는다.  npm config 명령은 사용자 및 글로벌 npmrc 파일의 내용을 업데이트하고 편집하는 데 사용할 수 있다.  사용 가능한 구성 옵션 목록은 npm-config를 참조하십시오. https://docs.npmjs.com/files/npmrc"

    strings:
        $NPM0 = /^\.?npmrc$/

    condition:
        $NPM0

}

rule DigitalOcean_doctl_command_line_client
{

    meta:
        description0 = "npm register에 대한 크리덴셜한 정보가 포함될 수 있다  npm은 명령줄, 환경 변수 및 npmrc 파일에서 구성 설정을 얻는다.  npm config 명령은 사용자 및 글로벌 npmrc 파일의 내용을 업데이트하고 편집하는 데 사용할 수 있다.  사용 가능한 구성 옵션 목록은 npm-config를 참조하십시오. https://docs.npmjs.com/files/npmrc"

    strings:
        $DigitalOcean_doctl_command_line_client0 = "doctl/config.yaml"

    condition:
        $DigitalOcean_doctl_command_line_client0

}

