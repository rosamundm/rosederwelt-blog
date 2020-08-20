from django.shortcuts import render

def handler404(request, template_name):
    response = render("mynewwebsite/mysite/mysite/templates/404.html")
    response.status_code = 404
    return response

def handler500(request, template_name="mynewwebsite/mysite/mysite/templates/500.html"):
    response = render(request, "template_name")
    response.status_code = 500
    return response


