# Author: David Emmons
# GitHub Username: Moritaur
# Date: 07/12/2023
# Description: This class creates a destination object. This objet stores information about a travel destination and can
# be assigned to a previous or future destination location.


class Destination:
    def __init__(self, destination_name, description, date, pictures, area_map):
        self._destination_name = destination_name
        self._description = description
        self._date = date
        self._pictures = pictures
        self._area_map = area_map

    def information(self):
        """This returns the information contained in the destination object."""
        pass

    def edit(self, variable):
        """This function allows one to edit the information present in the created Destination."""
        if variable == self._destination_name:
            self._destination_name = input('Enter updated destination name here: ')
        elif variable == self._description:
            self._description = input('Enter updated description here: ')
        elif variable == self._date:
            self._date = input('Enter updated date here: ')
        elif variable == self._pictures:
            print('updating pictures')
        elif variable == self._area_map:
            self._area_map = input('Enter updated area map here: ')
        else:
            print('No information found')

    def delete(self):
        """This class will delete the destination object."""
        pass
