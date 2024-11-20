import argparse
import pandas as pd

# Display information and accept arguments
def acceptArguments():
    scriptDesc = "Choose from the following aircraft types to view plane data: 767, 762, 650. Or choose based on carrier: Cargoject, Mesa Airlines, and Ameriflight."
    parser = argparse.ArgumentParser(description=scriptDesc)
    parser.add_argument("--carrier", help="The carrier of the aircraft.")
    parser.add_argument("--type", help="The type of aircraft.")

    args = parser.parse_args()
    if (args.carrier):
        displayCarrier(args.carrier)
    elif (args.type):
        displayType(args.type)
    else:
        print("No action specified. Use --help for usage instructions.")

def displayCarrier(carrier):
    # Use regex with pandas to find carrier in CSV file
    try:
        dataframe = pd.read_csv("planes.csv")
        regex = fr'\b{carrier}\b'
        rowExists = dataframe[dataframe['[Carrier]'].str.contains(regex, na=False)]
        print(rowExists)
    except pd.errors.ParserError as e:
        print(f"An unexpected error has occurred: {e}")

def displayType(type):
    # Use regex with pandas to display plane that has the type within the tail number
    try:
        dataframe = pd.read_csv("planes.csv")
        regex = fr'N{type}[a-zA-Z]'
        rowExists = dataframe[dataframe['[Tail Number]'].str.contains(regex, na=False)]
        print(rowExists)
    except pd.errors.ParserError as e:
        print(f"An unexpected error has occurred: {e}")

# Run the script
acceptArguments()