rule Git_credential_store_helper_ : need_config
{

    meta:
        description0 = "repo - scanner :git-credential-store helper credentials file"

    strings:
        $Git_credential_store_helper_0 = /^\.?git-credentials$/

    condition:
        $Git_credential_store_helper_0

}

