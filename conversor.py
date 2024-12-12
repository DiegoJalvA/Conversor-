# Conversor de dólares a euros
def conversor_dolares_a_euros():
    print("Conversor de Dólares a Euros 💵➡️💶")
    
    # Tasa fija de conversión (1 EUR = 1.0507 USD)
    tasa_cambio = 1 / 1.0507
    
    try:
        dolares = float(input("Ingresa la cantidad en dólares (USD): "))
        
        # Conversión
        euros = dolares * tasa_cambio
        print(f"{dolares:.2f} USD son aproximadamente {euros:.2f} EUR.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Ejecutar el conversor
conversor_dolares_a_euros()
