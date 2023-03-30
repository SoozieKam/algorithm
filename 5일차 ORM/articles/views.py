from django.shortcuts import render, redirect
from .models import Article

# Create your views here.


def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    # print(articles)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new에서 보낸 사용자 데이터를 받아야 함
    # print(request.GET)
    title_1 = request.POST.get('title')
    content_1 = request.POST.get('content')

    # 받은 데이터를 DB에 저장
    # 3번 방법은 되도록이면..사용X. 제약조건이 적용 안됨
    # Article.objects.create(title=title_1, content=content_1)

    article = Article(title=title_1, content=content_1)
    # 저장 전 유효성 검사
    article.save()

    # 결과 페이지 반환
    # return render(request, 'articles/create.html')

    # 결과 페이지(전체 조회 템플릿) 반환하면 안되나?
    # return render(request, 'articles/index.html')
    # 이렇게 하면 좀 이상한 페이지로 감 데이터 전체조회하지 않다 보니 데이터가 안나옴.

    # 여기부터는 페이지 대신 주소 응답 !!
    # 이동할 주소 (URL) 반환 (사용자에게 응답)
    # 페이지를 만드는 개념이 아니라 templates, context 만들 필요 없음.
    # return redirect('articles:index')
    #
    # 생성한 글의 단일 조회(detail) 주소(url)로 이동 응답
    return redirect("articles:detail", article.pk)


def delete(request, article_pk):
    # 삭제할 데이터 조회
    article = Article.objects.get(pk=article_pk)

    # 조회한 데이터 삭제 (DELETE)
    article.delete()

    # 전체 조회 페이지 이동
    return redirect("articles:index")


def edit(request, article_pk):
    # 수정할 데이터 조회
    article = Article.objects.get(pk=article_pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    # 수정 작업 과정
    # 1. 데이터 조회
    article = Article.objects.get(pk=article_pk)

    # 2. 데이터 수정
    # 2-1. 사용자가 입력한 form 데이터 저장
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2-2. 조회한 데이터(article)의 필드 값 변경
    article.title = title
    article.content = content

    # 3. 데이터 저장
    article.save()

    return redirect('articles:detail', article.pk)
