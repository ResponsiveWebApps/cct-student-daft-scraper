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
