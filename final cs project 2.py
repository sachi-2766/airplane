import re
from datetime import datetime


def validate_date(date_string):
    try:
        date = datetime.strptime(date_string, '%Y-%m-%d')
        today = datetime.today()

        # Check if the date is not in the past
        if date < today:
            return False

        # Check if the year, month, and day are valid
        year, month, day = date.year, date.month, date.day
        if year < 1 or month < 1 or month > 12 or day < 1:
            return False

        # Check if the day is valid for the given month
        max_day = 31  # Default to maximum days in a month
        if month in {4, 6, 9, 11}:
            max_day = 30
        elif month == 2:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                max_day = 29  # Leap year
            else:
                max_day = 28

        if day > max_day:
            return False

        return True

    except ValueError:
        return False


print("~~~~~~~~*********welcome to domestic airplane ticket booking*********~~~~~~~~~")

while True:
    x=input("Press '1' to sign up (create a new account) or press '2' to sign in (to existing account): ")
    if x not in '12':
        print('Enter either 1 or 2: ')
        continue
    else:
        break

import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",password="root",database="passenger")
cursor=mycon.cursor()

def validate_name(name):
    return all([i.isalpha() or i.isspace() for i in name])
       
if x=="1":
    while True:
        name=input("Enter name: ")
        if not validate_name(name):
            print('enter valid name')
            continue
        break

    while True:
        try:
            age=int(input("Enter age: "))
            if age <= 0:
                print('Enter a positive number!')
                continue
            break
        except Exception:
            print('Enter a number!')
            continue
    
    while True:
        email_id=input("enter email_id: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email_id):
            break
        continue

    
    correct_username=input("Enter username: ")
    correct_password=input("Enter password: ")
    sql1='''insert into login values('{}',{},'{}','{}','{}')'''.format(name,age,email_id,correct_username,correct_password)
    cursor.execute(sql1)
    mycon.commit()
    for i in range (10):
        username=input("Enter a username: ")
        if username==correct_username:
            password=input("Enter a password: ")
            if password==correct_password:
                print("~~~~~~~******You have signed up successfully!*****~~~~~~~")
                break
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        if i==10:
            print("10 incorrect attempts!")
        print("Try again")
        continue
        
elif x=="2":
    while True:
        user_name=input("Enter a username: ")  
        
        sql2="select username,password from login where username='%s'"%(user_name)
        cursor.execute(sql2)
        data=cursor.fetchall()

        if not data:
            print("Invalid username!")
            continue
        else:
            break

    password = data[0][1]
    
    
    while True:
        pwd=input("Enter a password: ")
        if pwd==password:
            print("~~~~~~~******You have signed in successfully!*****~~~~~~~")
            break
            
        else:
            print("Invalid password")
            continue
        
book=input('Enter "y" to book tickets or any other key to exit: ')
if book=='y':
    import random
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="root")
    cursor=mycon.cursor()
    cursor.execute("create database if not exists passenger")
    cursor.execute("use passenger")
    print('1.Air India')
    print('2.Indigo')
    print('3.Go Air')
    print('4.Spice Jet')
    print('5.Vistara')
    flight_dict={
        1:'Air India',
        2:'Indigo',
        3:'Go Air',
        4:'Spice Jet',
        5:'Vistara'
    }
    while True:
        try:
            flight=int(input('Select your boarding and landing destination from the above options: '))
            if 1 <= flight <= 5:
                break
            continue
        except Exception:
            print('Input a number from 1 to 5!')
            continue
    print('1.Mumbai to Kolkata(rs.5000)')
    print('2.Mumbai to Delhi(rs.5000)')
    print('3.Mumbai to Chennai(rs.5000)')
    print('4.Kolkata to Mumbai(rs.5000)')
    print('5.Kolkata to Delhi(rs.5000)')
    print('6.Kolkata to Chennai(rs.5000)')
    print('7.Delhi to Mumbai(rs.5000)')
    print('8.Delhi to kolkata(rs.5000)')
    print('9.Delhi to Chennai(rs.5000)')
    print('10.Chennai to Mumbai(rs.5000)')
    print('11.Chennai to Kolkata(rs.5000)')
    print('12.Chennai to Delhi(rs.5000)')

    destination_dict = {
        1: "Mumbai to Kolkata",
        2: "Mumbai to Delhi",
        3: "Mumbai to Chennai",
        4: "Kolkata to Mumbai",
        5: "Kolkata to Delhi",
        6: "Kolkata to Chennai",
        7: "Delhi to Mumbai",
        8: "Delhi to kolkata",
        9: "Delhi to Chennai",
        10: "Chennai to Mumbai",
        11: "Chennai to Kolkata",
        12: "Chennai to Delhi"    
    }
    while True:
        try:
            destination=int(input('select your boarding and landing destination from the above options'))
            if 1 <= destination <= 12:
                break
            continue
        except Exception:
            print('Input a number from 1 to 12!')
            continue
    
    
    time_dict = {
        1: '1. 09.00 am to 11.00 am ',
        2: '2. 12.30 pm to 02.30 am ',
        3: '3. 03.00 pm to 05.00 pm ',
        4: '4. 05.30 pm to 07.30 pm ',
        5: '5. 08.00 pm to 10.00 pm ',
        6: '6. 10.30 pm to 12.30 am '
    }
    while True:
        user_date = input('Enter Date (FORMAT: YYYY-MM-DD): ').strip()
        if not user_date: break
        ymd = user_date.split('-')
        valid = validate_date(user_date)
        if not valid:
            print("Invalid date!")
            continue
        else:
            break

    while True:
        print('1. 09.00 am to 11.00 am ')
        print('2. 12.30 pm to 02.30 am ')
        print('3. 03.00 pm to 05.00 pm ')
        print('4. 05.30 pm to 07.30 pm ')
        print('5. 08.00 pm to 10.00 pm ')
        print('6. 10.30 pm to 12.30 am ')

        try:
            timeofflight=int(input('select your boarding and landing destination from the above options'))
            if 1 <= timeofflight <= 6:
                break
            continue
        except Exception:
            print('Please select a number from 1 to 6!')
        

    while True:
        try:
            numberOfTickets=int(input('enter number of tickets required:'))
            break
        except Exception:
            print('Enter a number!')
            continue
    # source_dest_details = destination_dict.get(destination)
    for i in range(numberOfTickets):
        while True:
            nameOfPassenger=input('enter the name of the passenger:')
            if not validate_name(nameOfPassenger):
                print('Please enter alphabets only!')
                continue
            else:
                break
                
        while True:
            genderOfPassenger=input('enter the gender of the passenger (M)ale/(F)emale/(O)ther: ').upper().strip()
            if genderOfPassenger not in 'MFO':
                print('Please choose from the given options!')
                continue
            else:
                break

        while True:
            try:
                ageOfPassenger=int(input('enter the age of the passenger:'))
                if ageOfPassenger <= 0:
                    print('Please enter a nonzero number!')
                    continue
                break
            except Exception:
                print('Please enter a number!')
                continue

        seatno=random.randint(100000,999999)
        sq1='''insert into ticketDetails values('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(seatno, nameOfPassenger, genderOfPassenger, ageOfPassenger,flight,destination,timeofflight, user_date)
        print ('your ticket is booked and your seat no. is-',seatno)
        cursor.execute(sq1)
    ticket=input('If you want to display ticket(s) press "y", or press any other key to exit!')
    if ticket=='y':
        while True:
            try:
                n=int(input('enter no. of tickets u want to display'))
                break
            except ValueError:
                print('Please enter a number!')
                continue

        while n:
            while True:
                try:
                    seatnum=int(input('Enter your seat no.'))
                except Exception:
                    print('Please enter a number!')
                    continue

                sq2="select * from ticketDetails where seatno='%s'"%(seatnum)
                cursor.execute(sq2)
                data=cursor.fetchall()

                if not data:
                    print("Invalid seat no.!")
                    continue
                break
            no1=data[0][0]
            name1=data[0][1]
            gender1=data[0][2]
            age1=data[0][3]
            flight1=data[0][4]
            source1=data[0][5]
            time1=data[0][6]
            print('~~~~~~~~~~~~~~~~~~~~~~~~************************TICKET************************~~~~~~~~~~~~~~~~~~~~~')
            print('TICKET NO. :                           ',no1)
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('NAME :                                   ',name1)
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('GENDER :                               ',gender1)
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('AGE :                                      ',age1)
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('FLIGHT:                                  ',flight_dict.get(int(flight1)))
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('SOURCE & DESTINATION :                   ',destination_dict.get(int(source1)))
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('DATE & TIME:                                    ', user_date, time_dict.get(int(time1)))
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('COST :                                      Rs.5000')
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('~~~~~~~~~~~~~~~~~~~~~~~**************************THANKYOU*********************~~~~~~~~~~~~~~~~~~~~~~~~~')
            n -= 1
            
else:
    print('******************~~~~~~~~~~~THANK YOU FOR VISITING~~~~~~~~~****************')

mycon.commit()
cursor.close()
mycon.close()
