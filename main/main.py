from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from math import trunc

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class MainApp(App):

    def __init__(self, **kwargs):
        super().__init__()
        self.label1 = Label(text='0', font_size=50, halign='right', valign='center',
                            size_hint=(1, .4),
                            text_size=(400 - 20, 500 * 0.4 - 20))
        self.formula = '0'

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=10)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))
        bl.add_widget(self.label1)

        gl.add_widget(Button(text='7', on_press=self.add_numb))
        gl.add_widget(Button(text='8', on_press=self.add_numb))
        gl.add_widget(Button(text='9', on_press=self.add_numb))
        gl.add_widget(Button(text='x', on_press=self.add_operation))

        gl.add_widget(Button(text='4', on_press=self.add_numb))
        gl.add_widget(Button(text='5', on_press=self.add_numb))
        gl.add_widget(Button(text='6', on_press=self.add_numb))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_numb))
        gl.add_widget(Button(text='2', on_press=self.add_numb))
        gl.add_widget(Button(text='3', on_press=self.add_numb))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press=self.add_numb))
        gl.add_widget(Button(text='.', on_press=self.add_operation))
        gl.add_widget(Button(text='=', on_press=self.calc_result))

        bl.add_widget(gl)
        return bl

    def add_numb(self, instance):
        if self.formula == '0':
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text) == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def update_label(self):
        self.label1.text = self.formula

    def calc_result(self, instance):
        self.formula = str(eval(self.formula))
        if self.formula[:-2] == str(trunc(float(self.formula))):
            self.formula = str(trunc(float(self.formula)))
        self.update_label()
        self.formula = '0'


if __name__ == '__main__':
    app = MainApp()
    app.run()
