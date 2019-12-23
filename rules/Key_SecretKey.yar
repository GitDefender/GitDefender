rule _AWS_secret_key : need_config
{

    meta:
        description0 = "Cloud service platform"

    strings:
        $_AWS_secret_key0 = /aws(.{0,20})['\"][0-9a-zA-Z\/+]{40}['\"]/nocase

    condition:
        $_AWS_secret_key0

}

rule twitter_secret_key : need_config
{

    meta:
        description0 = "Necessary information about plugin used when conneting with twiiter-consists of key and secret"

    strings:
        $twitter_secret_key0 = /twitter(.{0,20})['\"][0-9a-zA-Z]{35,50}['\"]/nocase

    condition:
        $twitter_secret_key0

}

rule facebook_secret_key : need_config
{

    meta:
        description0 = "Key for using facebook api"

    strings:
              $facebook_secret_key0 = /(facebook|fb)(.{0,20})['\"][0-9a-fA-F]{32}['\"]/nocase


    condition:
        $facebook_secret_key0

}

rule linkedIn_secret_key : need_config
{

    meta:
        description0 = "LInkedIn secret."

    strings:
        $linkedIn_secret_key0 = /[A-Za-z0-9]{16}/
        $API_linkedIn = "api.linkedin.com/v2"

    condition:
        $linkedIn_secret_key0 and $API_linkedIn

}

