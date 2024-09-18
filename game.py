import random
from datetime import date

# Function to calculate number of days lived based on age
def calculate_days_lived(age):
    current_year = date.today().year
    birth_year = current_year - age
    today = date.today()
    birth_date = date(birth_year, today.month, today.day)
    
    # Calculate days lived from birth date to today
    days_lived = (today - birth_date).days
    return days_lived

# Function to calculate leap years passed
def calculate_leap_years(age):
    current_year = date.today().year
    birth_year = current_year - age
    leap_years = [year for year in range(birth_year, current_year + 1) if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))]
    return len(leap_years)

# Function to calculate Sundays passed
def calculate_sundays(days_lived):
    # There is 1 Sunday in every 7 days
    return days_lived // 7

# Function to generate random answers
def generate_random_answers(correct_answer):
    # Create random answers based on the correct one
    random_answers = [correct_answer + random.randint(-5, 5) for _ in range(3)]
    random_answers.append(correct_answer)  # Add the correct answer
    random.shuffle(random_answers)  # Shuffle answers to randomize their order
    return random_answers

# Function to ask a question and check if the user's answer is correct
def ask_question(question, correct_answer):
    # Generate random answers (including the correct one)
    options = generate_random_answers(correct_answer)

    # Display the question and options
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user's answer
    user_choice = int(input("\nChoose the correct answer (1-4): "))
    if options[user_choice - 1] == correct_answer:
        print("Correct!\n")
    else:
        print(f"Wrong. The correct answer was {correct_answer}.\n")

# Function to get user input and generate trivia questions
def trivia_game():
    age = int(input("Enter your age: "))

    # Calculate the number of days lived
    days_lived = calculate_days_lived(age)
    print(f"\nYou have lived approximately {days_lived} days on Earth.")

    # Calculate leap years and Sundays passed
    leap_years = calculate_leap_years(age)
    sundays = calculate_sundays(days_lived)
    hours_lived = days_lived * 24
    minutes_lived = hours_lived * 60
    seconds_lived = minutes_lived * 60

    # Ask questions
    ask_question("How many leap years have you passed?", leap_years)
    ask_question("How many Sundays have you passed?", sundays)
    ask_question("How many hours have you lived?", hours_lived)
    ask_question("How many minutes have you lived?", minutes_lived)
    ask_question("How many seconds have you lived?", seconds_lived)

# Run the trivia game
trivia_game()
