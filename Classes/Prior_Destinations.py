# Author: David Emmons
# GitHub Username: Moritaur
# Date: 07/12/2023
# Description: This class is a way to store destinations that one has already visited. It allows the importing or
# exporting of information as well as the editing / viewing of the list of destinations.


class PriorDestination:
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

    def remove_destination(self, destination):
        """Select a destination object from the list and remove it from the list."""
        for key in self._destinations:
            if self._destinations[key].get_destination_name() == destination:
                self._destinations.pop(key)
                self.decrement_dc()
                return destination

    def view_destinations(self):
        """List all the destinations in this list."""
        pass

    def import_from_csv(self, file_name):
        """Import destination(s) from a csv file."""
        pass

    def export_to_csv(self, file_name):
        """Export this list of destinations to a csv file."""
        pass
