from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Retrieves a value from a dictionary using a key.
    """
    try:
        return dictionary.get(key)
    except AttributeError:
        return None

@register.filter(name='mul')
def mul(value, arg):
    """
    Multiplies the value by the argument.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None
