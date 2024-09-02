valeur = -1  # Initialize as an integer to start the loop

# Loop until the user enters a positive number
while valeur < 0:
    valeur_str = input("Entre une température en Celsius (doit être positive) : ")
    
    # Try to convert the input to a float
    try:
        valeur = float(valeur_str)  # Convert string to float
        if valeur < 0:
            print("La température doit être un nombre positif. Essayez encore.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        valeur = -1  # Reset valeur to ensure the loop repeats

# Convert Celsius to Fahrenheit
Farenheit = valeur * (9/5) + 32

# Print the result
print(f"{valeur}°C en Farenheit est : {Farenheit}°F")
