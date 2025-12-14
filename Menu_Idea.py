import time

name = input("\nHi! what is your name? ").title()
print(f"\nWelcome to the Code Compiler Program {name}! This is Chrysler \nyour host, and here to guide you through this program.  ")

while True:
    print("\n\t****************************************************")
    print("\t*                   MAIN MENU                      *")
    print("\t****************************************************")
    print("\t* Please select from the options :                 *")
    print("\t*                                                  *")
    print("\t* C .  Exploring Print Statements.                 *")
    print("\t* H .  Understanding Variables.                    *")
    print("\t* R .  Working with Operators.                     *")
    print("\t* Y .  Using Conditional Statements.               *")
    print("\t* S .  Implementing Loops.                         *")
    print("\t* L .  Managing List.                              *")
    print("\t* E .  Defining Functions.                         *")
    print("\t* X .  Exiting Program.                            *")
    print("\t*                                                  *")
    print("\t****************************************************")

    choice = input("\nEnter selection and then press the ENTER key: ")

    if choice == "C":
        print("\nPlease Wait....")
        time.sleep(2)
        #Time sleep for countdown before the print comes up
        
        while True:
            print(f"\n\nHi, {name}! Welcome to Print Statements.")

            print("""
        The print() function in Python is your primary way
        to display output to the console. It takes one or 
        more arguments (values you want to display) and 
        shows them on the screen.
        """)
            
            print("\n\t==================================================")
            print("\t\t   * PRINT STATEMENTS MENU * ")
            print("\t==================================================")
            print("\n\t1. Print Statements Characteristics")
            print("\t2. Print Statements Implementation and Use Cases")
            print("\t3. Back to Main Menu")
            print("\t==================================================")

            sub_choice = input("\nEnter your choice: ")
            if sub_choice == '1':
                while True:
                    print("\nSelect again for its characteristics.")

                    print("\n\t┌" + "───────────────────────────────────────────" + "┐")
                    print("\t│   PRINT STATEMENTS CHARACTERISTICS MENU   │")
                    print("\t└" + "───────────────────────────────────────────" + "┘")

                    print("\t┌" + "───────────────────────────────────────────" + "┐")
                    print("\t│  a. Print Statements Definitions.         │")
                    print("\t│  b. Purpose of Print Statements.          │")
                    print("\t│  c. Return to Sub Menu                    │")
                    print("\t└" + "───────────────────────────────────────────" + "┘")
                    
                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nDEFINITION OF PRINT STATEMENTS:")
                        
                        print("""
        In Python, a print statement is a built-in function call,
        written as print(), that outputs text or data to the
        console or terminal. It evaluates its arguments, converts
        them into string representations, and displays the resulting
        text for the user.
        """)

                    elif newsub_choice == 'b':
                        print("\nPURPOSE OF PRINT STATEMENTS:")
                        
                        print("""
        The primary purpose of print statements in Python is to
        allow programmers to observe what a program is doing at
        runtime. This includes viewing the values of variables,
        checking the flow of logic, verifying correct program
        execution, and presenting information to users in a
        readable format.
        """)


                    elif newsub_choice == 'c':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")
                    
                    continue

            elif sub_choice == '2':
                while True:
                    print("\nSelect again for its implementation and use cases.")

                    print("\n\t┌" + "──────────────────────────────────────────────────────" + "┐")
                    print("\t│   PRINT STATEMENTS IMPLEMENTATION & USE CASES MENU   │")
                    print("\t└" + "──────────────────────────────────────────────────────" + "┘")

                    print("\t┌" + "──────────────────────────────────────────────────────" + "┐")
                    print("\t│  a.  Print Statements Example.                       │")
                    print("\t│  b.  Usage of Print Statements.                      │")
                    print("\t│  c.  Application of Print Statements.                │")
                    print("\t│  d.  Return to Sub Menu                              │")
                    print("\t└" + "──────────────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("EXAMPLE OF PRINT STATEMENTS:")
                        print("\n\tINPUT: ")
                        print("\n\tname = input(\"What is your name --> \")\n")
                        print("\tprint(\"\\t\\t\\t\\t\\t* \\n\\t\\t\\t\\t* \\t\\t* \\n\\t\\t\\t* \\t\\t\\t\\t*")
                        print("\t\\n\\t\\t* \\t\\tHi \\t\\t\\t\\t* \\n\\t* \\t\\t\\t\\t\", (name), \"\\t\\t\\t* ")
                        print("\t\\n\\t\\t* \\t\\t\\t\\t\\t\\t* \\n\\t\\t\\t* \\t\\t\\t\\t* \\n\\t\\t\\t\\t* \\t\\t* ")
                        print("\n\t\\n\\t\\t\\t\\t\\t*\")")

                        print("\n\tOUTPUT: ")

                        name = input("\n\tWhat is your name --> ").title()

                        print("\n\t\t\t\t\t* \n\t\t\t\t* \t\t* \n\t\t\t* \t\t\t\t* \n\t\t* \t\tHi \t\t\t\t* \n\t* \t\t\t\t",(name), "\t\t\t* \n\t\t* \t\t\t\t\t\t* \n\t\t\t* \t\t\t\t* \n\t\t\t\t* \t\t* \n\t\t\t\t\t*")


                    elif newsub_choice == 'b':
                        print("\nUSAGE OF PRINT STATEMENTS:")

                        print("""
        Using a print statement in Python involves calling
        the print() function and passing in one or more values
        to display. These values may include strings,
        numbers, variables, expressions, or formatted
        data.
        """)

                    elif newsub_choice == 'c':
                        print("\nAPPLICATION OF PRINT STATEMENTS:")

                        print("""
        Print statements are applied in debugging, testing,
        teaching, and simple user-interface outputs. They
        are used in virtually all Python programs when
        immediate visual information is needed.
        """)

                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '3':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                
                break

            else:
                print("\n\t# Error: ###############################")
                print("\t#                                      #")
                print("\t#      Invalid Option Selected!!!      #")
                print("\t#                                      #")
                print("\t########################################")
                print("\nPlease select only from the options.")
                
                continue
    
    elif choice == "H":
        print("\nPlease Wait....")
        time.sleep(2)
        
        while True:
            print(f"\n\nHi, {name}! Welcome to Variables.")
           
            print("\n\tVariables are fundamental building blocks in Python. \n\tThey act as containers for storing data values, allowing \n\tyou to refer to and manipulate these values \n\tthroughout your program. ")
            
            print("\n\t===========================================")
            print("\t\t    * VARIABLES MENU *  ")
            print("\t===========================================")
            print("\n\t1. Variables Characteristics")
            print("\t2. Variables Implementation and Use Cases")
            print("\t3. Back to Main Menu")
            print("\t===========================================")

            sub_choice = input("\nEnter your choice: ")
            
            if sub_choice == '1':
                while True:
                    print("\nSelect again for its characteristics.")

                    print("\n\n\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│     VARIABLES CHARACTERISTICS MENU     │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    print("\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│  a.  Variables Definition.             │")
                    print("\t│  b.  Purpose of Variables.             │")
                    print("\t│  c.  Variables Types.                  │")
                    print("\t│  d.  Return to Sub Menu                │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nDEFINITION OF VARIABLES:")
                        print("\n\tA variable in Python is a named reference to a value")
                        print("\tstored in memory. It allows programmers to label data")
                        print("\tso it can be reused and manipulated throughout a program.")
                    
                    elif newsub_choice == 'b':
                        print("\nPURPOSE O VARIABLES:")
                        print("\n\tThe purpose of a variable is to store information that")
                        print("\ta program needs to operate on. Variables make code")
                        print("\tflexible by allowing values to change without modifying")
                        print("\tthe entirecprogram.")

                    elif newsub_choice == 'c':
                        print("\nTYPES OF VARIABLES:")
                        print("\n\t1. Integer (int) > stores whole numbers, e.g., 10, -5")
                        print("\n\t2. Floating-point (float) > stores decimal numbers, \n\te.g., 3.14, -0.5")
                        print("\n\t3. String (str) > stores text, e.g., 'Hello', 'Python'")
                        print("\n\t4. Boolean (bool) > stores True or False")
                        print("\n\t5. List > stores multiple items in order, e.g., [1, \n\t2, 3]")
                        print("\n\t6. Tuple > stores multiple items in order (immutable), \n\te.g., (1, 2, 3)")
                        print("\n\t7. Dictionary (dict) > stores key-value pairs, e.g., \n\t{'name': 'Alice', 'age': 20}")
                        print("\n\t8. Set > stores unique items, e.g., {1, 2, 3}")

                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")
                    
                    continue

            elif sub_choice == '2':
                while True:
                    print("\nSelect again for its implementation and use cases.")

                    print("\n\n\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│   VARIABLES IMPLEMENTATION & USE CASES MENU   │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    print("\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│  a.  Variables Example.                       │")
                    print("\t│  b.  Application of Variables                 │")
                    print("\t│  c.  Return to Sub Menu                       │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")
                    if newsub_choice == 'a':
                        print("\nEXAMPLE VARIABLES:")
                        print("\nINPUT:")
                        print("\t+--------------------------------------------------+")
                        print("\t|             * VARIABLE EXAMPLE *                 |")
                        print("\t+--------------------------------------------------+")
                        print("\t|                                                  |")
                        print("\t| name = input(\"Type your name ---> \")             |")
                        print("\t| print(\"Welcome my friend\", name)                 |")
                        print("\t| print(\"Your name has\", len(name), \"characters.\") |")
                        print("\t|                                                  |")
                        print("\t+--------------------------------------------------+")

                        print("\nOUTPUT:")
                        name=input("\tType your name ---> ").title()
                        print("\n\tWelcome my friend", name) 
                        print("\tYour name has", len(name), "characters.")

                    elif newsub_choice == 'b':
                        print("\nAPPLICATION OF VARIABLES:")
                        print("\n\tVariables are applied in calculations, data processing,")
                        print("\tuser input storage, program state tracking, and nearly")
                        print("\tevery aspect of Python development. They enable")
                        print("\tprograms to handle dynamic, changing information rather")
                        print("\tthan fixed values.")


                    elif newsub_choice == 'c':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '3':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\n\t# Error: ###############################")
                print("\t#                                      #")
                print("\t#      Invalid Option Selected!!!      #")
                print("\t#                                      #")
                print("\t########################################")
                print("\nPlease select only from the options.")
                continue
    
    elif choice == "R":
        print("\nPlease Wait....")
        time.sleep(2)
        
        while True:
            print(f"\n\nHi, {name}! Welcome to Operators in Python.")
            
            print("\n\tOperators are special symbols in Python that perform \n\toperations on variables and values. They are essential \n\tfor performing calculations, making comparisons, and \n\tssmanipulating data in your programs.")
            
            print("\n\t=========================================")
            print("\t\t    * OPERATORS MENU * ")
            print("\t=========================================")
            print("\n\t1. Operators Characteristics")
            print("\t2. Operators Implementation and Use Cases")
            print("\t3. Back to Main Menu")
            print("\t=========================================")

            sub_choice = input("\nEnter your choice: ")
            
            if sub_choice == '1':
                while True:
                    print("\nSelect again for its characteristics.")

                    print("\n\n\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│     OPERATORS CHARACTERISTICS MENU     │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    print("\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│  a.  Operators Definition.             │")
                    print("\t│  b.  Purpose of Operators.             │")
                    print("\t│  c.  Operator Types.                   │")
                    print("\t│  d.  Return to Sub Menu                │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nDEFINITION OF OPERATORS:")
                        print("\n\tPython operators are special symbols that perform")
                        print("\toperations on variables and values, enabling you") 
                        print("\tto manipulate data. They are essential for performing") 
                        print("\tcalculations, comparisons, and logical operations in \n\tyour code.")

                        print("\n\tPython operators are special symbols that perform")
                        print("\toperations on variables and values, enabling you")
                        print("\tto manipulate data. They are essential for performing")
                        print("\tcalculations, comparisons, and logical operations in")
                        print("\tyour code.")
                        
                    elif newsub_choice == 'b':
                        print("\nPURPOSE OF OPERATORS:")
                        print("\n\tOperators allow you to perform arithmetic calculations")
                        print("\t(addition, subtraction), compare values (equal to,")
                        print("\tgreater than), and manipulate data logically (AND, 'OR,")
                        print("\tNOT), which are crucial for decision-making")
                        print("\tand data processing.")

                    elif newsub_choice == 'c':
                        print("\nTYPES OF OPERATORS:")
                        print("\n\tPython has several types of operators, including")
                        print("\tarithmetic, comparison, logical, assignment, bitwise,")
                        print("\tmembership, and identity operators, each serving a")
                        print("\tspecific purpose. Understanding these categories")
                        print("\thelps in writing efficient and effective code.")


                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")
                    
                    continue

            elif sub_choice == '2':
                while True:
                    print("\nSelect again for its implementation and use cases.")

                    print("\n\n\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│   OPERATORS IMPLEMENTATION & USE CASES MENU   │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    print("\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│  a.  Operator Example.                        │")
                    print("\t│  b.  Usage of Operators.                      │")
                    print("\t│  c.  Application of Operators.                │")
                    print("\t│  d.  Return to Sub Menu                       │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")
                    if newsub_choice == 'a':
                        print("\nEXAMPLE OF OPERATORS:")
                        print("\n\t+----------------------------------------------+")
                        print("\t|                 * INPUT *                    |")
                        print("\t+----------------------------------------------+")
                        print("\t| n1 = int(input(\"Enter the first number: \"))  |")
                        print("\t| n2 = int(input(\"Enter the second number: \")) |")
                        print("\t|                                              |")
                        print("\t| sum_ = n1 + n2                               |")
                        print("\t| diff = n1 - n2                               |")
                        print("\t| prod = n1 * n2                               |")
                        print("\t| quot = n1 / n2                               |")
                        print("\t|                                              |")
                        print("\t| print(\"Sum:\", sum_)                          |")
                        print("\t| print(\"Difference:\", diff)                   |")
                        print("\t| print(\"Product:\", prod)                      |")
                        print("\t| print(\"Quotient:\", quot)                     |")
                        print("\t+----------------------------------------------+")

                        print("\n\tOUTPUT: ")

                        n1 = int(input("\n\tEnter the first number: "))
                        n2 = int(input("\tEnter the second number: "))

                        sum_ = n1 + n2
                        diff = n1 - n2
                        prod = n1 * n2
                        quot = n1 / n2

                        print("\n\tSum:", sum_)
                        print("\tDifference:", diff)
                        print("\tProduct:", prod)
                        print("\tQuotient:", quot)
                    
                    elif newsub_choice == 'b':
                        print("\nUSAGE OF OPERATORS:")
                        # Math Operators
                        print("Math Operators: Used for calculations (e.g., + - * /)")

                        # Comparison Operators
                        print("Comparison Operators: Used to check conditions (e.g., == != > <).  Result is True or False.")

                        # Logical Operators
                        print("Logical Operators: Used to combine or reverse conditions (e.g., and, or, not)")

                        # Assignment Operators
                        print("Assignment Operators: Used to store and update values in variables (e.g., = += -=)")

                    elif newsub_choice == 'c':
                        print("\nAPPLICATION OF OPERATORS:")

                        print("\n\t1. Data Manipulation:")
                        print("\t   - Arithmetic operators (+, -, *, /) are used for performing calculations on numerical data.")

                        print("\n\t2. Decision Making:")
                        print("\t   - Comparison operators (==, !=, >, <) are used to make decisions based on data comparisons.")
                        
                        print("\n\t3. Conditional Logic:")
                        print("\t   - Logical operators (and, or, not) are used to combine or negate conditions.")

                        print("\n\t4. Variable Assignment:")
                        print("\t   - Assignment operators (=, +=, -=) are used to assign values to variables and update them.")

                        print("\n\t5. Looping and Iteration:")
                        print("\t   - Operators are used to control the flow of loops and iterate through data structures.")
                    
                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '3':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\n\t# Error: ###############################")
                print("\t#                                      #")
                print("\t#      Invalid Option Selected!!!      #")
                print("\t#                                      #")
                print("\t########################################")
                print("\nPlease select only from the options.")
                
                continue

    elif choice == "Y":
        # Your code for Conditional Statements goes here
        print("\nPlease wait...")
        time.sleep(2)
        
        while True:
            print(f"\n\nHi, {name}! Welcome to Conditional Statements.")
            
            print("\n\tConditional statements are a fundamental part of \n\tprogramming that allow you to control the flow of \n\texecution based on certain conditions. ")
            
            print("\n\t=======================================================")
            print("\t\t  * CONDITIONAL STATEMENTS MENU * ")
            print("\t=======================================================")
            print("\n\t1. Conditional Statements Characteristics")
            print("\t2. Conditional Statements Implementation and Use Cases")
            print("\t3. Back to Main Menu")
            print("\t=======================================================")

            sub_choice = input("\nEnter your choice: ")
            
            if sub_choice == '1':
                while True:
                    print("\nSelect again for its characteristics.")

                    print("\n\n\t┌" + "─────────────────────────────────────────────────" + "┐")
                    print("\t│   CONDITIONAL STATEMENTS CHARACTERISTICS MENU   │")
                    print("\t└" + "─────────────────────────────────────────────────" + "┘")

                    print("\t┌" + "─────────────────────────────────────────────────" + "┐")
                    print("\t│  a.  Conditional Statements Definitions.        │")
                    print("\t│  b.  Purpose of Conditional Statements.         │")
                    print("\t│  c.  Return to Sub Menu                         │")
                    print("\t└" + "─────────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nDEFINITION OF CONDITIONAL STATEMENTS:")
                        print("\n\tConditional statements are programming constructs that \n\tallow you to execute different blocks of code based on \n\twhether a specific condition is true or false. They enable \n\tprograms to make decisions and respond dynamically to \n\tdifferent inputs or situations.")
                            
                    elif newsub_choice == 'b':
                        print("\nPURPOSE OF CONDITIONAL STATEMENTS:")
                        print("\n\tConditional statements control the flow of execution \n\tin a program, enabling different actions based on varying \n\tconditions. This allows programs to handle different \n\tscenarios and provide tailored responses.")

                    elif newsub_choice == 'c':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break

                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '2':
                while True:
                    print("\nSelect again for its implementation and use cases.")

                    print("\n\n\t┌" + "────────────────────────────────────────────────────────────" + "┐")
                    print("\t│   CONDITIONAL STATEMENTS IMPLEMENTATION & USE CASES MENU   │")
                    print("\t└" + "────────────────────────────────────────────────────────────" + "┘")

                    print("\t┌" + "────────────────────────────────────────────────────────────" + "┐")
                    print("\t│  a.  Conditional Statements Example.                       │")
                    print("\t│  b.  Usage of Conditonal Statements.                       │")
                    print("\t│  c.  Application of Conditional Statements.                │")
                    print("\t│  d.  Return to Sub Menu                                    │")
                    print("\t└" + "────────────────────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nEXAMPLE OF CONDITIONAL STATEMENTS:")
                        print("\nINPUT:")
                        print("\t+------------------------------------------------+")
                        print("\t|       * CONDITIONAL STATEMENTS EXAMPLE *       |")
                        print("\t+------------------------------------------------+")
                        print("\t| grade = eval(input(\"What is your grade? \"))    |")
                        print("\t|                                                |")
                        print("\t| if grade >= 95 and grade <= 100:               |")
                        print("\t|     print(\"You got an A+\")                     |")
                        print("\t| elif grade >= 90 and grade <= 94:              |")
                        print("\t|     print(\"You got an A\")                      |")
                        print("\t| elif grade >= 85 and grade <= 89:              |")
                        print("\t|     print(\"You got a B\")                       |")
                        print("\t| elif grade >= 75 and grade <= 84:              |")
                        print("\t|     print(\"You got a C\")                       |")
                        print("\t| else:                                          |")
                        print("\t|     print(\"You did not pass\")                  |")
                        print("\t+------------------------------------------------+")


                        print("\nOUTPUT:")
                        grade= eval(input("\n\tWhat is your grade? "))

                        if grade >=95 and grade <= 100:
                            print("\n\tYou got an A+")
                        elif grade >=90 and grade <=94:
                            print("\n\tYou got an A")
                        elif grade >=85 and grade <=89:
                            print("\n\tYou got a B")
                        elif grade >=75 and grade <=84:
                            print("\n\tYou got a C")
                        else:
                            print("\n\tYou did not pass")
                    
                    elif newsub_choice == 'b':
                        print("\nUSAGE OF CONDITIONAL STATEMENTS:")
                        print("\n\tThe if statement starts a conditional block, followed by a \n\tcondition and a colon (:). For example, if x > 0: checks \n\tif the variable x is greater than 0, and if it is, \n\tthe indented code block under the if statement is executed.")
                        
                        #print("\n\tExample with if: \n\tx = 10 \n\tif x > 0: \n\t\tprint("x is positive")  #This line will be executed")

                        print("\n\tThe elif statement allows you to check multiple conditions in \n\tsequence. If the initial if condition is false, the elif \n\tcondition is evaluated. You can have multiple elif statements.")

                        #print("\n\tExample with elif: \n\tx = -5 \n\tif x > 0: \n\t\tprint("x is positive") \n\telif x < 0: \n\t\tprint("x is negative")  # This line will be executed")
                        
                        print("\n\tThe else statement provides a default block of code to \n\texecute when none of the preceding if or elif conditions \n\tare true. It is always the last statement in a \n\tconditional block.")
                        
                        #print("\n\tExample with else: x = 0 \n\tif x > 0: \n\t\tprint("x is positive") \n\telif x < 0: \n\t\tprint("x is negative") \n\telse: \n\t\tprint("x is zero")  # This line will be executed")

                    elif newsub_choice == 'c':
                        print("\nAPPLICATION OF CONDITIONAL STATEMENTS:")
                        print("\n\tConditional statements are fundamental in various \n\tapplications, including decision-making processes, \n\tinput validation, error handling, and creating dynamic \n\tuser interfaces. They allow programs to adapt their behavior \n\tbased on specific conditions or inputs.")

                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '3':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\n\t# Error: ###############################")
                print("\t#                                      #")
                print("\t#      Invalid Option Selected!!!      #")
                print("\t#                                      #")
                print("\t########################################")
                print("\nPlease select only from the options.")
                continue
        
    elif choice == "S":
       print("\nPlease Wait....")
       time.sleep(2)
       while True:
            print(f"\n\nHi, {name}! Welcome to the Loops.")
            
            print("\n\tLoops are fundamental control flow structures in Python \n\tthat allow you to execute a block of code repeatedly. \n\tThey are essential for automating repetitive tasks and \n\titerating over collections of data.")
            
            print("\n\t=====================================")
            print("\t             * LOOP MENU * ")
            print("\t=====================================")
            print("\n\t1. Loop Characteristics")
            print("\t2. Loop Implementation and Use Cases")
            print("\t3. Back to Main Menu")
            print("\t=====================================")

            sub_choice = input("\nEnter your choice: ")
            if sub_choice == '1':
                while True:
                    print("\nSelect again for its characteristics.")

                    print("\n\n\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│     LOOP CHARACTERISTICS MENU          │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    print("\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│  a.  Loop Definition.                  │")
                    print("\t│  b.  Purpose of Loop.                  │")
                    print("\t│  c.  Loop Types.                       │")
                    print("\t│  d.  Return to Sub Menu                │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nDEFINITION OF LOOP:")
                        print("\n\tA loop is a programming structure that allows you to \n\trepeat a set of instructions until a certain condition \n\tis met.")
                    
                    elif newsub_choice == 'b':
                        print("\nPURPOSE OF LOOP:")
                        print("\n\tThe purpose of loop is to execute a block of \n\tcode repeatedly for a specified number of times or \n\tuntil a certain condition is met.")

                    elif newsub_choice == 'c':
                        print("\nTYPES OF LOOP:")
                        print("\n\tFor loop – used to iterate over a sequence \n\t(list, tuple, string, range)")
                        print("\tWhile loop – repeats as long as a condition \n\tis true")
                        print("\tNested loop – a loop inside another loop \n\t(for–for, while–while, or mixed)")

                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")
                    continue

            elif sub_choice == '2':
                while True:
                    print("\nSelect again for its implementation and use cases.")

                    print("\n\n\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│     LOOP IMPLEMENTATION & USE CASES MENU      │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    print("\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│  a.  Loop Example.                            │")
                    print("\t│  b.  Usage of Loop.                           │")
                    print("\t│  c.  Application of Loop.                     │")
                    print("\t│  d.  Return to Sub Menu                       │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nEXAMPLE OF LOOP:")
                        
                        print("\nINPUT:")
                        print("\t+------------------------------------------------------+")
                        print("\t|               * MULTIPLICATION TABLE *               |")
                        print("\t+------------------------------------------------------+")
                        print("\t| columns = eval(input(\"Enter number of columns: \"))   |")
                        print("\t|                                                      |")
                        print("\t| for x in range(1, 11):                               |")
                        print("\t|     for y in range(1, columns+1):                    |")
                        print("\t|         print(f\"{x}x{y}={x*y}\", end=\"\\t\\t\")          |")
                        print("\t|     print()                                          |")
                        print("\t+------------------------------------------------------+")


                        print("\nOUTPUT:")
                        columns= eval(input("\nEnter number of columns: "))

                        for x in range(1, 11, 1):
                            for y in range(1, columns+1, 1):
                                print(f"{x}x{y}={x*y}", end="\t\t")
                            print()
                    
                    elif newsub_choice == 'b':
                        print("\nUSAGE OF LOOP:")
                        print("\n\tUse loops when you need to perform a task repeatedly, \n\tsuch iterating over a list or performing a calculation \n\tmultiple times.")

                    elif newsub_choice == 'c':
                        print("\nAPPLICATION OF LOOP:")
                        print("\n\tLoops are commonly used in data processing, \n\tgame development, and simulations.")

                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '3':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\n\t# Error: ###############################")
                print("\t#                                      #")
                print("\t#      Invalid Option Selected!!!      #")
                print("\t#                                      #")
                print("\t########################################")
                print("\nPlease select only from the options.")
                continue

    elif choice == "L":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print(f"\n\nHi! {name}, Welcome to the List.")
            
            print("\n\tLists are one of the most versatile and fundamental data \n\tstructures in Python. They allow you to store and manipulate \n\tan ordered collection of items, which can be of different \n\tdata types. ")
            
            print("\n\t======================================")
            print("\t\t     * LIST MENU * ")
            ("\t======================================")
            print("\t======================================")
            print("\n\t1. List Characteristics")
            print("\t2. List Implementation and Use Cases")
            print("\t3. Back to Main Menu")
            print("\t======================================")

            sub_choice = input("\nEnter your choice: ")
            if sub_choice == '1':
                while True:
                    print("\nSelect again for its characteristics.")

                    print("\n\n\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│       LIST CHARACTERISTICS MENU        │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    print("\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│  a.  List Definition.                  │")
                    print("\t│  b.  Purpose of List.                  │")
                    print("\t│  c.  Return to Sub Menu                │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")
                    if newsub_choice == 'a':
                        print("\nDEFINITION OF LIST:")
                        print("\n\tA list in Python is an ordered, mutable (changeable) \n\tcollection of items, where each item is separated \n\tby commas and enclosed in square brackets []. Lists \n\tcan contain elements of different data types, such \n\tas numbers, strings, and even other lists.")
                    
                    elif newsub_choice == 'b':
                        print("\nPURPOSE OF THE LIST:")
                        print("\n\tLists are used to store and manage collections of data \n\tin a structured manner. They allow you to perform various \n\toperations, such as adding, removing, accessing, and \n\tmodifying elements, making them essential for organizing \n\tand manipulating data.")

                    elif newsub_choice == 'c':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")
                    continue

            elif sub_choice == '2':
                while True:
                    print("\nSelect again for its implementation and use cases.")

                    print("\n\n\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│     LIST IMPLEMENTATION & USE CASES MENU      │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    print("\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│  a.  List Example.                            │")
                    print("\t│  b.  Usage of List.                           │")
                    print("\t│  c.  Application of List.                     │")
                    print("\t│  d.  Return to Sub Menu                       │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nEXAMPLE OF LIST:")
                        print("\nINPUT: ")
                        print("\t+--------------------------------------------------------------+")
                        print("\t|                      * ANIME LISTER *                        |")
                        print("\t+--------------------------------------------------------------+")
                        print("\t| print(\"OUTPUT:\")                                             |")
                        print("\t| Legit = True                                                 |")
                        print("\t| list = []                                                    |")
                        print("\t| name = input(\"What is your name? \")                          |")
                        print("\t| print(f\"Hi {name}, Welcome to Anime Lister\")                 |")
                        print("\t|                                                              |")
                        print("\t| while Legit == True:                                         |")
                        print("\t|     anime = input(\"Enter anime title (or 'exit'): \").lower() |")
                        print("\t|                                                              |")
                        print("\t|     if anime != 'exit':                                      |")
                        print("\t|         print(f\"'{anime}' added to your list.\")              |")
                        print("\t|         list.append(anime)                                   |")
                        print("\t|         continue                                             |")
                        print("\t|                                                              |")
                        print("\t|     elif anime == 'exit':                                    |")
                        print("\t|         print(\"You have exited the program.\")                |")
                        print("\t|         break                                                |")
                        print("\t|                                                              |")
                        print("\t|     else:                                                    |")
                        print("\t|         print(\"Please try again\")                            |")
                        print("\t|                                                              |")
                        print("\t| print(\"Your anime list includes:\")                           |")
                        print("\t| for anime in list:                                           |")
                        print("\t|     print(f\"- {anime}\")                                      |")
                        print("\t+--------------------------------------------------------------+")

                        print("\nOUTPUT: ")
                        Legit = True
                        list = [ ]
                        name = input("\n\tWhat is your name? ")
                        print(f"\ttHi {name}, Welcome to Anime Lister")

                        while Legit == True:
                            anime = input("\n\tEnter the title of an anime (or type 'exit' to finish): ").lower()
                        
                            if anime != 'exit':
                                print(f"\n\t'{anime}' has been added to your anime list.")
                                list.append(anime)
                                continue

                            elif anime == 'exit':
                                print("\n\tYou have exited the anime enrty program.")
                                break

                            else:
                                print("\tPlease try again")

                        print("\n\tYour anime list includes:")
                        for anime in list:
                            print(f"\t- {anime}")
                    
                    elif newsub_choice == 'b':
                        print("\nUSAGE OF LIST:")
                        
                        print("\n\tTo create a list, you enclose a comma-separated sequence \n\tof items within square brackets. ")
                        
                        print("\n\tYou can access elements in a list using their index, \n\tstarting from 0 for the first element.")
                        
                        print("\n\tBecause lists are mutable, you can change their elements. ")
                        
                        print("\n\tYou can add elements to a list using methods like \n\tappend(), insert(), and extend().")
                        
                        print("\n\tYou can remove elements using methods like remove(), pop(), \n\tand clear().")

                    elif newsub_choice == 'c':
                        print("\nAPPLICATION OF LIST:")
                        print("\n\tLists are used extensively in various applications, \n\tincluding data storage and manipulation, data analysis, \n\talgorithm implementation, and creating dynamic content. \n\tThey are essential for organizing and processing \n\tcollections of data efficiently.")

                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '3':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\n\t# Error: ###############################")
                print("\t#                                      #")
                print("\t#      Invalid Option Selected!!!      #")
                print("\t#                                      #")
                print("\t########################################")
                print("\nPlease select only from the options.")
                
                continue
        

    elif choice == "E":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print(f"\n\nHi! {name}, Welcome to Functions.")
            
            print("\n\tFunctions are a cornerstone of structured programming \n\tin Python. They allow you to encapsulate blocks of code \n\tinto reusable units, promoting modularity, readability, \n\tand maintainability.")
            
            print("\n\t==================================================")
            print("\t\t\t* FUNCTIONS MENU * ")
            print("\t==================================================")
            print("\n\t1. Function Characteristics")
            print("\t2. Function Implementation and Use Cases")
            print("\t3. Back to Main Menu")
            print("\t==================================================")

            sub_choice = input("\nEnter your choice: ")
            
            if sub_choice == '1':
                
                while True:
                    print("\nSelect again for its characteristics.")

                    print("\n\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│     FUNCTION CHARACTERISTICS MENU      │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    print("\t┌" + "────────────────────────────────────────" + "┐")
                    print("\t│  a.  Function Definition.              │")
                    print("\t│  b.  Purpose of Function.              │")
                    print("\t│  c.  Return to Sub Menu                │")
                    print("\t└" + "────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nDEFINITION OF FUNCTION:")
                        print("\n\tA function in Python is a named block of code \n\tthat performs a specific task. It can accept inputs \n\t(arguments), process them, and return a result.")
                        print("\n\tFunctions are defined using the def keyword, followed \n\tby the function name, parentheses containing optional \n\tparameters, and a colon.")
                    
                    elif newsub_choice == 'b':
                        print("\nPURPOSE OF FUNCTIONS:")
                        print("\n\tThe primary purpose of functions is to organize code, \n\tpromote reusability, and simplify complex tasks. They \n\tallow you to avoid code duplication, improve code \n\treadability, and make your programs more modular and \n\tmaintainable.")

                    elif newsub_choice == 'c':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")
                    
                    continue

            elif sub_choice == '2':
                while True:
                    print("\nSelect again for its implementation and use cases.")
                    print("\n\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│   FUNCTION IMPLEMENTATION & USE CASES MENU    │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    print("\t┌" + "───────────────────────────────────────────────" + "┐")
                    print("\t│  a.  Function Example.                        │")
                    print("\t│  b.  Usage of Function.                       │")
                    print("\t│  c.  Application of Function.                 │")
                    print("\t│  d.  Return to Sub Menu                       │")
                    print("\t└" + "───────────────────────────────────────────────" + "┘")

                    newsub_choice = input("\nEnter your choice: ")

                    if newsub_choice == 'a':
                        print("\nEXAMPLE OF FUNCTION:")
                        print("\nINPUT: ")
                        print("\t+------------------------------------------------------+")
                        print("\t|                 * FUNCTION EXAMPLE *                 |")
                        print("\t+------------------------------------------------------+")
                        print("\t| def student_info():                                  |")
                        print("\t|     name = input(\"Enter your name: \")                |")
                        print("\t|     age = int(input(\"Enter your age: \"))             |")
                        print("\t|     course = input(\"Enter your course: \")            |")
                        print("\t|                                                      |")
                        print("\t|     print(\"\\n--- STUDENT INFORMATION ---\")           |")
                        print("\t|     print(f\"Name: {name}\")                           |")
                        print("\t|     print(f\"Age: {age}\")                             |")
                        print("\t|     print(f\"Course: {course}\")                       |")
                        print("\t|                                                      |")
                        print("\t| student_info()                                       |")
                        print("\t+------------------------------------------------------+")
    
                        print("\nOUTPUT:")
                        def student_info():
                            name = input("\tEnter your name: ").title()
                            age = int(input("\tEnter your age: "))
                            course = input("\tEnter your course: ")

                            print("\n\t--- STUDENT INFORMATION ---")
                            print(f"\tName: {name}")
                            print(f"\tAge: {age}")
                            print(f"\tCourse: {course}")

                        student_info()
                    
                    elif newsub_choice == 'b':
                        print("\nUSAGE OF PRINT STATEMENTS:")
                        print("\n\tTo define a function, use the def keyword, followed \n\tby the function name, parentheses (), and a colon :. \n\tThe function body is indented below the def line.")

                    elif newsub_choice == 'c':
                        print("\nAPPLICATION OF PRINT STATEMENTS:")
                        print("\n\tFunctions are used in various applications to modularize \n\tcode, increase reusability, and simplify complex tasks. \n\tThey are fundamental to writing well-structured and \n\tmaintainable programs.")

                    elif newsub_choice == 'd':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("\n\t# Error: ###############################")
                        print("\t#                                      #")
                        print("\t#      Invalid Option Selected!!!      #")
                        print("\t#                                      #")
                        print("\t########################################")
                        print("\nPlease select only from the options.")

            elif sub_choice == '3':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                
                break

            else:
                print("\n\t# Error: ###############################")
                print("\t#                                      #")
                print("\t#      Invalid Option Selected!!!      #")
                print("\t#                                      #")
                print("\t########################################")
                print("\nPlease select only from the options.")
                
                continue

    elif choice == "X":
        print("\nExiting the program. . .")
        time.sleep(2)
        print("\n\t# SYSTEM'S OUT: ####################################")
        print("\t#                                                  #")
        print("\t# Thank you, for using Chrysler's code compiler..  #")
        print("\t# \t\tHave a lovely day!                 #")
        print("\t#                                                  #")
        print("\t####################################################")
        
        break # Kapag napindot ito, katapusan na - ng program.
    
    else:
        print("\n\t# Error: ###############################")
        print("\t#                                      #")
        print("\t#      Invalid Option Selected!!!      #")
        print("\t#                                      #")
        print("\t########################################")
        print("\nPlease select only from the options.")
        
        continue # Babalik po ulit ito sa main menu (sana lahat, nabalik!)