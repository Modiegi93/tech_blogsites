#!/usr/bin/python3
from django.shortcuts import render, get_object_or_404, redirect
from .forms import import BlogPostForm
from .models import BlogPost


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            if 'save_draft' in request.POST:
                blog_post.draft = True # Set the draft status
                blog_post.save()
                return redirect('blog:drafts') # Redirect to drafts
            else:
                blog_post.save()
                return redirect('blog:detail', pk=blog_post.pk)

    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

def blog_post_list(request):
    blog_posts = BlogPost.objects.filter(draft=False) #Exclude drafts from the list
    return render(request, 'blog/blog_post_list.html', {'blog_posts': blog_posts})

def drafts_list(request):
    drafts = BlogPost.objects.filter(draft=True)
    return render(request, 'blog/drafts_list.html', {'drafts': drafts})
