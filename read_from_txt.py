import pygame
import random
def guess_countries():
# Initialize an empty dictionary
    used_dict =[
        
    ]
    data_dict = {
        
    }

# Open the text file and read it line by line
    file_path = 'countries_europe.txt'

    with open(file_path, mode='r') as file:
        for line in file:
        # Split the line into key and value based on the delimiter (e.g., colon ':')
            name, facts = line.strip().split(':')
        
        # Split the facts string into a list of individual facts
            facts_list = [fact.strip() for fact in facts.split(',')]
        
        # Add the key-value pair to the dictioncary
            data_dict[name.strip()] = facts_list
    
   
    random_key, random_value = random.choice(list(data_dict.items()))
    while (random_key not in used_dict):
        #random_key, random_value = random.choice(list(data_dict.items()))
        break
    used_dict.append(random_key)
    print(random_key)
    #print(data_dict)
    #print(random_key)
    #print(random_value)
    #used_dict[random_key] = random_value
    #print(f"used dict {used_dict}")
    #random_country = random.choices(data_dict)
    #print(random_country)
    
    #print(random_key, random_value)
    """if random_key, random_value in used_dict:
        pass"""
    count = 0
    tries = len(random_value)
# Print the resulting dictionary
#print(name)
#print(f"Facts: {random_person[1]}")
    while True:
        for i in range(len(facts_list)):
            print(random_value[count])
        #print(facts_list[count])
            guess_country = input("Guess the country: ")
            if guess_country.title() == random_key:
                print("Correct")
                print(f"you have won {tries} points")
                break
            elif guess_country == "q":
                break
            else:
                count +=1
                tries -=1
                print(f"You have {tries} tries remaining.")
            if tries == 0:
                print("YOu lost.")
                print(f"The answer is {random_key}.")
    
            
guess_countries()   
    
#print(data_dict)
