rule Java_keystore_file
{

    meta:
        description0 = "facebook api를 사용할때 쓰는 key"

    strings:
        $Java_keystore_file0 = "jks"

    condition:
        $Java_keystore_file0

}

