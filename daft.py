from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location
import csv 

print("Hello CCT College student. I do not wish to be rude, but may I ask what you maximum rent should be?\n" +   
            "I assume as a sttudent there is no minimum rent.")
    maxRent = input("Max rent: ")

    print("Splendid. Would you like a house or an apartment?")
    propType = input("h or a?: ")

    print("Finally, one lump or two? How many bedrooms? Must be numerical.")
    numBedrooms = int(input("Bedrooms 1-10: "))
   

# Needs two different options settings for house and appartment.

    if propType == 'h':
        options = [
                    # Location always same setting. 
                    LocationsOption([Location.DUBLIN_CITY_CENTRE_DUBLIN]),

                    # Inputs.
                    PriceOption(0, maxRent),
                    BedOption(1, numBedrooms),
                    PropertyTypesOption([PropertyType.HOUSE])
                ]

    else:
        options = [
                    # Location always same setting. 
                    LocationsOption([Location.DUBLIN_CITY_CENTRE_DUBLIN]),

                    # Inputs.
                    PriceOption(0, maxRent),
                    BedOption(1, numBedrooms),
                    PropertyTypesOption([PropertyType.APARTMENT])
                ]

    # Will always be renting. 

    api = DaftSearch(SearchType.RENT)
    listings = api.search(options)

    return listings
