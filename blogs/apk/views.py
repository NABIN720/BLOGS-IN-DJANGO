from django.shortcuts import render, get_object_or_404
from .models import bPost


# Create your views here.
def index(request):
    mpost = bPost.objects.all()
    print(mpost)
    return render(request, 'apk/index.html',{'mpost':mpost})

def post(request,id):
    mposts = get_object_or_404(bPost, post_id=id)
    return render(request, 'apk/post.html',{'mposts':mposts})

# View for listing all blog posts
# def blog_list(request):
#     posts = blogPost.objects.filter(is_published=True).order_by('-created_at')  # Fetch published posts
#     return render(request, 'apk/blog_list.html', {'posts': posts})

# # View for displaying a single blog post
# def blog_detail(request, slug):
#     post = get_object_or_404(blogPost, slug=slug)  # Fetch post by slug
#     return render(request, 'apk/blog_detail.html', {'post': post})