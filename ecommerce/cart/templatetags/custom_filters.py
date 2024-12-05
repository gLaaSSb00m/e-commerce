from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    try:
        return dictionary.get(str(key))  # Convert key to string
    except AttributeError:
        return None



@register.filter(name='mul')
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None


# Test values
sales_price = 10.00
quantity = 2
total = mul(sales_price, quantity)
print(total)  # Should print 20.0

