from django.http import HttpResponse

def default(request):
    return HttpResponse("<h3> Hello, This is my page</h3>")