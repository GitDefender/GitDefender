rule _Ruby_on_Rails
{

    meta:
        description0 = "hub 파일 안에서 oauth_token 키워드로 관련 정보를 추출"

    strings:
        $_Ruby_on_Rails0 = "omniauth.rb"

    condition:
        $_Ruby_on_Rails0

}

