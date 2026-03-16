from django import template

register = template.Library()


@register.filter
def split(value, arg=","):
    """Split a string by a delimiter. Usage: "a,b,c"|split:"," """
    return value.split(arg)


@register.filter
def first_word(value):
    """Return the first word of a string."""
    parts = str(value).split()
    return parts[0] if parts else value


@register.filter
def last_word(value):
    """Return everything after the first word."""
    parts = str(value).split()
    return ' '.join(parts[1:]) if len(parts) > 1 else value


@register.filter
def get_item(dictionary, key):
    """Get an item from a dict by key. Usage: mydict|get_item:key """
    return dictionary.get(key, [])
