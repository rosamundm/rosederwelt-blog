from __future__ import absolute_import

from django import template

import markdown
import wagtail_markdown

register = template.Library()

@register.filter(name="markdown")
def markdown_filter(value):
    return markdown.markdown(
        value,
        output_format="html5"
#        extensions = ["markdown.extensions.md_in_html",]
    )
