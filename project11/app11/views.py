from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")
def logincheck(request):
    username=request.POST.get('name')
    password=request.POST.get('password')
    if(username=="mahesh"and password=="kota"):
        return render(request,"welcome.html")
    else:
        return render (request,"error.html")
