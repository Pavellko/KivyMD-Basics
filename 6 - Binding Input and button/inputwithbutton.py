from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import helpers
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(helpers.username_input)

        self.label = MDLabel(text="Привет!", halign="center", font_style="Subtitle2", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show)
        screen.add_widget(self.label)
        screen.add_widget(self.username)
        screen.add_widget(self.button)
        return screen

    def show(self, args):

        self.label.text = "Hello, " + self.username.text +"!"

DemoApp().run()
