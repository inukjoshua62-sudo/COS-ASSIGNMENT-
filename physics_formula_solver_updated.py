# PHYSICS FORMULA SOLVER
# Calculates five Physics formulas, rounds answers to 2 decimal places,
# displays the correct units, and asks whether to continue.

while True:
    print("\n" + "=" * 35)
    print("       PHYSICS FORMULA SOLVER")
    print("=" * 35)
    print("1. Momentum")
    print("2. Work Done")
    print("3. Power")
    print("4. Wave Speed")
    print("5. Pressure")

    choice = input("Choose a formula (1-5): ").strip()

    if choice == "1":
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))
        answer = mass * velocity
        print(f"Momentum = {answer:.2f} kg m/s")

    elif choice == "2":
        force = float(input("Enter force (N): "))
        distance = float(input("Enter distance (m): "))
        answer = force * distance
        print(f"Work Done = {answer:.2f} J")

    elif choice == "3":
        work = float(input("Enter work done (J): "))
        time = float(input("Enter time (s): "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            answer = work / time
            print(f"Power = {answer:.2f} W")

    elif choice == "4":
        frequency = float(input("Enter frequency (Hz): "))
        wavelength = float(input("Enter wavelength (m): "))
        answer = frequency * wavelength
        print(f"Wave Speed = {answer:.2f} m/s")

    elif choice == "5":
        force = float(input("Enter force (N): "))
        area = float(input("Enter area (m^2): "))
        if area == 0:
            print("Area cannot be zero.")
        else:
            answer = force / area
            print(f"Pressure = {answer:.2f} Pa")

    else:
        print("Invalid choice. Please select a number from 1 to 5.")

    again = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Thank you for using the Physics Formula Solver!")
        break
