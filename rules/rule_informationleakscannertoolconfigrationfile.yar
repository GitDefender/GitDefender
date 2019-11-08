rule Gitrob
{

    meta:
        description0 = "chef-repo 특정 구성 세부 사항을 지정하는데 사용된다.  clinet_key를 통해 클라이언트 키가 포함된 파일의 위치가 노출되며,  cookbook_email을 통한 개인의 Email,  validation_key를 통해 chef_client가 Chef 서버에 등록 될 때 사용되는 키가 포함된 파일의 위치를 알 수 있다 https://docs.chef.io/knife.html https://docs.chef.io/config_rb.html"

    strings:
        $Gitrob0 = /\\A\\.?gitrobrc\\z ^\.?gitrobrc$/

    condition:
        $Gitrob0

}

