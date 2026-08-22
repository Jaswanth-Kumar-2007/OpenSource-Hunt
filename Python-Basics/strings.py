name = "Too kaise hai aap sabhi"
city = "MP"
country = "India"

print("Name:", name)
print("City:", city)
print("Country:", country)

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

print("First character:", name[0])  # Off-by-one: should be name[0]
print("Last character:", name[-1])  # Off-by-one: should be name[-1]

print("Name length:", len(name))

print("Starts with T:", name.startswith("T"))
print("Ends with n:", name.endswith("n"))
