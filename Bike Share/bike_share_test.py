import urllib.request    #this loads a library you will need.  Put this line at the top of your file.
import pprint
"""
Author: Patrick Li

Bike Share is an application that allows the user to rent and return bikes.
However, currently this version is only the User Interface portion of the application and as a result
functions, such as functions that keep track of rented bikes and how many docks are available at each station,
are now currently stub functions and will be replace later on. 
"""

def readHtml():
    """
    Function loads the data from the url.
    The url parameter will contain the full link to the data that will be converted to a list.
    Returns the data into a list.
    """
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/bikes.txt")
    html = response.readlines() #reads one line
    data = []
    for html_data in html:
        data.append(html_data.decode('utf-8').split('\t'))
    return data


def cleansing_function(data):
    """
    Converts the data into their correct type as well as deleted any "\r\n" characters in the data list.
    """
    for data_index in range(1, len(data)):
        station_index = data[data_index]
        data[data_index] = [int(station_index[0]), station_index[1].rstrip(),
                            float(station_index[2]), float(station_index[3]),
                            int(station_index[4]), int(station_index[5]), 
                            int(station_index[6])]
    data[0][6] = data[0][6].rstrip()
    return data
        
   
def list_to_dictionaries(data):
    """
    The function will convert the list into a dictionary of dictionaries where the nested dictionary key corresponds to the columns. 
    Each of the nested dictionary are the values for the student_ID.
    The data parameter is the list containing the data from the load_data function.
    Returns a dictionary of dictionaries of the bike data.
    """
    key_list = []
    data_dict = {}
        
    for i in range(len(data[0])):
        key_list.append(data[0][i])

    for station_data in data[1:]:
        data_dict[station_data[0]] = {key_list[1]: station_data[1],
                                 key_list[2]: station_data[2], key_list[3]: station_data[3],
                                 key_list[4]: station_data[4], key_list[5]: station_data[5],
                                 key_list[6]: station_data[6]}
    return data_dict
    
def rent_bikes(rent_id_input, data):
    """
    The function will deal with renting bikes at a specific station.
    The function will edit the data if a bike is available (bike_available) as well as
    prompt a statement if the bike is rented out or not and ask the user to choose another station.
    The parameter ID enables the function to check if that specific station has a bike available.
    The parameter data is essentially the dictionary of dictionaries containing the data of Bike Share.
    returns True or False if the renting a bike is successful or not.
    """
    #This section is the actually function itself which will be implemented later on.
    #Current this is a stub function
    print("-" * 200)
    data_rent = data[rent_id_input]['num_bikes_available']
    
    while True:
        if data_rent > 0:
            data_rent = data_rent - 1
            print("The Bike has been successfully rented.")
            print("There are " + str(data_rent) + " bikes available left at station " + str(rent_id_input))
            return data_rent
        elif data_rent == 0:
            print("The Station you want to rent at has no more bikes available.")
            print("To see which station has bikes available go back to the overall rent menu and select the second option.")
            return


def return_bikes(return_id_input, data):
    """
    The function will deal with returning bikes at a specific station. It will edit the data if a dock is available. (Calls upon dock_available) 
    It will prompt a statement if a dock is available or not and ask the user to choose another station.
    #the parameter ID enables the function to check if that specific station has a bike available.
    #the parameter data is essentially the dictionary of dictionaries containing the data of Bike Share.
    #returns True or False if the returning a bike is successful or not.
    """
    #This section is the actually function itself which will be implemented later on.
    #Current this is a stub function
    print("-" * 200)
    data_return = data[return_id_input]['num_docks_available']
    while True:
        if data_return > 0:
            data_return = data_return - 1
            print("The Bike has been successfully returned.")
            print("There are " + str(data_return) + " docks available left at station " + str(return_id_input))
            return
        elif data_return == 0:
            print("The Station you want to rent at has no more docks available.")
            print("To see which station has d available go back to the overall rent menu and select the second option.")
            return


def dock_available(data):
    """
    checks to see if there are any docks available at a station with the specific ID given in the parameters
    based on the ID, it will scan the dictionary of dictionaries and go to the specific section within the dictionary that contains all the data on the dock availability
    the parameter ID is related to the specific stations data on the number of docks available. 
    returns True or False is a dock is available at that station. 
    """
    print("-" * 150)
    dock_availablility = []
    for station_id, station_value in data.items():
        data_dock = data[station_id]['num_docks_available']
        if data_dock != 0:
            dock_availablility.append([station_id, station_value['num_docks_available']])
    
    dock_availablility.sort(key=lambda x: x[1], reverse=True)
    
    print("Station ID  Dock Availability")
    
    for dock in dock_availablility:
        print("        ".join(map(str, dock)))
    
    back_or_quit()
    

