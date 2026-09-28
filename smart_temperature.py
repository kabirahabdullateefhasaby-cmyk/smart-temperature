def smart_temperature(value):
    try:
        celsius = float(value)
    except (ValueError, TypeError):
        return "Invalid temperature"
    
    fahrenheit = celsius * 9/5 + 32
    
    if celsius <= 0:
        status = "freezing"
    elif celsius < 20:
        status = "cold"
    elif celsius <= 30:
        status = "warm"
    else:
        status = "hot"
        
    return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: {status}"


print(smart_temperature(25))
