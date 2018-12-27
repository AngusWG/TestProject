#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/12/11 9:48
# @author  : zza
# @Email   : 740713651@qq.com


print("*" * 50)


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2


c = Circle(4)
print(c.radius)
print(c.area)

#####################
print("*" * 50)


class lazy(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2


c = Circle(4)
print(c.radius)
print(c.area)
print(c.area)
c.radius = 8
print(c.area)
print(3.14 * c.radius ** 2)

############
print("*" * 50)


def lazy_property(func):
    attr_name = "_lazy_" + func.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return _lazy_property


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy_property
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2


c = Circle(4)
print("before first visit")
print(c.__dict__)
c.area
print("after first visit")
print(c.__dict__)

c.radius = 8
print(c.area)
print(3.14 * c.radius ** 2)