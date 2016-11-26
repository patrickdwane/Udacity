from random import randint

#Welcome to this US Presidential themed Fill in the Blanks!
#GAME INSTRUCTIONS: US Presidential themed fill in the blanks, based on candidate tweets.
#You will need to summon all your geo plotitical, dimplomatic skills to get inside the mindset of
#a US presidential candidate. This is a 3 player game, players input their names to get started.
#A virtual coin toss to decide who goes first. There will be multiple choice answers, the player can
#pick what they think is true. One point per correct answer, First to 3 wins!! 

# Create the statements to fill in the blanks
statements = ["This election is a _______________. We are not a democracy",
              "I have never seen _______________ drinking Diet Coke.",
              "Sorry losers and haters, but my _______________ is one of the highest -and you all know it! Please don't feel so stupid or insecure,it's not your fault",
              "MAKE _______________ GREAT AGAIN!",
              "If Obama resigns from office NOW, thereby doing a great service to the country I will give him free lifetime _______________!",
              "I just realized that if you listen to _______________ for more than ten minutes straight, you develop a massive headache. She has zero chance!",
              "This very expensive GLOBAL WARMING _______________ has got to stop.",
              "@michellemalkin You were born _______________!",
              "The concept of global warming was created by and for the _______________ in order to make U.S. manufacturing non-competitive."]

# Create the possible responses for the blanks in the statements list
responses = [["delight", "total sham and a travesty", "wonderful story of political intrigue", "bummer"],
             ["a thin person", "Melania", "Hillary Clinton", "a doctor"],
             ["Twitter following", "I.Q.", "colesterol", "libedo"],
             ["ME", "CHINA", "MEXICO", "AMERICA"],
             ["golf at any one of my courses", "on demand use of my jet", "access to a suite at Trump Tower", "coaching on Twitter etiquite"],
             ["Carly Fiorina", "Melania", "Hillary Clinton", "Sarah Palin"],
             ["bullshit", "catastrophe", "problem caused by humanity", "TV show"],
             ["free", "slippy", "stupid", "ready"],
             ["the Japanese", "the Chinese", "the Mexicans", "the Europeans"]]

# Set the correct answers
answers = ["B", "A", "B", "D", "A", "A", "A", "C", "B"]

# Set the correct answers for printing
answers_toprint = ["total sham and a travesty", "a thin person", "I.Q.", "AMERICA", "golf at any one of my courses", "Carly Fiorina", "bullshit", "stupid", "the Chinese"]

# Create a record of previous questions
previous_questions = []


# Create a procedure to start another game, which loops back to the start of the game if the player selects Y, otherwise it will exit the game 
def play_again():
      while True:
            play_again = raw_input("Play again? [y/n] ")
            if 'y' in play_again.lower():
           	  return play_president()
            elif 'n' in play_again.lower():
           	  return False
            else:
                 print("Huh?")
                 
# Create the logic to power the game. Assigns the current player, keeps track of score, and switches between players
def game_engine(first_player, second_player, first_player_score, second_player_score, third_player, third_player_score):
      
      current_player = first_player #Assigns first player to the current player variable
      winner_threshold = 2 #Sets the threshold for a winners score
      
      
      #the while loop determines of a player score has passed the threshold..
      while(first_player_score <= winner_threshold and second_player_score <= winner_threshold and third_player_score <= winner_threshold): 
            choice = randint(0, len(statements)-1) # creates the game environment for Player 1, first randomly select a blank to fill in
            print statements[choice] #print the random choice selected
            print("\nYour choices are A, B, C or D") #print the multiple choices for the blanks associated with that statement
            print("\nA. "+ responses[choice][0])
            print("\nB. "+ responses[choice][1])
            print("\nC. "+ responses[choice][2])
            print("\nD. "+ responses[choice][3])
            current_player_choice = raw_input(current_player + ", Enter A, B, C or D: ") #Get the input for the user
            if current_player_choice == answers[choice]: #Check if it's the right answer for that statement
                  first_player_score = first_player_score + 1 #If it's correct add 1 point to that players score
                  current_player = second_player  #Switch players
                  if(first_player_score > winner_threshold): # Check to see if there's a winner i.e. score = 3
                        print("\nWe have a Winner!") #If there is a winner, confirm and exit the game
                        print("\n" + first_player + " WINS! ")
                        break
                  else:
                        print("\nCorrect. The answer is: "+ statements[choice].replace('_______________', answers_toprint[choice])) #Confirm the correct statement and switch players
                        print("\n "+ current_player + ", It's your turn")
            else:
                  current_player = second_player
                  print("\nIncorrect. "+ current_player + ", It's your turn") #Confirm an incorrect choice and switch players

            choice = randint(0, len(statements)-1) #creates the game environment for Player 2, similar format as player 1
            print statements[choice]
            print("\nYour choices are A, B, C or D")
            print("\nA. "+ responses[choice][0])
            print("\nB. "+ responses[choice][1])
            print("\nC. "+ responses[choice][2])
            print("\nD. "+ responses[choice][3])
            current_player_choice = raw_input(current_player + ", Enter A, B, C or D: ")
            if current_player_choice == answers[choice]:
                  second_player_score = second_player_score + 1
                  current_player = third_player
                  if(second_player_score > winner_threshold):
                        print("\nWe have a Winner!")
                        print("\n" + second_player + " WINS! ")
                        break
                  else:
                        print("\nCorrect. The answer is: "+ statements[choice].replace('_______________', answers_toprint[choice])) #Confirm the correct statement and switch players
                        print("\n "+ current_player + ", It's your turn")
            else:
                  current_player = third_player
                  print("\nIncorrect. "+ current_player + ", It's your turn")
                  
            choice = randint(0, len(statements)-1) #creates the game environment for Player 3, similar format as player 1
            print statements[choice]
            print("\nYour choices are A, B, C or D")
            print("\nA. "+ responses[choice][0])
            print("\nB. "+ responses[choice][1])
            print("\nC. "+ responses[choice][2])
            print("\nD. "+ responses[choice][3])
            current_player_choice = raw_input(current_player + ", Enter A, B, C or D: ")
            if current_player_choice == answers[choice]:
                  third_player_score = third_player_score + 1
                  current_player = first_player
                  if(third_player_score > winner_threshold):
                        print("\nWe have a Winner!")
                        print("\n" + third_player + " WINS! ")
                        break
                  else:
                        print("\nCorrect. The answer is: "+ statements[choice].replace('_______________', answers_toprint[choice])) #Confirm the correct statement and switch players
                        print("\n "+ current_player + ", It's your turn")
            else:
                  current_player = first_player
                  print("\nIncorrect. "+ current_player + ", It's your turn")

     
