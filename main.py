import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import logging
from kivy import platform
#if platform == "android":
#    from android.permissions import request_permissions, Permission
#    request_permissions([Permission.FOREGROUND_SERVICE])


from kivy.core.window import Window
Window.size = (360, 760)



class poSelectWindow(Screen):
    pass

class loginWindow(Screen):
    pass

class appWindow(Screen):
    pass

# class for managing screens
class windowManager(ScreenManager):
    pass

sm = windowManager()

class MainApp(MDApp):
    connection = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        kv = Builder.load_file('main.kv')

        Window.clearcolor = (0, 0, 1, 1)

        # adding theme_color
        self.theme_cls.theme_style = "Light"

        # adding screens
        sm.add_widget(poSelectWindow(name='screen_po_select'))
        sm.add_widget(loginWindow(name='screen_login'))
        sm.add_widget(appWindow(name='screen_app'))
        sm.current = 'screen_login'
        #sm.current = 'screen_app'

        return sm

    def rmshelper_client_connect(self):
        #reactor.connectTCP('localhost', 8000, EchoClientFactory(self))
        sm.current = 'screen_app'

    def clear(self):
        pass

    def po_select_exit(self):
        sm.current = 'screen_app'

    def rmshelper_po_select(self):
        sm.current = 'screen_app'

    def app_exit_cb(self, data):
        return self.root_window.close()

    def po_select_cb(self, data):
        sm.current = 'screen_po_select'

    def select_upc(self, data):
        pass

    def clear_app(self):
        clear_screen = self.root.get_screen('screen_app')
        clear_screen.ids.upc.text = ""
        clear_screen.ids.last_sold.text = ""
        clear_screen.ids.description.text = ""
        clear_screen.ids.desc1.text = ""
        clear_screen.ids.retail_price.text = ""
        clear_screen.ids.seven_day.text = ""
        clear_screen.ids.desc2.text = ""
        clear_screen.ids.sale_price.text = ""
        clear_screen.ids.fourteen_day.text = ""
        clear_screen.ids.desc3.text = ""
        clear_screen.ids.cost_price.text = ""
        clear_screen.ids.thirty_day.text = ""
        clear_screen.ids.dept.text = ""
        clear_screen.ids.sale_start.text = ""
        clear_screen.ids.supply.text = ""
        clear_screen.ids.sale_end.text = ""

    def print_upc(self):
        pass

MainApp().run()