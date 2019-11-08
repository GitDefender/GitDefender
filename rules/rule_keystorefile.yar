rule Java_keystore_file
{

    meta:
        description0 = "Java KeyStore(JKS)는 SSL 암호화에 사용되는 인증서와 함께 인증 인증서 또는 공용 키 인증서 등 보안 인증서의 저장소를 말한다."

    strings:
        $Java_keystore_file0 = "jks"

    condition:
        $Java_keystore_file0

}

