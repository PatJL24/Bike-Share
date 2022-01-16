import urllib.request  #imports the library called urllib.request
from math import * #imports math library
"""
Author: Patrick Li

Bike Share is an application that allows the user to rent and return bikes.

There are other features such as features to check which station has no docks available,
information on a specific station, a list of stations, order from greatest to least, based 
on how many bikes are available, and how many bikes are available at specific station. 
As well as a list of stations, from greatest to least, based on how many docks are available.
"""

def readHtml(url):
    """
    Function loads the data from the url.
    
    Parameter: url - Passes in through the data that is contained in the url.
    
    Returns: data - returns a list of all the data provided by the url
    """
    response = urllib.request.urlopen(url) #fetches the data from the url provided
    html = response.readlines() #reads one line
    data = [] 
    
    for html_data in html: 
        #appends the data into the empty list. Sorted by tabs.
        data.append(html_data.decode('utf-8').split('\t')) 
    
    return data

def cleansing_function(data):
    """
    Converts the data into their correct data type as well as deleted any "\r\n" characters in the data list.

    Parameters: data - passes through the data list given by the function readHtml
    
    Returns: data - returns the data list with the correct types of all the values as well as deletes the /r/n
    """
    for data_index in range(1, len(data)):
        station_index = data[data_index] 
        
        #converts all the data into their correct data type.
        data[data_index] = [int(station_index[0]), station_index[1].rstrip(),
                            float(station_index[2]), float(station_index[3]),
                            int(station_index[4]), int(station_index[5]), 
                            int(station_index[6])]
        
    data[0][6] = data[0][6].rstrip() #removes the /r/n from the list
    
    return data #returns the list data
        
def list_to_dictionaries(data):
    """
    The function will convert the list into a dictionary of dictionaries.
    The Keys are the Station ID and the values are the information on each specific Station ID.
    
    Parameter: data - contains the list of data that was cleansed via cleanse_function
    
    Return: data_dict - a dictionary of dictionaries of the bike data.
    """
    key_list = []
    data_dict = {}
        
    for i in range(len(data[0])):
        #appends the keys to a list called key_list
        key_list.append(data[0][i])
    
    #converts the list into a nested dictionary    
    for station_data in data[1:]:
        data_dict[station_data[0]] = {key_list[1]: station_data[1],
                                 key_list[2]: station_data[2], key_list[3]: station_data[3],
                                 key_list[4]: station_data[4], key_list[5]: station_data[5],
                                 key_list[6]: station_data[6]}
    
    return data_dict  #returns the list data
    
def docks_available(data):
    """
    Checks and prints out all stations that have any docks available in order from greatest to least.  
    
    Parameter: data - Passes the data throughout function docks_available.

    Returns: None
    """
    lines() #a function that prints dash lines
    dock_availablility = []
    
    #appends the data into a nested list
    for station_id, station_value in data.items():
        data_dock = data[station_id]['num_docks_available']
        
        if data_dock != 0:
            dock_availablility.append([station_id, station_value['num_docks_available']])
    
    #orders the list from greatest to least.
    dock_availablility.sort(key=lambda x: x[1], reverse=True)

    print("Station ID  Dock Availability")
    
    #joins the nested list together with a space string in the middle
    for dock in dock_availablility:
        print("        ".join(map(str, dock)))
    
def bike_available(int_specific_bike, data):
    """
    Checks to see if there are any bikes available at a station with the specific ID by the user.
    If there are bikes available at the station, it will print out how many.
    If there are no bikes available it will inform of the user. 
    
    Parameters: int_specific_bike - The Station ID based on the user's input.
                data - Passes through the data 
                
    Returns: True or False based on if the bike available at that station.
    """
    #checks to see if the inputed value is in the data keys.
    if int_specific_bike in data.keys():
        data_bike_available = data[int_specific_bike]['num_bikes_available']
        
        if data_bike_available == 0:
            return False
        elif data_bike_available > 0:
            return True

