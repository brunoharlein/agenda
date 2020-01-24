# coding: utf-8
import psycopg2
import psycopg2.extras

class Connection():
    """Class to manage the connection, the cursor and the requests to a database
        Classe pour gérer la connexion, le curseur et les requêtes vers une base de données"""
    # Store the username, the port and the database name as class attributs
    # In this case no host name and password because of my own configuration
    # Stockez le nom d'utilisateur, le port et le nom de la base de données en tant qu'attributs de classe
    # Dans ce cas, pas de nom d'hôte et de mot de passe en raison de ma propre configuration
    USER = "brunoharlein"
    PORT = "5432"
    DATABASE = "agenda"

    def __init__(self):
        # The class stores an instance of pyscopg2 connection and cursor classes
        # La classe stocke une instance de connexion pyscopg2 et des classes de curseur
        self.connection = None
        self.cursor = None

    def initialize_connection(self):
        """Instanciate a connection and a cursor and store them in the related attributs
            Instancier une connexion et un curseur et les stocker dans les attributs associés"""
        try:
            self.connection = psycopg2.connect(user = Connection.USER,
                                               port = Connection.PORT,
                                               database = Connection.DATABASE)
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

    def close_connection(self):
        """Close both connection and cursor
            Fermer la connexion et le curseur"""
        if(self.connection):
            self.cursor.close()
            self.connection.close()
