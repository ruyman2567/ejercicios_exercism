"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    ingredients_set = set(dish_ingredients)
    return(dish_name,ingredients_set)


def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return(drink_name + ' Mocktail')
    else:
        return drink_name + ' Cocktail'

def categorize_dish(dish_name, dish_ingredients):
    categorias =(
        (VEGAN,'VEGAN'),
        (VEGETARIAN,'VEGETARIAN'),
        (PALEO,'PALEO'),
        (KETO,'KETO'),
        (OMNIVORE, 'OMNIVORE')
    )
    
    for cate in categorias:
        if dish_ingredients.issubset(cate[0]):
            return dish_name + ': ' + cate[1]

def tag_special_ingredients(dish):
    ingredients = set(dish[1]) & SPECIAL_INGREDIENTS
    return (dish[0],ingredients)

def compile_ingredients(dishes):
    master_list = set()
    for dish in dishes:
        master_list = master_list | dish
    return master_list

def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))
  

def singleton_ingredients(dishes, intersection):
    all_ingredients = set()          
    for ingredients in dishes:
        all_ingredients = all_ingredients ^ ingredients
    return all_ingredients - intersection
