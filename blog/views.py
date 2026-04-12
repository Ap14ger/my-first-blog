from django.shortcuts import render

# Create your views here. es donde va la logica


def post_list(request):
    return render(request, 'blog/post_list.html', {})

