from django import template

register = template.Library()

@register.filter
def add_class(value, css_class):
    return value.as_widget(attrs={
        'class': value.field.widget.attrs.get('class', '') + ' ' + css_class,
    })