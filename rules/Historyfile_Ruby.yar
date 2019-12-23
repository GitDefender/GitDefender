rule Ruby_IRB_console_history_file
{

    meta:
        description0 = "Provide continuous sharing records to IRB through DRB"

    strings:
        $Ruby_IRB_console_history_file0 = /\.irb_history/

    condition:
        $Ruby_IRB_console_history_file0

}