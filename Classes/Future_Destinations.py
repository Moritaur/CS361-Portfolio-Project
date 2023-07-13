# Author: David Emmons
# GitHub Username: Moritaur
# Date: 07/12/2023
# Description: This class is a way to store destinations that one plans to visit. It allows the importing or
# # exporting of information as well as the editing / viewing of the list of destinations.


class FutureDestination:
    def __init__(self):
        self._destination_count = 0
        self._destinations = {}

    def get_dc(self):
        """Returns the current number of destinations"""
        return self._destination_count

    def get_destinations(self):
        """Returns the current destinations stored in this class."""
        return self._destinations

    def increment_dc(self):
        """Increase destination count by 1."""
        self._destination_count += 1

    def decrement_dc(self):
        """Decrease destination count by 1."""
        self._destination_count -= 1

    def add_destination(self, destination):
        """Create a destination object and add it to this list."""
        self._destinations[self._destination_count] = destination
        self.increment_dc()

    def remove_destination(self):
        """Select a destination object from the list and remove it from the list."""
        self.decrement_dc()

    def view_destinations(self):
        """List all the destinations in this list."""
        pass

    def import_from_csv(self, file_name):
        """Import destination(s) from a csv file."""
        pass

    def export_to_csv(self, file_name):
        """Export this list of destinations to a csv file."""
        pass
