import sys

Covid_data = {
    0: ['Australia', 7155],
    1: ['Morocco', 13030],
    2: ['Tunisia', 19746],
    3: ['Egypt', 1777],
    4: ['Ethiopia', 161974],
    5: ['Nigeria', 156960],
    6: ['Libya', 136587],
    7: ['Algeria', 113593],
    8: ['Kenya', 107329],
    9: ['Ghana', 84750],
    'SA': 27403,
    'USA': 1700000,
    'China': 82995
}


def main():
    menu()


def menu():
    choice = input("""
    Welcome to the COVID 19 support service. Please select an option below:\n
    1: Statistics
    2: Prevention
    3: Symptoms
    4: Treatment
    5: Report case
    6: Exit
    Enter choice(1/2/3/4/5/6): """)


    if choice == '1':
        Statistics()
    elif choice == '2':
        Prevention()
    elif choice == '3':
        Symptoms()
    elif choice == '4':
        Treatment()
    elif choice == '5':
        Report_case()
    elif choice == '6':
        sys.exit
    else:
        print("Invalid selection, you must choose a number between 0 and 6")
        print("\nPlease try again.")
        menu()

def Statistics():
        print("Currently in SA there are", Covid_data['SA'], "Confirmed cases")
        print("Currently in USA there are", Covid_data['USA'],
              "Confirmed cases")
        print("Currently in China there are", Covid_data['China'],
              "Confirmed cases")
        print()

        option = input(
            "Would you like to see the confirmed cases for a random country? y/n: \n"
        )

        if option == 'y' or option == 'Y':
            other = int(
            input("To select a random country, type a number from 0 to 9\n"))
        while other < 0 or other > 9:
            print("\ninvalid selection please try again:")

            other = int(
            input("To select a random country, type a number from 0 to 9\n"))
        if int(other) in Covid_data:
            print(Covid_data[other][0], 'has', Covid_data[other][1],
                  'confirmed cases')
        elif option == 'n' or option == 'N':
            sys.exit

def Prevention():

        print("""
To prevent the spread of COVID-19:\n
Clean your hands often. Use soap and water, or an alcohol-based hand rub.
Maintain a safe distance from anyone who is coughing or sneezing.
Dont touch your mouth.
Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
Stay home if you feel unwell.
If you have a fever, cough and difficulty breathing, seek medical attention. Call in advance.
Follow the directions of your local health authority.""")

def Symptoms():

        print("""
Most common symptons:
fever
Dry cough
tiredness
\nLess common symptoms:
aches and pains
sore throat
diarrhoea
conjunctivitis
headache
loss of taste or smell
a rash on skin, or discolouration of fingers or toes
\nSerious symptoms:
difficulty breathing or shortness of breath
chest pain or pressure
loss of speech or movement""")

def Treatment():
        print("""
If you are feeling sick you should rest, drink plenty of fluids, and eat nutritious food.
Stay in a separate room from other family members, and use a dedicated bathroom if possible.
clean and disinfect frequently touched surfaces""")

def Report_case():
        select = input("Do you have any of the symptoms? y/n: ")
        if select == 'n' or select == 'N':
            print("\nYou do not have COVID19")
        elif select == 'y' or select == 'Y':
            degree_sign = u'\N{DEGREE SIGN}'

        b = input('Is your temperature above 38.5{}'.format(degree_sign) +
                  'C? y/n: ')
        if b == 'n' or b == 'N':
            print("\nYou do not have COVID19")
        elif b == 'y' or b == 'Y':
            Country = input("""
 In which country are you? Select an option below:
 1: SA
2: USA
3: China
 """)

        if Country == '1':
            print('You have COVID 19 please see treatment\n')
            Covid_data['SA'] += 1
        elif Country == '2':
            print('You have COVID 19 please see treatment\n')
            Covid_data['USA'] += 1
        elif Country == '3':
            print('You have COVID 19 please see treatment\n')
            Covid_data['China'] += 1
        Statistics()  # merely called to show that the cases for the selected country has increased.


def exit():
    sys.exit


main()