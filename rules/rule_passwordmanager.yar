rule agile
{

    meta:
        description0 = "gitrob 정의 :  1Password password manager database file  드롭박스로 검색을 해야 나오는 정보임 (보통 깃플젝에 없음)"

    strings:
        $agile0 = ".agilekeychain"

    condition:
        $agile0

}

rule Microsoft_BitLocker_Trusted_Platform_Module
{

    meta:
        description0 = "gitrob 정의 :  Microsoft BitLocker Trusted Platform Module/ 1password : 비밀번호 관리 솔루션 (보통 깃플젝에 없음)"

    strings:
        $Microsoft_BitLocker_Trusted_Platform_Module0 = ".tpm"

    condition:
        $Microsoft_BitLocker_Trusted_Platform_Module0

}

rule Password_Safe_
{

    meta:
        description0 = "password를 저장해주는 데이터베이스"

    strings:
        $Password_Safe_0 = "psafe3"

    condition:
        $Password_Safe_0

}

rule Apple_Keychain
{

    meta:
        description0 = "Apple사의 민감한 데이터를 암호화하여 저장하는 도구이다. 노출 시 키없이 복호화가 어렵다."

    strings:
        $Apple_Keychain0 = " keychain"

    condition:
        $Apple_Keychain0

}

rule KDE_Wallet_Manager
{

    meta:
        description0 = "여러 인증 시스템들의 ID, password를 통합관리하는 도구이다."

    strings:
        $KDE_Wallet_Manager0 = "kwallet"

    condition:
        $KDE_Wallet_Manager0

}

rule KeePass_password_manager
{

    meta:
        description0 = "여러 인증 시스템들의 ID, password를 통합관리하는 도구이다."

    strings:
        $KeePass_password_manager0 = "^kdbx?$"

    condition:
        $KeePass_password_manager0

}

