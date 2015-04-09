from django import template

register = template.Library()

# Might be unnecessary, but I didn't like the way the dictionaries being return from the RSS feed were displayed
# In HTML.  This is a custom filter to gussy them up a tiny bit.
@register.filter(name="dict_get_image")
def dict_get_image(value, key):
    val = value.get(key, None)
    return val['url']
