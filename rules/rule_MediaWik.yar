rule MediaWiki_config
{

    meta:
        description0 = "미디어 위키에 관련된 DB접속 정보, 사용자 그룹별 열람/편집 정보 확인 가능, 파일 업로드 가능 확장자 파악가능."

    strings:
        $MediaWiki_config0 = "LocalSettings.php"

    condition:
        $MediaWiki_config0

}

