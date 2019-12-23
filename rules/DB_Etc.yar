rule GnuCash
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $GnuCash0 = "gnucash"

    condition:
        $GnuCash0

}

rule GNOME_Keyring_
{

    meta:
        description0 = "GNOME Keyring database file"

    strings:
        $GNOME_Keyring_0 = "keystore"
        $GNOME_Keyring_1 = "keyring"


    condition:
        $GNOME_Keyring_0 or $GNOME_Keyring_1

}

