def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def exibir_menu():
    print("\nConversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")
    print("7. Sair")

def calcular():
    while True:
        exibir_menu()
        opcao = input("Escolha a opção (1/2/3/4/5/6/7): ")

        if opcao == '7':
            print("Saindo do programa...")
            break

        if opcao in ['1', '2', '3', '4', '5', '6']:
            try:
                temperatura = float(input("Digite a temperatura: "))
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
                continue

            if opcao == '1':
                print(f"{temperatura}°C = {celsius_para_fahrenheit(temperatura)}°F")
            elif opcao == '2':
                print(f"{temperatura}°C = {celsius_para_kelvin(temperatura)}K")
            elif opcao == '3':
                print(f"{temperatura}°F = {fahrenheit_para_celsius(temperatura)}°C")
            elif opcao == '4':
                print(f"{temperatura}°F = {fahrenheit_para_kelvin(temperatura)}K")
            elif opcao == '5':
                print(f"{temperatura}K = {kelvin_para_celsius(temperatura)}°C")
            elif opcao == '6':
                print(f"{temperatura}K = {kelvin_para_fahrenheit(temperatura)}°F")
        else:
            print("Opção inválida. Tente novamente.")

# Rodar o programa
if __name__ == "__main__":
    calcular()
