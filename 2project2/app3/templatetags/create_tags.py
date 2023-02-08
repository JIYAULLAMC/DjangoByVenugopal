import imp
from django import template

register = template.Library()

@register.filter(name='first_tag')
def first_tag(value):
    """Removes all values of arg from the given string"""
    return value[2]

@register.filter(name="firstfive")
def firstfive(value):
    return value[0:4:1]

