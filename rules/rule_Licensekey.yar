rule IntelliJ_IDEA_14
{

    meta:
        description0 = "인텔리J => jetbrain 에서 출시한 java IDE 해당 IDE를 사용하기위한 LICENSE key 로 보임"

    strings:
        $IntelliJ_IDEA_140 = /^\.?idea14.key$/

    condition:
        $IntelliJ_IDEA_140

}

rule avastlic
{

    meta:
        description0 = "바이러스 백신 소프트웨어 라이센스 파일"

    strings:
        $avastlic0 = "avastlic"

    condition:
        $avastlic0

}

