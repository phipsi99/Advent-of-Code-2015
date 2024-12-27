from collections import deque

# Spell costs and effects
SPELLS = [
    {"cost": 53, "damage": 4, "heal": 0, "effect": None},
    {"cost": 73, "damage": 2, "heal": 2, "effect": None},
    {"cost": 113, "damage": 0, "heal": 0, "effect": {"armor": 7, "duration": 6}},
    {"cost": 173, "damage": 0, "heal": 0, "effect": {"poison": 3, "duration": 6}},
    {"cost": 229, "damage": 0, "heal": 0, "effect": {"recharge": 101, "duration": 5}},
]

def apply_effects(player, boss, active_effects):
    player["Armor"] = 0
    new_effects = {}
    for spell_id, timer in active_effects.items():
        effect = SPELLS[spell_id]["effect"]
        if effect:
            if "armor" in effect:
                player["Armor"] = effect["armor"]
            if "poison" in effect:
                boss["Hit Points"] -= effect["poison"]
            if "recharge" in effect:
                player["Mana"] += effect["recharge"]
        if timer > 1:
            new_effects[spell_id] = timer - 1
    return new_effects

def bfs_solve(player, boss):
    initial_state = {
        "player": player,
        "boss": boss,
        "active_effects": {},
        "mana_spent": 0,
        "turn": "player",
        "spell_sequence": [],
        "mana_steps": []
    }
    queue = deque([initial_state])
    min_mana_spent = float('inf')
    best_mana_steps = []

    while queue:
        state = queue.popleft()
        current_player = state["player"].copy()
        current_boss = state["boss"].copy()
        active_effects = state["active_effects"].copy()
        mana_spent = state["mana_spent"]
        turn = state["turn"]
        spell_sequence = state["spell_sequence"]
        mana_steps = state["mana_steps"]

        current_player["Hit Points"] -= 1 
        if current_player["Hit Points"] <= 0:
            continue


        # Apply effects
        active_effects = apply_effects(current_player, current_boss, active_effects)
        if current_boss["Hit Points"] <= 0:
            if mana_spent < min_mana_spent:
                min_mana_spent = mana_spent
                best_mana_steps = mana_steps
            continue

        if turn == "player":
            for spell_id, spell in enumerate(SPELLS):
                if spell_id in active_effects:
                    continue  # Skip if effect is already active

                if current_player["Mana"] < spell["cost"]:
                    continue  # Skip if not enough mana

                # Cast spell
                new_player = current_player.copy()
                new_boss = current_boss.copy()
                new_player["Mana"] -= spell["cost"]
                new_mana_spent = mana_spent + spell["cost"]

                if new_mana_spent >= min_mana_spent:
                    continue  # Prune paths that already cost too much

                new_active_effects = active_effects.copy()
                if spell["effect"]:
                    new_active_effects[spell_id] = spell["effect"]["duration"]
                new_boss["Hit Points"] -= spell["damage"]
                new_player["Hit Points"] += spell["heal"]

                if new_boss["Hit Points"] <= 0:
                    if new_mana_spent < min_mana_spent:
                        min_mana_spent = new_mana_spent
                        best_mana_steps = mana_steps + [new_mana_spent]
                    continue

                queue.append({
                    "player": new_player,
                    "boss": new_boss,
                    "active_effects": new_active_effects,
                    "mana_spent": new_mana_spent,
                    "turn": "boss",
                    "spell_sequence": spell_sequence + [spell_id],
                    "mana_steps": mana_steps + [new_mana_spent]
                })
        else:  # Boss turn
            damage = max(1, current_boss["Damage"] - current_player["Armor"])
            current_player["Hit Points"] -= damage
            if current_player["Hit Points"] > 0:
                queue.append({
                    "player": current_player,
                    "boss": current_boss,
                    "active_effects": active_effects,
                    "mana_spent": mana_spent,
                    "turn": "player",
                    "spell_sequence": spell_sequence,
                    "mana_steps": mana_steps
                })

    return min_mana_spent, best_mana_steps

def do_main():
    player = {"Hit Points": 50, "Armor": 0, "Mana": 500}
    boss = {"Hit Points": 58, "Damage": 9}
    min_mana_spent, mana_steps = bfs_solve(player, boss)
    print(f"Minimum mana spent: {min_mana_spent}")
    print(f"Mana spending steps: {mana_steps}")

if __name__ == '__main__':
    do_main()
