from django.shortcuts import render

def showindex(request):
    emp_info = {"idno":101,"name":"Ravi","salary":185000.00}
    return render(request,"main.html",emp_info)
