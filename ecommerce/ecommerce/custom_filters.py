from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None  # Return None or 0 as fallback
