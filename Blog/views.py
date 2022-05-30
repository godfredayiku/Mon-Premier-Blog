from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'Blog/post_list.html', {'posts1':posts})


def bonjour(request):
	return render(request, 'Blog/bonjour.html', {})