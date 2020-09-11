from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()



# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# TODO
return_path = []
# Going to need a set for visited rooms
# need to check initial neighbors to see if they have been explored
# travel in a direction and then have a reversed list to travel back to a room with
# unexplored areas

# directions up, right left, down
visited = set()
print(player.current_room.id)
visited.add(player.current_room.id)
while len(visited) < len(room_graph):
    if player.current_room.get_room_in_direction('n') is not None and player.current_room.get_room_in_direction('n').id not in visited:
        player.travel('n')
        traversal_path.append('n')
        return_path.append('s')
        visited.add(player.current_room.id)
        continue
    if player.current_room.get_room_in_direction('w') is not None and player.current_room.get_room_in_direction('w').id not in visited:
        player.travel('w')
        traversal_path.append('w')
        return_path.append('e')
        visited.add(player.current_room.id)
        continue
    if player.current_room.get_room_in_direction('s') is not None and player.current_room.get_room_in_direction('s').id not in visited:
        player.travel('s')
        traversal_path.append('s')
        return_path.append('n')
        visited.add(player.current_room.id)
        continue
    if player.current_room.get_room_in_direction('e') is not None and player.current_room.get_room_in_direction('e').id not in visited:
        player.travel('e')
        traversal_path.append('e')
        return_path.append('w')
        visited.add(player.current_room.id)
        continue
    return_direction = return_path.pop()
    traversal_path.append(return_direction)
    player.travel(return_direction)






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
