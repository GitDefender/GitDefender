rule agile
{

    meta:
        description0 = "Password password manager database file"

    strings:
        $agile0 = ".agilekeychain"

    condition:
        $agile0

}

rule Microsoft_BitLocker_Trusted_Platform_Module
{

    meta:
        description0 = "Microsoft BitLocker Trusted Platform Module/ password"

    strings:
        $Microsoft_BitLocker_Trusted_Platform_Module0 = ".tpm"

    condition:
        $Microsoft_BitLocker_Trusted_Platform_Module0

}

rule Password_Safe_
{

    meta:
        description0 = "store password in database."

    strings:
        $Password_Safe_0 = "psafe3"

    condition:
        $Password_Safe_0

}

rule Apple_Keychain
{

    meta:
        description0 = "This tool encrypts and stores Apple's sensitive data."

    strings:
        $Apple_Keychain0 = "keychain"

    condition:
        $Apple_Keychain0

}

rule KDE_Wallet_Manager
{

    meta:
        description0 = "It is a tool to manage ID and password of various authentication systems."

    strings:
        $KDE_Wallet_Manager0 = "kwallet"

    condition:
        $KDE_Wallet_Manager0

}

rule KeePass_password_manager
{

    meta:
        description0 = "KeePass password manager database file."

    strings:
        $KeePass_password_manager0 = "kdbx"

    condition:
        $KeePass_password_manager0

}

