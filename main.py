# Author: David Emmons
# GitHub Username: Moritaur
# Date: 07/12/2023
# Description: Main run file. The program here utilizes information (classes, data, csv files) from inside the working
# directory to create, edit, view, and perform other functionalities with vacation destinations.


import Classes
import time


def add_to_prior_destinations():
    name = input('Enter the destination\'s name: ')
    description = input('Enter a short description or leave this blank: ')
    date = input('When did you visit ' + name + '? \n')
    pic_count = int(input('How many pictures would you like to add?'))
    pictures = []
    for p in range(pic_count):
        pictures.append(input('Enter the path to your picture:\n'))
    area_map = 'insert map'
    new_destination = Classes.Destinations.Destination(name, description, date, pictures, area_map)
    return new_destination


def add_to_future_destinations():
    name = input('Enter the destination\'s name: ')
    description = input('Enter a short description or leave this blank: ')
    date = input('When did you visit ' + name + '? \n')
    pic_count = int(input('How many pictures would you like to add?'))
    pictures = []
    for p in range(pic_count):
        pictures.append(input('Enter the path to your picture:\n'))
    area_map = 'insert map'
    new_destination = Classes.Destinations.Destination(name, description, date, pictures, area_map)
    return new_destination


def main():
    """Main function, keeps programming running, watched for input, manages other classes, etc."""

    # Initialize list for prior and future destinations.
    prior_destinations_list = Classes.Prior_Destinations.PriorDestination()
    future_destinations_list = Classes.Future_Destinations.FutureDestination()
    print('For options, please enter help or h')

    while True:
        task = input('What would you like to do? ')

        if task == 'help' or task == 'h' or task == 'Help':
            print('Enter 0 to quit, 1 to add a previously visited destination and 2 to add a future destination. '
                  'Enter 3 to edit an already existing destination, and 4 to view current destinations.')

        elif task == '0':
            print('Thank you for using Trip Planner!')
            time.sleep(1)
            print('Your data has been saved, please have a great day!')
            time.sleep(1)
            break

        elif task == '1':
            new_destination = add_to_prior_destinations()

            print(type(prior_destinations_list), type(new_destination))

        elif task == '2':
            new_destination = Classes.Destinations.Destination
            print(type(future_destinations_list), type(new_destination))

        elif task == '3':
            pass

        elif task == '4':
            pass
        else:
            print('I am sorry, but there is no function for that button. Please enter "help" or "h" to see options.')


main()
