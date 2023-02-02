### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

# Note that we are only looking for errors here.

# **Not** any issues with, i.e.: 
# Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

# These aren't errors but rather standards that vary from developer to developer. 

# Only comment on errors that would stop the tests running.

class CardGame:

#The comparison operator here should be a double equals sign, not a single.
#There should be a semi-colon after 'else'.
    def check_for_ace(self, card):
        if card.value = 1:
            return True
        else
            return False


#'dif' is a typo and should be written as 'def'.
#There should be a comma between 'card1' and 'card2'.
#Everything from the if statement down should be indented by one.
# The first return statement should say 'return card1'.
    dif highest_card(self, card1 card2):
    if card1.value > card2.value:
        return card
    else:
        return card2


# The entire function needs to be indented.
#'total' is a variable that has not been assigned any value - it should be declared as 'total = 0'.
#The return statement should not be indented - as it is, the function will return a value for 'total' after the first iteration of the for loop and then stop.
#There should be a space at the end of the returned string so that the full sentence reads properly when the total is returned. As it is, it will be stuck on to the end of the word 'of'.
# Only strings can be concatenated, so the end of the final line needs to be changed to '+ str(total)'
def cards_total(self, cards):
    total
    for card in cards:
    total += card.value
    return "You have a total of" + total