def bike_available(data):
    """
    checks to see if there are any bikes available at a station with the specific ID given in the parameters and if so how many bikes are available at that station
    based on the ID, it will scan the dictionary of dictionaries and go to the specific section within the dictionary that contains all the data on the bike availability
    the parameter ID is related to the specific stations data on the number of bikes available. 
    returns True or False is a bike is available at that station. 
    """
    #This section is the actually function itself which will be implemented later on.
    #Current this is a stub function
    print("-" * 150)
    bike_availablility = []
    for station_id, station_value in data.items():
        data_bike = data[station_id]['num_bikes_available']
        if data_bike != 0:
            bike_availablility.append([station_id, station_value['num_bikes_available']])
    
    bike_availablility.sort(key=lambda x: x[1], reverse=True)
    
    print("Station ID  Bike Availability")
    
    for bike in bike_availablility:
        print("        ".join(map(str, bike)))
        
    back_or_quit()
    
def menu_help(data, options):
    """
    prints out an explanation telling the user how to use the basic navigation system.
    no parameters and returns nothing
    """
    print("To navigate through the application:")
    print("First, there will be options with a number beside it." )
    print("You will navigate through the application by inputing the number that correlates to the section you want to go to.")
    print("For example, when you first open the application, 6 different options pop up on your screen:")
    print_options(options)
    print("If you want to go to the rent section, enter the number 2 to go to the rent section.")
    print("The general idea is that a list of options with a corresponding number that will be display for you.")
    print("To navigate to a section you want enter the number that corresponds to that number.")
    print("However, there is one thing to notes is that at the end of the process within each section,")
    print("there will be a prompt that ask you if you want to go back to the main menu (by inputing B) or ")
    print("in some cases there will be an option for you to quit the application (by inputing Q).")
    back_or_quit()
    
def menu_rent(data):
    """
    this function asks the input for an ID of a station. Calls upon the rent_bike function 
    if a bike is available, calls the rent_bike function, if not, then it prompts the user to enter another station ID
    the parameter data is essentially the dictionary of dictionaries containing the data of Bike Share
    returns the new data points in the list after it has gone through the return_bike function. 
    """
    print("Welcome to the rent section!")
    print("If you want to rent out a bike enter 1.")
    print("If you want to see bikes availability enter 2.")
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    while True:
        print("-" * 200)
        print("Options: ")
        rent_options = (" 1. Rent", " 2. Bike Availability")
        print_options(rent_options)
        rent_options_input = input("Enter a number that corresponds to the section listed above (Enter B if you want to go back or Q to Quit): ").lower()
        if rent_options_input == "1":
            rent_back(data)
        elif rent_options_input == "2":
            bike_available(data)
        elif rent_options_input == 'b':
            return
        elif rent_options_input == 'q':
            exit()
        else:
            print("Invalid Input.")
        
def rent_back(data):
    """
    This function is related to the function menu_rent() and is apart of the UI system of the application.
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    """
    while True:
        print("-" * 200)
        rent_input = input("Enter the ID of the Station you want to rent at (Enter B if you want to go back to the previous section): ")
        if rent_input == "b":
            return
        
        try:
            rent_id_input = int(rent_input)
            if rent_id_input in data.keys():
                rent_bikes(rent_id_input, data)
            else:
                print("-" * 200)
                print("Invalid Station ID.")
        except ValueError: 
            print("Errors")
        
    back_or_quit()

def menu_return(data):
    """
    this function asks the input for an ID of a station. Calls upon the return_bike function
    if so, calls the return_bike function, if not, then it prompts the user to enter another station ID
    the parameter data is essentially the dictionary of dictionaries containing the data of Bike Share
    returns the new data points in the list after it has gone through the return_bike function. 
    """
    print("Welcome to the return section!")
    print("If you want to return a bike enter 1.")
    print("If you want to see dock availability enter 2.")
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    while True:
        print("-" * 200)
        return_options = (" 1. Return", " 2. Dock Availability")
        print_options(return_options)
        return_options_input = input("Enter a number that corresponds to the section listed above (Enter B if you want to go back or Q to Quit): ").lower()
        if return_options_input == "1":
            return_back(data)
        elif return_options_input == "2":
            dock_available(data)
        elif return_options_input == 'b':
            return
        elif return_options_input == 'q':
            exit()
        else:
            print("Invalid Input.")

def return_back(data):
    """
    This function is related to the function menu_return() and is apart of the UI system of the application.
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    """
    while True:
        print("-" * 200)
        return_input = input("Enter the ID of the Station you want to return at (Enter B if you want to go back to the previous section): ")
        if return_input == "b":
            return
        try:
            ret_id_input = int(return_input)
            
            if ret_id_input in data.keys():
                return_bikes(ret_id_input, data) 
            else:
                print("Invalid Station ID.")
        
        except ValueError:
            print("Invalid Input.")

