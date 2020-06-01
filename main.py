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
from kivy.uix.popup import Popup
from kivymd.button import MDRaisedButton
from kivymd.theming import ThemeManager
#from kivymd.textfields.MDTextField import MDTextField
from kivymd.textfields import MDTextField
from kivymd.label import MDLabel
from kivymd.dialog import MDDialog

from decimal import Decimal
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

        self.InchInput = MDTextField()
        self.InchInput.hint_text = "Inches"
        self.InchInput.multiline = False
        self.InchInput.on_text_validate = self.convert
        
        self.MMInput = MDTextField()
        self.MMInput.hint_text = "Millimeters"
        self.MMInput.multiline = False
        self.MMInput.on_text_validate = self.convert

        ConvButton = MDRaisedButton()
        ConvButton.text = "   <--- CONVERT -->   "
        ConvButton.on_press = self.convert
        
        self.add_widget(Title)
        self.add_widget(self.InchInput)
        self.add_widget(self.MMInput)
        self.add_widget(ConvButton)

    def convert(self):
        global pastConvTable
        global pastConvs

        def tofrac(x, largest_denominator=128):
            if not x >= 0:
                raise ValueError("x must be >= 0")
            scaled = int(round(x * largest_denominator))
            whole, leftover = divmod(scaled, largest_denominator)
            if leftover:
                while leftover % 2 == 0:
                    leftover >>= 1
                    largest_denominator >>= 1
            #return whole, leftover, largest_denominator
            if (whole == 0):
                stringVal = str(leftover) + "/" + str(largest_denominator)
            else:
                stringVal = str(whole) + " " + str(leftover) + "/" + str(largest_denominator)
            return stringVal

        #Converting Millimeters to Inches if Inches are blank
        if (self.InchInput.text == ""):
            mm = self.MMInput.text
            d = Decimal(mm)
            mm = float(mm)
            inch = mm/25.4
            if (d.as_tuple().exponent <= -3):
                digits = 5
            else:
                digits = 4
            pastConvs.insert(0, (inch, tofrac(inch), round(mm, digits)))
            self.InchInput.text = ""
            self.MMInput.text = ""

        #Converting Inches to Millimeters if Millimeters are blank
        elif (self.MMInput.text == ""):
            inch = self.InchInput.text
            d = Decimal(inch)
            inch = float(inch)
            mm = inch*25.4
            if (d.as_tuple().exponent <= -4):
                digits = 4
            else:
                digits = 3
            pastConvs.insert(0, (round(inch,digits), tofrac(inch), mm))
            self.InchInput.text = ""
            self.MMInput.text = ""

        #Error if there is a value in both boxes
        else:
            content = MDLabel(font_style='Body1', theme_text_color='Primary', text="Invalid Input!", size_hint_y=None, valign='top')
            popup = MDDialog(title='Invalid Input', content=content, auto_dismiss=True, size_hint=(None, None), size=(200, 200))
            popup.add_action_button("Dismiss", action=lambda *x: popup.dismiss())
            popup.open()
            self.InchInput.text = ""
            self.MMInput.text = ""


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