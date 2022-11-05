import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class UserInterface(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source='./kotik.jpeg'))

        self.input_label = Label(
            text="Вставь сюда ссылку! Убедись в ее правельности :)")
        self.window.add_widget(self.input_label)

        self.user_input = TextInput(multiline=False)
        self.window.add_widget(self.user_input)

        self.button = Button(text="Поихалы!")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        if os.path.isfile('links.txt'):
            os.remove('links.txt')
        with open('links.txt', 'w') as f:
            f.write(f'{self.user_input.text}')
        App.get_running_app().stop()
        Window.close()

