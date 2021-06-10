from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location
import csv 

# Inputs

def getInputs():

    print("Hello CCT College student. I do not wish to be rude, but may I ask what you maximum rent should be?\n" +   
            "I assume as a sttudent there is no minimum rent.")
    maxRent = input("Max rent: ")

    print("In Dublin 2 near CCT College or anywhere in the city?")
    area = input("n or a ? ")

    print("Splendid. Would you like a house or an apartment?")
    propType = input("h or a? ")

    print("Finally, one lump or two? How many bedrooms? Must be numerical.")
    numBedrooms = int(input("Bedrooms 1-10: "))

    # Needs two different options settings for house and appartment.

    if area.lower() == 'n':
        area = Location.DUBLIN_2_DUBLIN
    
    else:
        area = Location.DUBLIN_CITY_CENTRE_DUBLIN

    if propType.lower() == 'h':
        propType = PropertyType.HOUSE
    
    else:
        propType = PropertyType.APARTMENT

    options = [
               # Location always same setting. 
               LocationsOption([area]),

               # Inputs.
               PriceOption(0, maxRent),
               BedOption(1, numBedrooms),
               PropertyTypesOption([propType])
              ]

    # Will always be renting. 

    api = DaftSearch(SearchType.RENT)
    listings = api.search(options)

    return listings

# Print results

def printResults(listings):
    print("****************")
    print("Search complete:")
    print("****************")

    rows = []
    sorted_listings = sorted(list(listings), key=lambda a: a.price, reverse=False)

    for listing in sorted_listings:
        print("(" + str(getattr(listing, 'id')) + ")" + " €" + str(getattr(listing, 'price')) + " " + getattr(listing, 'title'))
        rows.append([getattr(listing, 'id'), getattr(listing, 'price'), getattr(listing, 'title')])

    return rows

# Write CSV

def writeCSV(rows):

    #print(rows)

    Details = ['id', 'price', 'address']  
    with open('daft_results.csv', 'w') as f: 
        write = csv.writer(f) 
        write.writerow(Details) 
        write.writerows(rows) 


# Run scraper and create CSV file with results.

writeCSV(printResults(getInputs()))

print("Happy hunting.")