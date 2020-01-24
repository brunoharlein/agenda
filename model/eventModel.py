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

    def get_single_event(self, date, hour):
        """Get on event by date and hour from database
            Obtenez sur l'événement par date et heure de la base de données"""
        sql = """select * from event
                 where event_date = %s
                 and event_time = %s"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        # we want a single event so we use fetch one
        # nous voulons un seul événement, donc nous en utilisons un
        event = self.db.cursor.fetchone()
        self.db.close_connection()
        # This function is used for checking
        # Cette fonction est utilisée pour vérifier
        # So if we find something we return an event object, otherwise false
        # Donc, si nous trouvons quelque chose, nous retournons un objet événement, sinon false
        if event:
            return Event(event)
        return False

    def add_event(self, event):
        """Insert an event object into the database
            Insérer un objet événement dans la base de données"""
        sql = """insert into event(title, description, event_date, event_time)
                 values(%s, %s, %s, %s)"""
        arguments = (event.title, event.description, event.event_date, event.event_time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, date, hour):
        """Delete an event from databse with date and hour
            Supprimer un événement de la base de données avec la date et l'heure"""
        sql = """delete from event
                 where event_date = %s
                 and event_time = %s"""
        arguments = (date, hour)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()



