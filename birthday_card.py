from datetime import datetime


def create_birthday_card():
    recipient_name = input("Enter the recipient's name: ")
    year_of_birth = int(input("Enter the year of birth: "))
    personalized_message = input("Enter a short personalized message: ")
    sender_name = input("Enter your name (the sender's name): ")

    current_year = datetime.now().year
    age = current_year - year_of_birth

    birthday_card = f"""
    Happy Birthday, {recipient_name}!

    Let's celebrate your {age} years of awesomeness!
    Wishing you a day filled with joy and laughter as you turn {age}!

    {personalized_message}

    With love and best wishes,
    {sender_name}
    """
    print(birthday_card)


create_birthday_card()
