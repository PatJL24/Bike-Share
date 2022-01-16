import bike_share
import pprint
#function test for readHtml
data = bike_share.readHtml("http://research.cs.queensu.ca/home/cords2/bikes.txt")
print(data)

#function test for cleansing_function
print(bike_share.cleansing_function(data))

#function test for list_to_dictionaries
print(bike_share.list_to_dictionaries(data))


mock_data = {7000: {'capacity': 31, 'lat': 43.639832, 'lon': -79.395954, 
                    'name': 'Ft. York / Capreol Crt.', 'num_bikes_available': 20, 
                    'num_docks_available': 11}, 
            7001: {'capacity': 15, 'lat': 43.647992, 'lon': -79.370907, 
                   'name': 'Lower Jarvis St / The Esplanade', 'num_bikes_available': 5, 
                   'num_docks_available': 10},
            7004: {'capacity': 11, 'lat': 43.656518, 'lon': -79.389099, 
                   'name': 'University Ave / Elm St', 'num_bikes_available': 0,
                   'num_docks_available': 11},
            7005: {'capacity': 19,'lat': 43.648093,'lon': -79.384749, 
                    'name': 'University Ave / King St W','num_bikes_available': 0,
                    'num_docks_available': 18},
            7211: {'capacity': 15,'lat': 43.6375, 'lon': -79.40611111, 
                    'name': 'Fort York/Garrison', 'num_bikes_available': 15, 
                    'num_docks_available': 0}
             }

#function test for line_print
bike_share.lines()

#function test for rent_bikes
print((bike_share.rent_bikes(7000, mock_data)))
print((bike_share.rent_bikes(7005, mock_data)))


bike_share.lines()

#function test for return_back/return bikes
print((bike_share.return_bikes(7001, mock_data)))
print((bike_share.return_bikes(7211, mock_data)))

#function test for line_print
bike_share.lines()

#function test for bike_available
print(bike_share.bike_available(7000, mock_data))
print(bike_share.bike_available(7005, mock_data))

#function test for dock_available
print(bike_share.docks_available(mock_data))

#function test for full_station
bike_share.full_station(mock_data)

bike_share.lines()
#function test for info_station
print(bike_share.info_station(7000, mock_data))

#function test for specific_station_bike
print(bike_share.specific_station_bike(7000, mock_data))

#function test for ranking_of_availability
bike_share.ranking_of_availability(mock_data)

bike_share.lines()

#function test for directions
"""
This function is meant to convert the 
two points of lat and long given by the two Stations that the User inputs 
and converts it to a bearing and returns the converted bearing.

Then in the function called direction_back_continued, which in that function
it will print out which direction to go to. 
"""
print(bike_share.directions(7000, 7001 ,mock_data))

bike_share.lines()

"""
This function I tested it by setting the starting input as a default value of 
7000 in order to check that the if statements correctly tells the user the general
direction to go towards.
"""
print("Enter a station ID (from the mock draft) as a test to see if the function works.")
bike_share.direction_back_continued(7000, mock_data)


