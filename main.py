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
        self.cols = 1
        self.rows = 2

        self.lp = LeftPane()
        self.rp = RightPane()

        self.add_widget(self.lp)

        self.add_widget(self.rp)

class LeftPaneSplitter(Splitter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rescale_with_parent = True
        self.sizable_from = 'bottom'
        self.add_widget(LeftPane())
        self.min_size = 200
        self.max_size = 200

class LeftPane(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 4
        self.row_force_default = True
        self.row_default_height = 40
        self.padding = (20, 5, 20, 20)

        self.size_hint = (500, 0.25)

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
        rp = RightPane()
        rp.pastConvs.insert(0, (2,2,2))
        rp.updateTable()
        

class RightPane(BoxLayout):

    pastConvs = [(0, 0, 0), (1, 1, 1)]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 20

        self.size_hint = (500, 0.75)

        self.pastConvTable = RstDocument(text = str(tabulate(self.pastConvs, headers=["INCH DEC", "INCH FRAC", "MILLIMETERS"], tablefmt="rst")))
       

        self.add_widget(self.pastConvTable)
    
    def updateTable(self):
        self.pastConvTable.text = str(tabulate(self.pastConvs, headers=["INCH DEC", "INCH FRAC", "MILLIMETERS"], tablefmt="rst"))
        self.pastConvTable.render()
        
        

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