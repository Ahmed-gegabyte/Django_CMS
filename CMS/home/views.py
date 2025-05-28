from django.shortcuts import render, get_object_or_404, redirect
from home.models import Article
from .forms import ArticleForm  # Import the form you will create
#superuser Admin , admin
# Create your views here.

def home(request):
    articles = Article.objects.all().order_by('-created_at')[:3]  # Show top 3 or whatever
    return render(request, 'html/home.html', {'articles': articles})

"""def home(request):
    return render(request , 'home.html')"""

def add_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title = title , content = content )
        article.save()
        print('Save in DB successfully')
    return render(request , 'html/add_article.html')

# View to list all articles
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')  # Fetch all articles, order by creation date
    return render(request, 'html/article_list.html', {'articles': articles})

# View to display a single article's detail
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)  # Get the article by its ID or return a 404 error
    return render(request, 'html/article_detail.html', {'article': article})

def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('html/article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'html/article_form.html', {'form': form, 'article': article})

def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('article_list')

    return render(request, 'html/article_confirm_delete.html', {'article': article})