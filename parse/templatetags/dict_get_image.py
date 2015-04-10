from django import template

register = template.Library()

# Created a filter for pulling the preview image out of a dictionary keyed on index. See utils. for more info.
@register.filter(name="dict_get_image")
def dict_get_image(value, key):
    val = value.get(key, None)
    return val['url']
