rule _Ruby_on_Rails1
{

    meta:
        description0 = "rails 프레임워크 OAUTH2 인증 토큰, ID, SECRET이 담겨있다"

    strings:
        $_Ruby_on_Rails0 = "omniauth.rb"

    condition:
        $_Ruby_on_Rails0

}

rule _Ruby_on_Rails2
{

    meta:
        description0 = "해당 프레임 워크에서 사용하는 token file,Rails 비밀 토큰을 알면 원격 코드 실행을 허용할 수 있다."

    strings:
        $_Ruby_on_Rails0 = "secret_token.rb"

    condition:
        $_Ruby_on_Rails0

}
