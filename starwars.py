""" This program uses the Star Wars API to  
print the names of people in the Star Wars Universe. 
Also gives the home planet and vehicle name of every individual  """

import urllib.parse
import requests 

main_api = 'https://swapi.dev/api/people/'
vehicles_api =  'http://swapi.dev/api/vehicles/14/'


jsondata = requests.get(main_api).json()

vehicledata = requests.get(vehicles_api).json()


def findPlanet(maindata):
    planet_api = maindata['homeworld']
    planetdata = requests.get(planet_api).json()
    return planetdata['name']


def findVehicle(individual_data):
    vehicle_data = individual_data['vehicles']
    myVehicle = []
    for i in vehicle_data:
        vehicle_info = requests.get(i).json()
        myVehicle.append(vehicle_info['name'])

    return myVehicle

namesAll = jsondata['results']
print("Here's a list of all people in the Star Wars Universe: \n")
for each in namesAll:
    print("Name: "+ each['name'])
    myplanet=findPlanet(each)
    print("My planet: " + myplanet)

    #print(each['vehicles'])
    myVehicles=findVehicle(each)
    print("My vehicle/s: ")
    print(myVehicles)
    print("\n")
