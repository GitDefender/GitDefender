rule PHP_config
{

    meta:
        description0 = "database 설정 부분(user, password, type, host), email, GET, POST 메소드 사용시 XSS 공격을 전역적으로 방어할지, 쿠키설정, CSRF 설정 등등 정보 노출."

    strings:
        $PHP_config0 = /config(\.inc)?\.php$/

    condition:
        $PHP_config0

}

