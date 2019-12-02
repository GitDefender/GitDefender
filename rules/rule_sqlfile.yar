rule Microsoft_SQL_
{

    meta:
        description0 = "Microsoft SQL database file"

    strings:
        $Microsoft_SQL_0 = ".mdf"

    condition:
        $Microsoft_SQL_0

}

rule Microsoft_SQL_server_compact_
{

    meta:
        description0 = "마이크로소프트사에서 만든 컴팩트 관계형 데이터베이스 형식이다.  전체 데이터베이스 내용이 포함되어 있다."

    strings:
        $Microsoft_SQL_server_compact_0 = "sdf"

    condition:
        $Microsoft_SQL_server_compact_0

}

rule SQLite_
{

    meta:
        description0 = "sql 내용들이다. 테이블 구조, 컬럼, 데이터들의 노출 가능성이 있다"

    strings:
        $SQLite_0 = "sqlite"

    condition:
        $SQLite_0

}

rule Ruby_On_Rails_database_schema_file
{

    meta:
        description0 = "database schema 파일이다. 테이블 구조, 컬럼, 데이터등의 노출 가능성이 있다"

    strings:
        $Ruby_On_Rails_database_schema_file0 = "schema.rb"

    condition:
        $Ruby_On_Rails_database_schema_file0

}

rule SQL_dump_file
{

    meta:
        description0 = "database schema 파일이다. 테이블 구조, 컬럼, 데이터등의 노출 가능성이 있다"

    strings:
        $SQL_dump_file0 = "^sql(dump)?$"

    condition:
        $SQL_dump_file0

}

