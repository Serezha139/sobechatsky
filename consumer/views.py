from django.shortcuts import  render

def index(request):
    return render(request, 'chat_v2.0.html', {})