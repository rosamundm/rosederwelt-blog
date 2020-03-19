import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.core import hooks

@hooks.register('register_rich_text_features')

def register_mark_feature(features):
    feature_name = 'code'
    type_ = 'CODE'
    tag = 'mark'

    control = {
        'type': type_,
        'label': '☆',
        'description': 'Code',
    }

   

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )



    db_conversion = {
       'from_database_format': {tag: InlineStyleElementHandler(type_)},
       'to_database_format': {'style_map': {type_: tag}},
   }



    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.default_features.append('code')





