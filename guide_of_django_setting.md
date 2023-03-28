# Django 개발 환경 설정 가이드

# 0. 왜 가상환경 설정이 필요한지 ?

협업 시 버전 간 충돌을 방지하기 위함.
모든 팀원이 동일한 환경과 의존성 아래에서 작업할 수 있음.
또한 라이브러리 및 패키지를 각 프로젝트마다 따로 사용하여 프로젝트를 독립적으로 관리할 수 있음.

# 1. 가상환경 생성

$ python -m venv venv
파이썬 모듈 중 'venv' 라는 모듈을 사용하여 'venv'라는 이름의 가상환경을 만든다는 뜻.
원하는 경로에서 터미널을 실행하고 위의 내용을 입력하면
venv라는 이름의 새로운 파일이 생성됨.
이때 가상환경 이름은 venv 로 고정하는 게 편함
$

# 1-추가. ctrl + shift + P 눌러서 파이썬 버전 설정

python: Select Interpreter > 앞서 생성한 'venv' 폴더가 표시된 파이썬 버전 선택
그럼 자동으로 2번이 됨...

# 2. 가상환경 활성화

$ source venv/Scripts/Activate
scripts와 activate는 자동완성 됨 (Tab 사용)
이 내용을 입력하면 터미널 창에 (venv) 라는 표시가 뜸. 가상환경 진입에 성공했다는 의미.
$

# 3. Django 설치

$ pip install django==3.2.18
버전을 안써주면 자동으로 최신 버전이 설치됨.
$
requirements.txt 가 이미 있는 파일을 pull 받은 경우
위에거 대신 pip install -r requirements.txt 하면 됨.

# 4. 의존성 파일 생성

$ pip freeze > requirements.txt
패키지 설치 시마다 진행해야 함.
$

# 5. .gitignore 설정

첫 add를 하기 전 설정해야 함!
https://www.toptal.com/developers/gitignore/
위 링크에서 'Django, Python, Windows, Mac, VisualStudioCode' 등 필요한 것들을 다 입력한 후 생성! 이후 .gitignore 파일에 생성된 내용 복붙하면 끝.

# 6. django 프로젝트 생성

$ django-admin startproject firstpjt .
'firstpjt' 라는 이름의 프로젝트를 생성한다는 뜻.
완료하면 해당 경로에 폴더 생성됨.
마지막 '.' 놓치지 말기!
$

# 7. django 서버 실행

$ python manage.py runserver

# 마지막으로 장고 서버인 http://127.0.0.1:8000/ 에 접속해서 로켓 발사 페이지가 나오면 성공!

# 서버 중지 : Ctrl + C

`~
$

# 8. django 앱 생성

$ python manage.py startapp articles
마지막 articles 부분 대신 원하는 앱 이름을 넣으면 됨
이 부분은 향후 링크 뒤에 붙을 것 $

# 9. settings.py 의 'ISTALLED_APPS' 목록에 앱 추가

# 10. urls.py 파일 수정

1. 아래 내용 추가
   from 앱 이름 import views

2. urlpatterns 리스트에 아래 내용 추가
   path('articles/', views.index),

index는 html 파일 이름에 맞게 수정하면 됨

# 11. views.py 파일 수정

아래 내용 추가
def index(request):
return render(request, 'articles/index.html')

생성된 앱 폴더 안에 'templates' 폴더 생성,
그 안에 또 앱 이름으로 된 폴더 생성
그 폴더 안에 html 파일 넣기.

# 12. 7번 'django 서버 실행' 후 확인 !

## model 을 통한 DB 관리

# 1. 테이블 설계를 위한 models.py 작성

articles/models.py 에 테이블 내용 작성
양식: 클래스 변수명 = models.메서드(제약조건)

class Article(models.Model):
title = models.CharField(max_length=30)
content = models.TextField()

# 2. migration 시작

$ python manage.py makemigrations (설계도 작성 단계)
$ python manage.py migrate (설계도를 DB에 전달, 반영)

# 3. 모델 필드 추가할 경우

3.1 models.py에 모델 필드 작성
3.2 makemigrations 명령어 - 1번 (직접 기본 값 입력)
3.3 migrate 명령어

# 4. admin 계정 생성

자동으로 관리자 인터페이스 제공,
데이터 관련 테스트 및 확인 용

$ python manage.py createsuperuser $

# 5. admin에 모델 클래스 등록

articles/admin.py 에 아래 내용 추가

from .models import Article(Article은 클래스 이름>)

admin.site.register(Article)

## django shell_plus

# 1. 패키지 설치

$ pip install ipython
$ pip install django_extensions

# 2. django_extensions App 등록

settings.py
INSTALLED_APPS 리스트에 django_extensions 추가

INSTALLED_APPS = [

# 생략 ...

"django_extensions",
]

# 3. shell 진입

$ python manage.py shell_plus
$

# 4.
