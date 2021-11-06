------

**Repository name:** 저장소의 이름

**Description:** 저장소에 대한 간단한 설명

 

**Public:** 저장소를 모두에게 공개

**Private:** 지정된 사람에게만 공개

 

**initialize this repository with a README**를 체크해주면

저장소가 생성될 때 **README.md** 파일이 자동으로 함께 생성된다.

 

모두 작성했다면 아래의 **Create repository** 버튼을 눌러 저장소를 생성해줍니다.

 

 

### **3. 내 컴퓨터에서 원격 저장소 가져오기**

 

로컬 저장소를 만들 디렉토리를 하나 생성해줍니다.

 

디렉터리 마우스 우클릭 - Git Bash here (윈도우 기준/Linux, Mac의 경우 터미널 열기)

 



![img](https://blog.kakaocdn.net/dn/dAcHkV/btq3UjJsx89/QHt2mVtkKkS8KrwqQ8oNi0/img.png)



 

**git 초기 설정(Git을 설치하고 초기 설정이 안된 분들은 해주셔야 합니다.)**

 

**[] 생략해주시고 가입이름, 이메일을 넣어주시면 됩니다.**



![img](https://blog.kakaocdn.net/dn/VXLZ3/btq3TsUBT2E/iDvcjBPnLCs5JMOZMbppk0/img.png)가입 이름 등록



 



![img](https://blog.kakaocdn.net/dn/kRwrC/btq3UbLEqNp/ckqiTCrnockMWoYEs85Z10/img.png)가입 이메일 등록



 

앞서 생성한 저장소를 가져오기전에 먼저 생성한 Repository로 이동하여 HTTPS에 해당하는 url을 복사해줍니다.



![img](https://blog.kakaocdn.net/dn/bLLQhP/btq3U6v55b9/LvCoejXxKCR1VAv11GN8bk/img.png)



그러고 나서 git init을 입력해줍니다.

 



![img](https://blog.kakaocdn.net/dn/dvSNJ5/btq3UGdnTXt/e8gW9RATJmCM81K0aVmvOK/img.png)



 

그럼 이제 디렉터리 안에 .git이라는 폴더가 생긴 것을 확인합니다.

 

그다음 git add .를 해줍니다.

 



![img](https://blog.kakaocdn.net/dn/bEH3l2/btq3XtK5rAm/caFjMMp4zsDhRxZfPJVZM0/img.png)git add .(또는 특정 파일이나 폴더)



그다음은 git commit - "커밋 메세지"로 커밋 로그를 작성해줍니다.



![img](https://blog.kakaocdn.net/dn/WLnnP/btq3WnEmmNz/CD69GZfw04IwwMZBKnLPnK/img.png)



 

 

 



![img](https://blog.kakaocdn.net/dn/vrkPu/btq3S0KVH7O/5m5ZKDuPpfj6ZJttq36J8k/img.png)



만약 위와 같은 에러가 뜬다면 다시 git init을 해줍니다.

 



![img](https://blog.kakaocdn.net/dn/bDMou6/btq3ThMn2dW/1ArTxZKDhKX2JquolOmgQk/img.png)



 

다시 git add . 와 git commit을 해주시면 됩니다.

 

------

 

### **3. push**

 

마지막으로 commit한 파일을 원격 저장소로 업로드(push)를 해줍니다.

 



![img](https://blog.kakaocdn.net/dn/ewnfzj/btq3TxIhLA3/9yqBoiMz8uo8Hx9hnayl71/img.png)



**origin:** 원격 저장소의 주소(Repository로 이동하여 HTTPS에 해당하는 url을 복사한 값 넣어주시면 됩니다.)

 

 

#### ***\* 붙여넣기: Shift + insert \****

 

위 명령어를 입력하시고 나면



![img](https://blog.kakaocdn.net/dn/dMX9Jt/btq3Xa5Rz5J/EOx5nt793No8Pr9nSoIG11/img.png)



 



![img](https://blog.kakaocdn.net/dn/b5xwKY/btq3WoiYDUG/y0qRKGE3JrK2qfk0ei5CbK/img.png)

![img](https://blog.kakaocdn.net/dn/bXDfCF/btq3TWVi2QB/P7rvMrhD6EqgPzPzKdMOL1/img.png)



 

다음과 같은 Github 로그인 창이 뜨는데 이름과 비밀번호를 입력하고 로그인해주면 최종적으로 push가 됩니다.

 

최종적으로 Github 저장소로 가셔서 올린 파일과 커밋 로그가 정상적으로 올라가셨으면 성공입니다.

 