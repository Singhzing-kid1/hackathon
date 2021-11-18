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

    return postKeys, postValues

def journalEntriesList(entries):
    journalKeys = []
    journalValues = []
    journalContent = []
    journalOverall = []
    journalDate = []

    for i in entries:
        for key in i.keys():
            journalKeys.append(key)

        for value in i.values():
            journalValues.append(value)

    for a in journalValues:
        journalContent.append(a['content'])
        journalOverall.append(a['overall'])
        journalDate.append(a['date'])

    journalKeys.reverse()
    journalContent.reverse()
    journalOverall.reverse()
    journalDate.reverse()
    return journalKeys, journalContent, journalOverall, journalDate

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

        section1Main = toga.SplitContainer()

        sec1_box2 = toga.Box(style=Pack(direction=COLUMN, padding=5))
        section1R = toga.Box(style=Pack(direction=COLUMN))
        section1L = toga.ScrollContainer(content=sec1_box2)
        section2 = toga.Box(style=Pack(direction=COLUMN))
        section3 = toga.Box(style=Pack(direction=COLUMN))
        section4 = toga.Box(style=Pack(direction=COLUMN))

        ######################################################################
        # Section 1 -- Shanza Code Here Start
        ######################################################################
        self.sec1_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

        journal = db.table('journal')

        self.titles, self.content, self.overall, self.journalDate = journalEntriesList(journal.all())

        self.openedJournalEAdder = False
        self.openedJournalEntry = False

        #print(titles)
        #print(content)
        #print(overall)

        newEntryButton = toga.Button(
            'New Entry',
            on_press=self.setJournalAdder,
            style=Pack(padding=5)
        )

        sec1_box2.add(newEntryButton)
        self.journalButtons = []

        for a,b in enumerate(self.titles):
            journalClass = journalEntries(self.titles[a], self.displayJournalEntry)


            self.journalButtons.append(journalClass.journalEntry())

        for i in self.journalButtons:
            print(i)
            sec1_box2.add(i)

        section1R.add(self.sec1_box)


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

            postTitle, postContent = postClass.connectPost()

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

        section1Main.content = [section1L, section1R]

        main_box.add('Checkin/journaling', section1Main)
        main_box.add('hurtmenot', section2)
        main_box.add('connect', section3)
        main_box.add('helplines', section4)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def newJournalEntry(self, widget):
        journal = db.table('journal')
        journal.insert({self.title.value : {'content':self.diary_writing.value, 'overall':str(self.overall.value),'date':str(self.today)}})
        self.sec1_box.remove(self.diary_writing)
        self.sec1_box.remove(self.overallBox)
        self.sec1_box.remove(self.enter)
        self.sec1_box.remove(self.title)
        self.openedJournalEAdder = False


    def setJournalAdder(self, widget):
        if self.openedJournalEntry == True:
            self.sec1_box.remove(self.titleLabel)
            self.sec1_box.remove(self.contentLabel)
            self.sec1_box.remove(self.overallLabel)
            self.sec1_box.remove(self.dateLabel)
            self.openedJournalEntry = False

        self.today = date.today()

        self.title = toga.TextInput(style=Pack(padding=(20, 5)), placeholder='Enter a creative title for you journal entry', readonly=False)

        self.diary_writing = toga.MultilineTextInput(style=Pack(padding=(20, 20)), initial='Enter your thoughts and feelings here', placeholder='Enter your thoughts and feelings here', readonly=False)

        self.overall = toga.NumberInput(min_value=0, max_value=10)
        overallLabel = toga.Label(
            'Overall feeling 1 - 10 scale:',
            style=Pack(padding=(5, 0))
        )

        self.overallBox = toga.Box(style=Pack(direction=ROW, padding=5))

        self.overallBox.add(overallLabel)
        self.overallBox.add(self.overall)

        self.enter = toga.Button(
            'Enter',
            on_press=self.newJournalEntry,
            style=Pack(padding=5)
        )



        #sec1_box.add(date)
        self.sec1_box.add(self.title)
        self.sec1_box.add(self.diary_writing)
        self.sec1_box.add(self.overallBox)
        self.sec1_box.add(self.enter)
        self.openedJournalEAdder = True

    def displayJournalEntry(self, widget):
        #print(self.journalButton.label)
        if self.openedJournalEAdder == True:
            self.sec1_box.remove(self.diary_writing)
            self.sec1_box.remove(self.overallBox)
            self.sec1_box.remove(self.enter)
            self.sec1_box.remove(self.title)
            self.openedJournalEAdder = False

        if self.openedJournalEntry == True:
            self.sec1_box.remove(self.titleLabel)
            self.sec1_box.remove(self.contentLabel)
            self.sec1_box.remove(self.overallLabel)
            self.sec1_box.remove(self.dateLabel)
            self.openedJournalEntry = False

        label = ''
        for i in self.journalButtons:
            if i == widget:
                label = i.label
                break

        num = 0

        for a in self.titles:
            if a == label:
                break
            num += 1

        self.titleLabel = toga.Label(
            label,
            style=Pack(padding=5)
        )

        self.dateLabel = toga.Label(
            'Date: ' + self.journalDate[num],
            style=Pack(padding=5)
        )

        self.contentLabel = toga.Label(
            self.content[num],
            style=Pack(padding=5)
        )

        self.overallLabel = toga.Label(
            'Overall Feeling: ' + self.overall[num],
            style=Pack(padding=5)
        )

        self.sec1_box.add(self.titleLabel)
        self.sec1_box.add(self.dateLabel)
        self.sec1_box.add(self.contentLabel)
        self.sec1_box.add(self.overallLabel)
        self.openedJournalEntry = True


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

    def connectPost(self):
        postTitle = toga.Label(
            self.title,
            style=Pack(padding=(0, 5))
        )
        postContent = toga.Label(
            self.content,
            style=Pack(padding=(0, 5))
        )

        return [postTitle, postContent]

class journalEntries:
    def __init__(self, text, onpress):
        self.text = text
        self.onpress = onpress

    def journalEntry(self):
        entryButton = toga.Button(
            self.text,
            on_press=self.onpress,
            style=Pack(padding=5)
        )

        return entryButton

##############################################################################
#Other Classes End
##############################################################################


def main():
    return mm()
