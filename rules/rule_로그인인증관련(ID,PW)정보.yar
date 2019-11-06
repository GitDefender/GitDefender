rule password
{

    meta:
        description0 = "repo scanner 도구의 정의 >  Contains word: password  password 이름의 파일이 있는지 확인"
        description1 = "git dork 정의 : [WFClient] Password= extension:ica  [WFClient] = defining the WinFrame Client  .ICA 파일은 Windows 10, Windows 7, Windows 8/8.1, Windows Vista, Windows XP와 같은 운영 체제에서 사용되는 Settings Files 카테고리  http://docs.testplant.com/epp/9.0.0/ePP/cvuunderstanding_ica_file_contents.htm"

    strings:
        $password0 = "password"
        $password1 = "[WFClient] Password= "

    condition:
        $password0 or $password1

}

rule JSForce
{

    meta:
        description0 = "JSforce (f.k.a. Node-Salesforce)는 Salesforce의 API를 활용한 이형성 자바스크립트 라이브러리: 브라우저에서나 Node.js에서나 모두 작동한다.  비동기 자바스크립트 함수 호출에서 Salesforce가 제공하는 다양한 API에 대한 액세스를 캡슐화한다.  다른 Salesforce API 라이브러리와 달리 서버측과 클라이언트측 앱 모두를 통합 인터페이스에 제공하기 위한 것이므로, 다른 환경에서 실행하기 위해서만 서로 다른 라이브러리로 유사한 로직들을 다시 쓸 필요가 없다.  또한 대화형 콘솔(REPL)을 제공하는 유용한 CLI(명령줄 인터페이스)가 있어 번거로움 없이 사용법을 익힐 수 있다.  jsforce 에서 conn.login 메소드에서 login url userid, passeord를 인자로 받기 때문에 id pw 가 노출될 수 있다. >> 참고자료 : https://jsforce.github.io/document/ "

    strings:
        $JSForce0 = "jsforce conn.login"

    condition:
        $JSForce0

}

rule firefox
{

    meta:
        description0 = "Firefox는 데이터를 Firefox 프로필 폴더의 logins.json 파일에 저장한다."

    strings:
        $firefox0 = "logins.json"

    condition:
        $firefox0

}

rule Salesforce
{

    meta:
        description0 = "Firefox는 데이터를 Firefox 프로필 폴더의 logins.json 파일에 저장한다."

    strings:
        $Salesforce0 = "SF_USERNAME salesforce"

    condition:
        $Salesforce0

}

