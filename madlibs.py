# import story function
from stories import *

# variables
story_num = 1

read_story = True

# loops through the stories
while read_story == True:

    # allows users to put in funny words
    # uses the input function to store words
    name = input("𝓱𝓲! 𝔀𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓱𝓮𝓪𝓭'𝓼 𝓶𝓪𝓭𝓵𝓲𝓫𝓼!\ntype in a name, any name:")

    # adjectives
    print('\ntype 3 adjectives!')
    adj1 = input('type in an adjective:')
    adj2 = input('type in another adjective:')
    adj3 = input('type in your last adjective:')

    # nouns
    print('\nnow for your nouns!')
    noun1 = input('type in a noun: ')
    noun2 = input('type in another noun: ')
    noun3 = input('type in one last noun: ')

    # story is chosen with if statements
    if story_num == 1:
        story_1(name, adj1, adj2, adj3, noun1, noun2, noun3)

    elif story_num == 2:
        story_2(name, adj1, adj2, adj3, noun1, noun2, noun3)

    elif story_num == 3:
        story_3(name, adj1, adj2, adj3, noun1, noun2, noun3)
        story_num = 0

    # increases the story counter
    story_num += 1

    # ask the player if they want to quit
    stop_reading = input('\nyou liked it? want to read another?\ntype "quit", and press enter if you want to stop reading. otherwise if you want to make and read more stories, tell me a funny joke!')

    if stop_reading == 'quit':
        print('\n𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙛𝙞𝙣𝙞𝙨𝙝𝙚𝙙 𝙧𝙚𝙖𝙙𝙞𝙣𝙜!')
        read_story = False
