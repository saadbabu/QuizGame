import random

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


def get_TOF_statement1 ():
    statemets1 = [  ]
    statemets1.append(["English is an international language", "T" ])
    statemets1.append([ "Australia is the Largest continent of the world", 'F' ])
    statemets1.append([ "Asia is the largest continent of the world", "T" ])
    statemets1.append([ "Brazil has won more World Cup (soccer) championships than any other country", "T" ])
    statemets1.append([ "Fencing is one of the sports of the modern pentathlon.", "T" ])
    return statemets1


def TF1():
    print("================= TRUE AND FALSE =================")
    print("===================== LEVEL 1 ====================")
    tof_statements = get_TOF_statement1()
    random.shuffle(tof_statements)


    for s in tof_statements:
        print("Q: ", s[ 0 ])
        guess = input(" => PRESS T or F FOR ANSWERING : ")

        if guess == s[ 1 ]:
            print(" => CORRECT!!")
        else:
            print(" => INCORRECT!!!")

        print()
        print("--------------------------------------------------")


class Linkedlist(object):
    def __init__ (self):
        self.head = None

    def Enqueue(self, newdata):
        print(newdata)
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = newNode

    def isempty (self):
        if self.head == None:
            return True
        else:
            return False


def TF2 ():
    print()
    print("================= TRUE AND FALSE =================")
    print("===================== LEVEL 2 ====================")
    Queue = Linkedlist()
    Queue.Enqueue("1) Muhammad Ali jinnah is the first Governor General of Pakistan?")
    Ans1 = input(str("=> Enter Correct Option : "))
    if (Ans1 == "T"):
        print("=> Correct\n")
    else:
        print("=> Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("2) Did Pakistan win the Cricket World Cup of 1996?")
    Ans2 = input(str("=> Enter Correct Option : "))
    if (Ans2 == "F"):
        print("=> Correct\n")
    else:
        print("=> Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("3) In 1960 ,Pakistan win Olympic gold medal in Hockey for the first time?")
    Ans3 = input(str("=> Enter Correct Option : "))
    if (Ans3 == "T"):
        print("=> Correct\n")
    else:
        print("=> Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("4) General Pervez Musharraf born in Karachi?")
    Ans4 = input(str("=> Enter Correct Option : "))
    if (Ans4 == "F"):
        print("=> Correct\n")
    else:
        print("=> Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("5) National flower of Pakistan is Jasmine? ")
    Ans5 = input(str("=> Enter Correct Option : "))
    if (Ans5 == "T"):
        print("=> Correct\n")
    else:
        print("=> Incorrect\n")
    print("--------------------------------------------------")

def get_TOF_statement2():
    statemets1 = []
    statemets1.append(["Mount Kilimanjaro is the highest mountain in the world", 'F'])
    statemets1.append(["Strictly Come Dancing first aired in the UK in 2005", 'F'])
    statemets1.append(["a group of swans is known as a bevy", 'T'])
    statemets1.append(["Nepal is the only country in the world which does not have a rectangular flag?", 'T'])
    statemets1.append(["Switzerland shares land borders with four other countries?", 'F'])

    return statemets1


def TF3():
    print("================= TRUE AND FALSE =================")
    print("===================== LEVEL 3 ====================")
    tof_statements = get_TOF_statement2()
    random.shuffle(tof_statements)


    for s in tof_statements:

        print("Q: ", s[ 0 ])
        guess = input(" => PRESS T or F FOR ANSWERING : ")

        if guess == s[ 1 ]:
            print(" => CORRECT!!")
        else:
            print(" => INCORRECT!!!")

        print()
        print("--------------------------------------------------")

