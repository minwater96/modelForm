from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터를 저장

    # ==========

    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 사용자가 입력한 데이터를 저장

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid(): # 데이타를 제대로 입력했는지 확인
            form.save() # True값 저장
            return redirect('articles:index')

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

def delete(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.delete()

    return redirect('articles:index')

def update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':    
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form': form
    }

    return render(request, 'form.html', context)

