# Define a function that will be used to call the actions of a length unit converter
def length_unit_converter():
    print("Welcome to the Length Unit Converter!")

    # Available units and conversion to meters
    unit_to_meters = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "mile": 1609.34
    }

    # Output the units available
    units_list = list(unit_to_meters.keys())
    print("\nAvailable units:", ', '.join(units_list))

    # Get length value
    value_input = input("\nEnter the length value: ")
    if not value_input.replace('.', '', 1).isdigit():
        print("Invalid input: Please enter a number.")
        return
    value = float(value_input)

    # Get source unit
    source_unit = input("Enter the source unit (e.g., mm, cm, m, km, in, ft, mile): ").lower()
    if source_unit not in unit_to_meters:
        print(f"Invalid source unit. Available units are: {', '.join(units_list)}")
        return

    # Get destination unit that is the main destination 
    destination_unit = input("Enter the destination unit: ").lower()
    if destination_unit not in unit_to_meters:
        print(f"Invalid destination unit. Available units are: {', '.join(units_list)}")
        return

    # Convert source to meters, then to destination
    value_in_meters = value * unit_to_meters[source_unit]
    converted_value = value_in_meters / unit_to_meters[destination_unit]

    # Output result
    print(f"\nResult: {value} {source_unit} = {converted_value:.4f} {destination_unit}")

# Call the function of the converter
length_unit_converter()
