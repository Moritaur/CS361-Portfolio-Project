# Author: David Emmons
# GitHub Username: Moritaur
# Date: 07/12/2023
# Description: Main run file. The program here utilizes information (classes, data, csv files) from inside the working
# directory to create, edit, view, and perform other functionalities with vacation destinations.


import Classes
import time


def add_to_prior_destinations():
    """This function will create a new destination and add it to the prior destinations list."""
    name = input('Enter the destination\'s name: ')
    description = input('Enter a short description or leave this blank: ')
    date = input('When did you visit ' + name + '? ')
    pic_count = input('How many pictures would you like to add? Please enter an integer: ')
    if pic_count == '':
        pic_count = 0
    pic_count = int(pic_count)
    pictures = []
    while pic_count > 0:
        pictures.append(input('Enter the path to your picture: '))
        pic_count -= 1
    area_map = 'insert map'
    new_destination = Classes.Destinations.Destination(name, description, date, pictures, area_map)
    return new_destination


def add_to_future_destinations():
    """This function will create a new destination and add it to the prior destinations list."""
    name = input('Enter the destination\'s name: ')
    description = input('Enter a short description or leave this blank: ')
    date = input('When will you visit ' + name + '? ')
    pictures = []
    area_map = 'insert map'
    new_destination = Classes.Destinations.Destination(name, description, date, pictures, area_map)
    return new_destination


def view_destinations(prior_destinations, future_destinations):
    print('Your saved prior destinations are:\n')
    prior_destinations = prior_destinations.get_destinations()
    for i in prior_destinations:
        print(prior_destinations[i].get_destination_name())
        i += 1
    print('\n', '------------------------------------------------------------' '\n')
    print('Your saved future destinations are:\n')
    future_destinations = future_destinations.get_destinations()
    for i in future_destinations:
        print(future_destinations[i].get_destination_name())
        i += 1
    return


def edit_destination(destination_list):
    """Prompt user to determine what attribute they want to edit, then allow them to edit that attribute in a given
    destination"""
    # Ensure the given name exists in the chosen list.
    destination_name = input('Please enter the name of the destination that has a feature you would like to'
                             ' edit: ')
    destinations = {}
    for destination in destination_list.get_destinations():
        destinations.update({destination_list.get_destinations()[destination].get_destination_name(): destination})
    if destination_name not in destinations:
        print('No destination by this name currently exists')
        return
    target = destination_list.get_destinations()[destinations[destination_name]]
    print(target.get_destination_name())

    # Determine what attribute the user wants to edit
    to_edit = input('Would you like to edit destination name (0), description (1), date (2), '
                    'pictures (3), or area map (4)?\n')
    if to_edit not in ['0', '1', '2', '3', '4', 'destination name', 'description', 'date', 'pictures',
                       'area map']:
        print('There is no detail by that name to edit.\n')
        return 1

    # Edit destination name.
    elif to_edit == '0' or to_edit == 'destination name':
        print('The current destination name is: ' + target.get_destination_name())
        new_name = input('Enter new destination name: ')
        target.set_destination_name(new_name)
        print('The destination name has been changed to: ' + new_name)

    # Edit description.
    elif to_edit == '1' or to_edit == 'description':
        print('The current description is: ' + target.get_description())
        new_desc = input('Enter new description: ')
        target.set_description(new_desc)
        print('The description has been changed to: ' + new_desc)

    # Edit date.
    elif to_edit == '2' or to_edit == 'date':
        print('The current date listed is: ' + target.get_date())
        new_date = input('Enter new date: ')
        target.set_date(new_date)
        print('The date has been changed to: ' + new_date)

    # Edit pictures.
    elif to_edit == '3' or to_edit == 'pictures':
        print('Sorry, this feature is not implemented yet')

    # Edit area map.
    elif to_edit == '4' or to_edit == 'area map':
        print('The current area map is: ' + target.get_area_map())
        new_map = input('Enter new area map location: ')
        target.set_area_map(new_map)
        print('The associated area map has been changed to: ' + new_map)
    return 0


def delete_destination(prior_destinations_list, future_destinations_list):
    """This function will remove the specified destination from the chose list."""
    view = input('If you need to view the available destinations enter 0, otherwise press enter: ')
    if view == '0':
        view_destinations(prior_destinations_list, future_destinations_list)
    list_to_delete = input('Enter 0 to remove a prior destination or 1 to remove a future destination, '
                           'any other key will stop deletion. ')
    del_name = ''
    list_name = 'Nothing'
    if list_to_delete == '0':
        del_name = prior_destinations_list.remove_destination(input('Enter prior destination to delete: '))
        list_name = 'prior destinations.'
    elif list_to_delete == '1':
        del_name = future_destinations_list.remove_destination(input('Enter future destination to delete: '))
        list_name = "future destinations."
    if del_name != '':
        print(del_name + ' has been deleted from your ' + list_name)
    else:
        print(list_name + ' has been deleted.')


def main():
    """Main function, keeps programming running, watched for input, manages other classes, etc."""

    # Initialize list for prior and future destinations.
    prior_destinations_list = Classes.Prior_Destinations.PriorDestination()
    future_destinations_list = Classes.Future_Destinations.FutureDestination()
    print('For options, please enter help or h')

    while True:
        # Stores what task user wishes to accomplish.
        task = input('What would you like to do? ')

        if task == 'help' or task == 'h' or task == 'Help' or task == 'HELP':
            # Explain options to user.
            print('Enter 0 to quit, 1 to add a previously visited destination and 2 to add a future destination.\n'
                  'Enter 3 to edit an already existing destination, 4 to view current destinations, and 5 to delete a'
                  'destination.')

        elif task == '0':
            # User wants to exit program.
            print('Thank you for using Trip Planner!')
            time.sleep(1)
            print('Your data has been saved, please have a great day!')
            time.sleep(1)
            break

        elif task == '1':
            # User wants to create a new prior destination.
            new_destination = add_to_prior_destinations()
            prior_destinations_list.add_destination(new_destination)
            print(new_destination, new_destination.get_destination_name())

        elif task == '2':
            # user wants to create a new future destination.
            new_destination = add_to_future_destinations()
            future_destinations_list.add_destination(new_destination)
            print(new_destination, new_destination.get_destination_name())

        elif task == '3':
            # User wants to edit a destination, follow prompts below.
            view = input('If you need to view the available destinations enter 0, otherwise press enter: ')
            if view == '0':
                view_destinations(prior_destinations_list, future_destinations_list)
            list_to_edit = input('Would you like to edit a prior destination (0), or a future destination (1)? ')
            if list_to_edit == '0':
                list_to_edit = prior_destinations_list
            elif list_to_edit == '1':
                list_to_edit = future_destinations_list
            else:
                print('Please try again, when prompted for a list to edit input 0 to edit a prior destination, or 1'
                      ' to edit a future destination.')
                return
            edited = '1'
            while edited == '1':
                edit_destination(list_to_edit)
                edited = input('Enter 0 to stop editing or 1 to edit more: ')

        elif task == '4':
            # User wants to view all stored destinations.
            view_destinations(prior_destinations_list, future_destinations_list)

        elif task == '5':
            delete_destination(prior_destinations_list, future_destinations_list)

        else:
            print('I am sorry, but there is no function for that button. Please enter "help" or "h" to see options.')


main()

