from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)


from wagtail.core import blocks
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock,
StructBlock, TextBlock, FieldBlock, DateBlock, ListBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock
from markdown import markdown

from wagtailmarkdownblock.blocks import MarkdownBlock


from wagtail_markdown.utils import MarkdownPanel, MarkdownField


class TitleBlock(blocks.CharBlock):
    title = CharBlock(
        classname="post_title",
        required=False,
        template = "blog/streams/title_block.html"
    )

    class Meta:
        icon = "title"


class ParaBlock(blocks.RichTextBlock):
    paragraph = RichTextBlock(
        classname="post_text",
        required=False,
        template = "blog/streams/para_block.html"
    )
    editor = "default"

    class Meta:
        icon = "edit"



class PicBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)
   # template = "blog/streams/pic_block.html"

    class Meta:
        icon = "image"
        template = "blog/streams/pic_block.html"


class DmyBlock(blocks.DateBlock):
    date = DateBlock(
        classname="post_date",
        required=False,
        template = "streams/date_block.html"
    )
    format = "%d %B %Y"


class CodingBlock(blocks.StructBlock):
    code = CodeBlock(classname = "post_code", required=False)
    language = blocks.ChoiceBlock(default="python")
    text = blocks.TextBlock()


    class Meta:
        icon = "code"
        template = "blog/streams/code_block.html"
"""
# in construction:
class MDBlock(blocks.TextBlock):
    md = MarkdownField()
    class Meta:
        icon = "wagtail-inverse"
        template = "blog/streams/md_block.html"

"""
# all blocks put together in one stream for use in blog/models:
class MyStream(blocks.StreamBlock):
    paragraph = ParaBlock()
    image = PicBlock()
    code = CodeBlock()
#    md = MarkdownBlock()
  
