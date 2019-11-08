#all_need_config

rule Google_Oauth : need_config
{

    meta:
        description0 = "구글 인증(auth)에 인증요청 보낼떄 사용하는 key 라고 판단"
        description1 = "구글 인증(auth)에 인증요청 보낼떄 사용하는 데이터들이 저장됨 ( url, client 관련정보(secret key)) json 형태로 저장"

    strings:
        $Google_Oauth0 = /"(\"client_secret\":\"[a-zA-Z0-9-_]{24}\")"/
        $Google_Oauth1 = /(i)(google|gcp|auth)(.{0,20})?['"][0-9]+-[0-9a-z_]{32}\.apps\.googleusercontent\.com['"]/

    condition:
        $Google_Oauth0 or $Google_Oauth1

}

rule Facebook_Oauth
{

    meta:
        description0 = "facebook client secret key"

    strings:
        $Facebook_Oauth0 = /[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]/

    condition:
        $Facebook_Oauth0

}

rule Github_Oauth : need_config
{

    meta:
        description0 = "35,44 길이에 해당하는 ? 정보를 찾긴 어려우나 인증 요청을 보낼때 사용하는 정보로 추정"

    strings:
        $Github_Oauth0 = /[0-9a-zA-Z]{35,40}/

    condition:
        $Github_Oauth0

}

rule Twitter_Oauth
{

    meta:
        description0 = "35,44 길이에 해당하는 ? 정보를 찾긴 어려우나 인증 요청을 보낼때 사용하는 정보로 추정"

    strings:
        $Twitter_Oauth0 = /[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]/

    condition:
        $Twitter_Oauth0

}

rule Square_OAuth_secret
{

    meta:
        description0 = "35,44 길이에 해당하는 ? 정보를 찾긴 어려우나 인증 요청을 보낼때 사용하는 정보로 추정"

    strings:
        $Square_OAuth_secret0 = /sq0csp-[0-9A-Za-z\\-_]{43}/

    condition:
        $Square_OAuth_secret0

}

