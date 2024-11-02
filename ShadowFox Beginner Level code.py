#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating the variable pi and storing the value 22/7 in it
pi = 22/7

# Checking the data type of the variable pi
type_of_pi = type(pi)
print(type_of_pi)


# In[2]:


for = 4
#This will raise a SyntaxError with a message indicating that you cannot assign to a reserved keyword. 


# In[3]:


# Storing the principal amount, rate of interest, and time in variables
P = 10000  # Principal amount in currency (e.g., dollars)
R = 5      # Rate of interest in percentage
T = 3      # Time in years

# Calculating the Simple Interest
Simple_Interest = (P * R * T) / 100
print(Simple_Interest)


# In[4]:


def format_value(number, format_spec):
    return format(number, format_spec)

# Calling the function with 145 and 'o'
result = format_value(145, 'o') #In this case, 'o' stands for octal format, which represents numbers using base-8.
print(result)


# In[5]:


import math

# Given values
radius = 84  # in meters
pi = 3.14  # value of π
water_per_sqm = 1.4  # liters of water per square meter

# Calculate the area of the pond
area = pi * (radius ** 2)

# Calculate the total amount of water in the pond
total_water = area * water_per_sqm

# Print the results
print(f"Area of the pond: {area} square meters")
print(f"Total amount of water in the pond (liters): {int(total_water)}")


# In[6]:


# Given values
distance = 490  # in meters
time_minutes = 7  # in minutes

# Convert time from minutes to seconds
time_seconds = time_minutes * 60

# Calculate speed in meters per second
speed = distance / time_seconds

# Print the result without any decimal point
print(int(speed))


# In[7]:


# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members in the Justice League
num_members = len(justice_league)
print(f"Number of members: {num_members}")

# 2. Add Batgirl and Nightwing to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning of the list
justice_league.remove("Wonder Woman")  # Remove Wonder Woman from the list
justice_league.insert(0, "Wonder Woman")  # Insert her at the beginning
print("After moving Wonder Woman to the beginning:", justice_league)

# 4. Move either Green Lantern or Superman in between Aquaman and Flash
# Let's choose Superman
justice_league.remove("Superman")  # Remove Superman from the list
# Insert Superman between Aquaman and Flash
aqua_index = justice_league.index("Aquaman")
justice_league.insert(aqua_index + 1, "Superman")
print("After separating Aquaman and Flash:", justice_league)

# 5. Replace the existing list with new members
new_members = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league = new_members
print("After replacing with new members:", justice_league)

# 6. Sort the Justice League alphabetically
justice_league.sort()
print("After sorting the Justice League alphabetically:", justice_league)

# Determine the new leader
new_leader = justice_league[0]
print("The new leader of the Justice League is:", new_leader)

# BONUS: Predict who the new leader will be
# The new leader is expected to be the first member in the sorted list.


# In[8]:


# Function to calculate BMI category
def bmi_category():
    # Get user input for height and weight
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine BMI category
    if bmi >= 30:
        print("Obesity")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    else:
        print("Underweight")

# Call the function
bmi_category()


# In[9]:


# List of cities per country
cities_per_country = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Function to find the country for a given city
def find_country(city):
    for country, cities in cities_per_country.items():
        if city in cities:
            return country
    return None

# Get user input for city name
city_name = input("Enter a city name: ")

# Determine the country
country = find_country(city_name)

# Print the result
if country:
    print(f"{city_name} is in {country}")
else:
    print(f"{city_name} is not found in the list.")


# In[10]:


# List of cities per country
cities_per_country = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Function to find the country for a given city
def find_country(city):
    for country, cities in cities_per_country.items():
        if city in cities:
            return country
    return None

# Get user input for two city names
first_city = input("Enter the first city: ")
second_city = input("Enter the second city: ")

# Determine the countries for both cities
country_first = find_country(first_city)
country_second = find_country(second_city)

# Check if both cities belong to the same country
if country_first and country_second:
    if country_first == country_second:
        print(f"Both cities are in {country_first}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both of the cities were not found in the list.")


# In[11]:


import random

# Number of rolls
num_rolls = 20

# Initialize counters
count_six = 0
count_one = 0
count_double_six = 0

# Previous roll tracker
previous_roll = None

# Simulate rolling the die
for _ in range(num_rolls):
    roll = random.randint(1, 6)  # Roll the die

    # Count occurrences
    if roll == 6:
        count_six += 1
        if previous_roll == 6:
            count_double_six += 1
    if roll == 1:
        count_one += 1

    # Update previous roll
    previous_roll = roll

