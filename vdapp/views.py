from django.shortcuts import render  # HttpResponse
# from .models import Index
from .models import *

# Create your views here.


def index(request):
    post = Index.objects.all()
    print(post)
    return render(request, 'index.html', {'post': post})
    # return HttpResponse(" this is home page")
