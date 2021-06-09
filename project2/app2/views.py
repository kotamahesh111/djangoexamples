from django.http import HttpResponse
def showindex(httprequest):
    message="hi this is my second project"
    return HttpResponse(message)