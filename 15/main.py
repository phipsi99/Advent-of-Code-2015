import itertools

import tqdm

# Function to read ingredient data and set up the optimization problem
def calculate_properties(ingredient_amounts, ingredients):
    # Calculate the properties for the given amounts of each ingredient
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for i, ingredient in enumerate(ingredients):
        capacity += ingredient_amounts[i] * ingredients[ingredient]["capacity"]
        durability += ingredient_amounts[i] * ingredients[ingredient]["durability"]
        flavor += ingredient_amounts[i] * ingredients[ingredient]["flavor"]
        texture += ingredient_amounts[i] * ingredients[ingredient]["texture"]
        calories += ingredient_amounts[i] * ingredients[ingredient]["calories"]
    return capacity, durability, flavor, texture, calories

# Objective function (we want to maximize the score, so minimize the negative of the score)
def objective(ingredient_amounts, ingredients):
    capacity, durability, flavor, texture, calories = calculate_properties(ingredient_amounts, ingredients)
    
    # If any property is negative, the score becomes 0
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        return 0, calories  # Return a large number to indicate an invalid solution
    
    # Return the negative of the product of properties (for minimization)
    return capacity * durability * flavor * texture, calories

ingredients_case2 = {
    "Sugar": {"capacity": 3, "durability": 0, "flavor": 0, "texture": -3, "calories": 2},
    "Sprinkles": {"capacity": -3, "durability": 3, "flavor": 0, "texture": 0, "calories": 9},
    "Candy": {"capacity": -1, "durability": 0, "flavor": 4, "texture": 0, "calories": 1},
    "Chocolate": {"capacity": 0, "durability": 0, "flavor": -2, "texture": 2, "calories": 8}
}


# Example: Generate all combinations where the sum of 4 variables equals 100
total_sum = 100
num_variables = 4

combinations =  [combo for combo in itertools.product(range(total_sum + 1), repeat=num_variables) if sum(combo) == total_sum]


max_score = 0

# Loop through all possible combinations of teaspoons
for comb  in tqdm.tqdm(combinations):  # 0 to 100 teaspoons for Butterscotch
    score, calories = objective(comb, ingredients_case2)
    if score > max_score and calories == 500:
        max_score = score
        best_combination = comb

print(f"Best combination: {best_combination} with max score {max_score}")
