'''
Brielle Foster
CSC110
Project -1
This program is creating a story based on the users input.
'''

def create_story(person_one, street_name, person_two, \
                 object_name, vehicle, adjective):
    '''
    This function returns the story of the mad lib
    Args:
        All arguments are strings given by the user to include in the story.
    Returns: 
        The story which is a string.
    '''
    story = ""
    # This story variable is being used to create the madlib story.
    story += person_one + " decided to move from their apartment " + \
"on 5th\nto a condo on " + street_name + \
            ". They called their friend " + person_two + "\nfor help. " + \
                "However, they could not fit " + object_name + \
                    " into\nthe moving truck, so they had to rent a " + \
                        adjective + " " + vehicle + "\nin order to move it!"
    return story

def main():

    story = create_story("Janet", "Loopdydoo Avenue", \
                         "Richard", "Christmas tree", \
                            "Horse-drawn carriage ", "Off-road")
    print(story)
main()