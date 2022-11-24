from django.shortcuts import render

# Create your views here.
def jinja_operation(request):
    d={'a':250,'b':300,'c':400}
    return render(request,'jinja_operation.html',context=d)

