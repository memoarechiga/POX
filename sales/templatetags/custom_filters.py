from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    return float(value * arg)

@register.filter
def sum(value, arg):
    return value + arg