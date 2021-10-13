from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import RedirectView
from . import urls


class RedirectHomeToBlogView(RedirectView):
    def redirect_home_to_blog(request):
        return HttpResponseRedirect(reverse("blog"))
