from wagtail.core import blocks
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock,
StructBlock, TextBlock, DateBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock


class TitleBlock(blocks.CharBlock):
    title = CharBlock(classname="post_title", required=True)
    template = "blog/blocks/title_block.html"

    class Meta:
        icon = "title"
        template = "blog/blocks/title_block.html"

class ParaBlock(blocks.RichTextBlock):
    paragraph = RichTextBlock(classname="post_text", required=True)
    editor = "default"          

    class Meta:
        template = "blog/blocks/para_block.html"

class PicBlock(blocks.StructBlock):
    image = ImageChooserBlock(classname="post_image", required=False)
    caption = CharBlock(required=False)
  
    class Meta:
        icon = "image"
        template = "blog/blocks/pic_block.html"

class DmyBlock(blocks.DateBlock):
    date = DateBlock(classname="post_date", required=True)
    format = "%d %B %Y"

    class Meta:
       template = "blog/blocks/date_block.html"


class CodingBlock(blocks.StructBlock):
    code = CodeBlock(classname = "post_code", required=False)

    class Meta:
        template = "blog/blocks/code_block.html"

