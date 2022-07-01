library = {}
final_list = []

while True:
    run = str(input("press any key to start the program otherwise q for quit:"))
    if run=="q" or run=="Q":
        print("thank you for this program")
        break
    else:
        subject_name = str(input("enter the name of subject:"))
        shell = str(input("choose the shell from a,b,c,d:"))
        a = []
        b = []
        c = []
        d = []
        if shell =="a":
            while True:
                book_name = str(input("please enter the book name otherwise type Stop to add book:"))
                if book_name=="Stop" or book_name=="stop" or book_name=="STOP":
                    break
                else:
                    a.append(book_name)
        elif shell=="b":
            while True:
                book_name = str(input("please enter the book name otherwise type Stop to add book:"))
                if book_name=="Stop" or book_name=="stop" or book_name=="STOP":
                    break
                else:
                    b.append(book_name)
        elif shell=="c":
            while True:
                book_name = str(input("please enter the book name otherwise type Stop to add book:"))
                if book_name=="Stop" or book_name=="stop" or book_name=="STOP":
                    break
                else:
                    c.append(book_name)
        elif shell=="d":
            while True:
                book_name = str(input("please enter the book name otherwise type Stop to add book:"))
                if book_name=="Stop" or book_name=="stop" or book_name=="STOP":
                    break
                else:
                    d.append(book_name)
        else:
            print("please enter the correct book shelll id")
        library.update({subject_name:{"a":a,"b":b,"c":c,"d":d}})    
        print(library)
        final_list.append(library)
print(final_list)