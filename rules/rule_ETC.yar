rule yml_
{

    meta:
        description0 = "사용하는 API 키정보를 모아둔 파일, 그래서 API키 정보가 노출 될 수 있음"

    strings:
        $yml_0 = "secrets.yml"

    condition:
        $yml_0

}

