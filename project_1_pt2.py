'''
Brielle Foster
CSC110
Project -1
This program is creating a story based on the users input.
'''

def create_story(person_one, person_two, pet_name, animal, place, \
                 adjective, verb, adverb, ):
    '''
    This function returns the story of the vacation.
    Args:
        All arguments are strings given by the user to include in the story.
    Returns:
        The story which is a string.
    '''
    story = ""
    # This story variable is being used to create the vacation story.
    story += person_one + " and " + person_two + " were best friends.\n" + \
        "One day " + person_one + " and " + person_two + \
            " decided to go on a\nvacation to " + place + \
                ". However, they didn\'t know\nwhat to do with their " + \
                    adjective + " pet " + animal + " named " + pet_name + \
                        ".\n" + pet_name + " had been causing problems, " + \
                            "due to constant " + verb + "ing.\n" + \
                                person_one + " found a sitter for " + \
                                    "their pet, and " + adverb + \
                    " went on the trip."
    return story
    
def main():
    story = create_story("Joe", "Lily", "Poncho", "polar bear", "Madagascar", \
                         "Ridiculous", "plank", "spastically")
    print(story)
main()