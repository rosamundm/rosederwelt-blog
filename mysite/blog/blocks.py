from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core import blocks
from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    RawHTMLBlock,
    FieldBlock,
    DateBlock,
    ListBlock,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock
from django.utils.translation import gettext_lazy as _


class TitleBlock(blocks.CharBlock):
    title = CharBlock(
        form_classname="post_title",
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blog/streams/title_block.html"


class ParaBlock(blocks.RichTextBlock):
    paragraph = RichTextBlock(
        form_classname="post_text",
        required=False,
    )
    editor = "default"

    class Meta:
        icon = "edit"
        template = "blog/streams/para_block.html"


class HTMLBlock(blocks.RawHTMLBlock):
    html = RawHTMLBlock()

    class Meta:
        icon = "form"
        # no template needed


class PicBlock(StructBlock):
    image = ImageChooserBlock(label=_("Image"))
    caption = CharBlock(required=False, label=_("Caption"))
    float = blocks.ChoiceBlock(
        required=False,
        choices=[
            ("right", _("Right")),
            ("left", _("Left")),
            ("center", _("Center")),
        ],
        default="center",
        label=_("Float"),
    )
    size = blocks.ChoiceBlock(
        required=False,
        choices=[
            ("small", _("Small")),
            ("medium", _("Medium")),
            ("large", _("Large")),
        ],
        default="medium",
        label=_("Size"),
    )

    class Meta:
        icon = "image"
        # no template needed


class DmyBlock(blocks.DateBlock):
    date = DateBlock(form_classname="post_date", required=False)
    format = "%d %B %Y"

    class Meta:
        icon = "date"
        template = "blog/ streams/date_block.html"


class CodingBlock(blocks.StructBlock):
    code = CodeBlock(form_classname="post_code", required=False)
    language = blocks.ChoiceBlock(default="python")
    text = blocks.TextBlock()

    class Meta:
        icon = "code"
        template = "blog/streams/code_block.html"


# blocks put together in one stream, to be imported into models:
class MyStream(blocks.StreamBlock):
    paragraph = ParaBlock()
    code = CodeBlock()
    html = HTMLBlock()
    image = PicBlock()
