from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
import helpers


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(helpers.username_input)
        button = MDRectangleFlatButton(text='Показать имя!',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is not "":
            user_error = self.username.text + " привет, привет!."
        else:
            user_error = "Напиши что-нибудь!"
        self.dialog = MDDialog(title='Привет, Мотенька, сынок!',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Закрыть', on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()



DemoApp().run()
