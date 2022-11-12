items={
    "apple":{"desc":"A small red apple. Looks edible","type":"food","on_use":"heal", "amount":5},
    "key":{"desc":"A rusty key","type":"tool","on_use":"unlock"},
    "sword":{"desc":"A rusty sword","type":"weapon", "damage":5}
}
room_items={"chest_1":{"name":"Chest","desc": "A small chest with no lock", "is_locked":False, "contents":{"apple", "key"}},
        "chest_2":{"name":"Chest","desc": "A large wooden chest with a rudementary lock","is_locked":True, "contents":{"sword"}}}