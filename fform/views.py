from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect

def post(request):
	return render(request, 'post.html')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
             return render(request,'post.html')
    else:
        form = PostForm()
        return render(request, 'post_edit.html', {'form': form})
