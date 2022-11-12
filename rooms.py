
rooms= {
"room_a_1":{"desc":"You enter a small room with a door to the south and east","items":{"chest":"chest_1"}, "north":{"is_possible":False, "reason":"A wall is in the way"},"west":{"is_possible":False, "reason":"A wall is in the way"},"east":{"is_possible":True, "next_room":"room_a_2"},"south":{"is_possible":True, "next_room":"room_b_1"}},
"room_a_2":{"desc":"You are in room a_2", "items":False, "north":{"is_possible":False, "reason":"A wall is in the way"},"west":{"is_possible":True, "next_room":"room_a_1"},"east":{"is_possible":False, "reason":"A wall is in the way"},"south":{"is_possible":True, "next_room":"room_b_2"}},
"room_b_1":{"desc":"You are in room b_1","items":{"chest":"chest_2"}, "north":{"is_possible":True,  "next_room":"room_a_1"},"west":{"is_possible":False, "reason":"wall"},"east":{"is_possible":True, "next_room":"room_b_2"},"south":{"is_possible":False, "reason":"Wall"}},
"room_b_2":{"desc":"You are in room b_2","items":False, "north":{"is_possible":True,  "next_room":"room_a_2"},"west":{"is_possible":True, "next_room":"room_b_1"},"east":{"is_possible":False, "reason":"A wall is in the way"},"south":{"is_possible":False, "reason":"Wall"}}
}

