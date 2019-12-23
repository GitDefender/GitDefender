rule MySQL_history
{

    meta:
        description0 = "mysql 각 각의 명령문을 .mysql_history에 올림. 명령어중에 password나 각 종 credential한 정보가 포함될 수 있음 추가적으로 table구조, 컬럼, 데이터등 노출가능"

    strings:
        $MySQL_history0 = /\\A\\.?mysql_history\\z ^\.?mysql_history$/

    condition:
        $MySQL_history0

}

rule PostgreSQL_history_
{

    meta:
        description0 = "mysql 각 각의 명령문을 .mysql_history에 올림. 명령어중에 password나 각 종 credential한 정보가 포함될 수 있음 추가적으로 table구조, 컬럼, 데이터등 노출가능"

    strings:
        $PostgreSQL_history_0 = /\\A\\.?psql_history\\z ^\.?psql_history$/

    condition:
        $PostgreSQL_history_0

}

