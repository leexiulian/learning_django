from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
	"""主页面"""
	articles = Article.objects.all()
	context = {'articles':articles}
	return render(request,'blog/index.html',context)

def article_page(request,article_id):
	"""文章详情页"""
	article = Article.objects.get(id=article_id)
	context = {'article':article}
	return render(request,'blog/article_page.html',context)

def edit_page(request,article_id):
	if str(article_id) == '0':
		return render(request,'blog/edit_page.html')
	else:
		article = Article.objects.get(pk=article_id)
		context = {'article':article}
		return render(request,'blog/edit_page.html',context)

def edit_action(request):
	title = request.POST.get('title','Title')
	content = request.POST.get('content','Content')
	article_id = request.POST.get('article_id')
	if article_id == '0':
		Article.objects.create(title=title,content=content)
		articles = Article.objects.all()
		context = {'articles':articles}
		return render(request,'blog/index.html',context)
	else:
		article = Article.objects.get(id=article_id)
		article.title = title
		article.content = content
		article.save()
		context = {'article':article}
		return render(request,'blog/article_page.html',context)
