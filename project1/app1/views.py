from django.http import HttpResponse
def wish(httprequest):
        message="hello django students"
        return HttpResponse(message)
