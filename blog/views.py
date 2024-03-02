from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_new(request):
    pass

@login_required
def post_list(request):
    Post.objects.filter().order_by('published_date')
    return render(request, 'blog/post_list.html', {})

@login_required
def post_edit():
    pass

@login_required
def post_remove():
    pass