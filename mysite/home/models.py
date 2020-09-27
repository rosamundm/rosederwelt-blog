from django import forms
from django.db import models

# from modelcluster.fields import ParentalKey, ParentalManyToManyField
# from modelcluster.contrib.taggit import ClusterTaggableManager
# from taggit.models import TaggedItemBase

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

# from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtail.search import index
# from wagtail.snippets.models import register_snippet
from blog.blocks import MyStream

import datetime


class HomePage(Page):
    body = RichTextField(blank=True)

    contents = StreamField(
        MyStream(),
        verbose_name="My Stream",
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        StreamFieldPanel("contents"),
    ]

    def copyright_context(request):
        current_datetime = datetime.datetime.now()
        return {"current_year": current_datetime.year}
