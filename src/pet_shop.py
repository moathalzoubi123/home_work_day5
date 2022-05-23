# WRITE YOUR FUNCTIONS HERE
from operator import index
from unicodedata import name


def get_pet_shop_name(pet_shop):
     return pet_shop["name"] 


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"] 


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    



def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"] 


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,breed):
    pet_list=[]
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(breed)    
    return pet_list      



def increase_pets_sold(pet_shop,amount):
    pet_shop["admin"]["pets_sold"] += amount


def find_pet_by_name(shop_pet,pet_name):
    for pet in shop_pet["pets"]:
        if pet["name"]== pet_name:
          return pet
    return None   


# def remove_pet_by_name(shop_pet,pet_name):
#     for pet in shop_pet["pets"]:
#      if pet["pets"] == pet_name:
#        shop_pet["pets"].pop(pet_name)

def remove_pet_by_name(pet_shop, pet_name):
    for index, pet in enumerate(pet_shop["pets"]):        
       if pet["name"] == pet_name:
            pet_shop["pets"].pop(index)     


def add_pet_to_stock(pet_shop,new_pet): 
     pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers,cash):
    customers["cash"] -= cash



# def get_customer_cash(customers):
#     for customer in customers[0]:
#         if customer["cash"] == 1000:
#             return customer 

# def remove_customer_cash(customer, remove_cash):
#      customer[0]["cash"] -= remove_cash 
   

def get_customer_pet_count(customers):
     return len(customers["pets"])


def add_pet_to_customer(customers,new_pet):
    customers["pets"].append(new_pet)

# def add_pet_to_customer(customers,pet):
#      return get_customer_pet_count(customers) + len(pet)





# optional 


def customer_can_afford_pet(customers,pets):
    if customers["cash"] >= pets["price"]:
     return True 
    else:
     return False



# def sell_pet_to_customer(pet_shop,pet,customer):
#     for pet in pet_shop["name"]:
#         if pet["name"] == pet:      
#            get_customer_pet_count(customer) + 1
#            get_pets_sold(pet_shop) + 1
#            get_customer_cash(customer)
#            get_total_cash(pet_shop) + pet["price"]



# def sell_pet_to_customer(pet_shop, pet, customers):
#    for pet in pet_shop["name"]:
#       if pet["name"] == pet:
#        customers["pets"].append(pet)
#        pet_shop["admin"]["pets_sold"] += 1
#        customers["cash"] - pet_shop["price"]
#        pet_shop["admin"]["total_cash"] 
#       elif:
#         return 

def sell_pet_to_customer(pet_shop, pet, customer):
     if pet != None and customer_can_afford_pet(customer, pet):
         remove_pet_by_name(pet_shop, pet["name"])
         add_pet_to_customer(customer, pet)
         remove_customer_cash(customer, pet["price"])
         add_or_remove_cash(pet_shop, pet["price"])
         increase_pets_sold(pet_shop, 1)