rule AWS_CLI_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $AWS_CLI_0 = /\.?aws/credentials$/

    condition:
        $AWS_CLI_0

}

