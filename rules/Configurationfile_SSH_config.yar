rule SSH_configuration_file
{

    meta:
        description0 = "SSH configuration file"

    strings:
        $SSH_configuration_file0 = /\\.?ssh\/config\\z/
        $SSH_configuration_file1 = /\.?ssh\/config/

    condition:
        $SSH_configuration_file0 or $SSH_configuration_file1

}


rule Jenkins_publish_over_SSH_plugin
{

    meta:
        description0 = "Jenkins publish over SSH plugin"

    strings:
        $Jenkins_publish_over_SSH_plugin0 = "jenkins.plugins.publish_over_ssh.BapSshPublisherPlugin.xml"

    condition:
        $Jenkins_publish_over_SSH_plugin0

}

