rule Ruby_On_Rails
{

    meta:
        description0 = "rails > 루비로 작성된 웹프레임 워크  잠재적인 데이터베이스의 configration 파일 >  데이터 베이스 자격증명 관련 정보 노출 ip, port, username,pw, mac address등 많은 정보 노출"

    strings:
        $Ruby_On_Rails0 = "database.yml"

    condition:
        $Ruby_On_Rails0

}

rule Django
{

    meta:
        description0 = "django 프레임워크의 설정파일 secret key노출과 databases 설정정보, debug모드 on off에 대해 알 수 있음"

    strings:
        $Django0 = "settings.py"

    condition:
        $Django0

}

rule Drupal
{

    meta:
        description0 = "django 프레임워크의 설정파일 secret key노출과 databases 설정정보, debug모드 on off에 대해 알 수 있음"

    strings:
        $Drupal0 = "databases password"

    condition:
        $Drupal0

}

