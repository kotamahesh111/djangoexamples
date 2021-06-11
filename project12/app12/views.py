from django.shortcuts import render

def showIndex(request):
    if request.method=="POST":
        username=request.POST.get("name")
        password=request.POST.get("password")
        if username == "mahesh" and password == "kota":
            return render(request,"index.html",{"message":"TRUE"})
        else:
             return render(request,"index.html",{"message":"FALSE"})

    else:
        return render(request,"index.html")