def TF4 ():
    print()
    print("================= TRUE AND FALSE =================")
    print("===================== LEVEL 4 ====================")
    print()
    Queue = Linkedlist()
    print("--------------------------------------------------")
    Queue.Enqueue("1) The mosquito has caused more human deaths than anyother creature in history?")
    Ans1 = input(str("Enter Correct Option : "))
    if (Ans1 == "T"):
        print("Correct\n")
    else:
        print("Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("2) Russia has the largest area of any country in the world?")
    Ans2 = input(str("Enter Correct Option : "))
    if (Ans2 == "T"):
        print("Correct\n")
    else:
        print("Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("3) Corn is the most produced crop in the world?")
    Ans3 = input(str("Enter Correct Option : "))
    if (Ans3 == "T"):
        print("Correct\n")
    else:
        print("Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("4) Carl Lewis holds the record for most individual gold medals at the Olympics?")
    Ans4 = input(str("Enter Correct Option : "))
    if (Ans4 == "F"):
        print("Correct\n")
    else:
        print("Incorrect\n")
    print("--------------------------------------------------")
    Queue.Enqueue("5) the five rings on the Olympic flag are interlocking?")
    Ans5 = input(str("Enter Correct Option : "))
    if (Ans5 == "T"):
        print("Correct\n")
    else:
        print("Incorrect\n")
    print("--------------------------------------------------")


def Correct_Ans ():
    def Bubble_sort (Sort):
        n = len(Sort)

        for i in range(n):
            for j in range(0, n - i - 1):
                if Sort[ j ] > Sort[ j + 1 ]:
                    Sort[ j ], Sort[ j + 1 ] = Sort[ j + 1 ], Sort[ j ]
        return Sort

    Sort = [ ("=> English is an international language", 'True'),
             ("=> Australia is the Largest continent of the world", 'False'),
             ("=> Asia is the largest continent of the world", 'True'),
             ("=> Brazil has won more World Cup (soccer) championships than any other country", 'True'),
             ("=> Fencing is one of the sports of the modern pentathlon.", 'True'),
             ("=> The mosquito has caused more human deaths than anyother creature in history", 'True'),
             ("=> Russia has the largest area of any country in the world", 'True'),
             ("=> Corn is the most produced crop in the world" , 'True'),
             ("=> Carl Lewis holds the record for most individual gold medals at the Olympics", 'F'),
             ("=> the five rings on the Olympic flag are interlocking", 'True'),
             ("=> Mount Kilimanjaro is the highest mountain in the world", 'False'),
             ("=> Strictly Come Dancing first aired in the UK in 2005", 'False'),
             ("=> A group of swans is known as a bevy", 'True'),
             ("=> Nepal is the only country in the world which does not have a rectangular flag?", 'True'),
             ("=> Switzerland shares land borders with four other countries?", 'F'),
             ("=> Muhammad Ali jinnah is the first Governor General of Pakistan?" , 'True'),
             ("=> Did Pakistan win the Cricket World Cup of 1996?", 'False'),
             ("=> In 1960 ,Pakistan win Olympic gold medal in Hockey for the first time?", 'True'),
             ("=> General Pervez Musharraf born in Karachi?", 'False'),
             ("=> National flower of Pakistan is Jasmine?", 'True')]
    print(*Bubble_sort(Sort), sep="\n")
    print("--------------------------------------------------")

def MCQ1 ():
    statemets2 = [ ]
    statemets2.append(["What is name of father of Computer___?\na. you\nb. Reena bey\nc. Bill gates\nd. Charles baggage\n", "D" ])
    statemets2.append(["MS-Word is an example of\na. An operating system\nb. A processing device\nc. An application software\nd. An input device",'C' ])
    statemets2.append(["What is the capital of USA?\na. Zimbabwe\nb. New York\nc. Washington\nd. Do not exist", "C" ])
    statemets2.append(["The staple food of the Vedic Aryan was\na.  Barley and rice\nb. Milk and its products\nc. Rice and pulses\nd. Vegetables and fruits","B" ])
    return statemets2


def MCQS1 ():
    print("====================== MCQS ======================")
    print("===================== LEVEL 1 ====================")
    MCQS = MCQ1()
    random.shuffle(MCQS)

    for s in MCQS:

        print("Q: ", s[ 0 ])
        print("--------------------------------------------------")
        guess = input(" => PRESS A OR B OR C OR D FOR ANSWERING: ")

        if guess == s[ 1 ]:
            print("CORRECT!!")
        else:
            print(' => Incorrect!!! try again.')
        print("--------------------------------------------------")


