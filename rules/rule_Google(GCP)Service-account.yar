rule Google_GCP_Service
{
    meta:
     description = "서비스 계정은 개별 최종 사용자가 아닌 애플리케이션 또는 가상 머신에 속한 특별한 유형의 Google 계정입니다. 애플리케이션이 서비스 계정 ID를 사용하여 Google API를 호출하므로 사용자가 직접 관여하지 않습니다. 서비스 계정은 Google에 인증하는 데 사용되는 서비스 계정 키의 쌍을 0개 이상 보유할 수 있습니다.
"
    strings:
     $google_gcp_service= /"\"type\": \"service_account\""/
    condition:
     $google_gcp_service
}