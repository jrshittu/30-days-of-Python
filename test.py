user_profiles = {
    "Albert": {"name": "Albert Smith", "email": "albert@example.com", "age": 20},
    "Troy": {"name": "Troy Jones", "email": "troy@example.com", "age": 25},
}

new_profile = {
    "John": {"name": "John Dalton", "email": "john@example.com", "age": 26}
}

user_profiles.update(new_profile)
print(user_profiles)
