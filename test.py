user_profiles = {
    "Albert": {"name": "Albert Smith", "email": "albert@example.com", "age": 20},
    "Troy": {"name": "Troy Jones", "email": "troy@example.com", "age": 25},
}

print("Username: ")
for names in user_profiles.keys():
    print(names)

print("\nEmail Address: ")
for email in user_profiles.values():
    print(email["email"])

print("User_details: ")
for key, value in user_profiles.items():
    print(key,":", value)