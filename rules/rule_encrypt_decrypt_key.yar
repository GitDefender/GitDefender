rule Private_SSH_key
{

    meta:
        description0 = "공개키"
        description1 = "공개키"
        description2 = "공개키"
        description3 = "공개키"

    strings:
        $Private_SSH_key0 = /\\A.*_rsa\\z ^.*_rsa$/
        $Private_SSH_key1 = /\\A.*_dsa\\z ^.*_dsa$/
        $Private_SSH_key2 = /\\A.*_ed25519\\z/
        $Private_SSH_key3 = /\\A.*_ecdsa\\z/

    condition:
        $Private_SSH_key0 or $Private_SSH_key1 or $Private_SSH_key2 or $Private_SSH_key3

}

rule Potential_cryptographic__private_key
{

    meta:
        description0 = ".pem: X.509 v3 파일의 한 형태 PEM (Privacy Enhanced Mail)은 Base64인코딩된 ASCII text file이다. 원래는 secure email에 사용되는 인코딩 포멧이었는데 더이상 email쪽에서는 잘 쓰이지 않고 인증서 또는 키값을 저장하는데 많이 사용된다. -----BEGIN XXX-----, -----END XXX----- 로 묶여있는 text file을 보면 이 형식으로 인코딩 되어있다고 생각하면 된다. (담고있는 내용이 무엇인지에 따라 XXX 위치에 CERTIFICATE, RSA PRIVATE KEY 등의 키워드가 들어있다) 인증서(Certificate = public key), 비밀키(private key), 인증서 발급 요청을 위해 생성하는 CSR (certificate signing request) 등을 저장하는데 사용된다.  https://www.letmecompile.com/certificate-file-format-extensions-comparison/"
        description1 = "PuTTYgen에 의해 생성 된 파일을 PPK 파일 개인키가 포함되어 있다"
        description2 = "명확하게 어떤 서비스의 복호화 보다는 범용적으로 keypair 라는 키워드로 모든 암복호화에 사용되는 키를 찾는 느낌 "

    strings:
        $Potential_cryptographic__private_key0 = "pem"
        $Potential_cryptographic__private_key1 = "ppk"
        $Potential_cryptographic__private_key2 = /\\Akey(pair)?\\z ^key(pair)?$/

    condition:
        $Potential_cryptographic__private_key0 or $Potential_cryptographic__private_key1 or $Potential_cryptographic__private_key2

}

rule Chef_private_key
{

    meta:
        description0 = "Chef 서버에 대한 인증에 사용할 수 있음(개인키파일)"

    strings:
        $Chef_private_key0 = /\.?chef/(.*)\.pem$/

    condition:
        $Chef_private_key0

}

rule Potential_cryptographic__key_bundle
{

    meta:
        description0 = "인증서 키파일 (raw data 로 존재)"
        description1 = "인증서 키파일 (raw data 로 존재)"
        description2 = "인증서 키파일 (raw data 로 존재)"
        description3 = "인증서 키파일 (raw data 로 존재)"

    strings:
        $Potential_cryptographic__key_bundle0 = ".pkcs12"
        $Potential_cryptographic__key_bundle1 = ".pfx"
        $Potential_cryptographic__key_bundle2 = ".p12"
        $Potential_cryptographic__key_bundle3 = ".asc"

    condition:
        $Potential_cryptographic__key_bundle0 or $Potential_cryptographic__key_bundle1 or $Potential_cryptographic__key_bundle2 or $Potential_cryptographic__key_bundle3

}

rule Pidgin_OTR_private_key
{

    meta:
        description0 = "Pidgin > OTR 프로토콜을 사용하는 채팅 프로그램   OTR> 비밀 메신저 프로토콜  // OTF 프로토콜의 private key 가 노출되는 케이스"

    strings:
        $Pidgin_OTR_private_key0 = "otr.private_key"

    condition:
        $Pidgin_OTR_private_key0

}

rule Generic_private_key
{

    meta:
        description0 = "repo scanner 도구의 정의 >  Contains word: private, key  private, key 이름의 파일이 있는지 확인"

    strings:
        $Generic_private_key0 = "private.*key"

    condition:
        $Generic_private_key0

}

rule PGP_private_key
{

    meta:
        description0 = "PGP(Pretty Good Privacy)는 데이터 암호화 및 암호 해독 컴퓨터 프로그램으로, 데이터 통신에 암호 프라이버시와 인증을 제공한다. PGP는 전자우편 통신의 보안을 강화하기 위해 텍스트, 전자우편, 파일, 디렉터리 및 전체 디스크 파티션에 서명, 암호화 및 암호 해독하는 데 자주 사용된다."

    strings:
        $PGP_private_key0 = "-----BEGIN PGP PRIVATE KEY BLOCK-----"

    condition:
        $PGP_private_key0

}

rule EC_private_key
{

    meta:
        description0 = "open ssl 에서 사용하는  타원 곡선 암호 = EC 이 암호화를 할때 사용하는  key https://wiki.openssl.org/index.php/Command_Line_Elliptic_Curve_Operations"

    strings:
        $EC_private_key0 = "-----BEGIN EC PRIVATE KEY-----"

    condition:
        $EC_private_key0

}

rule Generic_secret_key
{

    meta:
        description0 = "30 글자 secret~ entropy가 어느정도 있는 key로 사용되는 문자열로 추측 , 확실한 정보는 없음"
        description1 = "20 글자 secret~ entropy가 어느정도 있는 key로 사용되는 문자열로 추측, 확실한 정보는 없음"

    strings:
        $Generic_secret_key0 = /"[s|S][e|E][c|C][r|R][e|E][t|T].{0,30}['\"\\s][0-9a-zA-Z]{32,45}['\"\\s]/
        $Generic_secret_key1 = /(?i)secret(.{0,20})?['|"][0-9a-zA-Z]{32,45}['|"]/

    condition:
        $Generic_secret_key0 or $Generic_secret_key1

}

rule PKCS8
{

    meta:
        description0 = "인증서 관련 키 파일"

    strings:
        $PKCS80 = "-----BEGIN PRIVATE KEY-----"

    condition:
        $PKCS80

}

rule PGP_
{

    meta:
        description0 = "인증서 관련 키 파일"

    strings:
        $PGP_0 = "-----BEGIN PGP PRIVATE KEY BLOCK-----"

    condition:
        $PGP_0

}

rule RSA
{

    meta:
        description0 = "인증서 관련 키 파일"

    strings:
        $RSA0 = "-----BEGIN RSA PRIVATE KEY-----"

    condition:
        $RSA0

}

rule SSH_OPENSSH
{

    meta:
        description0 = "인증서 관련 키 파일"

    strings:
        $SSH_OPENSSH0 = "-----BEGIN OPENSSH PRIVATE KEY-----"

    condition:
        $SSH_OPENSSH0

}

rule Rails__encrypted_credentials_key_암호화된_인증서_키
{

    meta:
        description0 = "인증서 관련 키 파일"

    strings:
        $Rails__encrypted_credentials_key_암호화된_인증서_키0 = /\\.?config/master\\.key\\z/

    condition:
        $Rails__encrypted_credentials_key_암호화된_인증서_키0

}
