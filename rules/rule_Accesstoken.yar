rule Square_access_token
{

    meta:
        description0 = "Square : 모바일 결제 시스템"

    strings:
        $Square_access_token0 = /sq0atp-[0-9A-Za-z\-_]{22}/

    condition:
        $Square_access_token0

}

rule PayPal_Braintree_access_token
{

    meta:
        description0 = "Paypal Braintree : 온라인 지불 시스템 / Paypal의 부서중 하나가 Braintree"

    strings:
        $PayPal_Braintree_access_token0 = /access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}'/

    condition:
        $PayPal_Braintree_access_token0

}

rule facebook_access_token
{

    meta:
        description0 = "페이스북 페이지 엑세스 토큰을 말하는데, facebook page를 관리하는데 사용된다, 페이지 대신 api를 호출할수 있다. 예를들어, 사용자의 타임라인이 아닌 페이지에 상태 업데이트를 게시하거나 데이터를 읽을수 있다"

    strings:
        $facebook_access_token0 = "EAACEdEose0cBA[0-9A-Za-z]+"

    condition:
        $facebook_access_token0

}

rule Google_OAuth_access_token
{

    meta:
        description0 = "OAuth : 인증 프로토콜, 소셜 인증을 통한 로그인 및 권한 제어를 위해 사용됨"

    strings:
        $Google_OAuth_access_token0 = /ya29\.[0-9A-Za-z\-_]+/

    condition:
        $Google_OAuth_access_token0

}

rule PayTabs
{

    meta:
        description0 = "PayTabs:온라인 B2B 결제솔루션 제공업체"

    strings:
        $PayTabs0 = "PT_TOKEN"

    condition:
        $PayTabs0

}

rule Github_
{

    meta:
        description0 = "지킬:블로그 등 정적 사이트 생성기"
        description1 = "홈브루( SW패키지 관리 시스템) API "

    strings:
        $Github_0 = "JEKYLL_GITHUB_TOKEN"
        $Github_1 = "HOMEBREW_GITHUB_API_TOKEN language:shell"

    condition:
        $Github_0 or $Github_1

}

rule Hub
{

    meta:
        description0 = "hub 파일 안에서 oauth_token 키워드로 관련 정보를 추출"

    strings:
        $Hub0 = "hub"

    condition:
        $Hub0

}

rule Slack_token
{

    meta:
        description0 = "hub 파일 안에서 oauth_token 키워드로 관련 정보를 추출"

    strings:
        $Slack_token0 = /(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})/

    condition:
        $Slack_token0

}

