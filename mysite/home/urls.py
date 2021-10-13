from django.urls import include, path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from .views import RedirectHomeToBlogView


urlpatterns = [
    path("/", RedirectHomeToBlogView.as_view(), name="blog"),
]
