rule Azure
{

    meta:
        description0 = "Azure service에 대한 환경설정으로서 API key가 나올 수있고 username, password등 설정에 관련된 credentail한 정보를 포함하고 있다 + 서비스 구성 파일은 서비스의 각 역할에 대해 배포할 역할 인스턴스의 수, 구성 설정의 값 및 역할에 연결된 인증서의 지문을 지정 서비스가 Virtual Network의 일부인 경우, 가상 네트워킹 구성 파일 뿐 아니라 서비스 구성 파일에도 네트워크에 대한 구성 정보를 제공"

    strings:
        $Azure0 = "cscfg"

    condition:
        $Azure0

}

rule Carrierwave
{

    meta:
        description0 = "Can contain credentials for cloud storage systems such as Amazon S3 and Google Storage 클라우드 시스템의 크리덴셜한 정보가 노출 될 수있다."

    strings:
        $Carrierwave0 = "carrierwave.rb"

    condition:
        $Carrierwave0

}

rule openshift
{

    meta:
        description0 = "       express.conf - configuration file for OpenShift rhc 클라이언트 도구를 처음 사용할 때 생성되며 시스템 사용자별로 사용자 지정할 수 있습니다"

    strings:
        $openshift0 = "openshift/express.conf"

    condition:
        $openshift0

}

rule S3cmd
{

    meta:
        description0 = "S3cmd는 Amazon S3 및 Google Cloud Storage 또는 DreamHost DreamObjects와 같은 S3 프로토콜을 사용하는 기타 클라우드 스토리지 서비스 공급자의 데이터를 업로드, 검색 및 관리하기위한 무료 명령 줄 도구이자 클라이언트입니다.  해당 cmd의 설정 파일인데 , 테스트 코드를 보면 누가 봐도 AWS key가 노출되었다는 것을 확인 할 수 있다."

    strings:
        $S3cmd0 = /\\A\\.?s3cfg\\z ^\.?s3cfg$/

    condition:
        $S3cmd0

}

rule Terraform_variable
{

    meta:
        description0 = "S3cmd는 Amazon S3 및 Google Cloud Storage 또는 DreamHost DreamObjects와 같은 S3 프로토콜을 사용하는 기타 클라우드 스토리지 서비스 공급자의 데이터를 업로드, 검색 및 관리하기위한 무료 명령 줄 도구이자 클라이언트입니다.  해당 cmd의 설정 파일인데 , 테스트 코드를 보면 누가 봐도 AWS key가 노출되었다는 것을 확인 할 수 있다."

    strings:
        $Terraform_variable0 = "terraform.tfvars"

    condition:
        $Terraform_variable0

}

