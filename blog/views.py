from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.db.models import Q


def post_list(request):
    posts = Post.objects.filter(Q(published_date__lte=timezone.now()) & ~Q(title='Sample title 2')).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
