from pywinauto.application import Application

# app = Application("uia").start("Todo.exe")
# app = Application("uia").connect(title="Todo.exe", timeout=3)
app = Application("uia").connect(title="Microsoft To Do", timeout=3)
print(app.windows())
windows = app.windows()
# main_window = app.window()

main_body = windows[0].children()[0].children()[2].capture_as_image().save("123.png")
