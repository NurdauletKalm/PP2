def fahrenheit_to_celcius(fahrenheit):
    celcius = (5 / 9) * (fahrenheit - 32)
    print(celcius, "C")
celcius = int(input("Фаренгейт бойынша қандай температура?: "))
fahrenheit_to_celcius(celcius)