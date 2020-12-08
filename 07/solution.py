import re

luggage_rules_custom = {
    "light red bags": [["1", "bright white bag"], ["2", "muted yellow bags"]],
    "dark orange bags": [["3", "bright white bags"], ["4", "muted yellow bags"]],
    "bright white bags": [["1", "shiny gold bag"]],
    "muted yellow bags": [["2", "shiny gold bags"], ["9", "faded blue bags"]],
    "shiny gold bags": [["1", "dark olive bag"], ["2", "vibrant plum bags"]],
    "dark olive bags": [["3", "faded blue bags"], ["4", "dotted black bags"]],
    "vibrant plum bags": [["5", "faded blue bags"], ["6", "dotted black bags"]],
    "faded blue bags": [[]],
    "dotted black bags": [[]]
}

# Find the bags that directly contain X...Add those bags to a list...Increase Bag Counter
# Loop through list and find the bags that contain the bags in the list...


def determine_number_of_bags(luggage_rules):

    my_bag = "shiny gold"
    matches = []

    for k, v in luggage_rules.items():
        selected_bag = k
        for entry in v:
            if entry:
                num = entry[0]
                bag = entry[1]

                if my_bag in bag:
                    matches.append(selected_bag[:-4].strip())

    for big_bag in matches:
        for k, v in luggage_rules.items():
            selected_bag = k
            for entry in v:
                if entry:
                    num = entry[0]
                    bag = entry[1]
                    if big_bag in bag:

                        matches.append(selected_bag[:-4].strip())

    print(len(set(matches)))


def load_bags():
    bags = {}

    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            first_bag_regex = re.compile(r'^(.*?)bags')
            first_bag = first_bag_regex.search(line).group()
            bags[first_bag] = []


            bag_contains_regex = re.compile(r'(\d .*?)bags*\b')
            list_of_bags = bag_contains_regex.findall(line)

            for bag in list_of_bags:
                if bag:
                    num = bag[0]
                    bag_name = bag[2:].strip()
                    bags[first_bag].append([num, bag_name])

    return bags



def determine_number_of_bags_part_2(luggage_rules):
    my_bag = "shiny gold bags"
    matches = []
    num_of_bags = 1

    first_bag = luggage_rules.get(my_bag)
    for entry in first_bag:
        num_of_b = entry[0]
        b = entry[1]
        potential_bags = luggage_rules.get(b)
        # while potential_bags:
        #     for bag_2 in potential_bags:
        #         x = "test"
        #         continue
        #
        #

    # for k, v in luggage_rules.items():
    #     selected_bag = k
    #     for entry in v:
    #         if entry:
    #             num = entry[0]
    #             bag = entry[1]
    #
    #             if my_bag in bag:
    #                 matches.append(selected_bag[:-4].strip())
    #                 num_of_bags += 1
    #
    # print(matches)
    # print(luggage_rules)
    #
    # for big_bag in matches:
    #     for k, v in luggage_rules.items():
    #         selected_bag = k
    #         for entry in v:
    #             if entry:
    #                 num = entry[0]
    #                 bag = entry[1]
    #                 if big_bag in bag:
    #
    #                     matches.append(selected_bag[:-4].strip())
    #
    # print(matches)




luggage = load_bags()
import json
# print(json.dumps(luggage, indent=4))

# determine_number_of_bags(luggage)
determine_number_of_bags_part_2(luggage_rules_custom)