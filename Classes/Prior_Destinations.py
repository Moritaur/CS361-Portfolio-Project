# Author: David Emmons
# GitHub Username: Moritaur
# Date: 07/12/2023
# Description: This class is a way to store destinations that one has already visited. It allows the importing or
# exporting of information as well as the editing / viewing of the list of destinations.


class PriorDestination:
    def __init__(self):
        self._destinations = {}

    def add_destination(self, destination):
        """Create a destination object and add it to this list."""
        self._destinations[len(self._destinations)] = destination

    def remove_destination(self):
        """Select a destination object from the list and remove it from the list."""
        pass

    def view_destinations(self):
        """List all of the destinations in this list."""
        pass

    def import_from_csv(self, file_name):
        """Import destination(s) from a csv file."""
        pass

    def export_to_csv(self, file_name):
        """Export this list of destinations to a csv file."""
        pass
