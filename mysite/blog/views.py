from django.shortcuts import render

# Create your views here.


def handler404(request, exception, template_name="mynewwebsite/mysite/mysite/templates/404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def handler500(request, template_name="500.html"): #does not need 'exception' argument!
    response = render_to_response("500.html")
    response.status_code = 500
    return response
