from django.shortcuts import render

# Create your views here.
def cdn_static(request):
    return render(request,'cdn_static.html')
