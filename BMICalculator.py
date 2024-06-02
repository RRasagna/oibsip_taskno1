def calculate_bmi(weight, height):
    # Calculate the bmi index with the formula and return the value
    bmi = weight/(height**2)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5:
        return "Under Weight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Over Weight"
    elif 30 <= bmi <= 39.9:
        return "Obesity"
    else:
        return "Severe Obesity"


def main():
    # Allow the user to enter the weight and height
    weight = float(input("Enter your Weight(in kilograms):"))
    height = float(input("Enter your height(in meters):"))

    # Calling the functions
    BMI = calculate_bmi(weight,height)
    Category = bmi_category(BMI)
    print(" "*30)

    print(f"Your BMI index is:{BMI:.02f}")
    print(f"Yor category is:{Category}")
    print(" "*30)

    print("BMI Categories")
    print("Under Weight: BMI < 18.5")
    print("Normal: 18.5 <= BMI <= 24.9")
    print("Over Weight: 25 <= BMI < 29.9")
    print("Obesity : 30 <= BMI < 39.9")
    print("Severe Obesity: BMI >= 40")


if __name__ == "__main__":
    main()










