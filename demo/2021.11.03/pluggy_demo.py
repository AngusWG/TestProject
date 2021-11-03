# encoding: utf-8
# @Time   : 2021/8/3 11:52
# @author : zza
# @Email  : 740713651@qq.com
# @File   : pluggy_demo.py
import pluggy
# 创建插件规范类装饰器
hookspac = pluggy.HookspecMarker('example')
# 创建插件类装饰器
hookimpl = pluggy.HookimplMarker('example')

class MySpec(object):
    # 创建插件规范
    @hookspac
    def myhook(self, a, b):
        pass

class Plugin_1(object):
    # 定义插件
    @hookimpl
    def myhook(self, a, b):
        return a + b

class Plugin_2(object):
    @hookimpl
    def myhook(self, a, b):
        return a - b

# 创建manger和添加hook规范
pm = pluggy.PluginManager('example')
pm.add_hookspecs(MySpec)

# 注册插件
pm.register(Plugin_1())
pm.register(Plugin_2())

# 调用插件中的myhook方法
results = pm.hook.myhook(a=10, b=20)
print(results)