def menu_directions(data):
    """
    This function asks the input for the ID of the starting station and the ID of the station the user wants to go to. 
    Calls upon the directions function.
    The parameter data is essentially the dictionary of dictionaries containing the data of Bike Share.
    Return the direction of where the user should head to get to the other station.
    """
    print("Welcome to the direction section!")
    print("Enter the ID of two stations.")
    print("The first input is the starting station and the second input is the station you want to go to.")
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    while True:
        print("-" * 200)
        direction_options = (" 1. Direction", " 2. List of Stations")
        print_options(direction_options)
        direction_options_input = input("Enter a number that corresponds to the section listed above (Enter B if you want to go back): ").lower()
        if direction_options_input == "1":
            direction_back(data)
        elif direction_options_input == "2":
            direction_station_back(data)
        elif direction_options_input == 'b':
            return
        else: 
            print("Invalid Input")

def direction_back(data):
    """
    This function is related to the function menu_direction() and is apart of the UI system of the application.
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    """
    while True:
        print("-" * 200)
        starting_station = input("Enter the ID of the Station you are currently at (Enter B if you want to go back to the previous section): ")
        if starting_station == "b":
            return
        ending_station = input("Enter the ID of the Station you want to go to (Enter B if you want to go back to the previous section): ")
        if ending_station== "b":
            return
        #Once the real data has been implemented, then there will be a for loop to run through the nested dictionary
        starting_int = int(starting_station)
        ending_int = int(ending_station)
        if starting_int == data[0]['station_id']:
            if ending_int == data[0]['station_id']:
                directions(starting_int, ending_int, data)
                return False
            else:
                print("Invalid Station ID")
        else:
            print("Invalid Station ID.")


def direction_station_back(data):
    """
    This function is related to the function menu_direction() and is apart of the UI system of the application.
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    """
    while True:
        print("-" * 200)
        rent_return_options = (" 1. List of Stations with bikes available", " 2. List of Stations with docks available.")
        print_options(rent_return_options)
        rent_return_input = input("Enter a number or (Enter B if you want to go back): ").lower()
        if rent_return_input == "b":
            return
        elif rent_return_input == "1":
            ranking_of_availability(data)
            return False
        elif rent_return_input == "2":
            full_station(data)
            return False
        else:
            print("Invalid input.")
            
def directions(start_station, end_station, data):
    """
    This function will provide them with the direction to travel to get from one specified station to another.
    Parameter start_station is the initial station where the user is at.
    Parameter end_station is the station the user wants to go to.
    The parameter data is essentially the dictionary of dictionaries containing the data of Bike Share.
    Returns which direction the user heads to (i.e north).
    """
    #This section is the actually function itself which will be implemented later on.
    #Current this is a stub function
    print("-" * 200)
    print("Go in the northwest Direction to each the end destination.")
    back_or_quit()

def menu_stations(data):
    """
    This function asks the user if they want to either know how many bikes are at a specific station 
    (call function specific_station_bike), or if they want a list of all the stations ranking
    from most available bikes to least (calls avaliability_ranking), 
    or if they want a list of all the stations that are full (call full_station)
    The parameter data is essentially the dictionary of dictionaries containing the data of Bike Share
    No returns.
    """
    print("Welcome to the station section!")
    print("This section will allow you to learn all the information you need to know about any of the stations.")
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    while True:
        print("-" * 200)
        print("Options: ")
        stations_options = (" 1. Number of bikes at a specific station", " 2. Stations ranked by Bike availability ",  " 3. Stations ranked by Dock Availability ", " 4. All information on a specific Station.")
        print_options(stations_options)
        stations_options_input = input("Enter a number that corresponds to the section listed above (Enter B if you want to go back or Q to Quit): ").lower()
        if stations_options_input == "1":
            num_back(data)
        elif stations_options_input == "2":
            ranking_of_availability(data)
        elif stations_options_input == "3":
            full_station(data)
        elif stations_options_input == "4":
            info_back(data)
        elif stations_options_input =='b':
            return
        elif stations_options_input == 'q':
            exit()
        else:
            print("Invalid Input.")

def info_back(data):
    """
    This function is related to the function menu_station() and is apart of the UI system of the application.
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    """
    while True:
        print("-" * 200)
        info_input = input("Enter the station ID to see all the information about that station (Enter B if you want to go back to the previous section): ")
        if info_input == "b":
            return
        #Once the real data has been implemented, then there will be a for loop to run through the nested dictionary
        info_int = int(info_input)
        if info_int == data[0]['station_id']:
            info_station(info_int, data)
            return False
        else:
            print("Invalid Station ID.")