class Stack:

    def __init__(self):
        self.head = None

    def isempty (self):
        if self.head == None:
            return True
        else:
            return False

    def push (self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

        # Remove element that is the current head (start of the stack

    def display (self):

        node = self.head
        if self.isempty():
            print("empty")

        else:

            while (node != None):
                print(node.data)
                node = node.next
                return


def MCQS2 ():
    print("====================== MCQS ======================")
    print("===================== LEVEL 2 ====================")
    mystack = Stack()
    print("-----------------------------------")

    mystack.push("1) Who wrote Tarana-e-Pakistan?:\na. Hafeez Jallundhari \nb. Ahmed Chagla\nc. Abdul Rab Nishtar\nd. Jagannath Azad\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans1 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans1 == "A"):
        print("Correct")

    else:
        print("Incorrect")

    print("--------------------------------------------------")
    mystack.push("2) How is Pakistan’s film industry known? \na. Bollywood \nb. Hollywood\nc. Tollywood \nd. Lollywood\n")
    mystack.display()

    print("--------------------------------------------------")
    Ans2 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans2 == "D"):
        print("Correct")

    else:
        print("Incorrect")

    print("--------------------------------------------------")
    mystack.push("3) Which party was in power in North West Frontier Province at the time of independence? \na. Justice Party \nb. Congress\nc. Muslim League\nd. Communist Party\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans3 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans3 == "B"):
        print("Correct")

    else:
        print("Incorrect")
    print("--------------------------------------------------")
    mystack.push("4) What does the name Pakistan mean? \na. Land Of Pure \nb. Land Of Dirt \nc. None Of Above \nd. Both A and B\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans4 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans4 == "A"):
        print("Correct")

    else:
        print("Incorrect")
    print("--------------------------------------------------")
    mystack.push("5) Which country does not border Pakistan? \na. Nepal \nb. China \nc. India \nd. Afghanistan \n")
    mystack.display()
    print("--------------------------------------------------")
    Ans5 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans5 == "A"):
        print("Correct")

    else:
        print("Incorrect")
    print("--------------------------------------------------")


def QUESTIONS3():
    statemets2 = [ ]
    statemets2.append([ "Today the most popular social networking site is \na. Myspace\nb. Twitter\nc. Weibo\nd. Facebook\n", "D" ])
    statemets2.append(["Creating a website or group that looks like it originated from concerned grassroots efforts of citizens is known as\na. Lurking\nb. Trolling\nc. Phising\nd. Astroturfing",'D' ])
    statemets2.append(["Two increasingly important ethical aspects of social media are\na. ratings and traffic\nb. transparency and privacy\nc. identity and honesty\nd. Virtue and virality","B" ])
    statemets2.append([ "Which of these cities is NOT a national capital\na.  Sydney\nb. Prague\nc. Cairo\nd. Bangkok", "A" ])
    statemets2.append([ "Which of these countries was NEVER part of the British Empire\na.  Newzeland\nb. Ireland\nc. Thailand\nd. Kenya","C" ])
    return statemets2


def MCQS3 ():
    print("====================== MCQS ======================")
    print("===================== LEVEL 3 ====================")
    MCQS = QUESTIONS3()
    random.shuffle(MCQS)
    for s in MCQS:

        print()
        print("Q: ", s[ 0 ])
        print()
        print("--------------------------------------------------")
        guess = input("PRESS A OR B OR C OR D FOR ANSWERING: ")
        print()

        if guess == s[ 1 ]:
            print("CORRECT!!")
        else:
            print('Incorrect!!! try again.')

        print("--------------------------------------------------")

def MCQS4 ():

    print("====================== MCQS ======================")
    print("===================== LEVEL 4 ====================")
    mystack = Stack()
    mystack.push("1) What is one of the big differences between traditional media and social media?\na. participatory production\nb. social media reaches only a few people at a time\n c. the management structure of the companies\nd. traditional media offers no way for audiences to communicate with media producers\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans1 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans1 == "A"):
        print("Correct")
    else:
        print("Incorrect")
    print("--------------------------------------------------")
    mystack.push("2)  Which of the following is NOT a fundamental area of change regarding people's media habits?\na. conversation\nb. collaboration\nc. choice\nd. communication\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans2 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans2 == "D"):
        print("Correct")
    else:
        print("Incorrect")
    print("--------------------------------------------------")
    mystack.push("3) A portable chunk of code that can be embedded in Web pages to give extra functionality is known as a?\na. folksonomy\nb. widget\n c. curator\nd. wiki\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans3 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans3 == "B"):
        print("Correct")
    else:
        print("Incorrect")
    print("--------------------------------------------------")
    mystack.push("4) The state of spam, or unwanted commercial emails, in today's Internet could best be described as?\n a. Increased numbers of spam messages have made email largely useless for business today.\n b. Spammers have become far more sophisticated in their techniques to avoid spam filters.\n c. Anti-spam legislation and technology have helped reduced spam to a five-year low.\nd. Spam filters have largely been ineffective and spam continues to grow as a percentage of online traffic.\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans4 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans4 == "C"):
        print("Correct")
    else:
        print("Incorrect")
    print("--------------------------------------------------")
    mystack.push("5) A website that lets anyone add, edit, or delete pages of content is called a?\n a. wiki\nb. online forum\nc. usenet\nd. lurker site\n")
    mystack.display()
    print("--------------------------------------------------")
    Ans5 = input(str(("PRESS A OR B OR C OR D FOR ANSWERING: ")))
    if (Ans5 == "A"):
        print("Correct")
    else:
        print("Incorrect")
    print("--------------------------------------------------")
def Correct_MCQS():
    def Selection ( arr, n ):
        for i in range(n):
            index = i
            str = arr[ i ]

            for j in range(i + 1, n):

                if str > arr[ j ]:
                    str = arr[ j ]
                    index = j

            if index != i:
                temp = arr[ i ]
                arr[ i ] = arr[ index ]
                arr[ index ] = temp

        return arr

    arr = [ ("=> What is name of father of Computer___? => Ans :Charles baggage"),
            ("=> MS-Word is an example of ? => Ans :An application software"),
            ("=> What is the capital of USA? => Ans :Washington"),
            ("=> The staple food of the Vedic Aryan was? => Ans :Milk and its products"),
            ("=> which of these cities does not border the Greatest Lake?=> Ans :Pittsburgh"),
            ("=> What is one of the big differences between traditional media and social media? => Ans :Participatory production"),
            ("=> Which of the following is NOT a fundamental area of change regarding people's media habits? => Ans :communication"),
            ("=> A portable chunk of code that can be embedded in Web pages to give extra functionality is known as a? => Ans :widget"),
            ("=> The state of spam, or unwanted commercial emails, in today's Internet could best be described as? => Ans :Anti-spam legislation and technology have helped reduced spam to a five-year low."),
            ("=> A website that lets anyone add, edit, or delete pages of content is called a? => Ans :Wiki"),
            ("=> Today the most popular social networking site is?  => Ans :Facebook"),
            ("=> Creating a website or group that looks like it originated from concerned grassroots efforts of citizens is known as => Ans :Astroturfing"),
            ("=> Two increasingly important ethical aspects of social media are? => Ans :transparency and privacy"),
            ("=> Which of these cities is NOT a national capital => Ans :Sydney"),
            ("=> Which of these countries was NEVER part of the British Empire => Ans :Thailand"),
            ("=> Who wrote Tarana-e-Pakistan? => Ans :Hafeez Jallundhari"),
            ("=> How is Pakistan’s film industry known?  => Ans :Lollywood"),
            ("=> Which party was in power in North West Frontier Province at the time of independence? => Ans :Congress"),
            ("=> What does the name Pakistan mean? => Ans :Land Of Pure"),
            ("=> Which country does not border Pakistan? => Ans :. Nepal")]

    for i in range(len(Selection(arr, len(arr)))):
        print(Selection(arr, len(arr))[ i ])

class Linked_List:

    def __init__ (self):
        self.head = None

    def Print (self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push (self, data1):
        node = Node(data1)
        node.next = self.head
        self.head = node

# main menu

def main_menu ():
    print("====================================================================")
    print("WELCOME TO THE QUIZ GAME PREPARED BY MUHAMMAD SAAD AND AFNAN ANSARI")
    print("====================================================================")
    print()
    print("Please enter your name: ")
    name = input()
    print("--------------------------------------------------")
    print(name, " pleasure to see you!!")
    print("--------------------------------------------------")
    print(name, " please select any of the following")
    print("(1)TRUE AND FALSE \n(2) MCQS")
    choice = input("Press Button : ")
    print("--------------------------------------------------")

    # calls the part 1 questions

    if choice == "1":
        TF1()
        TF2()
        TF3()
        TF4()
        print("please hit 1 to continue")
        print("Press 2 to Study Whole True/False")
        print("Press 3 to end")
        hit1 = int(input("Enter Digit : "))
        print("--------------------------------------------------")
        if hit1 == 1:
            main_menu()
        elif hit1 == 2:
            Correct_Ans()
            main_menu()
        elif hit1 == 3:
            fuctions()
        else:
            print("INVALID INPUT!!!")

            # calls the part 2 questions

    elif choice == "2":
        MCQS1()
        MCQS2()
        MCQS3()
        MCQS4()

        print("Press 1 to continue")
        print("Press 2 to Study Whole MCQS")
        print("Press 3 to end")
        hit2 = int(input("Enter Digit : "))
        print("--------------------------------------------------")
        if hit2 == 1:
            main_menu()
        elif hit2 == 2:
            Correct_MCQS()
            main_menu()
        elif hit2 == 3:
            fuctions()
        else:
            print("INVALID INPUT!!!")
    else:
        print("INVALID INPUT!!")
        print("IF WANT TO CONTINUE HIT Y OR TO END HIT N")
        again = input()
        if again == "Y":
            main_menu()
        else:
            fuctions()

# funcction panel
i=0
def fuctions ():
    while (i < 2):
        print()
        print("1 : Want To Add Question In The List")
        print("2 : Display Question You Have Added")
        print("3 : Want To Search your Score Level Vise")
        print("4 : Leave Suggestions")
        print("5 : Quit The Game")
        choice = int(input("Enter your Choice: "))
        if (choice == 1):
            saad = Linked_List()
            print("ENTER YOUR QUESTION:")
            question = input()
            saad.push(question)
            print("ADDED SUCCESSFULLY!")
            print()

            print("ENTER YOUR QUESTION:")
            question1 = input()
            saad.push(question1)
            print("ADDED SUCCESSFULLY!")
            print()

            print("ENTER YOUR QUESTION:")
            question2 = input()
            saad.push(question2)
            print("ADDED SUCCESSFULLY!")

        elif (choice == 2):
            saad = Linked_List()
            saad.head = Node(question)
            second = Node(question1)
            third = Node(question2)
            saad.head.next = second
            second.next = third
            saad.Print()

        elif (choice == 3):

            arr1 = [ level1, level2 ]
            lengthofarray = len(arr1)
            x = input("enter your choice:")
            result = binary(arr1, x)
            if result != -1:
                print("element is present!!!!")
                if x == 'level1':
                    print("your score of level1: ", score1)
                elif x == 'level2':
                    print("your score of level2: ", score2)
                else:
                    print("INVALID INPUT!!!!")
            else:
                print("element is not present!!!!")

        elif choice == 4:
            suggestion()
        elif choice == 5:
            print("THANKS FOR PLAYING THE GAME!!!!")
            break
    print()

def Exit ():
    print()

    # suggestion pannel


def suggestion ():
    print()
    print("WE HOPE YOU LOVE PLAYING OUR GAME PLEASE GIVE YOUR SUGGESTION REGARDING THIS GAME")
    suggest = input("SUGGESTIONS: ")
    if suggest == "":
        print("PLEASE LEAVE YOUR SUGGESTIONS")
    else:
        print("THANKS FOR YOUR SUPPORT!!")

main_menu()