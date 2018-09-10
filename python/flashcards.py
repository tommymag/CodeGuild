import random

# object-oriented programming development flashcards 

# otherwise OOPDF

dict_of_terms_acronym = {  # Will need to figure out case sensitve - levels of difficulty

    "API" : "Application Programming Interface",
    "BASh" : "Born Again Shell",
    "JS" : "Javascript",
    "UI" : "User Interface",
    "CSS" : "Cascading Style Sheets",
    "DOM" : "Document Object Model",             # Dictionary of 'terms' and 'definitions'
    "GIF" : "Graphical Interchange Format",
    "PNG" : "Portable Network Graphics",
    "MNG" : "Multiple-image Network Graphics",
    "GUI" : "Graphical User Inerface",
    "REPL" : "Read Evaluate Print Loop",
    "RAM" : "Random Access Memory",
    "ROM" : "Read Only Memory",
    "HDD" : "Hard Disk Drive",
    "OS" : "Operating System",
    "SSD" : "Solid State Drive",
    "JPEG" : "Joint Photographic Experts Group",
    "ORM" : "Object Relational Mapping",                # research moore on this
    "DBMS" : "Database Management system",
    "CPU" : "Central Processing Unit",
    "IT" : "Information Technology",                        # First 20 are in the admin!
    "WSGI" : "Web Server Gateway Interface",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition"    
}

dict_of_terms_easy = {


    "Directory" : "A file system cataloging structure which contains references to other computer files, and possibly other directories",
    "Layout" : "Arrangement of text and graphics",
    "Float" : "Decimal",
    "Integer" : "Whole Number",
    "BMP" : "Bitmap",
    "W3C" : "World Wide Web Consortium",
    "Grid" : "An intersecting set of horizontal and vertical lines",
    "Pixel" : "The smallest controllable element of a picture represented on the screen",
    "Query" : "A request for information from a database",
    "Django" : "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design",
    "Term" : "",
    "Class" : "Pre-object; list of attributes",
    "Variable" : "Data represented",
    "Module" : "Part of a program that contains one or more routines",
    "Javascript" : "High level interpretive. ",
    "Crash" : "an unexpected termination of a process",
    "Process" : "a program that is running on your computer",
    "JSON" : "JavaScript Object Notation",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition"

}

dict_of_terms_medium = { # unsure of how to create as of yet

    "The Document Object Model (DOM)" : "an object-oriented representation of the web page, which can be modified with a scripting language such as JavaScript represents the document as nodes and objects",
    "Web Page" : "a document",
    "Array" : "ordered, linear collections of elements",
    "<head>" : "HTML; this element is a container for metadata and is placed between the <html> tag and the <body> tag",
    "<html>" : "The <html> tag tells the browser that this is an HTML document. The <html> tag represents the root of an HTML document. The <html> tag is the container for all other HTML elements",
    "Modular Programming" : "a software design technique that emphasizes separating the functionality of a program into independent peices such that each part contains everything necessary to execute only one aspect of the desired functionality.",
    "JSON" : " an open standard format that allows data to be transferred across the web by using attribute-value pairs",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition"
}

dict_of_terms_hard = {
    "WSGI" : "a simple calling convention for web servers to forward requests to web applications or frameworks written in Python",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition",
    "Term" : "Definition"

}

while True:

    fc_menu = input("""
                        1. Add Term
                        2. Change term
                        3. Study
                        4. Face The Challenge
                        5. Quit
                        """)

    if fc_menu == "1":
        new_term = input("What is the term you would like to add?: ")
    definition = input("What is the definition you would like stored?: ")
    dict_of_terms_easy[new_term] = definition
    print(new_term + " added to flashcards with the definition: " + definition + "\n")
    print("Anything Else?")

    # elif menu == "2":
    #     while True:
    #         try:
    #             new_term = input("Which term you would like to change?:"):
    #     break
    # except KeyError:
    # print("huh?! Stop messing around..")
    # term_change = input("What is the new name?: ")
    # p_info = dict_of_terms[new_term]
    # del terms[name]
    # phone_book[name_change] = p_info
    # print("\nAnything else?")
    # elif menu == "4":
    # while True:
    #     try:
    #         name = input("Which name would you like to delete?: ")
    #         terms[name]
    #         break
    #     except KeyError:
    #         print("Who?!")
    # del terms[name]
    # print("{} has been deleted.\n".format(name))
    # print("Anything else?")
    elif fc_menu == "5":
        print("\nGoodbye!\n")
        quit()
phonebook()
    
