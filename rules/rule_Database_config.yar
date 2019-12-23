rule DBeaver
{

    meta:
        description0 = "여러 데이터베이스 통합 관리 도구로서 해당 서버가 사용하고 있는 database와 username, IP, password, port등을 알 수 있다."

    strings:
        $DBeaver0 = /\\A\\.?dbeaver-data-sources.xml\\z ^\.?dbeaver-data-sources.xml$/

    condition:
        $DBeaver0

}

rule Robomongo_MongoDB_manager
{

    meta:
        description0 = "robomongo > mongoDB를 사용하기위한 도구 해당 도구의 configration 파일 >데이터 베이스 자격증명 관련 정보 노출 username, userpassword, serverhost, port , 암복호화 키등 여러정보 노출"

    strings:
        $Robomongo_MongoDB_manager0 = "robomongo.json"

    condition:
        $Robomongo_MongoDB_manager0

}

rule _Oracle_SQL_Developer
{

    meta:
        description0 = "Oracle SQL Developer는 Oracle 데이터베이스에서 SQL과 함께 작업하기 위한 IDE(Integrated Development Environment)이다. Oracle Corporation은 이 제품을 무료로 제공하고 있으며 Java Development Kit를 사용한다.  DB 연결정보가 저장된 파일이다.  connections.xml 에 들어있는 내용 :  test connection anliases, ports, usernames, roles, authentcation types, etc  참조 :  https://papago.naver.com/?sk=en&tk=ko&hn=0&st=have%20an%20application%20that%20I%20can%25%2339t%20get%20connected%20to%20my%20Oracle%20Database%2011g%20Express%20Edition.%20I%20created%20a%20test%20database%20in%20this%20edition%2C%20and%20I%20can%20connect%20to%20the%20database%20fine%20using%20Oracle%20SQL%20Developer%2C%20"

    strings:
        $_Oracle_SQL_Developer0 = "connections.xml"

    condition:
        $_Oracle_SQL_Developer0

}

rule Sequel_Pro_MySQL_database_manager_bookmark_file
{

    meta:
        description0 = "mysql client환경에서 쓰는 Squel pro의 설정파일이다.  접속에 관련된  id, ip, port, password등의 정보를 포함하고 있다"

    strings:
        $Sequel_Pro_MySQL_database_manager_bookmark_file0 = " Favorites.plist"

    condition:
        $Sequel_Pro_MySQL_database_manager_bookmark_file0

}

rule PostgreSQL
{

    meta:
        description0 = "PostgreSQL의 연결 접속 설정 파일"

    strings:
        $PostgreSQL0 = /\\A\\.?pgpass\\z ^\.?pgpass$/

    condition:
        $PostgreSQL0

}

rule Apache_Phoenix
{

    meta:
        description0 = "PostgreSQL의 연결 접속 설정 파일"

    strings:
        $Apache_Phoenix0 = "prod.exs"

    condition:
        $Apache_Phoenix0

}

