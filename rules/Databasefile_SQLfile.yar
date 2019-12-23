rule Microsoft_SQL
{

    meta:
        description0 = "Microsoft SQL database file"

    strings:
        $Microsoft_SQL0 = ".mdf"

    condition:
        $Microsoft_SQL0

}

rule Microsoft_SQL_server_compact
{

    meta:
        description0 = "It is a compact relational database format created by Microsoft. Full database content is included."

    strings:
        $Microsoft_SQL_server_compact0 = "sdf"

    condition:
        $Microsoft_SQL_server_compact0

}

rule SQLite
{

    meta:
        description0 = "sql contents-table structure, columns, data, etc."

    strings:
        $SQLite0 = "sqlite"

    condition:
        $SQLite0

}

rule Ruby_On_Rails_database_schema_file
{

    meta:
        description0 = "Database schema file. -Table structure, columns, data, etc."

    strings:
        $Ruby_On_Rails_database_schema_file0 = "schema.rb"

    condition:
        $Ruby_On_Rails_database_schema_file0

}

rule SQL_dump_file
{

    meta:
        description0 = "Database dump contains records from the table structure and data from the db, usually in the form of a list of sql statements."

    strings:
        $SQL_dump_file0 = /sql(dump)?/
        $SQL_dump_file1 = /\\Asql(dump)?\\z/

    condition:
        $SQL_dump_file0 or $SQL_dump_file1

}