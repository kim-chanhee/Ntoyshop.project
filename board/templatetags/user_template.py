from django import template

register = template.Library()

@register.filter(name='reStr')
def reStr(value):
    fom = ""
    if value == 0:
        return ""
    else:
        for i in range(value):
            fom += "[re]&nbsp;"
        return fom + " : "