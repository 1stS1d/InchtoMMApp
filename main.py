import os
import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.config import Config
from kivy.core import window

from kivy.uix.rst import RstDocument

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.splitter import Splitter
from kivy.uix.button import Button
from kivymd.button import MDRaisedButton
from kivymd.theming import ThemeManager
#from kivymd.textfields.MDTextField import MDTextField
from kivymd.textfields import MDTextField
from kivymd.label import MDLabel

from tabulate import tabulate

class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        #self.orientation='vertical'
        self.padding = (20, 5, 20, 20)
        self.cols = 1
        self.rows = 2

        self.lp = LeftPane()
        self.rp = RightPane()

        self.add_widget(self.lp)

        self.add_widget(self.rp)

pastConvs = [(0,0,0), (1,1,1)]
pastConvTable = RstDocument(text = str(tabulate(pastConvs, headers=["INCH DEC", "INCH FRAC", "MILLIMETERS"], tablefmt="rst")))

class LeftPane(GridLayout):
    def __init__(self, **kwargs):
        super(LeftPane, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 4
        self.row_force_default = True
        self.row_default_height = 40

        self.size_hint = (500, 0.3)

        self.spacing = (0, 10)

        Title = MDLabel()
        Title.text = "Quick Inch <--> MM Converter"

        InchInput = MDTextField()
        InchInput.hint_text = "Inches"
        InchInput.multiline = False
        
        MMInput = MDTextField()
        MMInput.hint_text = "Millimeters"
        MMInput.multiline = False

        ConvButton = MDRaisedButton()
        ConvButton.text = "   <--- CONVERT -->   "
        ConvButton.on_press = self.convert
        
        self.add_widget(Title)
        self.add_widget(InchInput)
        self.add_widget(MMInput)
        self.add_widget(ConvButton)

    def convert(self):
        global pastConvTable
        global pastConvs
        pastConvs.insert(0, (2,2,2))
        pastConvTable.text = str(tabulate(pastConvs, headers=["INCH DEC", "INCH FRAC", "MILLIMETERS"], tablefmt="rst"))

class RightPane(BoxLayout):

    pastConvs = [(0, 0, 0), (1, 1, 1)]

    def __init__(self, **kwargs):
        super(RightPane, self).__init__(**kwargs)

        self.size_hint = (500, 0.7)

        global pastConvTable
        global pastConvs

        self.add_widget(pastConvTable)        
        

class MyApp(App):

    theme_cls = ThemeManager()

    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '750')
    Config.write()

    window.size = (500, 750)

    def build(self):
        self.title = "Quick Inch <--> MM Converter"

        return MainPage()


if __name__ == '__main__':
    MyApp().run()