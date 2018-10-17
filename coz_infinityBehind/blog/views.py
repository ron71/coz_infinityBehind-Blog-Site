from django.shortcuts import render
from blog.models import Post

# Create your views here.


def blog(request):
    blog_list = Post.objects.order_by('-date')
    blog_dict = {"blog_records": blog_list,}

    return render(request, "blog/blog.html", context=blog_dict)

def portfolio(request):
	return render(request, "blog/portfolio.html")
