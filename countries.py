countries = ["USA", "France", "Japan", "China", "UK"]

print("Welcome to stupid add settlement super yay game (S.A.S.S.Y)")
print("Choose a country from the following list: " + str(countries))

country = input()

if country != countries[0] or country != countries[1] or country != countries[2] or country != countries[3] or country != countries[4]:
    print("AY it needa b one from da list!!!")
else:
    print("Nice.")