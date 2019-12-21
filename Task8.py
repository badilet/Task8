def choice_to_number(choice):
#"""Convert choice to number."""
# If choice is Usain you should get back 1.
    if choice == "Usain":
        return 1
    elif choice == "Me":
        return 2
    else:
        return 3

def number_to_choice(number):
#"""Convert number to choice."""
# if number is 1 then return usain bolt.
    if number == 1:
        return 'Usain'
    elif number == 2:
        return 'Me'
    else:
        return 'Aybek'


#DO NOT remove lines below here, this is designed to test your code.
def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Aybek') == 3
def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Aybek'
def test_all():
    try:

        test_choice_to_number()
        test_number_to_choice()
    except AssertionError:
        print("WRONG")
    else:
        print("SUCCESS")
#test your code by un-commenting the line(s) below
test_all()