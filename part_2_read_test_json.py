import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###
    for game_data in json_data:
        print(game_data)

        platform_data = game_data["platform"]
        platform = test_data.Platform(platform_data["name"], platform_data["launch_year"])

        game = test_data.Game(game_data["title"], platform, game_data["year"])
        game_library.add_game(game)

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###

with open(input_json_file, "r") as reader:
    test_data_json = json.load(reader)

print(test_data_json)
lib = make_game_library_from_json (test_data_json)
print(lib)