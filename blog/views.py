from django.shortcuts import render
from .models import Post

posts	=	[
	{
		'title'			:	'Blog Post 1',
		'author'			:	'Teejay',
		'content'		:	'First Blog Post',
		'date_posted'	:	'December 24th, 2020',	
	},
	{
		'title'			:	'Blog Post 2',
		'author'			:	'Test',
		'content'		:	'Second Blog Post',
		'date_posted'	:	'December 25th, 2020',	
	},
]

def index(request):
    context = {
        # 'posts' :   posts,
        'posts' :   Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title' : 'Contact'})

