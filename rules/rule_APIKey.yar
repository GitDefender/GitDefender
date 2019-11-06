rule Recon-ng
{

    meta:
        description0 = "kail 에서 쓰는 web scanning? 툴이라고 하는데 거기에 쓰는 키값"

    strings:
        $Recon-ng0 = /\\.?recon-ng\\/keys\\.db\\z \.?recon-ng/keys\.db$/

    condition:
        $Recon-ng0

}

rule Google
{

    meta:
        description0 = "구글 API key"

    strings:
        $Google0 = /AIza[0-9A-Za-z\\-_]{35}/

    condition:
        $Google0

}

rule Picatic
{

    meta:
        description0 = "Picatic는 온라인 티켓팅과련  서비스 > 외국에서 주로 사용하는 서비스?  Picatic API Key 테스트 코드밖에 없고, 키 판별이 확실해서 깃헙에 많이 존재하지 않음 실제 의미있는건 아닌것같음  이 API를 쓰는 이유 ? Picatic API는 사용자들에게 당신의 앱이나 웹사이트에서 직접 온라인으로 티켓을 판매할 수 있는 도구를 제공한다. 또한 Picatic API는 새로운 이벤트를 빠르게 만들고, 자신의 웹사이트에 이벤트를 나열하며, 온라인 티켓 구매 링크를 만들고, 이벤트에서 데이터를 검색하고 저장하며, 자동으로 CRM에 등록자를 추가하고, 활동에 기반한 트리거된 이메일 전송, 참석자 보기, 주문 및 설문 정보 등을 제공한다. 이 API를 통해 사용자는 보고 데이터에 실시간으로 액세스할 수 있으며 개인화된 보고서를 만들 수 있다. Picatic은 프로모터가 이벤트 페이지를 생성하여 이벤트를 예약하기 전에 자금을 조달할 수 있도록 하는 고유한 접근 방식을 가진 티켓팅 플랫폼이다."

    strings:
        $Picatic0 = /sk_live_[0-9a-z]{32}/

    condition:
        $Picatic0

}

rule MailGun
{

    meta:
        description0 = "MailGun API key Api를 이용하여 이메일을 보내고 받을 수 있는 서비스로 메일의 상태에 따른 WebHook을 보낼 수 있는것도 특징이다. 가격도 인당이 아닌 메일 건당으로 측정되고 개인이 사용하기에는 무료"

    strings:
        $MailGun0 = /(?i)(mailgun|mg)(.{0,20})?['"][0-9a-z]{32}['"]/

    condition:
        $MailGun0

}

rule Stripe_Standard
{

    meta:
        description0 = "외국에서 사용하는 결제시스템 https://stripe.com/docs/connect/standard-accounts"

    strings:
        $Stripe_Standard0 = /(?i)stripe(.{0,20})?['\"][sk|rk]_live_[0-9a-zA-Z]{24}/

    condition:
        $Stripe_Standard0

}

rule MailChimp
{

    meta:
        description0 = "마케팅 자동화 플랫폼이자 e-메일 마케팅 서비스"

    strings:
        $MailChimp0 = /(?i)(mailchimp|mc)(.{0,20})?['"][0-9a-f]{32}-us[0-9]{1,2}['"]/

    condition:
        $MailChimp0

}

rule Heroku
{

    meta:
        description0 = "클라우드 서비스 플랫폼"
        description1 = "description does not exist"
        description2 = "description does not exist"

    strings:
        $Heroku0 = /(?i)heroku(.{0,20})?['"][0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}['"]/
        $Heroku1 = /[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}/
        $Heroku2 = "HEROKU_API_KEY"

    condition:
        $Heroku0 or $Heroku1 or $Heroku2

}

rule AWS_key
{

    meta:
        description0 = "description does not exist"

    strings:
        $AWS_key0 = /(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}/

    condition:
        $AWS_key0

}

rule Twilio_api_key
{

    meta:
        description0 = "서비스형 클라우드 커뮤니케이션 플랫폼(CPaaS)이다. Twilio는 소프트웨어 개발자들이 프로그래밍 방식으로 전화를 걸고 받고, 문자 메시지를 주고 받고, 웹 서비스 API를 사용하여 다른 통신 기능을 수행할 수 있도록 해준다.   > 홈페이지에 게시된 key 예시를 보면 두 정규 표현식 / 결국 같은 api key를 잡는다는 걸 확인 할 수 있음 (하나는 twilio 문자열을 추가로 잡고 뒤에 32 글자 를 잡는 정규 표현식이고/ 다른 하나는 SK + 32 글자를 잡는 정규표현식 -> 따라서 동일) https://www.twilio.com/docs/iam/keys/api-key"
        description1 = "description does not exist"

    strings:
        $Twilio_api_key0 = /(?i)twilio(.{0,20})?['\"][0-9a-f]{32}['\"]/
        $Twilio_api_key1 = /SK[a-z0-9]{32}/

    condition:
        $Twilio_api_key0 or $Twilio_api_key1

}

rule GENERIC
{

    meta:
        description0 = "일반적인 api key에 대해서 잡는 것 같음 키워드와 문자로 잡는 방식"
        description1 = "description does not exist"

    strings:
        $GENERIC0 = /(?i)(api_key|apikey)(.{0,20})?['|"][0-9a-zA-Z]{32,45}['|"]/
        $GENERIC1 = /[a|A][p|P][i|I][_]?[k|K][e|E][y|Y].{0,30}['\"\\s][0-9a-zA-Z]{32,45}['\"\\s]/

    condition:
        $GENERIC0 or $GENERIC1

}

rule shodan
{

    meta:
        description0 = "쇼단에서 사용하는 api key 쇼단은 특정한 조건에 맞는 서버(Server), 라우터(Router), CCTV 카메라, 각종 IoT 디바이스-----를 찾아줌"

    strings:
        $shodan0 = "shodan_api_key"

    condition:
        $shodan0

}

rule Google_Cloud_Platform_API_key
{

    meta:
        description0 = "  https://cloud.google.com/docs/authentication/api-keys - 사용자 인증 정보를 공개적으로 노출하면 계정이 유출되어 계정에 예상치 못한 비용이 부과될 수 있다"

    strings:
        $Google_Cloud_Platform_API_key0 = /(?i)(google|gcp|youtube|drive|yt)(.{0,20})?['\"][AIza[0-9a-z\\-_]{35}]['\"]/

    condition:
        $Google_Cloud_Platform_API_key0

}

rule dark_sky_api
{

    meta:
        description0 = "dark sky 기상정보? 와 관련된 서비스 ,일기예보에 사용되는 서비스와 관련되어보임If you're trying to use our service, you probably wanted one of these endpoints: /forecast/APIKEY/LATITUDE,LONGITUDE /forecast/APIKEY/LATITUDE,LONGITUDE,TIMESTAMP /v1/status.txt D "

    strings:
        $dark_sky_api0 = "api.forecast.io"

    condition:
        $dark_sky_api0

}

rule AWS_MWS_key
{

    meta:
        description0 = "dark sky 기상정보? 와 관련된 서비스 ,일기예보에 사용되는 서비스와 관련되어보임If you're trying to use our service, you probably wanted one of these endpoints: /forecast/APIKEY/LATITUDE,LONGITUDE /forecast/APIKEY/LATITUDE,LONGITUDE,TIMESTAMP /v1/status.txt D "

    strings:
        $AWS_MWS_key0 = /amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/

    condition:
        $AWS_MWS_key0

}

