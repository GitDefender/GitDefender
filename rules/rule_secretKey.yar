rule _AWS_secret_key : need_config
{

    meta:
        description0 = "클라우드 서비스 플랫폼"

    strings:
        $_AWS_secret_key0 = /(i)aws(.{0,20})(i)['\"][0-9a-zA-Z\/+]{40}['\"]/

    condition:
        $_AWS_secret_key0

}

rule twitter_secret_key : need_config
{

    meta:
        description0 = "twiiter랑 connet할때 사용하는 plugin에 대해 필요한정보들 ? 뭔가의 key, secret으로 이뤄짐  "

    strings:
        $twitter_secret_key0 = /(i)twitter(.{0,20})?['\"][0-9a-z]{35,44}['\"]/

    condition:
        $twitter_secret_key0

}

rule facebook_secret_key : need_config
{

    meta:
        description0 = "facebook api를 사용할때 쓰는 key"

    strings:
        $facebook_secret_key0 = /(i)(facebook|fb)(.{0,20})(i)['\"][0-9a-f]{32}['\"]/

    condition:
        $facebook_secret_key0

}

rule linkedIn_secret_key : need_config
{

    meta:
        description0 = "facebook api를 사용할때 쓰는 key"

    strings:
        $linkedIn_secret_key0 = /(i)linkedin(.{0,20})?['\"][0-9a-z]{16}['\"]/

    condition:
        $linkedIn_secret_key0

}

