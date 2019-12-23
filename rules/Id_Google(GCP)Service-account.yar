rule Google_GCP_Service
{
    meta:
     description = "gcp service id"
    strings:
     $google_gcp_service= /"\"type\": \"service_account\""/
    condition:
     $google_gcp_service
}