def bike_available_boolean(data):
    """
    This function is meant to check what the user inputs:
    If the user inputs b then the function will go back to the previous section
    If the user inputs q then the function will exit the program.
    If the user inputs a valid station ID then the function will call bike_available function
    
    Parameters: data - Passes the data throughout the function. (data is just a nested dictionary containing information from the url.)
    
    Returns: None
    """
    lines()
    
    while True:
        specific_bike_station = input("Enter a valid Station ID (B to go back to the previous section or Q to Quit): ").lower()
        
        if specific_bike_station == "b":
            return        
        elif specific_bike_station == "q":
            exit()
            
        try:     
            int_specific_bike = int(specific_bike_station)
            
            #checks to see if the inputed value is one of the keys in data.
            if int_specific_bike in data.keys():
                bike_available(int_specific_bike, data)    
                
                data_bike_available = data[int_specific_bike]['num_bikes_available']
                
                #if bike_available returns true, it will continue with the if statement
                if bike_available(int_specific_bike, data):  
                    lines()
                    print("The number of bikes available at station " + str(int_specific_bike) + ": " + str(data_bike_available))
                    back_or_quit()
                    return
                else:
                    lines()
                    print("No Bikes available at station " + str(int_specific_bike))
                    back_or_quit()
            else:
                lines()
                print("Invalid Station ID.")
                lines()
                
        except ValueError:
            lines()
            print("Invalid Input.")
            lines()

