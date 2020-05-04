from django.shortcuts import render

# Create your views here.
def index(request):
    template = ''
    context = {}
    return render(request, template, context)
