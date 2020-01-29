from model.eventModel import eventModel
from model.entities.event import Event

class eventView():
    """View or controller taking care of all the logic related to event in the app.
        Vue ou contrôleur prenant en charge toute la logique liée à l'événement dans l'application."""
    model = eventModel()

    def __init__(self):
        pass

    def show_events(self):
        """Display all the events for specific date from database to the screen
            Afficher tous les événements pour une date spécifique de la base de données à l'écran"""
        date = input("Vous souhaitez voir votre agenda pour quelle journée ? : ")
        events = self.model.get_events(date)
        print("\nVotre agenda du {}\n".format(date))
        if events:
            for event in events:
                print(event)
        else:
            print("Rien ce jour là, bravo vous êtes libre :-)")
        input("Tapez sur une touche pour continuer")

    def new_event(self):
        """Displays inputs to register a new event in the database
            Affiche les entrées pour enregistrer un nouvel événement dans la base de données"""
        event = Event()
        event.title = input('Titre : ')
        event.description = input('Description (optionnelle) : ')
        event.event_date = input('Date (aaaa-mm-jj) : ')
        event.event_time = input('Heure (hh:mm) : ')
        # Check the hour of the new event is free
        while self.model.get_single_event(event.event_date, event.event_time):
            print("Vous avez déjà quelque chose à cette heure là !")
            event.event_time = input('Nouvelle heure : ')
        self.model.add_event(event)

    def delete_event(self):
        """Display an input to delete a event from database by date and hour
            Afficher une entrée pour supprimer un événement de la base de données par date et heure"""
        date = input("Jour de l'événement : ")
        hour = input("Heure de l'événement : ")
        self.model.delete_event(date, hour)

    def update_event(self):
        """Allow user to change attribut's value for specific event
            Autoriser l'utilisateur à modifier la valeur de l'attribut pour un événement spécifique"""
        # Retrieve an event if it exists
        # Récupérer un événement s'il existe
        choice = ""
        while choice != "s":
            date = input("Jour de l'événement : ")
            hour = input("Heure de l'événement : ")
            event = self.model.get_single_event(date, hour)
            if event : break
            print("Nous ne trouvons rien à cette date")
            choice = input("Tapez s pour arrêter, n'importe quelle touche pour continuer")
        # If we have found an event
        # Si nous avons trouvé un événement
        if event:
            print("Voici les informations enregistrées")
            # User can change attributs as long as he wants
            # L'utilisateur peut modifier les attributs aussi longtemps qu'il le souhaite
            while True:
                print(event)
                print("Tapez s pour arrêter")
                attribut = input("Attribut à modifier : ")
                if attribut == 's' : break
                value = input("Nouvelle valeur : ")
                # If he chooses to change the hour then we check the hour is free
                # S'il choisit de changer l'heure, nous vérifions que l'heure est gratuite
                if attribut == "event_time":
                    while self.model.get_single_event(event.event_date, value):
                        print("Vous avez déjà quelque chose à cette heure là !")
                        value = input('Nouvelle heure : ')
                # Set the new value and update the database
                # Définissez la nouvelle valeur et mettez à jour la base de données
                setattr(event, attribut, value)
            self.model.update_event(event)
