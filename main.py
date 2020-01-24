import os
import time
import calendar
import locale
from datetime import datetime

from view.eventView import eventView

# Main file acting like a routing system
# Fichier principal agissant comme un système de routage
# Call the right method from the view, depending on user input
# Appelez la bonne méthode à partir de la vue, en fonction de l'entrée de l'utilisateur

# Simple intro for the app
# Introduction pour l'application
os.system('cls' if os.name == 'nt' else 'clear')
print("Bienvenue sur votre agenda personnel")
time.sleep(3)

# Set locale zone to France and get the current month and year to display right calendar
# Réglez la zone locale sur la France et obtenez le mois et l'année en cours pour afficher le bon calendrier
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
currentYear = datetime.now().year
currentMonth = datetime.now().month

# The action the user wants to do, by default nothing
# L'action que l'utilisateur veut faire, par défaut rien
action = ""
# while the user does not chose to leave the program
# alors que l'utilisateur n'a pas choisi de quitter le programme
while action != 'q':
    view = eventView()
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print the current date
    print("Nous sommes le : {}".format(datetime.today().strftime('%d %B %Y')))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    # Print the current calendar
    print (calendar.month(currentYear, currentMonth, 2, 1))
    print("Que souhaitez vous gérer ? (v: voir, a: annuler, n: nouveau, m: modifier, s: suivant, p: précédent, q: quitter)")
    action = input(": ")
    # Call the right action function according to user input
    # Appeler la fonction d'action appropriée en fonction de l'entrée utilisateur
    if action == "s":
        # If we reach december then go back to january
        # Si nous atteignons décembre, revenons à janvier
        if currentMonth < 12:
            currentMonth += 1
        else:
            currentMonth = 1
            currentYear += 1
    elif action == "p":
        # If we reach january then go bakc to december
        # Si nous arrivons en janvier, retournons en décembre
        if currentMonth > 1:
            currentMonth -= 1
        else:
            currentMonth = 12
            currentYear -= 1
    elif action == "v":
        view.show_events()
    elif action == "n":
        view.new_event()
    elif action == "a":
        view.delete_event()
    elif action == "m":
        view.update_event()
    else:
        pass

# Leave the program
# Quittez le programme
print("Merci et au revoir")
time.sleep(3)
exit()
