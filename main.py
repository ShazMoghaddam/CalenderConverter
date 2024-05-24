import convertdate


def convert_calendar(date, from_calendar, to_calendar):
    """
    Converts a date between different calendar systems.

    Args:
        date (tuple): A tuple representing the date (year, month, day)
        from_calendar (str): The calendar system of the input date
        to_calendar (str): The desired calendar system for the output

    Returns:
        tuple: A tuple representing the converted date (year, month, day)
            or None if conversion is not supported.
    """

    try:
        converting_date = convertdate.convert(date, from_calendar, to_calendar)
        return converting_date[0:3]  # Extract year, month, day
    except Exception as e:  # Catch any exception related to conversion
        # Check if the error message indicates a compatibility issue
        if "compatibility" in str(e).lower():
            print(f"Conversion from '{from_calendar}' to '{to_calendar}"
                  f"' might not be supported in your 'convertdate' version.")
        else:
            print(f"An error occurred during conversion: {e}")
        return None

# Example usage


date_to_convert = (2024, 5, 23)  # Today's date in Gregorian calendar
converted_date = convert_calendar(date_to_convert, 'gregorian', 'islamic')

if converted_date:
    print(f"Converted date (Islamic): {converted_date[0]}-{converted_date[1]}-{converted_date[2]}")
else:
    print("Conversion failed!")


def main():
    while True:
        date_str = input("Enter a date (YYYY-MM-DD) or 'q' to quit: ")
        if date_str.lower() == 'q':
            break

        try:
            year, month, day = map(int, date_str.split('-'))
            from_calendar = input("Enter source calendar (e.g., gregorian, islamic): ")
            to_calendar = input("Enter target calendar: ")
            converting_date = convert_calendar((year, month, day), from_calendar, to_calendar)

            if converted_date:
                print(f"Converted date ({to_calendar}): {converted_date[0]}-{converted_date[1]}-{converted_date[2]}")
            else:
                print("Conversion failed.")
        except ValueError:
            print("Invalid date format. Please enter YYYY-MM-DD.")


if __name__ == "__main__":
    main()
