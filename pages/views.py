from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'pages/index.html'
    return render(request, template)
