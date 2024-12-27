from itertools import combinations, product

# Define the data as dictionaries
weapons = {
    "Dagger": {"Cost": 8, "Damage": 4, "Armor": 0},
    "Shortsword": {"Cost": 10, "Damage": 5, "Armor": 0},
    "Warhammer": {"Cost": 25, "Damage": 6, "Armor": 0},
    "Longsword": {"Cost": 40, "Damage": 7, "Armor": 0},
    "Greataxe": {"Cost": 74, "Damage": 8, "Armor": 0},
}

armors = {
    "Leather": {"Cost": 13, "Damage": 0, "Armor": 1},
    "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2},
    "Splintmail": {"Cost": 53, "Damage": 0, "Armor": 3},
    "Bandedmail": {"Cost": 75, "Damage": 0, "Armor": 4},
    "Platemail": {"Cost": 102, "Damage": 0, "Armor": 5},
}

rings = {
    "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0},
    "Damage +2": {"Cost": 50, "Damage": 2, "Armor": 0},
    "Damage +3": {"Cost": 100, "Damage": 3, "Armor": 0},
    "Defense +1": {"Cost": 20, "Damage": 0, "Armor": 1},
    "Defense +2": {"Cost": 40, "Damage": 0, "Armor": 2},
    "Defense +3": {"Cost": 80, "Damage": 0, "Armor": 3},
}


player = {
    "Hit Points": 100,
    "Damage": 0,
    "Armor": 0
}

def play_game(player, boss):
    while player["Hit Points"] > 0 and boss["Hit Points"] > 0:
        boss["Hit Points"] -= max(1, player["Damage"] - boss["Armor"])
        if boss["Hit Points"] <= 0:
            return True
        player["Hit Points"] -= max(1, boss["Damage"] - player["Armor"])
        if player["Hit Points"] <= 0:
            return False
    return False


def generate_combinations():
    weapon_keys = list(weapons.keys())
    armor_keys = list(armors.keys())
    ring_keys = list(rings.keys())
    
    armor_keys.append(None)
    ring_keys.append(None)
    ring_keys.append(None)
    
    # Combine 1 weapon, 1 armor, and 2 rings
    all_combinations = []
    for weapon, arm in product(weapon_keys, armor_keys):  # 1 weapon and 1 armor
        for ring_pair in combinations(ring_keys, 2):  # 2 different rings
            all_combinations.append((weapon, arm, ring_pair))
    
    return all_combinations

def do_main(debug_mode=False):

    point_sum = 0

    combs = generate_combinations()

    best_cost = float("inf")
    worst_cost = 0

    for comb in combs:
        damage = 0 
        armor = 0
        cost = 0
        damage += weapons[comb[0]]["Damage"]
        armor += weapons[comb[0]]["Armor"]
        cost += weapons[comb[0]]["Cost"]
        if comb[1] is not None:
            damage += armors[comb[1]]["Damage"]
            armor += armors[comb[1]]["Armor"]
            cost += armors[comb[1]]["Cost"]
        for ring in comb[2]:
            if ring is not None:
                damage += rings[ring]["Damage"]
                armor += rings[ring]["Armor"]
                cost += rings[ring]["Cost"]
        player = {
            "Hit Points": 100,
            "Damage": damage,
            "Armor": armor
        }
        
        boss = {
            "Hit Points": 104,
            "Damage": 8,
            "Armor": 1
        }
        if play_game(player, boss):
            best_cost = min(best_cost, cost)
        else:
            worst_cost = max(worst_cost, cost)


    print(best_cost)
    print(worst_cost)

if __name__ == '__main__':
    do_main(False)