from atexit import register
from re import A
from django import template

register=template.Library()


@register.filter
def dd(data):
    a=0
    for i in data:
        a+=i
    return a


@register.filter(name='reStr')
def reStr(value):
    fom = ""
    if value == 0:
        return ""
    else:
        for i in range(value):
            fom += "[re]&nbsp;"
        return fom + " : "


@register.filter
def mul(data,e):
    d=int(data)
    b=int(e)
    return d*b