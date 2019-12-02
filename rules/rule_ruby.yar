rule Ruby_IRB_console_history_file
{

    meta:
        description0 = "mysql 각 각의 명령문을 .mysql_history에 올림. 명령어중에 password나 각 종 credential한 정보가 포함될 수 있음 추가적으로 table구조, 컬럼, 데이터등 노출가능"

    strings:
        $Ruby_IRB_console_history_file0 = /\\A\\.?irb_history\\z ^\.?irb_history$/

    condition:
        $Ruby_IRB_console_history_file0

}

