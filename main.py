from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.support import install_twisted_reactor
import logging

install_twisted_reactor()

from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        logging.info('Client Received Message')
        self.factory.app.print_message(data.decode('utf-8'))


class EchoClientFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, app):
        self.app = app

    def startedConnecting(self, connector):
        self.app.print_message('Started to connect.')

    def clientConnectionLost(self, connector, reason):
        self.app.print_message('Lost connection.')

    def clientConnectionFailed(self, connector, reason):
        self.app.print_message('Connection failed.')

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

MainApp().run()