def main():
    mass = int(input("Mass in kg: "))
    energy = convert(mass)
    print(energy)

def convert(m):
    c = 300000000
    return m*c**2

main()
