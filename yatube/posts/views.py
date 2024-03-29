from django.shortcuts import render, get_object_or_404
from .models import Group, Post


def index(request):
    amount = 10
    posts = Post.objects.order_by('-pub_date')[:amount]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    amount = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:amount]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
