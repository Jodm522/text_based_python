import rooms
import items
import player
class Room:
    def __init__(self,room_info):
        self.description = room_info["desc"]
        self.north = room_info["north"]
        self.south = room_info["south"]
        self.east = room_info["east"]
        self.west = room_info["west"]
        self.items = room_info["items"]

current_room = False

def change_rooms(new_room):
    print(new_room)
    current_room= Room(rooms.rooms[new_room])
    player_turn(current_room)

def interact(item, current_room):
    player_action = input("What would you like to do with " + item["name"]+ "? > " )
    
    if (item["name"] == "Chest"):
            if(player_action == "open"):
                if(item["is_locked"]):
                    print("It's locked")
                elif(item["contents"]== "none"):
                    print("It's empty")
                else:
                    print("You find:")
                    for contents in item["contents"]:
                        print(contents) 
                        player.player_items[contents]= items.items[contents]
                    print("You put what you found in your bag")
                    player_turn(current_room)
            if(player_action == "unlock"):
                if(not item["is_locked"]):
                    print("It's not locked")
                elif(not "key" in player.player_items):
                    print("You don't have anything to unlock it with")
                else:
                    print("You use a key to unlock the chest")
                    player.player_items["key"] = False
                    print("You find:")
                    for contents in item["contents"]:
                        print(contents) 
                        player.player_items[contents]= items.items[contents]
                    print("You put what you found in your bag")
                    player_turn(current_room)
                
            else:       
                print("I can't "+ player_action +" the Chest")

    
    
def investigate(current_room):
    is_investigating = True
    if not current_room.items:
        print("There's nothing to look at")
        player_turn(current_room)
    else:
        while is_investigating:
            print("What would you like to investigate?")
            for item in current_room.items:
                print(item)
            player_action = input("> ")
            if(player_action == "q"):
                is_investigating = False
                player_turn(current_room)
            if(player_action in current_room.items):
                print("You see: " + items.room_items[current_room.items[player_action]]["desc"])
                interact(items.room_items[current_room.items[player_action]], current_room)
            else: print("I don't know that") 

def player_turn(current_room):
    print(current_room.description)
    player_action = input("What would you like to do? > ")
    if(player_action == "n"):
        if(current_room.north["is_possible"]):
            change_rooms(current_room.north["next_room"])
        else:
            print("You cannot go that way " + current_room.north["reason"])
            player_turn(current_room)
        
    if(player_action == "s"):
        if(current_room.south["is_possible"]):
            change_rooms(current_room.south["next_room"])
        else:
            print("You cannot go that way " + current_room.south["reason"])
            player_turn(current_room)
    if(player_action == "e"):
        if(current_room.east["is_possible"]):
            change_rooms(current_room.east["next_room"])
        else:
            print("You cannot go that way " + current_room.east["reason"])
            player_turn(current_room)
    if(player_action == "w"):
        if(current_room.west["is_possible"]):
            change_rooms(current_room.west["next_room"])
        else:
            print("You cannot go that way. " + current_room.west["reason"])
            player_turn(current_room)
    if (player_action == "investigate"):
        investigate(current_room)
    else:
        print("I don't know " + player_action)
        player_turn(current_room)
    if(player_action == "q"):
        print("Goodbye!")












def start_game(current_room):
    current_room = Room(rooms.rooms['room_a_1'])
    player_turn(current_room)

start_game(current_room)
