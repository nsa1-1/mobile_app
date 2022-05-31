from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

Button_Text = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '+', '-', '.', '=']


class MainApp(App):
    global Button_Text

    def build(self):
        self.label1 = Label(text='0', font_size=50, halign='right', valign='center',
                            size_hint=(1, .4),
                            text_size=(400 - 20, 500 * 0.4 - 20))
        bl = BoxLayout(orientation='vertical', padding=10)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))
        bl.add_widget(self.label1)
        # gl.add_widget(Widget())
        for widget_text in Button_Text:
            gl.add_widget(Button(text=widget_text))
        bl.add_widget(gl)
        return bl


if __name__ == '__main__':
    app = MainApp()
    app.run()
