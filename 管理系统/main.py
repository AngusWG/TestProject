from kivy.core.text import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class ScreenManager2(ScreenManager):
    def __init__(self):
        super().__init__()
        # self.add_widget(Loginscreen())
        self.add_widget(MainScreen())

    pass


class Loginscreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "Login"
        self.add_widget(LoginLayout())

    def login_in(self):
        self.manager.current = 'Main'


class LoginLayout(GridLayout):
    def __init__(self, **kwargs):
        super(LoginLayout, self).__init__(**kwargs)
        self.padding = 30
        self.cols = 1
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        x = Button()
        x.text = 'login'
        x.on_release = self.check
        self.x1213 = x
        self.add_widget(x)

    def check(self):
        if self.username.text == '123456' and self.password.text == '123456':
            self.parent.login_in()


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "Main"
        self.add_widget(ItemLayout())

    def sx(self):
        print("another")
        self.parent.current = 'home'


class ItemLayout(GridLayout):

    def __init__(self, **kwargs):
        super(ItemLayout, self).__init__(**kwargs)
        super().__init__(**kwargs)
        self.cols = 1
        for i in range(20):
            x = Button()
            x.text = 'Go back home x' + str(i + 1)
            x.height = "400dp"
            x.size_hint_y = 50
            x.on_release = self.sx
            self.add_widget(x)

    def sx(self):
        print("666666")


class TestApp(App):
    def build(self):
        return ScreenManager2()


TestApp().run()
