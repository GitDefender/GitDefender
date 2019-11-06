rule Git-credential-store_helper_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $Git-credential-store_helper_0 = /^\.?git-credentials$/

    condition:
        $Git-credential-store_helper_0

}

