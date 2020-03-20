from django import template
register = template.Library()
 
@register.simple_tag
def include_anything(file_name):
    return open(file_name).read()