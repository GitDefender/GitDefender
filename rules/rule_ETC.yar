rule yml_
{

    meta:
        description0 = "인텔리J => jetbrain 에서 출시한 java IDE 해당 IDE를 사용하기위한 LICENSE key 로 보임"

    strings:
        $yml_0 = "secrets.yml"

    condition:
        $yml_0

}

