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
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    pass


def tag_special_ingredients(dish):
    ingredients = set(dish[1]) & SPECIAL_INGREDIENTS
    return (dish[0],ingredients)
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    pass


def compile_ingredients(dishes):
    master_list = set()
    for dish in dishes:
        master_list = master_list | dish
    return master_list

def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """


def singleton_ingredients(dishes, intersection):
    all_ingredients = set()          
    for ingredients in dishes:
        all_ingredients = all_ingredients ^ ingredients
    return all_ingredients - intersection
