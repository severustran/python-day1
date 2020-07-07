import source

while True:
    print("Enter 1 to run exercise 77")
    print("Enter 2 to run exercise 78")
    print("Enter 3 to run exercise 132")
    print("Enter 0 to exit")
    option = int(input("Your choice: "))
    if option == 0:
        print("Bye!")
        break
    if option == 1:
        source.exercise_77()
        pass
    if option == 2:
        source.exercise_78()
        pass
    if option == 3:
        source.exercise_132()
        pass
    pass

