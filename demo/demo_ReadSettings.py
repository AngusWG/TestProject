from readsettings import ReadSettings

data = ReadSettings("tmp_config.yaml")
data["foo"] = "Hello World"
data["foo2"] = "Hello World"
data["中文"] = "测试"
print(data["foo"])
'Hello World'
del data["foo"]