from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, 0)
@register.filter
def rangeCustom(number):
    chainedNumbers = ''
    for i in range(number):
        chainedNumbers += str(i+1)
        
    return chainedNumbers
