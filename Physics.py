print("================================")
print("     PHYSICS FORMULA SOLVER")
print("================================")

print("1. Speed = Distance / Time")
print("2. Force = Mass × Acceleration")
print("3. Density = Mass / Volume")
print("4. Work Done = Force × Distance")
print("5. Pressure = Force / Area")

choice = int(input("\nChoose a formula (1-5): "))

if choice == 1:
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))

    speed = distance / time
    print("Speed =", speed, "m/s")

elif choice == 2:
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))

    force = mass * acceleration
    print("Force =", force, "N")

elif choice == 3:
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))

    density = mass / volume
    print("Density =", density, "kg/m³")

elif choice == 4:
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))

    work = force * distance
    print("Work Done =", work, "J")

elif choice == 5:
    force = float(input("Enter force (N): "))
    area = float(input("Enter area (m²): "))

    pressure = force / area
    print("Pressure =", pressure, "Pa")

else:
    print("Invalid choice! Please select 1-5.")