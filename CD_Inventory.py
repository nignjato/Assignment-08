#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Nik Ignjatovic, 2021-Dec-08, updated file
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstTbl = [] # list of CD objects
CD_UniqueID = 0

class CD:
    """Stores data about a CD:

    properties:
        cd_ID: (int) with CD ID
        cd_Title: (string) with the title of the CD
        cd_Artist: (string) with the artist of the CD
    methods:
        __init__: initialize object
        __str__: standard format for object

    """
    def __init__(self,cd_ID,cd_Title,cd_Artist):
        self.__cd_ID = cd_ID
        self.__cd_Title = cd_Title
        self.__cd_Artist = cd_Artist

    def __str__(self):
        return '{}, {}, {}'.format(self.__cd_ID,self.__cd_Title,self.__cd_Artist)
    
    
    @property
    def cd_ID(self):
        return self.__cd_ID
    
    @cd_ID.setter
    def cd_ID(self,value):
        if str(value).isnumeric():
            self.cd_ID = value
        else:
            raise Exception('CD ID must be a number.')
            
    
    @property
    def cd_Title(self):
        return self.__cd_Title
    
    @cd_Title.setter
    def cd_Title(self,value):
        if str(value).isnumeric():
            raise Exception('CD Title cannot be a number.')
        else:
            self.cd_Title = value
    
    
    @property
    def cd_Artist(self):
        return self.__cd_Artist
    
    @cd_Artist.setter
    def cd_Artist(self,value):
        if str(value).isnumeric():
            raise Exception('CD Artist cannot be a number.')
        else:
            self.cd_Artist = value
    


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:
        file_name: name of the file
        table = table of objects
    methods:
        save_inventory(file_name, table): -> None
        load_inventory(file_name, table): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name, table):
        """Function to load data from file.
        
        Args:
            file_name: name of the file
            table: list of objects
        Returns:
            None
        """
        table.clear()
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            data_pop = [data[0].strip(),data[1].strip(),data[2].strip()]
            id_pop = data_pop[0]
            title_pop = data_pop[1]
            artist_pop = data_pop[2]
            table_pop = CD(id_pop, title_pop, artist_pop)
            table.append(table_pop)
        objFile.close()
    
    @staticmethod
    def save_inventory(file_name, table):
        """Function to save data to file.
        
        Args:
            file_name: name of the file
            table: list of objects
        Returns:
            None
        """
        objFile = open(file_name, 'w')
        for row in table:
            objFile.write(str(row) + '\n')
        objFile.close()
        
# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    
    @staticmethod
    def welcome():
        """Function to welcome the user. I know it's unnecessary :)
        
        Args:
            None
        Returns:
            None
        """
        print('\nWelcome to the CD Inventory program.\n')
    
    @staticmethod
    def menu():
        """Function to show the menu.
        
        Args:
            None
        Returns:
            None
        """
        print('\n---MENU---')
        print('[l] load inventory from file')
        print('[a] add a new CD')
        print('[i] show current inventory')
        print('[s] save inventory to file')
        print('[x] exit the program')
               
    @staticmethod
    def useraction():
        """Function get intended menu action of user.
        
        Args:
            None
        Returns:
            action: the user's menu choice
        """
        action = input('Enter the letter of the action you wish to execute: ')
        return action
    
    @staticmethod
    def display_inventory(table):
        """Function to display inventory.
        
        Args:
            table: table of objects
        Returns:
            None
        """
        print('======= The Current Inventory: =======')
        print('ID, CD Title, Artist\n')
        for row in table:
            print(row)
        print('======================================')
    
    @staticmethod
    def add_CD():
        """Function to add a new CD.
        
        Args:
            None
        Returns:
            ID_add: new CD's ID
            Title_add: new CD's Title
            Artist_add: new CD's Artist
        """
        ID_add = input('Enter an ID: ')
        Title_add = input('Enter the title: ')
        Artist_add = input('Enter the Artist: ')
        return ID_add, Title_add, Artist_add

# -- Main Body of Script -- #

# Welcome
IO.welcome()

# Load data from file into a list of CD objects on script start

while True:
    try:
        FileIO.load_inventory(strFileName, lstTbl)
        print('Data from the file has been loaded.\n')
        break
    except FileNotFoundError:
        print('No file was found!')
        FileIO.save_inventory('cdInventory.txt',lstTbl)
        print('A new cdInventory.txt file was created.')
        break
    except Exception:
        print('There was an error.')
        break


# Main Loop
while True:

    # Display Menu
    IO.menu()
    # User selects action
    action = IO.useraction()
    if action == 'x':
        break
    if action == 'l':
        FileIO.load_inventory(strFileName, lstTbl)
        print('\nYour data has been loaded:')
        IO.display_inventory(lstTbl)
        continue 
    if action == 'a':
        ID_add, Title_add, Artist_add = IO.add_CD()
        CD_UniqueID = CD_UniqueID + 1
        CD_UniqueName = CD_UniqueID
        CD_UniqueName = CD(ID_add, Title_add, Artist_add)
        print('\nYou entered:')
        print(CD_UniqueName)
        lstTbl.append(CD_UniqueName)
        print('\nThis CD has been added to inventory.')
        continue
    if action == 'i':
        print()
        IO.display_inventory(lstTbl)
        continue
    if action == 's':
        FileIO.save_inventory(strFileName, lstTbl)
        print('Your data has been saved to the file.')
        continue
    else:
        print('There was an error. Please try again.')
        


