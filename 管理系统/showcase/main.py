#!/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder

import os
import kivy

kivy.require('1.9.0')


class ParamInput(BoxLayout):
    value = StringProperty('')
    label_text = StringProperty('Param label')

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class ParamInputText(ParamInput):
    pass


class ParamInputDropdown(ParamInput):
    pass


class ParamInputBoolean(ParamInput):
    pass


class ParamInputPopup(ParamInput):
    pass


class ParamInputBrowseFile(ParamInput):
    file = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_choose(self):
        content = ChooseDialog(choose=self.choose, cancel=self.dismiss_popup)
        self._popup = Popup(title='Choose file', content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def choose(self, path, filename):
        self.value = os.path.join(path, filename[0])
        self.dismiss_popup()



class ChooseDialog(FloatLayout):
    choose = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class FormPanel(BoxLayout):
    savefile = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title='Save file', content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.params_summary())

        self.dismiss_popup()

    def params_summary(self):
        output = []
        output.append('Params: ')
        for key, param in self.ids.items():
            if isinstance(param, ParamInput):
                output.append("{0}: {1}".format(key, param.get_value()))
        return os.linesep.join(output)


class ShowcaseApp(App):

    def build(self):
        return FormPanel()


if __name__ == '__main__':
    ShowcaseApp().run()