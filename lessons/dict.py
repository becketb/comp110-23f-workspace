"""Practice with Dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")
ice_cream["vanilla"] += 2
"mint" in ice_cream
"chocolate" in ice_cream
print(len(ice_cream))
print(ice_cream["chocolate"])
print(ice_cream["vanilla"])
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")
for key in ice_cream:
    print(f"{[key]} has {ice_cream[key]}")
    