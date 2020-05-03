#Compute and display information relating to moving truck rental.
#For a specified customer,the program will compute and display the
#amount of money charged the customer’s truck rental.
#there are 3 truck classifications: A, B and C
#price is based off of Base Charge Daily, Mileage Charge (Daily
#Rentals), Base Charge Weekly and Mileage Charge (Weekly Rentals).

#Base Charges Daily: A=19.95, B=29.95, C=39.95
#Base Charges Weekly: A=125.68 (13.97 savings), B=188.68 (20.97
#savings) & C= 251.68 (27.68 savings)

#Mileage Charge (Daily): A=0.59/mile, B=0.79/mile &
#C=0.85/mile
#Mileage Charge (Weekly): A= 0.59/mile, B=0.79/mile &
#C=0.85/mile. These are the prices per mile after the first
#200 miles per week, resets weekly.

#given examples:
#User wants a Class B truck for 2 days and will drive 130 miles.
#The cost is $162.60 (daily rate $29.95 for
#2 days = 59.90 + 130 miles * .79 = 102.70)
#User wants a Class C truck for 1 week and will drive 210 miles.
#The cost is $260.18 (weekly rate $251.68 for
#1 week + (210-200) miles * .85 = 8.50)**
#** note: Weekly rentals include mileage. Our example takes total
#mileage – 200 (allowance) to determine 10 additional miles.
#Refunds are not given for unused miles.

#Your application will calculate the rental rate for a customer
#and display it to screen. From a menu, the user will select
#truck classification. After truck classification has been selected,
#display a menu with the rental options of daily or weekly.
#The program then needs to gather how many days or weeks
#the user wants to rent the truck and then how many miles will be driven.

#Your program must include the following concepts:
#Functions - you must begin your program with main().
#Lists – consider the Classification, Base Charge Daily, Daily Mileage
#Charge, Base Charge Weekly, Mileage Charge Weekly, Allowed Mileage Weekly
#as parallel lists or a two-dimensional list.
#Variables – data input/output to the user will most likely
#be stored in variables.
#Loops – after the completion of computing a customer’s total,
#loop to the beginning of the program making it ready for the next customer.
#Conditions – you will use if/else statements to compare values.
#Menu – your application needs to have a menu of choices (rent truck, exit)
#with professional formatting.
#Exception handling – input errors should be handled.

