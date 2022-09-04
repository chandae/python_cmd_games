import sys, time
from random import randint

def information():
    # print full hangman and game information at onset of game
    information = """
            HANGMAN! CAN YOUR BRAINS SAVE HIM? LET'S FIND OUT!
            GUESS THE WORD BELOW LETTER BY LETTER. LETTERS YOU GUESS
            RIGHT WILL BE REVEALED. The word is a country name.
            
            GAME OVER IF HANGMAN IS HANGED!
        """
    print(information)
    space = " " * 30
    layer_1 = 'O'.center(5)
    layer_2 = '/|\\'
    layer_3 = '/ \\'
    print(space, layer_1, '\n', space, layer_2, '\n', space, layer_3)

def hangman(word, name):
    # print game information
    information()

    # function prints parts of hangman if latter is wrong
    head = 'O'.center(3)
    edge = '___'
    rope = '|'.center(3)
    man_parts = [edge + '\n', rope + '\n', rope + '\n', head, '\n' + '/', '|', '\\', '\n' + '/', ' \\']
    bars = ['_ ' for i in range(len(word))]
    help = ['~~ help me!!!', '~~ ughh..', '~~ I don\'t wanna die...', '~~ I\'m dying!!']

    build = ""
    index = 0

    # display the word prompt details and input interface to the player
    print(f"Word ({len(word)}) letters: %s" % ' '.join(bars))

    while True and index < len(man_parts):

        try:
            # get input letter from the player
            letter = input("Enter letter: ").upper()
            print(end="\n")
            if letter not in word:
                # Add parts to build for printing
                print(help[randint(0,len(help) - 1)])
                build += man_parts[index]
                print(build)
                index += 1
                # show the state of the word still
                print('\n')
                print(f"Word ({len(word)}) letters: %s" % ' '.join(bars).title())
            else:
                # letter is in the word
                display(bars, word, letter)

                # check if the player has won
                if has_won(bars, word):
                    print('\n')
                    print(f"CONGRATULATIONS {name}! YOU WON AND SAVED HANGMAN FROM DYING!")
                    break
        except:
            print("Oops! Something terrible happened to your computer. Jokes! Some error occurred!")
            print("Quitting Hangman...")
            time.sleep(5)
            sys.exit()

    if not has_won(bars, word):
        print('\n')
        print(f"YOU CAN'T SAVE ANYONE {name}! The Word was {word}.")

    try:
        wants_to_continue = input("Do you want to PLAY AGAIN? Type (y/n). Press Q to quit: ").lower()
        if wants_to_continue == 'q' or wants_to_continue == 'n':
            sys.exit()
        elif wants_to_continue == 'y':
            return True
        else:
            return False
    except:
        print("Wrong command. Quitting Hangman...")
        sys.exit()

def prompt():
    # world countries stored alphabetically in a list
    countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua & Deps', 'Argentina', 'Armenia',
         'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
         'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
         'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Rep', 'Chad', 'Chile',
         'China', 'Colombia', 'Comoros', 'Congo', 'Congo {Democratic Rep}', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
         'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt',
         'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon',
         'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana',
         'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland {Republic}', 'Israel',
         'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North',
         'Korea South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
         'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
         'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
         'Montenegro', 'Morocco', 'Mozambique', 'Myanmar, {Burma}', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
         'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea',
         'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda',
         'St Kitts & Nevis', 'St Lucia', 'Saint Vincent & the Grenadines', 'Samoa', 'San Marino', 'Sao Tome & Principe',
         'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
         'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland',
         'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago',
         'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
         'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

    index = randint(0, len(countries))

    # get a random country from the countries list and return it
    return countries[index].upper()

def display(bars, word, letter):
    word = list(word)

    for i in range(len(word)):
        if word[i] == letter:
            bars[i] = letter

    # display the new state of the game
    print(f"Word ({len(word)}) letters: %s" % ' '.join(bars).title())

def has_won(bars, word):
    # convert word to list and compare with bars to find the winner
    if list(word) == bars:
        return True
    else:
        return False


if __name__ == '__main__':
    print('\n')
    print("Welcome to hangman WORLD COUNTRIES! LOADING...")
    print("By Emmanuel Chanda @2022.")
    time.sleep(3)
    name = input("Enter your name: ")
    print("The Game is Starting Now! Go Save Hangman...")

    while True:
        word = prompt()
        # invoke main function hangman
        wants_to_continue = hangman(word, name)
        if not wants_to_continue:
            break
    print("Quiting Hangman...")
    time.sleep(3)
