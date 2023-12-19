from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """Домашняя страница, на которой выводятся все посты"""
    blogposts = BlogPost.objects.order_by("-date_added")

    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)


def new_blogpost(request):
    """Определяет новый блогпост"""
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма
        form = BlogPostForm()
    else:
        # Отправленны данные POST; обработать данные.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)


def edit_blogpost(request, blogpost_id):
    """Рекдактирует существующий пост"""
    blogpost=BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        # Исходный запрос, форма заполняется данными текущего поста
        form = BlogPostForm(instance=blogpost)
    else:
        # Отправка данных POST, обработать данные
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)