def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("===  BMI Calculator ===\n")
    while True:
        try:
            weight = float(input("Enter your weight (in KG): "))
            height = float(input("Enter your height (in Meter): "))
        except ValueError:
            print(" Invalid input! Please enter numbers only.\n")
            continue

        # Validation check
        if weight <= 0 or height <= 0:
            print(" Weight and Height must be positive numbers. Try again.\n")
            continue

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print("\n Result:")
        print(f"   Your BMI: {bmi:.2f}")
        print(f"   Category: {category}\n")

        # Option to continue or exit
        choice = input("Do you want to calculate again? (y/n): ").lower()
        if choice != "y":
            print("\n Thank you for using the BMI Calculator!")
            break


if __name__ == "__main__":
    main()
