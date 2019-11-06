rule LinkedIn_ID
{

    meta:
        description0 = "LinkedIn ID를 의미한다."

    strings:
        $LinkedIn_ID0 = /(?i)linkedin(.{0,20})?(?-i)['\"][0-9a-z]{12}['\"]/

    condition:
        $LinkedIn_ID0

}

rule Twitter__client_ID
{

    meta:
        description0 = "Tweiiter client ID를 의미한다."

    strings:
        $Twitter__client_ID0 = /(?i)twitter(.{0,20})?['\"][0-9a-z]{18,25}['\"]/

    condition:
        $Twitter__client_ID0

}

rule FACEBOOK_Client_ID
{

    meta:
        description0 = "Tweiiter client ID를 의미한다."

    strings:
        $FACEBOOK_Client_ID0 = /(?i)(facebook|fb)(.{0,20})?['\"][0-9]{13,17}['\"]/

    condition:
        $FACEBOOK_Client_ID0

}

