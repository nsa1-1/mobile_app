from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        label = Label(text='first_comm',
                      size_hint=(1, 1),
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()
