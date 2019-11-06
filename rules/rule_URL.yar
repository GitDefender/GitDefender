rule mongolab
{

    meta:
        description0 = "몽고랩:몽고DB 데이터베이스를 호스팅하는 매니지드 클라우드 데이터베이스 서비스"

    strings:
        $mongolab0 = "mongolab.com"

    condition:
        $mongolab0

}

rule slack_webhook
{

    meta:
        description0 = "웹후크 : 앱에서 슬랙으로 메시지를 올리는 간단한 방법, 웹후크 생성시, 메시지 텍스트와 일부 옵션이 포함된 JSON 페이로드에 대한 고유한 URL이 제공됨"

    strings:
        $slack_webhook0 = /https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}/

    condition:
        $slack_webhook0

}

rule Password_in_URL
{

    meta:
        description0 = "http://username:password@example.com 은 FireFox, Chrome, Safari 에서만 작동하고, IE에서는 작동하지 않는다."

    strings:
        $Password_in_URL0 = /[a-zA-Z]{3,10}://[^/\\s:@]{3,20}:[^/\\s:@]{3,20}@.{1,100}[\"'\\s]/

    condition:
        $Password_in_URL0

}

rule Mongo_DB
{

    meta:
        description0 = "MongoDB의 비밀번호, 포트번호 등을 알아낼 수 있음"

    strings:
        $Mongo_DB0 = ".mlab.com password"

    condition:
        $Mongo_DB0

}

rule RDS
{

    meta:
        description0 = "MongoDB의 비밀번호, 포트번호 등을 알아낼 수 있음"

    strings:
        $RDS0 = "rds.amazonaws.com password"

    condition:
        $RDS0

}

