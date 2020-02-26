import json

import cc_classes
import cc_dat_utils

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

input_json_file = "data/rchew_cc1.json"

with open(input_json_file, "r") as reader:
    json_levels = json.load(reader)

    new_level_pack = cc_classes.CCLevelPack()

    for json_level in json_levels:
        new_level = cc_classes.CCLevel()

        new_level.level_number = json_level["level_number"]
        new_level.time = json_level["time"]
        new_level.num_chips = json_level["num_chips"]
        new_level.upper_layer = json_level["upper_layer"]
        new_level.lower_layer = json_level["lower_layer"]

        for json_field in json_level["optional_fields"]:
            field_type = json_field["field_type"]

            if field_type == "hint":
                new_hint_field = cc_classes.CCMapHintField(json_field["hint"])
                new_level.add_field(new_hint_field)
            elif field_type == "title":
                new_title_field = cc_classes.CCMapTitleField(json_field["title"])
                new_level.add_field(new_title_field)
            elif field_type == "password":
                new_password_field = cc_classes.CCEncodedPasswordField(json_field["password"])
                new_level.add_field(new_password_field)

            elif field_type == "monsters":
                monsters = []
                for json_monster in json_field["monsters"]:
                    x = json_monster["x"]
                    y = json_monster["y"]
                    new_monster_coord = cc_classes.CCCoordinate(x,y)
                    monsters.append(new_monster_coord)
                new_monster_field = cc_classes.CCMonsterMovementField(monsters)
                new_level.add_field(new_monster_field)

            elif field_type == "traps":
                traps = []
                for json_trap in json_field["traps"]:
                    # new_button_coord = cc_classes.CCCoordinate(json_trap["x_button"], json_trap["y_button"])
                    # new_trap_coord = cc_classes.CCCoordinate(json_trap["x_trap"], json_trap["y_trap"])
                    traps.append(cc_classes.CCTrapControl(json_trap["x_button"], json_trap["y_button"], json_trap["x_trap"], json_trap["y_trap"]))

                new_level.add_field(cc_classes.CCTrapControlsField(traps))

            elif field_type == "cloners":
                cloners = []
                for json_cloner in json_field["cloners"]:
                    # new_button_coord = cc_classes.CCCoordinate(json_trap["x_button"], json_trap["y_button"])
                    # new_cloner_coord = cc_classes.CCCoordinate(json_trap["x_cloner"], json_trap["y_cloner"])
                    cloners.append(cc_classes.CCCloningMachineControl(json_cloner["x_button"], json_cloner["y_button"], json_cloner["x_cloner"], json_cloner["y_cloner"]))

                new_level.add_field(cc_classes.CCCloningMachineControlsField(cloners))

        new_level_pack.add_level(new_level)

    cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/rchew_cc1.dat")
    level_pack_from_dat = cc_dat_utils.make_cc_level_pack_from_dat("data/rchew_cc1.dat")
    print(level_pack_from_dat)
