"""
hackathon project
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class mm(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.OptionContainer()

        section1 = toga.Box(style=Pack(direction=COLUMN))
        section2 = toga.Box(style=Pack(direction=COLUMN))
        section3 = toga.Box(style=Pack(direction=COLUMN))
        section4 = toga.Box(style=Pack(direction=COLUMN))

        ######################################################################
        # Section 1 -- Shanza Code Here Start
        ######################################################################
        sec1_label = toga.Label(
            'sec1',
            style=Pack(padding=(0, 5))
        )

        sec1_box = toga.Box(style=Pack(direction=ROW, padding=5))
        sec1_box.add(sec1_label)

        section1.add(sec1_box)

        ######################################################################
        # Section 1 -- Shanza Code Here End
        ######################################################################

        ######################################################################
        # Section 2 -- Rohan Code Here Start
        ######################################################################
        sec2_label = toga.Label(
            'sec2',
            style=Pack(padding=(0, 5))
        )

        sec2_box = toga.Box(style=Pack(direction=ROW, padding=5))
        sec2_box.add(sec2_label)

        section2.add(sec2_box)

        ######################################################################
        # Section 2 -- Rohan Code Here End
        ######################################################################

        ######################################################################
        # Section 3 -- Veer Code Here Start
        ######################################################################
        sec3_label = toga.Label(
            'sec3',
            style=Pack(padding=(0, 5))
        )

        sec3_box = toga.Box(style=Pack(direction=ROW, padding=5))
        sec3_box.add(sec3_label)

        section3.add(sec3_box)

        ######################################################################
        # Section 3 -- Veer Code Here End
        ######################################################################

        ######################################################################
        # Section 4 -- Veer Code Here Start
        ######################################################################
        kidsHelpPhone = toga.Label(
            'Kids Help Phone: 1-800-668-6868',
            style=Pack(padding=(0, 5))
        )

        abWideMentalHealthPhone = toga.Label(
            'Alberta Wide Mental Health Helpline: 1-877-303-2642',
            style=Pack(padding=(0, 5))
        )

        yycMentalHealthHelpline = toga.Label(
            'Calgary Mental Health Helpline: 1-877-303-2642',
            style=Pack(padding=(0, 5))
        )

        yycsuicidePreventionHotline = toga.Label(
            'Calgary Suicide Hotline: 833-456-4566',
            style=Pack(padding=(0, 5))
        )


        sec4_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        sec4_box.add(kidsHelpPhone)
        sec4_box.add(abWideMentalHealthPhone)
        sec4_box.add(yycMentalHealthHelpline)
        sec4_box.add(yycsuicidePreventionHotline)

        section4.add(sec4_box)

        ######################################################################
        # Section 4 -- Veer Code Here End
        ######################################################################

        main_box.add('Checkin/journaling', section1)
        main_box.add('hurtmenot', section2)
        main_box.add('connect', section3)
        main_box.add('helplines', section4)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return mm()