def num_back(data):
    """
    This function is related to the function menu_station() and is apart of the UI system of the application.
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    """
    while True:
        print("-" * 200)
        num_bikes = input("Enter the station ID to see the number of bikes available at that specific station (Enter B to go back): ")
        if num_bikes == "b":
            return
        #Once the real data has been implemented, then there will be a for loop to run through the nested dictionary
        num_int = int(num_bikes)
        for i in range(len(data)):
            if num_int == data[i]['station_id']:
                specific_station_bike(num_int, data)
                return False
            else:
                print("Invalid Station ID.")


def specific_station_bike(specific_input, data): 
    """
    This function returns the number of bikes available from a specific station.
    The parameter specific_input enables the function to check if that specific station has a bike available.
    The parameter data is essentially the dictionary of dictionaries containing the data of Bike Share.
    Returns the number of bikes available from a specific station.
    """
    print("-" * 200)
    print("There are ____ number of bikes at that specific station.")
    back_or_quit()

def ranking_of_availability(data):
    """
    this function acquires the data for bikes available and puts all the stations with available bikes into 
    one dictionary in the order of availability from greatest and least. Prints out that dictionary.
    the parameter data is essentially the dictionary of dictionaries containing the data of Bike Share.
    returns the dictionary.
    """
    #This section is the actually function itself which will be implemented later on.
    #Current this is a stub function
    print("-" * 200)
    print("List of Stations in bike availability from greatest to least: ")
    back_or_quit()

def full_station(data):
    """
    This function acquires the data for docks available and puts the value of station ID .
    and the availability of bikes into a separate dictionary, only those stations whose docks are completely filled
    The parameter data is essentially the dictionary of dictionaries containing the data of Bike Share.
    Returns a dictionary of stations whose docks are completely filled.
    """
    #This section is the actually function itself which will be implemented later on.
    #Current this is a stub function
    print("-" * 200)
    print("List of stations with docks available from greatest to least: ")
    back_or_quit()

def info_station(info_int, data):
    """
    This function returns all the information on the specific station that is linked with the ID in the parameters
    The parameter info_input enables the function to check if that specific station has a bike available
    The parameter data is essentially the dictionary of dictionaries containing the data of Bike Share
    Returns all the information about the specific station linked with the ID in the parameter
    """
    #This section is the actually function itself which will be implemented later on.
    #Current this is a stub function
    mock_data = ("station ID: 7000", "name: Ft. York / Capreol Crt", "lat: 43.639832", "lon: -79.395954", "num_bikes_available: 20", "num_docks_available: 11") 
    print_options(mock_data)
    back_or_quit()

def print_options(options):
    """
    Prints the options that the user can input to navigate through the application.
    The options parameter is just a list of options that the user uses to navigate through the application.
    """
    print ('\n'.join(options))

def main_menu(data):
    """
    Prompts the user for an numeric input based on the options listed 
    and the program will always run unless the user enters a certain number to quit the application.
    The function will check if the inputed word matches any of the options and 
    if it does calls the function relating to the word 
    (menu_rent, menu_return, option_station, direction).
    """
    while True:
        main_options = (" 1. Help", " 2. Rent", " 3. Return", " 4. Directions", " 5. Stations")
        print("-" * 200)
        print("Here are your options: ")
        print_options(main_options)
        print("-" * 200)
        print("To go to a certain section, enter a number that correlates with that section.")
        print("To quit the application, enter Q.")
        print("-" * 200)
        user_input = input("Please enter your input: ").lower()
        print("-" * 200)
        if user_input == 'q':
            exit()
        else:
            check_input(user_input, data, main_options)

def back_or_quit():
    """
    The function is meant to give the user the option to either go back to the
    main menu or quit the application. 
    """
    print("-" * 200)
    print("To go back to the previous section, please enter B. ")
    print("To quit the application, please enter Q. ")
    while True:
        repeat_input = input("Please Enter B or Q: ").lower()
        if repeat_input == 'b':
            return 
        elif repeat_input == 'q':
            exit()
        else:
            print("Please try again: ")
    print("-" * 200)
        
def check_input(user_input, data, options):
    """
    Checks the user input to see what number that the user entered and calls the 
    correct function to execute based on the input. 
    """
    if user_input == "1":
        menu_help(data, options)
    elif user_input == "2":
        menu_rent(data)
    elif user_input == "3":
        menu_return(data)
    elif user_input == "4":
        menu_directions(data)
    elif user_input == "5":
        menu_stations(data)
    else:
        print("Invalid Input, Please enter a number listed. ")
        
def main():
    """
    To initialize and store local variables as well as call upon other functions.
    No returns or parameters.
    data_dict is a sample data in order to test out the user functions.
    """
    data = readHtml()
    data = cleansing_function(data)
    data = list_to_dictionaries(data)
    print(data[7000]['name'])
    print("Hello, welcome to Bike Share! ")
    main_menu(data)
    
if __name__ == "__main__":
    main()
