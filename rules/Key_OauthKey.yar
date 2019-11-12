rule Google_Oauth
{

    meta:
        description0 = "Google OAuth key"

    strings:
        $Google_Oauth0 = /client_secret:[a-zA-Z0-9-_]{24}/
        $Google_Oauth1 = /(google|gcp|auth)(.{0,20})?['"][0-9]+-[0-9a-z_]{32}\.apps\.googleusercontent\.com['"]/

    condition:
        $Google_Oauth0 or $Google_Oauth1

}

rule Facebook_Oauth
{

    meta:
        description0 = "facebook client secret key"

    strings:
        $Facebook_Oauth0 = /[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]/

    condition:
        $Facebook_Oauth0

}

rule Github_Oauth
{

    meta:
        description0 = "Github OAuth Key"

    strings:
        $Github_Oauth0 = /[g|G][i|I][t|T][h|H][u|U][b|B].{0,30}['\"\\s][0-9a-zA-Z]{35,40}['\"\\s]/

    condition:
        $Github_Oauth0

}

rule Twitter_Oauth
{

    meta:
        description0 = "Twitter OAuth Key"

    strings:
        $Twitter_Oauth0 = /[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]/

    condition:
        $Twitter_Oauth0

}

rule Square_OAuth_secret
{

    meta:
        description0 = "Square OAuth Key"

    strings:
        $Square_OAuth_secret0 = /sq0csp-[0-9A-Za-z\\-_]{43}/

    condition:
        $Square_OAuth_secret0

}

