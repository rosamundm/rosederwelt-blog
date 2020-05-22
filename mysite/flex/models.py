from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtailcodeblock.blocks import CodeBlock
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
from blog.models import BlogPageTag

class CustomBlogPage(Page):
    # Streamfield attributes:
    body = StreamField(block_types = [
        ("title", blocks.CharBlock(classname="post title")),
        ("paragraph", blocks.RichTextBlock()),
        ("image", ImageChooserBlock()),
        ("code", CodeBlock())
    ])
    # non-StreamField attributes:
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("tags"),
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Custom blog page"

    # (double check indentation?)
    class CustomBlogPageTag(TaggedItemBase):
        content_object = ParentalKey(
            'CustomBlogPage',
            related_name='tagged_items',
            on_delete=models.CASCADE
        )

