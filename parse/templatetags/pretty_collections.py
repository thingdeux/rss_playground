from django import template

register = template.Library()

# Might be unnecessary, but I didn't like the way the dictionaries being return from the RSS feed were displayed
# In HTML.  This is a custom filter to gussy them up a tiny bit.
@register.filter(name="pretty_collections")
def pretty_collections(value):
    if isinstance(value, dict):
        return_string = u''
        for key, value in value.iteritems():
            return_string = return_string + u'\r' + u"{}: {}".format(key, value)
        return return_string

    elif isinstance(value, list):
        return_string = u''
        for item in value:
            return_string = return_string + u'\r' + u"{}".format(item)
        return return_string
    else:
        return value
