import sys, time
from random import randint

def gameIntro():
    """ print full hangman and game information at onset of game """
    information = """
            GUESS THE WORD BELOW LETTER BY LETTER. LETTERS YOU GUESS
            RIGHT WILL BE REVEALED. The word is a country name.

            GAME OVER IF HANGMAN IS HANGED! 
            
            HINT: Some countries have these characters [&,space,the period]
        """
    print(information)
    print("       ________    ", '\n'
          "      |       |    ", '\n'
          "      |            ", '\n'
          "      |            ", '\n'
          "      |            ", '\n'
          "      |       O  ~~ please help me! :( ", '\n'
          "      |      /|\\    I don't wanna die...", '\n'
          "      |      / ) ", '\n'
          "  ____|____", '\n')

def hangman(word, name):
    """ Main game thread """
    gameIntro()

    bars = ['_ ' for _ in range(len(word))]
    index = 0
    # display the word prompt details and input interface to the player
    print(f"Word ({len(word)}) letters: %s" % ' '.join(bars))

    while True and index < 7:
        try:
            letter = input("Enter letter (Use 'exit' to QUIT): ").upper()
            if letter == 'EXIT': raise KeyboardInterrupt
            print(end="\n")
            if letter not in word:
                display_hangman(index)
                index += 1
                print()
                print(f"Word ({len(word)}) letters: %s" % ' '.join(bars).title())
            else:
                display_word(bars, word, letter)
                if has_won(bars, word):
                    print('\n')
                    print(f"CONGRATULATIONS {name}! YOU WON AND SAVED HANGMAN FROM DYING!")
                    break
        except KeyboardInterrupt:
            print("\nThanks for playing")
            print("Quitting Hangman...")
            time.sleep(3)
            sys.exit()
        except Exception as err:
            print("\nOops! Something terrible happened to your computer. Jokes! An error occurred!")
            print("Quitting Hangman...")
            time.sleep(3)
            sys.exit()

    print('\n')
    print(f"YOU COULDN'T SAVE HANGMAN {name}! The Word was {word}.")
    play_again = input("Do you want to PLAY AGAIN? Type (y/n): ").lower()
    if play_again == 'n':
        return False
    return True

def display_hangman(index):

    if index == 0:
        print("    ________     ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "____|____", '\n')

    elif index == 1:
        print("    ________     ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "____|____", '\n')

    elif index == 2:
        print("    ________     ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       O    ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "____|____", '\n')
    elif index == 3:
        print("    ________     ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       O    ~~...somebody!!", '\n'
              "    |      /|    ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "____|____", '\n')

    elif index == 4:
        print("    ________     ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       O    ~~ I'm dying...", '\n'
              "    |      /|\\  ", '\n'
              "    |            ", '\n'
              "    |            ", '\n'
              "____|____", '\n')

    elif index == 5:
        print("    ________     ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       O    ", '\n'
              "    |      /|\\  ", '\n'
              "    |      /    ~~ ...one more leg and I'm gone... ", '\n'
              "    |            ", '\n'
              "____|____", '\n')

    elif index == 6:
        print("    ________     ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       |    ", '\n'
              "    |       O    ", '\n'
              "    |      /|\\    ", '\n'
              "    |      / \\    ~~ ....ugh", '\n'
              "    |              ", '\n'
              "____|____", '\n')

def display_word(bars, word, letter):
    word = list(word)
    # replace the dashes with the correct letter
    for i in range(len(word)):
        if word[i] == letter:
            bars[i] = letter
    # display the new state of the game
    print(f"Word ({len(word)}) letters: %s" % ' '.join(bars).title())

def has_won(bars, word):
    if list(word) == bars:
        return True
    return False

def prompt():
    # World countries stored alphabetically
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

if __name__ == '__main__':
    print('\n')
    print("Welcome to hangman WORLD COUNTRIES! LOADING...")
    print("By Emmanuel Chanda @2022 (emmanuelvchanda1@gmail.com).")
    time.sleep(2)
    name = input("Enter your name: ")
    print(f"\nHello {name.upper()}! The Game is Starting Now! Go Save Hangman...")
    while True:
        word = prompt()
        # invoke main function hangman
        wants_to_continue = hangman(word, name)
        if not wants_to_continue:
            break
    print("Thanks for playing!")
    print("Quiting Hangman...")
    time.sleep(2)
