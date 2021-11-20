"""
hackathon project
"""

##############################################################################
#briefcase specific imports start
##############################################################################

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

##############################################################################
#briefcase specific imports end
##############################################################################

##############################################################################
#other imports start
##############################################################################

from tinydb import TinyDB, Query
from datetime import date

##############################################################################
#other imports start
##############################################################################


db = TinyDB('src/mm/resources/database.json') # defining the database connection

##############################################################################
#Function Definition Start
##############################################################################

# This Function sorts out the titles and content of each connect post.
def connectPostsList(posts):
    postKeys = []
    postValues = []
    for i in posts:
        for key in i.keys():
            postKeys.append(key)

        for value in i.values():
            postValues.append(value)

    return postKeys, postValues

# This Function does the same stuff as the last function but for a different section
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
        # Definition of the main screen.
        main_box = toga.OptionContainer()

        #Definition of each section
        section1Main = toga.SplitContainer()
        self.sec1_box2 = toga.Box(style=Pack(direction=COLUMN, padding=5))
        section1R = toga.Box(style=Pack(direction=COLUMN))
        section1L = toga.ScrollContainer(content=self.sec1_box2)
        section2 = toga.Box(style=Pack(direction=COLUMN))
        section3 = toga.Box(style=Pack(direction=COLUMN))
        section4 = toga.Box(style=Pack(direction=COLUMN))

        ######################################################################
        # Section 1 -- Shanza Code Here Start
        ######################################################################
        # Defining some variables used in the journaling section
        self.openedJournalEAdder = False # this keeps track of whether or not the journal entry adder elements have been printed to the gui
        self.openedJournalEntry = False # this keeps track of the journal entry elements
        self.onStartup = True # this keeps track of stuff that needs to be run once on startup as well as stuff that gets updated later on.
        self.journalButtons = [] # a place for the journal entry selection buttons to reside as they are all instances of one class. I have them here to be able to call on them later.

        self.sec1_box = toga.Box(style=Pack(direction=COLUMN, padding=5)) # Defining the box that the journal entry selectors will be printed to.
        self.journal = db.table('journal') # accessing the journal table in the database

        # This button calls on the journal entry adder gui
        newEntryButton = toga.Button(
            'New Entry',
            on_press=self.setJournalAdder,
            style=Pack(padding=5)
        )

        self.sec1_box2.add(newEntryButton) # This adds the button 'newEntryButton' to the screen




        self.sec1_box2.add(newEntryButton) # This adds the button
        self.sec1_box2.add(newEntryButton) # This adds the button
        if self.onStartup == True: #this checks if the app has just started up


            self.titles, self.content, self.overallList, self.journalDate = journalEntriesList(self.journal.all()) # this calls on the data base and gets the titles, conent, date and overall feelings
            # into seperate lists

            for a,b in enumerate(self.titles): # this iterates through the titles.
                journalClass = journalEntries(self.titles[a], self.displayJournalEntry) # this initializes the journal buttons


                self.journalButtons.append(journalClass.journalEntry()) # this creates the journal buttons and adds them to 'self.journalButtons'

            for i in self.journalButtons: # this iterates through the 'self.journalbuttons' list and prints them to the screen
                self.sec1_box2.add(i)

            self.onStartup == False # this tells the rest of the program that the start up has finished.

        section1R.add(self.sec1_box) # this adds the box that contains the journal entry adder elements and the journal entry elements to the main window.


        ######################################################################
        # Section 1 -- Shanza Code Here End
        ######################################################################

        ######################################################################
        # Section 2 -- Shanza Code Here Start
        ######################################################################
        container = toga.ScrollContainer(content=section2, horizontal=False) # the section2 Container for the self harm abstinance section
        container.vertical = True # TODO this is redundant as the container defaults to vertical: remove it

        # Q1 promt/question
        question1_prompt = toga.Label(
            'Q1: Have you committed any acts of self harm today?',
            style=Pack(padding=(10, 0))
        )

        # Q1 responses start
        question1_yes = toga.Button(
            'Yes',
            style=Pack(padding=(3, 10)),
        )

        question1_no = toga.Button(
            'No',
            style=Pack(padding=(3, 10))
        )
        # Q1 responses end


        question1Box = toga.Box(style=Pack(direction=COLUMN)) # Box for question prompts and responses. Only here for organization
        question1Box.add(question1_prompt) # adding the prompt to the box

        # adding responses to the box start
        question1Box.add(question1_yes)
        question1Box.add(question1_no)
        # adding responses to the box end

        # Q2 promt/question
        question2_prompt = toga.Label(
                'Q2: If "No" for question 1...did you have any thoughts of self harm?',
                style=Pack(padding=(20, 0))
            )

        # Q2 responses start
        question2_yes = toga.Button(
                'Yes',
                style=Pack(padding=(3, 10)),
            )

        question2_no = toga.Button(
                'No',
                style=Pack(padding=(3, 10)),
            )
        # Q2 responses end

        question2Box = toga.Box(style=Pack(direction=COLUMN)) # Box for question prompts and responses. Only here for organization
        question2Box.add(question2_prompt) # adding the prompt to the box

        # adding responses to box 2 start
        question2Box.add(question2_yes)
        question2Box.add(question2_no)
        # adding responses box 2 end

        # Q3 promt/question
        question3_prompt = toga.Label(
            'Q3: If "Yes" for question 1...what form of self harm?',
            style=Pack(padding=(20, 0))
        )

        # Q3 responses start
        question3_opt1 = toga.Button(
            'Physical pain',
            style=Pack(padding=(3, 10)),
        )
        question3_opt2 = toga.Button(
            'Starvation',
            style=Pack(padding=(3, 10)),
        )
        question3_opt3 = toga.Button(
            'Excessive exercise',
            style=Pack(padding=(3, 10)),
        )
        question3_opt4 = toga.Button(
            'Poisoning',
            style=Pack(padding=(3, 10)),
        )
        question3_opt5 = toga.Button(
            'Others',
            style=Pack(padding=(3, 10)),
        )
        # Q3 responses end

        question3Box = toga.Box(style=Pack(direction=COLUMN)) # Box for question prompts and responses. Only here for organization
        question3Box.add(question3_prompt) # adding the prompt to the box

        # adding responses to box 3 start
        question3Box.add(question3_opt1)
        question3Box.add(question3_opt2)
        question3Box.add(question3_opt3)
        question3Box.add(question3_opt4)
        question3Box.add(question3_opt5)
        # adding responses box 3 end

        # Q4 promt/question
        question4_prompt = toga.Label(
            'Q4: If "Yes" for question 1...are you proud of your self harm?',
            style=Pack(padding=(20, 0))
        )

        # Q4 responses start
        question4_yes = toga.Button(
            'Yes, I deserve/wanted it',
            style=Pack(padding=(3, 10)),
        )
        question4_no = toga.Button(
            "No, I wish I didn't",
            style=Pack(padding=(3, 10)),
        )
        # Q4 responses end

        question4Box = toga.Box(style=Pack(direction=COLUMN)) # Box for question prompts and responses. Only here for organization
        question4Box.add(question4_prompt) # adding the prompt to the box

        # adding responses to box 4 start
        question4Box.add(question4_yes)
        question4Box.add(question4_no)
        # adding responses to box 4 end

        # Q5 promt/question
        question5_prompt = toga.Label(
            'Q5: If "Yes" for question 1...does anyone know you did it?',
            style=Pack(padding=(20, 0))
        )

        # Q5 responses start
        question5_yes = toga.Button(
            'Yes',
            style=Pack(padding=(3, 10)),
        )
        question5_no = toga.Button(
            "No",
            style=Pack(padding=(3, 10)),
        )
        # Q5 responses end

        question5Box = toga.Box(style=Pack(direction=COLUMN)) # Box for question prompts and responses. Only here for organization
        question5Box.add(question5_prompt) # adding the prompt to the box

        # adding responses to box 5 start
        question5Box.add(question5_yes)
        question5Box.add(question5_no)
        # adding responses to box 5 end

        # Q6 promt/question
        question6_prompt = toga.Label(
            'Q6: How are you feeling right now?',
            style=Pack(padding=(20, 0))
        )

        # Q6 responses start
        question6_better = toga.Button(
            'Better',
            style=Pack(padding=(3, 10)),
        )
        question6_worse = toga.Button(
            "Worse",
            style=Pack(padding=(3, 10)),
        )
        question6_same = toga.Button(
            "The same",
            style=Pack(padding=(3, 10)),
        )
        # Q6 responses end

        question6Box = toga.Box(style=Pack(direction=COLUMN)) # Box for question prompts and responses. Only here for organization
        question6Box.add(question6_prompt) # adding the prompt to the box

        # adding responses to box 6 start
        question6Box.add(question6_better)
        question6Box.add(question6_worse)
        question6Box.add(question6_same)
        # adding responses to box 6 end

        divider = toga.Divider() # added a divider to divide the Enter button and the rest of the questions

        # definition of the enter button for the questionaire
        enter = toga.Button(
            "Enter",
            style=Pack(padding=(3, 10)),
        )


        # definition for the blurb of encourgement
        ending = toga.MultilineTextInput(style=Pack(padding=(20, 5)), initial=
            'Thank you for taking your daily check. '
            'Things may seem tough at times, but they will eventually get better, I promise!'
            'Always remember that you are special and of worth! You do not deserve any pain, only love!'
            'Talking to someone close always helps or you can connect with people through the connect tab or call a helpline.',
            placeholder='Thank you for taking your daily check. '
            'Things may seem tough at times, but they will eventually get better, I promise!'
            'Always remember that you are special and of worth! You do not deserve any pain, only love!'
            'Talking to someone close always helps or you can connect with people through the connect tab or call a helpline.',readonly=True)

        section2.add(question1Box) # adds the Q1 Box to the main window box
        section2.add(question2Box) # adds the Q2 Box to the main window box
        section2.add(question3Box) # adds the Q3 Box to the main window box
        section2.add(question4Box) # adds the Q4 Box to the main window box
        section2.add(question5Box) # adds the Q5 Box to the main window box
        section2.add(question6Box) # adds the Q6 Box to the main window box
        section2.add(divider) # adds the divider to the main window box
        section2.add(enter) # adds the enter button to the main window box
        section2.add(ending) # adds the blurb of encourgement to the main window box

        ######################################################################
        # Section 2 -- Shanza Code Here End
        ######################################################################

        ######################################################################
        # Section 3 -- Veer Code Here Start
        ######################################################################
        connect = db.table('connect') # connects to the 'connect' table that is part of the database

        titles, content = connectPostsList(connect.all()) # gets the titles and content from the connect posts


        sec3_box = toga.Box(style=Pack(direction=COLUMN, padding=5)) # creates the box that stores the elements

        for a, b in enumerate(titles): # iterates through the connect titles
            postClass = connectPosts(titles[a], content[a]) #initailizes the post

            postTitle, postContent = postClass.connectPost() # creates the posts

            divider = toga.Divider() # creates a divider that will divide the posts

            sec3_box.add(postTitle) # adds the post title to the screen
            sec3_box.add(postContent) # adds the post content to the screen
            sec3_box.add(divider) # and this line adds the divder to the screen

        section3.add(sec3_box) # adds 'sec3_box' to the main window
        ######################################################################
        # Section 3 -- Veer Code Here End
        ######################################################################

        ######################################################################
        # Section 4 -- Veer Code Here Start
        ######################################################################

        # this stuff is kinda self explanitory

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


        sec4_box = toga.Box(style=Pack(direction=COLUMN, padding=5)) # stores the elements defined above
        sec4_box.add(kidsHelpPhone)                #
        sec4_box.add(abWideMentalHealthPhone)      # Adds the elements defined above to the screen
        sec4_box.add(yycMentalHealthHelpline)      #
        sec4_box.add(yycsuicidePreventionHotline)  #

        section4.add(sec4_box) # adds all the elements to the main window

        ######################################################################
        # Section 4 -- Veer Code Here End
        ######################################################################

        section1Main.content = [section1L, section1R] # this is the journaling section. The journaling section is a split section so i have split it up as Section 1 Left and section 1 R.

        main_box.add('Checkin/journaling', section1Main) #
        main_box.add('hurtmenot', container)             # Adding the different sections to the main box
        main_box.add('connect', section3)                #
        main_box.add('helplines', section4)              #

        self.main_window = toga.MainWindow(title=self.formal_name) # creates the main window and gives it a title
        self.main_window.content = main_box # give the main window content of main box
        self.main_window.show() # displays the main window

    def newJournalEntry(self, widget): # does what it says it does
        journal = db.table('journal') # connects to the journal table in the data base
        journal.insert({self.title.value : {'content':self.diary_writing.value, 'overall':str(self.overall.value),'date':str(self.today)}}) # inserts a new journal entry
        self.sec1_box.remove(self.diary_writing) #
        self.sec1_box.remove(self.overallBox)    # Removes the elements from the screen so other elements can be added to the screen
        self.sec1_box.remove(self.enter)         #
        self.sec1_box.remove(self.title)         #

        # updates the button list. same stuff as lines 113-126
        self.titles, self.content, self.overallList, self.journalDate = journalEntriesList(self.journal.all())
        for i in self.journalButtons:
            self.sec1_box2.remove(i)
            self.journalButtons = []

        for a,b in enumerate(self.titles):
            journalClass = journalEntries(self.titles[a], self.displayJournalEntry)


            self.journalButtons.append(journalClass.journalEntry())

        for i in self.journalButtons:
            self.sec1_box2.add(i)

        self.openedJournalEAdder = False # tells the app that other elements can be added to the screen


    def setJournalAdder(self, widget): # shows the elements required to create a new journal entry
        if self.openedJournalEntry == True: # checks to see if a journal entry has been opened up
            self.sec1_box.remove(self.titleLabel)    #
            self.sec1_box.remove(self.contentLabel)  # If there has been one opened up, it removes the journal entry elements from the screen
            self.sec1_box.remove(self.overallLabel)  #
            self.sec1_box.remove(self.dateLabel)     #
            self.openedJournalEntry = False # and then tell the app that there is nothing being displayed on the screen

        self.today = date.today() # gets the current days date

        self.title = toga.TextInput(style=Pack(padding=(20, 5)), placeholder='Enter a creative title for you journal entry', readonly=False) # creates the textinput for a title

        # creates the multilinetext input that you put your thoughts and feelings into for the journal entry
        self.diary_writing = toga.MultilineTextInput(style=Pack(padding=(20, 20)), initial='Enter your thoughts and feelings here', placeholder='Enter your thoughts and feelings here', readonly=False)

        self.overall = toga.NumberInput(min_value=0, max_value=10) # creats the overall feeling input

        # provides 'self.overall' with a label to tell people what 'self.overall' is
        overallLabel = toga.Label(
            'Overall feeling 1 - 10 scale:',
            style=Pack(padding=(5, 0))
        )

        self.overallBox = toga.Box(style=Pack(direction=ROW, padding=5)) # creates a seperate box for 'self.overall' and its label. mainly for organization

        self.overallBox.add(overallLabel) # adds 'self.overall' and 'overallLabel' to 'self.overallBox'
        self.overallBox.add(self.overall) #

        # creates the button that create the journal entry
        self.enter = toga.Button(
            'Enter',
            on_press=self.newJournalEntry,
            style=Pack(padding=5)
        )



        #sec1_box.add(date)
        self.sec1_box.add(self.title)          #
        self.sec1_box.add(self.diary_writing)  # addes the elements defined above to the screen
        self.sec1_box.add(self.overallBox)     #
        self.sec1_box.add(self.enter)          #
        self.openedJournalEAdder = True # tells the app that the journal entry adder has been toggled and is being displayed to the screen

    def displayJournalEntry(self, widget): # displays the journal entrys
        if self.openedJournalEAdder == True: # checks if the journal entry adder elements have been printed to the screen.
            self.sec1_box.remove(self.diary_writing) #
            self.sec1_box.remove(self.overallBox)    # if they have been printed to the screen it removes these elements from the screen
            self.sec1_box.remove(self.enter)         #
            self.sec1_box.remove(self.title)         #
            self.openedJournalEAdder = False # and then tell the app that there is nothing being displayed on the screen

        if self.openedJournalEntry == True: # checks to see if a journal entry has been opened up
            self.sec1_box.remove(self.titleLabel)   #
            self.sec1_box.remove(self.contentLabel) # if a entry has been opend up, it will remove the journal entry elements from the screen
            self.sec1_box.remove(self.overallLabel) #
            self.sec1_box.remove(self.dateLabel)    #
            self.openedJournalEntry = False # and then tell the app that there is nothing being displayed on the screen

        label = '' # empty string to store the label of the button.

        for i in self.journalButtons: # runs through the list of all created journal entries
            if i == widget: # if one of these entries(buttons) match the button that ran this function
                label = i.label # then save that buttons label in the empty label string
                break # and stop the loop

        num = 0 # create a temporary int value

        for a in self.titles: # loop through the titles
            if a == label: # if one of the titles match 'label'
                break # then break the loop
            num += 1 # adds one to 'num'. This keeps track of the index

        # creates the entry title
        self.titleLabel = toga.Label(
            label,
            style=Pack(padding=5)
        )

        # because of the way the title, content, date and overall feeling lists are created the index of a title from the title list will match
        # up with the index of the titles corresponding date, content and overall feeling

        # creates the date label
        self.dateLabel = toga.Label(
            'Date: ' + self.journalDate[num],
            style=Pack(padding=5)
        )

        # creates the content label
        #unfortunatly, briefcase(the library we are using to create the app) does not support multiline labels, only multilinetextinputs
        self.contentLabel = toga.MultilineTextInput(
            initial = self.content[num],
            placeholder = self.content[num],
            style=Pack(padding=5),
            readonly=True
        )

        # creates the overall feeling label
        self.overallLabel = toga.Label(
            'Overall Feeling: ' + self.overallList[num],
            style=Pack(padding=5)
        )

        self.sec1_box.add(self.titleLabel)   #
        self.sec1_box.add(self.dateLabel)    # addes the journal entry elements to the screen
        self.sec1_box.add(self.contentLabel) #
        self.sec1_box.add(self.overallLabel) #

        self.openedJournalEntry = True # tells the app that there are elements that have to removed before other elements can be printed to the screen


##############################################################################
#App Class End
##############################################################################

##############################################################################
#Other Classes start
##############################################################################

class connectPosts: # creates the posts.
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

class journalEntries: # creates the journal entry buttons
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
