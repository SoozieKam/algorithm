from django.db import models

# Create your models here.
class Article(models.Model):
    # 필드 이름(변수명) / 데이터 타입 / 제약조건 (모델 필드 클래스의 키워드 인자)
    # id 필드는 자동 생성
    # model 클래스 하나는 테이블 하나
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 기본값은 false
    updated_at = models.DateTimeField(auto_now=True) # 기본값은 false