def menu_help(options):
    """
    Prints out an explanation telling the user how to use the basic navigation system.
    
    Parameters: options - Passes through the options which were created in the main_menu function.
    
    Returns: None
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
    print("there will be a prompt that ask you if you want to go back to the main menu (by inputing B) or Q to quit the program")
    back_or_quit()
    
def menu_rent(data):
    """
    The function is a menu that deals with the options relating to rent. 
    Such as Rent, Bike Availability, and Bike Availability at a Specific Station.
    
    Parameters: data - Passes the data throughout function menu_rent.
    
    Returns: None
    """
    print("Welcome to the rent section!")
    print("If you want to rent out a bike enter 1.")
    print("If you want to see bikes availability enter 2.")
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    while True:
        lines()
        print("Options: ")
        rent_options = (" 1. Rent", " 2. Bike Availability", " 3. Bike Availability at a Specific Station")
        print_options(rent_options)
        rent_options_input = input("Enter a number that corresponds to the options listed above (B to go back to the previous section or Q to Quit): ").lower()
        
        if rent_options_input == "1":
            rent_back(data)
            
        elif rent_options_input == "2":
            ranking_of_availability(data)
            back_or_quit()
            
        elif rent_options_input == "3":
            bike_available_boolean(data)
        
        elif rent_options_input == 'b':
            return
        
        elif rent_options_input == 'q':
            exit()
        
        else:
            print("Invalid Input.")
        
def rent_back(data):
    """
    This function is related to the function menu_rent().
    Allows the user to go back to the previous section or quit the application.
    Checks to see if the user inputs a valid station ID before calling upon the rent function.
    
    Parameters: data - Passes the data throughout function rent_back
    
    Returns: None
    """
    while True:
        lines()
        rent_input = input("Enter a valid Station ID (B to go back to the previous section or Q to Quit): ").lower()
        
        if rent_input == "b":
            return
        
        elif rent_input == "q":
            exit()
        
        try:
            rent_id_input = int(rent_input)
            
            #checks to see if the inputed value matches one of the keys in data.
            if rent_id_input in data.keys():
                rent_boolean(rent_id_input, data)
                return
            
            else:
                lines()
                print("Invalid Station ID.")
        
        except ValueError: 
            lines()
            print("Invalid Station ID.")
        
    back_or_quit()

def rent_bikes(rent_id_input, data):
    """
    The function will deal with renting bikes at a specific station.
    It will edit the data if a bike is available.
    
    Parameters: rent_id_input - Passes through the Station ID that the user inputed.
                data - Passes the data throughout function rent_bikes
   
    Returns: True or False if the renting a bike is successful or not.
    """
    data_rent = data[rent_id_input]['num_bikes_available']
    
    if data_rent == 0:
        return False
    
    elif data_rent > 0:
        data[rent_id_input]['num_bikes_available'] = data[rent_id_input]['num_bikes_available'] - 1
        data[rent_id_input]['num_docks_available'] = data[rent_id_input]['num_docks_available'] + 1
        return True

def rent_boolean(rent_id_input, data):
    """
    Checks to see whether or not the rent_bikes returns True or False.
    Based on that, it will print out the appropriate statements.
    
    Parameters: rent_id_input - the value in the variable is the user's input of the Station ID.
                data - 
    """
    #if rent_bikes returns True then it continues with the if statements.
    if rent_bikes(rent_id_input, data):
        lines()
        print("The Bike has been successfully rented.")
        print("Station " + str(rent_id_input) + " has " + str(data[rent_id_input]['num_bikes_available']) + " bikes available.")
        back_or_quit()
    
    else:
        lines()
        print("Rent unsuccessful.")
        print("Station " + str(rent_id_input) + " has " + str(data[rent_id_input]['num_bikes_available']) + " bikes available.")
        print("To see which station has bikes available go back to the overall rent menu and select the second option.")
        back_or_quit()
    
def menu_return(data):
    """
    The function is a menu that deals with the options relating to rent. 
    Such as Return, and Dock Availability
    
    Parameters: data - Passes the data throughout function menu_return.
    
    Returns: None
    """
    print("Welcome to the return section!")
    print("If you want to return a bike enter 1.")
    print("If you want to see dock availability enter 2.")
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    while True:
        lines()
        return_options = (" 1. Return", " 2. Dock Availability", " 3. Dock Availability at Specific Station")
        print_options(return_options)
        return_options_input = input("Enter a number that corresponds to the options listed above (B to go back to the previous section or Q to Quit): ").lower()
        
        if return_options_input == "1":
            return_back(data)
        
        elif return_options_input == "2":
            docks_available(data)
            back_or_quit()
        
        elif return_options_input == "3":
            specific_station_bike_back(data)
        
        elif return_options_input == 'b':
            return
        
        elif return_options_input == 'q':
            exit()
        
        else:
            print("Invalid Input.")

def return_back(data):
    """
    This function is related to the function menu_return().
    Allows the user to go back to the previous section or quit the application.
    Checks to see if the user inputs a valid station ID before calling upon the return function.
    
    Parameters: data - Passes the data throughout function return_back
    
    Returns: None
    """
    while True:
        lines()
        return_input = input("Enter a valid Station ID (B to go back to the previous section or Q to Quit): ").lower()
        
        if return_input == "b":
            return
        
        elif return_input == "q":
            exit()
            
        try:
            return_id_input = int(return_input)
            
            #checks to see if the inputed value matches one of the keys in data.
            if return_id_input in data.keys():
                return_boolean(return_id_input, data)
                return
            
            else:
                print("Invalid Station ID.")
        
        except ValueError:
            print("Invalid Input.")

def return_bikes(return_id_input, data):
    """
    The function will deal with returning bikes at a specific station.
    It will edit the data if a dock is available.
    
    Parameters: return_id_input - Passes through the Station ID that the user inputed.
                data - Passes the data throughout function return_bikes
   
    Returns: True or False if the returning a bike is successful or not.
    """
    data_return = data[return_id_input]['num_docks_available']
    
    if data_return == 0:
        return False
    
    elif data_return > 0:
        data[return_id_input]['num_docks_available'] = data[return_id_input]['num_docks_available'] - 1
        data[return_id_input]['num_bikes_available'] = data[return_id_input]['num_bikes_available'] + 1
        return True

def return_boolean(return_id_input, data):
    """
    Will print out statements based on if the return_bikes function returns True or False.
    
    Parameters: return_id_input - Passes the user's input throughout the function
                data - Passes the data throughout function return_boolean.
    
    Returns: None
    """
    if return_bikes(return_id_input, data):
        lines()
        print("The Bike has been successfully returned.")
        print("Station " + str(return_id_input) + " has " + str(data[return_id_input]['num_docks_available']) + " docks available.")
        back_or_quit()
    
    else:
        lines()
        print("Returned unsuccessful.")
        print("Station " + str(return_id_input) + " has " + str(data[return_id_input]['num_docks_available']) + " docks available.")
        print("To see which station has docks available go back to the overall return menu and select the second option.")
        back_or_quit()


def menu_directions(data):
    """
    The function is a menu that deals with the options relating to directions.
    Such as Direction and List of Stations.
    
    Parameters: data - Passes the data throughout function menu_return.
    
    Returns: None
    """
    print("Welcome to the direction section!")
    
    print("Enter the ID of two stations.")
   
    print("The first input is the starting station and the second input is the station you want to go to.")
    
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    
    while True:
        lines()
        direction_options = (" 1. Direction", " 2. List of Stations")
        print_options(direction_options)
        direction_options_input = input("Enter a number that corresponds to the option listed above (B to go back to the previous section or Q to Quit): ").lower()
        
        if direction_options_input == "1":
            direction_back(data)
        
        elif direction_options_input == "2":
            direction_station(data)
        
        elif direction_options_input == "b":
            return
        
        elif direction_options_input == "q":
            exit()
       
        else: 
            print("Invalid Input.")

def direction_station(data):
    """
    This function is related to the function menu_direction().
    This function is to allow the user to go back to the previous section or quit the application. 
    Checks to see if the user inputed correctly based on the options given.
    If so then the function will call the appropriate function based on what the user inputed. 
    
    Parameters: data - Passes the data throughout the function direction_station
    
    Return: None
    """
    while True:
        lines()
        print("List of Stations by: ")
        station_options = (" 1. Bike Availability", " 2. Dock Availability")
        print_options(station_options)
        choice_input = input("Enter the number that corresponds to the option listed above (B to go back to the previous section or Q to Quit): ")
        
        if choice_input == "1":
            ranking_of_availability(data)
            back_or_quit()
        
        elif choice_input == "2":
            docks_available(data)
            back_or_quit()
        
        elif choice_input == "b":
            return
        
        elif choice_input == "q":
            exit()
        
        else:
            print("Invalid Input.")

def direction_back(data):
    """
    This function is related to the function menu_direction().
    This function is to allow the user to go back to the previous section or quit the application. 
    Checks to see if the user inputed correctly based on the options given.
    The function will ask the user for a input of the Station ID of the starting station
    and will pass the starting station ID to another function. 
    
    Parameters: data - Passes the data throughout the function direction_station
    
    Return: None
    """
    while True:
        lines()
        starting_station = input("Enter the ID of the Station you are currently at (B to go back to the previous section or Q to Quit): ").lower()
        
        if starting_station == "b":
            return
        
        elif starting_station == "q":
            exit()
       
        try:        
            starting_station_int = int(starting_station)    
            
            #checks to see if the inputed value matches one of the keys in data.
            if starting_station_int in data.keys(): 
                direction_back_continued(starting_station_int, data)
                return
            else:
                lines()
                print("Invalid Station ID.")
                
        except ValueError:
            lines()
            print("Invalid Input. Please Restart the Process.")

def direction_back_continued(starting_station_int, data):
    """
    Ask the user to input the Station ID of the station they want to go to.
    It checks to see if the user inputed 'b' (to go back to the previous section),
    'q' (to quit), or will check to see if the user inputed a valid Station ID.
    If the ID is valid, then it will call the direction function and determine what 
    direction the user should go to get to the Station they want to go to.
    
    Parameters: starting_station_int - Passes through the value of the user's input
                data - Passes the data throughout function direction_back_continued
    
    Returns: None
    
    """
    while True:
        ending_station = input("Enter the ID of the Station you want to go to (B to go back to the previous section or Q to Quit): ").lower()
        
        if ending_station== "b":
            return
        
        elif ending_station == "q":
            exit()
                    
        ending_station_int = int(ending_station)
        
        #checks to see if the second input matches the first input
        if ending_station_int == starting_station_int:
            lines()
            print("You are already at the Station.")
            back_or_quit()
            return
        
        #checks to see if the inputed value matches one of the keys in data.
        if ending_station_int in data.keys():
            directions(starting_station_int, ending_station_int, data)
            the_directions = int(directions(starting_station_int, ending_station_int, data))
            lines()
            
            if the_directions == 0:
                print("Head East.")
                back_or_quit()
                return
            
            elif the_directions > 0 and the_directions < 90:
                print("Head Northeast.")
                back_or_quit()
                return
            
            elif the_directions == 90:
                print("Head North.")
                back_or_quit()
                return
           
            elif the_directions > 90 and the_directions < 180:
                print("Head Northwest.")
                back_or_quit()
                return
            
            elif the_directions == 180:
                print("Head West.")
                back_or_quit()
                return
            
            elif the_directions > 180 and the_directions < 270:
                print("Head Southwest.")
                back_or_quit()
                return
           
            elif the_directions == 270:
                print("Head South.")
                back_or_quit()
                return
            
            elif the_directions > 270 and the_directions < 360:
                print("Head Southeast.")
                back_or_quit()
                return
            
            else:
                print("Error")
        
        else:
            lines()
            print("Invalid Station ID.")
            lines()

def directions(start_station, end_station, data):
    """
    After getting the information on the latitude and longitude of the two stations,
    the function will pass the information into a formula and then convert it to a 
    bearing where it will be used to determine which direction to go to.
    
    Parameter: - start_station: the initial station where the user is at.
               - end_station: the station the user wants to go to.
               - data: Passes the data throughout the function directions
   
    Returns: converted_bearings - a degree which will be used later on to acquire the correct direction.
    """
    data_starting = data[start_station]
    data_ending = data[end_station]
    start_position = []
    end_position = []
    
    start_position.append(data_starting['lat'])
    start_position.append(data_starting['lon'])
    
    end_position.append(data_ending['lat'])
    end_position.append(data_ending['lon'])
    
    #converts the ints into radians
    lat_start = radians(start_position[0])
    lat_end = radians(end_position[0])
    diff_long = radians(end_position[1] - start_position[1])
    
    #Calculates the x and y coordinates/values
    x_bearing = sin(diff_long) * cos(lat_end)
    y_bearing = cos(lat_start) * sin(lat_end) - (sin(lat_start) * cos(lat_end) * cos(diff_long))
    
    #calculates the initial bearings
    init_bearing = atan2(x_bearing, y_bearing)
    
    #converts the radians to degrees
    init_bearing_deg = degrees(init_bearing)
    
    #sets the range from -180 to +180 from 0 to 360
    converted_bearing = (init_bearing_deg + 360) % 360
    
    return converted_bearing

def menu_stations(data):
    """
    This function asks the user if they want to either know how many bikes are at a specific station 
    (call function specific_station_bike), or if they want a list of all the stations ranking
    from most available bikes to least (calls avaliability_ranking), 
    
    Parameters: data - Passes the data through the function menu_stations
    
    Returns: None
    """
    print("Welcome to the station section!")
    print("This section will allow you to learn all the information you need to know about any of the stations.")
    print("Enter B to go back to the main menu or Enter Q to Quit the Program.")
    
    while True:
        lines()
        print("Options: ")
        stations_options = (" 1. Number of bikes available at a Specific Station", " 2. Stations ranked by Bike Availability ",  " 3. Stations ranked by Dock Availability ", " 4. All information on a Specific Station", " 5. Stations with no Docks Available")
        print_options(stations_options)
        stations_options_input = input("Enter a number that corresponds to the options listed above (B if you want to go back or Q to Quit): ").lower()
        
        if stations_options_input == "1":
            specific_station_bike_back(data)
        
        elif stations_options_input == "2":
            ranking_of_availability(data)
            back_or_quit()
        
        elif stations_options_input == "3":
            docks_available(data)
            back_or_quit()
        
        elif stations_options_input == "4":
            info_back(data)
            back_or_quit()
        
        elif stations_options_input == "5":
            full_station(data)
            back_or_quit()
        
        elif stations_options_input =='b':
            return
        
        elif stations_options_input == 'q':
            exit()
        
        else:
            lines()
            print("Invalid Input.")

def info_back(data):
    """
    This function is related to the function menu_station().
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    
    Checks to see if the user's input is in the data, if so, calls the info_station_data function.
    
    Parameters: data - Passes the data through the function info_back
    
    Returns: None
    """
    while True:
        lines()
        info_input = input("Enter a valid Station ID (Enter B to go back to the previous section or Q to Quit): ").lower()
        
        if info_input == "b":
            return
        
        elif info_input == "q":
            exit()
        
        try:
            info_int_input = int(info_input)
            
            #checks to see if the inputed value matches one of the keys in data.
            if info_int_input in data.keys():
                info_station_data = info_station(info_int_input, data)
                lines()
                return print_options(info_station_data)
            
            else:
                print("Invalid Station ID.")
                
        except ValueError:
            print("Invalid Input.")

def info_station(info_int_input, data):
    """
    Returns all the information on the specific station based on the station ID that user inputed.
    
    Parameter: info_int_input - Passes the value inside info_int_input throughout the function.
               data - Passes the data throughout the function.

    Returns: info_string - all the information about the specific station.
    """
    info_data = data[info_int_input]
    
    info_string = ("Station ID: " + str(info_int_input), "name: " + str(info_data['name']), "latitude: " + str(info_data['lat']), "longitude: " + str(info_data['lon']), "Capacity: " + str(info_data['capacity']),
    "Bikes Available: " + str(info_data['num_bikes_available']), "Docks Available: " + str(info_data['num_docks_available']))
    
    return info_string

def specific_station_bike_back(data):
    """
    This function is related to the function menu_station().
    This function is to allow the user to go back to the previous section in case the user made a mistake,
    whether the mistake was a mistype or if the user doesn't know the station id. 
    
    Checks to see if the user's input is b, q, or a valid station ID.
    If the valid station ID is valid, then it calls the function specific_station_bike.
    
    Parameters: data - Passes the data throughout the function.
    
    Returns: None
    """
    while True:
        lines()
        num_bikes_input = input("Enter a valid Station ID (Enter B to go back to the previous section or Q to Quit): ").lower()
        
        if num_bikes_input == "b":
            return
        
        elif num_bikes_input == "q":
            exit()
        
        try:
            num_int = int(num_bikes_input)
            
            #checks to see if the inputed value matches one of the keys in data.
            if num_int in data.keys():
                bike_specific_data = (specific_station_bike(num_int, data))
                print("The number of bikes available at Station " + str(num_int) + " is: " + str(bike_specific_data))
                back_or_quit()      
                return
            
            else:
                lines()
                print("Invalid Station ID.")
       
        except ValueError:
            lines()
            print("Invalid Input.")

def specific_station_bike(specific_input, data): 
    """
    This function returns the number of bikes available from a specific station.
    
    Parameters: specific_input - Passes the user's input to the rest of the function.
                data - Passes the data throughout the function.  (Data is just a nested dictionary containing information from the url.)
    
    Returns: bike_available - the number of bikes available from a specific station.
    """
    lines()
    bike_available_specifc = data[specific_input]['num_bikes_available']
    return bike_available_specifc

def ranking_of_availability(data):
    """
    This function acquires the data for bikes available and puts all the stations with available bikes into 
    a list which is then ordered from greatest and least. 
    Prints out that dictionary.
    
    Parameter: data - Passes the data throughout the function. (data is just a nested dictionary containing information from the url.)
    
    Returns: None
    """
    lines()
    bike_availablility = []
    
    #appends the data into a nested list
    for station_id, station_value in data.items():
        data_bike = data[station_id]['num_bikes_available']
        
        if data_bike != 0:
            bike_availablility.append([station_id, station_value['num_bikes_available']])

    #orders the list from greatest to least.
    bike_availablility.sort(key=lambda x: x[1], reverse=True)

    print("Station ID  Bike Availability")
    
    #joins the nested list together with a space string in the middle
    for bike in bike_availablility:
        print("        ".join(map(str, bike)))
    
def full_station(data):
    """
    This function acquires the data for docks available and puts the value of station ID .
    and the availability of bikes into a separate list, only those stations whose docks are completely filled.
    
    Parameter: data - Passes the data throughout the function. (data is just a nested dictionary containing information from the url.)
    
    Returns: None
    """
    lines()
    dock_full = []
    
    #appends the data into a nested list
    for station_id, station_value in data.items():
        data_dock = data[station_id]['num_docks_available']
        
        if data_dock == 0:
            dock_full.append([station_id, station_value['num_docks_available']])
    
    #orders the list from greatest to least.
    dock_full.sort(key=lambda x: x[1], reverse=True)
    
    print("Station ID  Dock Availability")
    
    #joins the nested list together with a space string in the middle
    for dock in dock_full:
        print("        ".join(map(str, dock)))
        
def print_options(options):
    """
    Prints the options that the user can input to navigate through the application.
    The options parameter is just a list of options that the user uses to navigate through the application.
    
    Parameters: options - Any variable that deals with needing to print out the options are passed through this parameter.
    
    Returns: None
    """
    print ('\n'.join(options))

def main_menu(data):
    """
    Prompts the user for an numeric input based on the options listed 
    and the program will always run unless the user enters a certain number to quit the application.
    The function will check if the inputed word matches any of the options and 
    if it does calls the function relating to the word 
    (menu_rent, menu_return, option_station, direction).
    
    Parameters: data - Passes the data throughout the function. (data is just a nested dictionary containing information from the url.)
    
    Returns: None
    """
    while True:
        main_options = (" 1. Help", " 2. Rent", " 3. Return", " 4. Directions", " 5. Stations")
        lines()
        print("Here are your options: ")
        print_options(main_options)
        lines()
        print("To go to a certain section, enter a number that correlates with that section.")
        print("To quit the application, enter Q.")
        lines()
        user_input = input("Please enter your input: ").lower()
        lines()
        
        if user_input == 'q':
            exit()
        
        else:
            check_input(user_input, data, main_options)

def check_input(user_input, data, options):
    """
    Checks the user input to see what number that the user entered and calls the 
    correct function to execute based on the input. 
    
    Parameters: User_input - Passes the user's input throughout the function
                data - Passes the data throughout the function
                options - Passes the options variable into the function
                
    Returns: None
    """
    if user_input == "1":
        menu_help(options)
    
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

def back_or_quit():
    """
    The function is meant to give the user the option to either go back to the
    main menu or quit the application. 
    
    Parameters: None
    
    Returns: None
    """
    lines()
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
    lines()

def lines():
    """
    Function makes it quicker and easier to print out dash lines
    
    Parameters: None
    
    Returns: None
    """
    print("-" * 200)
        
def main():
    """
    To initialize and store local variables as well as call upon other functions.
    To call the main_menu function.
    
    Parameters: None
    
    Returns: None
    """
    data = readHtml("http://research.cs.queensu.ca/home/cords2/bikes.txt")
    data = cleansing_function(data)
    data = list_to_dictionaries(data)   
    print("Hello, welcome to Bike Share!")
    main_menu(data)

#To differentiate between the bike_share.py and test.py
if __name__ == "__main__":
    main()
