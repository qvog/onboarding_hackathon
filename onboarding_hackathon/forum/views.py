from django.shortcuts import render

def topic(request):
    return render(request, 'forum/topic.html')

def topic_page(request):
    return render(request, 'forum/topic_page.html')