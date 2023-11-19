from django.shortcuts import render, HttpResponse

# Create your views here.
def detail(request, chat_id):
    context = {}
    return render(request, "chat/index.html", context)

