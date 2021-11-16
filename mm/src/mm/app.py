"""
hackathon project
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from tinydb import TinyDB, Query
from datetime import date

db = TinyDB('src/mm/resources/database.json')
User = Query()

##############################################################################
#Function Definition Start
##############################################################################

def connectPostsList(posts):
    postKeys = []
    postValues = []
    for i in posts:
        for key in i.keys():
            postKeys.append(key)

        for value in i.values():
            postValues.append(value)

    print(postKeys)
    print(postValues)

    return postKeys, postValues

##############################################################################
#Function Definition End
##############################################################################

##############################################################################
#App Class Start
##############################################################################

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


        # some suggestions. because the date of the journal entry is going to be the day of
        # then we can replace date with today = date.today()

        #date = toga.TextInput(style=Pack(padding=(0, 2)), initial='Date: ', placeholder='Date: ', readonly=False)
        self.today = date.today()


        self.diary_writing = toga.MultilineTextInput(style=Pack(padding=(20, 5)), initial='Enter your thoughts and feelings here', placeholder='Enter your thoughts and feelings here', readonly=False)

        self.overall = toga.NumberInput(min_value=0, max_value=10)
        overallLabel = toga.Label(
            'Overall feeling 1 - 10 scale:',
            style=Pack(padding=(5, 0))
        )

        overallBox = toga.Box(style=Pack(direction=ROW, padding=5))

        overallBox.add(overallLabel)
        overallBox.add(self.overall)

        enter = toga.Button(
            'Enter',
            on_press=self.newJournalEntry,
            style=Pack(padding=5)
        )

        sec1_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

        #sec1_box.add(date)
        sec1_box.add(self.diary_writing)
        sec1_box.add(overallBox)
        sec1_box.add(enter)

        section1.add(sec1_box)

        ######################################################################
        # Section 1 -- Shanza Code Here End
        ######################################################################

        ######################################################################
        # Section 2 -- Rohan Code Here Start
        ######################################################################
        # if no, next question: had any thoughts of self harm? -yes, no. if yes/no, 'how do you feel right now' - the same/worse/better. once done say "Thank you for doing your daily check. Sometimes things may seem tough at times, but they will eventually get better, I promise! In the mean time, connect.. or want to call helpline.."
        # if yes: 'what form of self harm' - physical pain/starvation/excessive exercise/poisioning/others. for any: 'are you proud of your self-harm?' - yes, i deserve/wanted it / no,i wish i didn't. for any: 'does someone know about this?" - yes/no. for any: 'how are you feeling right now?' -the same/worse/better. once done, say : Thank you very much for doing your daily check! Always remember that you are special and of worth! u dont deserve pain, talk to someone close or connnect with people here or call helpline'
        #after 3 days of no self harm, reward 5 points. after 25 points total, you win prize
        question1_prompt = toga.Label(
            'Have you committed any acts of self harm today?',
            style=Pack(padding=(10, 0))
        )

       #question1.add(question1_prompt)

        question1_yes = toga.Button(
            'Yes',
        #  on_press= .clear(),
            style=Pack(padding=(20, 10))
        )

        question1_no = toga.Button(
            'No',
            #  on_press= .clear(),
            style=Pack(padding=(40, 10))
        )
       #question1.add(question1_no)

        sec2_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        section2.add(sec2_box)
        sec2_box.add(question1_prompt)
        sec2_box.add(question1_yes)
        sec2_box.add(question1_no)

        ######################################################################
        # Section 2 -- Rohan Code Here End
        ######################################################################

        ######################################################################
        # Section 3 -- Veer Code Here Start
        ######################################################################
        connect = db.table('connect')

        titles, content = connectPostsList(connect.all())


        print(titles)
        print(content)

        sec3_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

        for a, b in enumerate(titles):
            postClass = connectPosts(titles[a], content[a])

            postTitle, postContent = postClass.journalEntry()

            sec3_box.add(postTitle)
            sec3_box.add(postContent)

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
            'Calgary Suicide Prevention Hotline: 833-456-4566',
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

    def newJournalEntry(self, widget):
        journal = db.table('journal')
        journal.insert({str(self.today) : {'content':self.diary_writing.value, 'overall':str(self.overall.value)}})
        self.diary_writing.clear()
        self.overall.refresh()

##############################################################################
#App Class End
##############################################################################

##############################################################################
#Other Classes start
##############################################################################

class connectPosts:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def journalEntry(self):
        postTitle = toga.Label(
            self.title,
            style=Pack(padding=(0, 5))
        )
        postContent = toga.Label(
            self.content,
            style=Pack(padding=(0, 5))
        )

        return [postTitle, postContent]

##############################################################################
#Other Classes End
##############################################################################


def main():
    return mm()
