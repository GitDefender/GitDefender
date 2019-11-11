rule mongolab
{

    meta:
        description0 = "Managed Cloud Database Services Hosting Mongolia DB Databases"
    strings:
        $mongolab0 = "mongolab.com"

    condition:
        $mongolab0

}

rule slack_webhook
{

    meta:
        description0 = "Simple way to post messages with Slack in app, unique URL for JSON payload with message text and some options when creating webhook"

    strings:
        $slack_webhook0 = /https:\/\/hooks.slack.com\/services\/T[a-zA-Z0-9_]{8}\/B[a-zA-Z0-9_]{8}\/[a-zA-Z0-9_]{24}/

    condition:
        $slack_webhook0

}

rule Password_in_URL
{

    meta:
        description0 = "http: // username: password@example.com works only on FireFox, Chrome, and Safari, not IE."

    strings:
        $Password_in_URL0 = /[a-zA-Z]{3,10}:\/\/[^/\\\s:@]{3,20}:[^/\\\s:@]{3,30}@.{1,100}[\"'\\\s]/

    condition:
        $Password_in_URL0

}

rule Mongo_DB
{

    meta:
        description0 = "MongoDB password, port number, etc.
"

    strings:
        $Mongo_DB0 = ".mlab.com password"

    condition:
        $Mongo_DB0

}

rule RDS
{

    meta:
        description0 = "Amazon rds instance password"

    strings:
        $RDS0 = "rds.amazonaws.com password"

    condition:
        $RDS0

}

