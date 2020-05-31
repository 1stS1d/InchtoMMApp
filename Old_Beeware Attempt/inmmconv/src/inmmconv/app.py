"""
For converting between inches and millimeters quickly.
"""
import toga
from toga.style import Pack
from toga.style.pack import *


class InchtoMMApp(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        titleLabel = toga.Label("Quick Inch <-> MM Conversion Tool", style=Pack(text_align=LEFT))

        left_container = toga.Box()

        left_container.add(titleLabel)



        data = [("TEST", "TEST 2", "TEST 3"), ("TEST 4", "TEST 5", "TEST 6")]

        right_container = toga.Table(headings=['INCH DEC', "INCH FRAC", "MILLIMETERS"], data=data)

        right_container.style.update(width=400)


        left_container.style.update(width=400, padding_left=10)

        split = toga.SplitContainer(direction="VERTICAL")

        split.style.update(width=1000)

        split.content = [right_container, left_container]

        main_box.add(split)

        main_box.style.update(direction=COLUMN, padding_top=10)

        titleLabel.style.update(width=350, padding_left=10, padding_bottom=10)



        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return InchtoMMApp()