# Print the results
print(f"Number of times rolled a 6: {count_six}")
print(f"Number of times rolled a 1: {count_one}")
print(f"Number of times rolled two 6s in a row: {count_double_six}")


# In[12]:


def jumping_jacks_workout():
    total_jumping_jacks = 100
    completed_jumping_jacks = 0
    set_size = 10

    while completed_jumping_jacks < total_jumping_jacks:
        # Perform a set of jumping jacks
        completed_jumping_jacks += set_size
        print(f"You completed {completed_jumping_jacks} jumping jacks.")

        # Check if the workout is complete
        if completed_jumping_jacks >= total_jumping_jacks:
            print("Congratulations! You completed the workout.")
            break

        # Ask if the user is tired
        tired = input("Are you tired? (yes/no): ").strip().lower()

        if tired in ["yes", "y"]:
            # Ask if they want to skip remaining sets
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip in ["yes", "y"]:
                print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
                break
        elif tired in ["no", "n"]:
            remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
            print(f"{remaining_jumping_jacks} jumping jacks are remaining.")
        else:
            print("Invalid response. Please answer with 'yes' or 'no'.")

# Run the workout simulation
jumping_jacks_workout()


# In[13]:


# List of friends' names
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Create a list of tuples with name and its length
friends_with_length = [(friend, len(friend)) for friend in friends]

# Print the list of tuples
print(friends_with_length)


# In[14]:


# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Your partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for each person
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Print total expenses
print(f"Your total expenses: ${your_total}")
print(f"Your partner's total expenses: ${partner_total}")

# Determine who spent more
if your_total > partner_total:
    print("You spent more money overall.")
elif your_total < partner_total:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount overall.")

# Find the category with the significant difference in spending
significant_difference = 0
category_with_difference = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > significant_difference:
        significant_difference = difference
        category_with_difference = category

# Print the category and the difference
print(f"The category with the significant difference is '{category_with_difference}' with a difference of ${significant_difference}.")


# In[16]:


class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, is_leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.is_leader = is_leader  # Property to indicate if the hero is a leader

    def get_info(self):
        return (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Super Power: {self.super_power}, Weapon: {self.weapon}")

    def is_leader_method(self):  # Renamed method
        return self.is_leader


# Create instances for each superhero
superheroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 45, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows"),
]

# Display information about each superhero
for hero in superheroes:
    print(hero.get_info())
    if hero.is_leader_method():  # Using the renamed method
        print(f"{hero.name} is a leader of the Avengers.")
    print()  # Add a newline for better readability


# In[18]:


class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_info(self):
        return (f"Screen Type: {self.screen_type}, Network Type: {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")

    def make_call(self, number):
        print(f"Making a call to {number}...")

    def receive_call(self, number):
        print(f"Receiving a call from {number}...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.front_camera} front camera...")

class Apple(MobilePhone):
    def __init__(self, model, front_camera="12MP", dual_sim=False):
        super().__init__("Touch Screen", "4G/5G", dual_sim, front_camera, "12MP", "4GB", "64GB")
        self.model = model

    def display_info(self):
        return f"Apple {self.model} - " + super().display_info()

class Samsung(MobilePhone):
    def __init__(self, model, front_camera="16MP", dual_sim=True):
        super().__init__("Touch Screen", "4G/5G", dual_sim, front_camera, "48MP", "6GB", "128GB")
        self.model = model

    def display_info(self):
        return f"Samsung {self.model} - " + super().display_info()

# Create instances of Apple with different properties
iphone_13 = Apple("iPhone 13", front_camera="12MP", dual_sim=False)
iphone_14 = Apple("iPhone 14", front_camera="12MP", dual_sim=True)

# Create instances of Samsung with different properties
samsung_a52 = Samsung("Galaxy A52", front_camera="32MP", dual_sim=True)
samsung_s22 = Samsung("Galaxy S22", front_camera="10MP", dual_sim=False)

# Display information about each phone and use functionalities
phones = [iphone_13, iphone_14, samsung_a52, samsung_s22]

for phone in phones:
    print(phone.display_info())
    phone.make_call("123-456-7890")
    phone.receive_call("098-765-4321")
    phone.take_a_picture()
    print()  # Add a newline for better readability


# In[ ]:




