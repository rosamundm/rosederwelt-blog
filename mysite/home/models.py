from django import forms
from django.db import models

#from modelcluster.fields import ParentalKey, ParentalManyToManyField
#from modelcluster.contrib.taggit import ClusterTaggableManager
#from taggit.models import TaggedItemBase

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
#from wagtail.images.edit_handlers import ImageChooserPanel
#from wagtail.search import index
#from wagtail.snippets.models import register_snippet


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]




