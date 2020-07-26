from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)


from wagtail.core import blocks
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock,
    StructBlock, TextBlock, RawHTMLBlock, 
    FieldBlock, DateBlock, ListBlock
    )
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock
#from wagtail_markdown.utils import MarkdownPanel, MarkdownField


class TitleBlock(blocks.CharBlock):
    title = CharBlock(
        classname="post_title",
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blog/streams/title_block.html"

class ParaBlock(blocks.RichTextBlock):
    paragraph = RichTextBlock(
        classname="post_text",
        required=False,
    )
    editor = "default"

    class Meta:
        icon = "edit"
        template = "blog/streams/para_block.html"


class HTMLBlock(blocks.RawHTMLBlock):
    html = RawHTMLBlock()

    class Meta:
        icon = "wagtail-inverse"
        verbose_name = "HTML"
        # no template needed

class PicBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    caption = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blog/streams/pic_block.html"
      

class DmyBlock(blocks.DateBlock):
    date = DateBlock(
        classname="post_date",
        required=False,
        template = "blog/ streams/date_block.html"
    )
    format = "%d %B %Y"


class CodingBlock(blocks.StructBlock):
    code = CodeBlock(classname = "post_code", required=False)
    language = blocks.ChoiceBlock(default="python")
    text = blocks.TextBlock()

    class Meta:
        icon = "code"
        template = "blog/streams/code_block.html"


# all blocks put together in one stream for use in blog/models:

class MyStream(blocks.StreamBlock):
    paragraph = ParaBlock()
  #  image = PicBlock()
    code = CodeBlock()  
    html = HTMLBlock()
