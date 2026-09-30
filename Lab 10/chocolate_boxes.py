# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 6 Activity 2 Team
# # Date: 28 OCT 2025

import random
from itertools import combinations

def is_valid_box(truffle_ids, chocolates):
    seen_profiles = set()
    fillings = set()
    toppings = set()
    shapes = set()
    dark_count = 0

    for tid in truffle_ids:
        choco_type, shape, filling, topping = chocolates[tid]
        profile = (choco_type, shape, filling, topping)
        if profile in seen_profiles:
            return False
        seen_profiles.add(profile)
        fillings.add(filling)
        toppings.add(topping)
        shapes.add(shape)
        if choco_type == "dark":
            dark_count += 1

    if "caramel" in fillings and "vanilla" in fillings:
        return False
    if "sprinkles" in toppings and "nuts" in toppings:
        return False
    if "rectangle" in shapes and "square" in shapes:
        return False
    if dark_count not in [0, 2, 3]:
        return False

    return True

def make_boxes(chocolates):
    truffle_ids = list(chocolates.keys())
    random.shuffle(truffle_ids)

    boxes = []
    used = set()

    def find_valid_box(available_ids):
        for combo in combinations(available_ids, 4):
            if is_valid_box(combo, chocolates):
                return list(combo)
        return None

    while len(boxes) < 25:
        available_ids = [tid for tid in truffle_ids if tid not in used]
        box = find_valid_box(available_ids)
        if box:
            boxes.append(box)
            used.update(box)
        else:
            # Restart if we can't find a valid box with remaining truffles
            random.shuffle(truffle_ids)
            boxes = []
            used = set()

    return boxes