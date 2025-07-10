import sys

def clase_espectral(temp):
    if 30000 <= temp <= 60000:
        return "O"
    elif 10000 <= temp < 30000:
        return "B"
    elif 7500 <= temp < 10000:
        return "A"
    elif 6000 <= temp < 7500:
        return "F"
    elif 5000 <= temp < 6000:
        return "G"
    elif 3500 <= temp < 5000:
        return "K"
    elif 2000 <= temp < 3500:
        return "M"
    else:
        return None

def main():
    if len(sys.argv) != 2:
        print("Correct use: python spectral.py <temperatura>")
        return
    
    try:
        temperature = float(sys.argv[1])
        SC = clase_espectral(temperature)
        if SC:
            print(f"The spectral class is: {SC}")
        else:
            print("Temperature out of range for spectral classification.")
    except ValueError:
        print("The entered value is not in the correct format")

if __name__ == "__main__":
    main()
