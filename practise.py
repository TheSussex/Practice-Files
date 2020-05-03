transport_means = ['motorcycle', 'car', 'danfo', 'uber']
transport_means.sort()
print(transport_means)
car_type = ['Toyota', 'Benz', 'Honda']
car_type[1] = 'Bugatti'
message = "I go to work in a " + car_type[1] + " " + transport_means[1].title() + ".\n"
print(message)

dream_destination = ['Kenya', 'Bali', 'Abuja', 'Cuba', 'Rwanda']
dream_destination.sort(reverse=True)
for destination in dream_destination:
    print(destination.upper() + " is a nice country to visit")
    print("I can't wait to visit and see cool places in " + destination + ".\n\n")

print(dream_destination)

nouns = ['fought', 'honest', 'redeemed', 'kunle']

for noun in nouns:
    if noun == 'kunle':
        print(noun.upper())
    else:
        print(noun.title())


age = 21
if age == 21:
    print("You are a young girl")
if age != 21:
    print("Na old woman you be!")
else:
    print("Better go and get married")


hrs = input("enter hours: ")
rate = input("enter rate: ")
gross = float(hrs) * float(rate)
print("pay:", gross)

