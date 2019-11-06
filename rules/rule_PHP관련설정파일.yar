rule PHP_config
{

    meta:
        description0 = "S3cmd는 Amazon S3 및 Google Cloud Storage 또는 DreamHost DreamObjects와 같은 S3 프로토콜을 사용하는 기타 클라우드 스토리지 서비스 공급자의 데이터를 업로드, 검색 및 관리하기위한 무료 명령 줄 도구이자 클라이언트입니다.  해당 cmd의 설정 파일인데 , 테스트 코드를 보면 누가 봐도 AWS key가 노출되었다는 것을 확인 할 수 있다."

    strings:
        $PHP_config0 = /config(\.inc)?\.php$/

    condition:
        $PHP_config0

}

