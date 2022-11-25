from django.shortcuts import render

# Create your views here.
def for_loops(request):
    d={'name':'laddu'}
    return render(request,'for_loops.html',d)