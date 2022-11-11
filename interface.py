import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


def file_cleaner(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)


class UserInterface(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.image = Image(
            source='./kotik.jpeg',
        )
        self.window.add_widget(self.image)

        self.input_label = Label(
            text="Вставь сюда ссылку! Убедись в ее правельности :)",
            font_size=18,
            color='#673AB7'
        )
        self.window.add_widget(self.input_label)

        self.user_input = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1.5, 0.5)
        )
        self.window.add_widget(self.user_input)

        self.button = Button(
            text="Гаффф, Жмиииии!",
            size_hint=(1.5, 0.5),
            bold=True,
            background_color='#673AB7',
            background_normal="",
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        file_cleaner('links.txt')
        with open('links.txt', 'w') as f:
            f.write(f'{self.user_input.text}')
        App.get_running_app().stop()
        Window.close()
