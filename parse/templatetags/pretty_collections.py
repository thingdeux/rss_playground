from django import template

register = template.Library()

# Might be unnecessary, but I didn't like the way the dictionaries being return from the RSS feed were displayed
# In HTML.  This is a custom filter to gussy them up a tiny bit.
@register.filter(name="pretty_collections")
def pretty_collections(value):
    if isinstance(value, dict):
        return pretty_print_dicts(value)

    elif isinstance(value, list):
        return_string = u''
        for item in value:
            if isinstance(item, dict):
                return_string += pretty_print_dicts(item)
            else:
                return_string += u'\r' + u"{}".format(item)
        return return_string
    else:
        return value


def pretty_print_dicts(dict):
    str_to_return = u''
    for key, value in dict.iteritems():
            str_to_return += u'\r' + u"{}: {}".format(key, value)
    return str_to_return