#Create the play_president function to run the game - delivers game instructions, takes player names, decides who goes first, calls the game logic defined above 
def play_president():
   # Print the basic instructions for the game
      print("\n\n\n\nWelcome to this US Presidential themed Fill in the Blanks!") 
      print("\nGAME INSTRUCTIONS: US Presidential themed fill in the blanks, based on candidate tweets.")
      print("You will need to summon all your geo plotitical, dimplomatic skills to get inside the mindset of")
      print("a US presidential candidate. This is a 3 player game, players input their names to get started.")
      print("A virtual coin toss to decide who goes first. There will be multiple choice answers, pick what you think is true.")   
      print("\nFirst to 3 wins!!") 
  
    # We take the user input and create the Players and inform them of the virtual coin toss to start the game
      Player1 = raw_input("\nPlayer 1, What is your name? ")
      print("\nNice to meet you " + Player1 + "!")

      Player2 = raw_input("\nPlayer 2, What is your name? ")
      print("\nNice to meet you " + Player2 + "!")
      
      Player3 = raw_input("\nPlayer 3, What is your name? ")
      print("\nNice to meet you " + Player3 + "!")
      
      print("\nLets play Presidential themed fill in the blanks!\n")
      print("\nWe'll decide if " + Player1 + " or " + Player2 + " or " + Player3 + " goes first, via a 2 round virtual coin toss\n") 

      # Initialize Player 1, 2, 3
      first_player = Player1
      second_player = Player2
      third_player = Player3
      
      # Get the users to participate in coin toss to see who goes first. It's a 2 round coin toss, Winner from Round 1 goes into
      # Round 2..the winners of the rounds dictate who goes first, second and third.

      player1_choice = raw_input("\nRound 1: " + Player1 + " Heads or Tails [h/t] ")
      result = randint(1, 2)
      if 'h' in player1_choice.lower() and result == 1:
            print("\n" + Player1 + " goes into Round 2 ")
            first_player = Player1
            second_player = Player2
      elif 't' in player1_choice.lower() and result == 2:
            print("\n" + Player1 + " goes into Round 2!")
            first_player = Player1
            second_player = Player2
      else:
            print("\n" + Player2 + " goes into Round 2!")
            first_player = Player2
            second_player = Player1
            
      player3_choice = raw_input("\nRound 2: " + Player3 + " Heads or Tails [h/t] ")
      result = randint(1, 2)
      if 'h' in player3_choice.lower() and result == 1:
            print("\n" + Player3 + " goes first! Here's your first question ")
            third_player = second_player
            second_player = first_player
            first_player = Player3
      elif 't' in player3_choice.lower() and result == 2:
            print("\n" + Player3 + " goes first! Here's your first question ")
            third_player = second_player
            second_player = first_player
            first_player = Player3
      else:
            print("\n" + first_player + " goes first! Here's your first question ")
            third_player = Player3
      
       # Set the socres to 0
      first_player_score = 0
      second_player_score = 0
      third_player_score = 0

      # Call the game engine function to start the fill in the blanks quiz and validate correct answers
      game_engine(first_player, second_player, first_player_score, second_player_score, third_player, third_player_score)

#Call the play president function to start the game
play_president()

#Call the play again function to see if players want to play again
play_again()
