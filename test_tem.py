#-*- encoding:utf-8 -*-
__author__ = ''
class Foo(object):
    def __init__(self):
        self.name="abc"
    def func(self):
        return 'ok'

obj=Foo()
ret=getattr(obj,'func')
r=ret()
print(r)
