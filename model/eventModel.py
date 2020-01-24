# coding: utf-8
from .connection import Connection
from .entities.event import Event

class eventModel():
    """Class to perform all queries related to the event table in the database
        Classe pour effectuer toutes les requêtes liées à la table d'événements dans la base de données"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        # Créer une instance de la classe de connexion pour accéder à la base de données
        self.db = Connection()

    def get_events(self, date):
        """Select all events on a specific date from the database
            Sélectionnez tous les événements à une date spécifique dans la base de données"""
        sql = """select event_id, title, description, event_time from event
                 where event_date = %s
                 order by event_time"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        events = self.db.cursor.fetchall()
        self.db.close_connection()
        # Turn each list from events into an event object
        # Transformez chaque liste d'événements en un objet d'événement
        for key, value in enumerate(events):
            events[key] = Event(value)
        return events
