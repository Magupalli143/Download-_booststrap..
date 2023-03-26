from django.shortcuts import render

# Create your views here.
def bootstrap_static(request):
    return render(request,'bootstrap_static.html')