rule SSH_configuration_file
{

    meta:
        description0 = "포트가 보이게 되면 , 포트를 통해 공격시나리오를 구성할수 있다. 예를 들면 SMTP취약점의 경우 25번 포트를 이용하는데 25번 포트를 이용한다면 공격시나리오를 재구성할 근거가 된다."

    strings:
        $SSH_configuration_file0 = /\\.?ssh/config\\z \.?ssh/config$/

    condition:
        $SSH_configuration_file0

}

rule Jenkins_publish_over_SSH_plugin
{

    meta:
        description0 = "포트가 보이게 되면 , 포트를 통해 공격시나리오를 구성할수 있다. 예를 들면 SMTP취약점의 경우 25번 포트를 이용하는데 25번 포트를 이용한다면 공격시나리오를 재구성할 근거가 된다."

    strings:
        $Jenkins_publish_over_SSH_plugin0 = "jenkins.plugins.publish_over_ssh.BapSshPublisherPlugin.xml"

    condition:
        $Jenkins_publish_over_SSH_plugin0

}

