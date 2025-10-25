class RomanConverter:
    def __init__(self, number=0):
        self.number = number

    def to_roman(self):
        """Convert the integer to a Roman numeral."""
        num = self.number
        if not (0 < num < 4000):
            return "Number must be between 1 and 3999."

        # Roman numeral mapping
        roman_numerals = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]

        roman_value = ""
        for symbol, value in roman_numerals:
            while num >= value:
                roman_value += symbol
                num -= value
        return roman_value


def main():
    # Take integer input from the user
    try:
        number = int(input("Enter an integer (1–3999): "))
        converter = RomanConverter(number)
        print(f"Roman numeral: {converter.to_roman()}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
