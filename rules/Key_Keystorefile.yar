rule Java_keystore_file
{

    meta:
        description0 = "Authentication certificate or public key certificate with certificate used for SSL encryption"

    strings:
        $Java_keystore_file0 = "jks"

    condition:
        $Java_keystore_file0

}

