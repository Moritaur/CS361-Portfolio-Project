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

    # Get methods for Destination class.
    def get_destination_name(self):
        """Getter method, returns destination name."""
        return self._destination_name

    def get_description(self):
        """Getter method, returns description."""
        return self._description

    def get_date(self):
        """Getter method, returns date."""
        return self._date

    def get_pictures(self):
        """Getter method, returns pictures."""
        return self._pictures

    def get_area_map(self):
        """Getter method, returns area map."""
        return self._area_map

    # Set methods for Destination class.
    def set_destination_name(self, new_name):
        """Setter method, sets destination name."""
        self._destination_name = new_name

    def set_description(self, new_description):
        """Setter method, sets description."""
        self._description = new_description

    def set_date(self, new_date):
        """Setter method, sets date."""
        self._date = new_date

    def set_pictures(self, new_pictures):
        """Setter method, sets pictures."""
        self._pictures = new_pictures

    def set_area_map(self, new_area_map):
        """Setter method, sets area map."""
        self._area_map = new_area_map

    # Non setter / getter functions.
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

