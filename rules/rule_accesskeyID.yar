rule AWS_API_CLIENT_ID
{

    meta:
        description0 = "Tweiiter client ID를 의미한다."

    strings:
        $AWS_API_CLIENT_ID = "aws_access_key_id"

    condition:
        $AWS_API_CLIENT_ID

}