def main():

    def menu():
 
        print("Hello, welcome to Stanson's Truck Rental,")
        print("the top supplier of rental trucks for 50 years and counting!")

        #determine whether the user wants  to use the program or not
        print('Do you plan on renting from us today?')
        answer_1 = input("Enter 'Y' to begin the truck rental process, press 'N' if you want to exit: ")

        if answer_1 == 'Y':
            print("Great, let's begin!")

        elif answer_1 != 'Y' or 'N':
            print('Invalid!')
            answer_1a = input("Enter 'Y' or 'N': ")
            if answer_1a != 'Y' or 'N':
                print('You have failed to enter a valid answer. Goodbye!')
                exit()
        

        elif answer_1 == 'N':
            answer_2 = input("Are you sure that you'd like to exit? Y/N: ")
            if answer_2 == 'Y':
                print('Goodbye!')
                exit()
            elif answer_2 == 'N':
                print("Great, let's begin!")


        print('At our company we offer 3 different classes of trucks: Class A, Class B, and Class C.')
        print('Class A is the cheapest option available while Class C is the most expensive.')
        print('Payment prices vary depending on if you are planning on renting daily or weekly.')
        print('Daily prices apply to a truck rental with a duration of 6 days or less.')
        print('Weekly prices apply to a truck rental with a duration of 7 days or more.')
        print('Weekly rentals have a slight price decrease, decrease varies on truck class.')
        print('Daily rentals have a constant price per mile and the prices vary within the classes.')
        print('Weekly rentals have the same rate, except that the first 200 miles driven per')
        print('week are free. There are no refunds for unused miles.')

        answer_3 = input('Are you still interested in renting from us? Y/N: ')

        if answer_3 == 'Y':
            print("Alright! Let's continue!")

        elif answer_3 != 'Y' or 'N':
            print('Invalid!')
            answer_3a = input("Enter 'Y' or 'N': ")
            if answer_3a != 'Y' or 'N':
                print('You have failed to enter a valid answer. Goodbye!')
                exit()

        elif answer_3 == 'N':
            answer_4 = input("Are you sure that you'd like to exit? Y/N: ")
            if answer_4 == 'Y':
                print('Goodbye!')
                exit()
            elif answer_4 == 'N':
                print("Alright! Let's continue!")

    menu()
    
    def lets_continue(): 
       
        print('As mentioned earlier, prices vary between classes.')
        print('Class A is $19.95 for daily rentals, $125.68 for weekly.')
        print('Class B is $29.95 for daily rentals, $188.68 for weekly.')
        print('Class C is $39.95 for daily rentals, $251.68 for weekly.')
        print('Class A costs $0.59/mile, Class B costs $0.79/mile &')
        print('Class C costs $0.85/mile.')
        print('The first 200 miles driven at the beginning of each week are free.')

        answer_5 = input('Are you ready to continue? Y/N : ')
        if answer_5 == 'Y':
            print("Alright! Let's continue!")

        elif answer_5 != 'Y' or 'N':
            print('Invalid!')
            answer_5a = input("Enter 'Y' or 'N': ")
            if answer_5a != 'Y' or 'N':
                print('You have failed to enter a valid answer. Goodbye!')
                exit()

        elif answer_5 == 'N':
            answer_6 = input("Would you like to exit? Y/N: ")
            if answer_6 == 'Y':
                print('Goodbye!')
                exit()
            elif answer_6 == 'N':
                print("Alright! Let's continue!")
        
    lets_continue()

    def lets_continue_2():
            
        print('Which classification would you like to rent from?')
        g = input('Enter classification . A/B/C: ')
    
        miles = float(input('Enter estimated distance (in miles): '))
    
        day_answer = input('Will you be travelling for less than one week? Y/N: ')
        if day_answer == 'Y':
            days = int(input('How many days?: '))

            groups = ['A', 'B', 'C'] 
            charge_daily = [19.95*days, 29.95*days, 39.95*days]
            mile_charge_daily = [0.59*miles, 0.79*miles, 0.85*miles]

            print('You have decided to pick the truck from class', g,'.')
            print('You said you will travel roughly', miles, 'miles.')
            print('You will be travelling for', days, 'days.')

            if g == 'A':
                    pay_a = mile_charge_daily[0] + charge_daily[0]
                    print('Your projected price will be $', pay_a)
            elif g == 'B':
                    pay_b = mile_charge_daily[1] + charge_daily[1]
                    print('Your projected price will be $', pay_b)
            elif g == 'C':
                    pay_c = mile_charge_daily[2] + charge_daily[2]
                    print('Your projected price will be $', pay_c)

        elif day_answer == 'N':
            weeks = float(input('How many weeks?: '))

            groups = ['A', 'B', 'C'] 
            charge_weekly = [125.68*weeks, 188.68*weeks, 251.68*weeks]
            mile_charge_weekly = [0.59, 0.79, 0.85]
            mile_allowance = [200]

            print('You have decided to pick the truck from class', g,'.')
            print('You said you will travel roughly', miles, 'miles.')
            print('You will be travelling for', weeks, 'weeks.')

            if g == 'A':
                    pay_aa = ((miles - mile_allowance[0]) * (mile_charge_weekly[0])) + charge_weekly[0]
                    print('Your projected price will be $', pay_aa)
            elif g == 'B':
                    pay_bb = ((miles - mile_allowance[0]) * (mile_charge_weekly[1])) + charge_weekly[1]
                    print('Your projected price will be $', pay_bb)
            elif g == 'C':
                    pay_cc = ((miles - mile_allowance[0]) * (mile_charge_weekly[2])) + charge_weekly[2]
                    print('Your projected price will be $', pay_cc)
                
    lets_continue_2()          


    def loop_thru():
        answer = input('Will you please reset for next customer? Y/N: ')
        if answer == 'Y':
            print('Thanks!')
            main()
        elif answer == 'N':
            print('Rude.')
            exit()
    loop_thru()
main()    













   
   

   





