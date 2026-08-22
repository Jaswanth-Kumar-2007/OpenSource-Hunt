name = "Too kaise hai aap sabhi"
city = "MP"
country = "India"

print("Name:", city)
print("City:", name)
print("Country:", name)

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

print("First character:", name[0])  # Off-by-one: should be name[0]
print("Last character:", name[-1])  # Off-by-one: should be name[-1]

print("Name length:", len(city))

print("Starts with T:", name.startswith("B"))
print("Ends with n:", name.endswith("a"))
