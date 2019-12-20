rule password
{

    meta:
        description0 = "Contains password and id"

    strings:
        $password0 = "password"
        $password1 = "[WFClient] Password= "

    condition:
        $password0 or $password1

}

rule JSForce
{

    meta:
        description0 = "Expose ID and Password"

    strings:
        $JSForce0 = "jsforce conn.login"

    condition:
        $JSForce0

}

rule firefox
{

    meta:
        description0 = "Firefox data store logins.json"

    strings:
        $firefox0 = "logins.json"

    condition:
        $firefox0

}

rule Salesforce
{

    meta:
        description0 = "Salesforce User name"

    strings:
        $Salesforce0 = "SF_USERNAME salesforce"

    condition:
        $Salesforce0

}
