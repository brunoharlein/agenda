from .connection import Connection
from .entities.event import Event

class eventModel():
    """Class to perform all queries related to the event table in the database
        Classe pour effectuer toutes les requêtes liées à la table event dans la base de données agenda"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        # Créer une instance de la classe de connexion pour accéder à la base de données
        self.db = Connection()

    def get_events(self, date):
        """Select all events on a specific date from the database
            Sélectionnez tous les événements à une date spécifique dans la base de données"""
        sql = """SELECT event_id, title, description, event_time FROM event
                 WHERE event_date = %s
                 ORDER BY event_time"""
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
            Obtenez un single sur event par date et heure de la base de données"""
        sql = """SELECT * FROM event
                 WHERE event_date = %s
                 AND event_time = %s"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        # we want a single event so we use fetch one
        # nous voulons un seul événement, donc nous en utilisons un fetchone
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
            Insérer un objet event dans la base de données agenda"""
        sql = """INSERT INTO event(title, description, event_date, event_time)
                 VALUES(%s, %s, %s, %s)"""
        arguments = (event.title, event.description, event.event_date, event.event_time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, date, hour):
        """Delete an event from databse with date and hour
            Supprimer un event de la base de données agenda avec la date et l'heure"""
        sql = """DELETE FROM event
                 WHERE event_date = %s
                 AND event_time = %s"""
        arguments = (date, hour)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def update_event(self, event):
        """Update and event object in the database
            Mise à jour d'un event dans la base de données"""
        sql = """UPDATE event
                 SET title=%s, description=%s, event_date=%s, event_time=%s
                 WHERE event_id=%s"""
        arguments = (event.title, event.description, event.event_date, event.event_time, event.event_id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()


