from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.conf import settings
from django.http import Http404


def index(request):
    return render(
        request,
        'blog/index.html',
        {'post_list': Post.objects.published()[:settings.POSTS_PER_PAGE]}
    )


def post_detail(request, id):
    post = get_object_or_404(Post.objects.published(), id=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    post_list = category.posts.published()
    if not post_list.exists():
        raise Http404
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })
