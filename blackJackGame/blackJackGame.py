import random
import tkinter
import time


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    # for each suits, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = './playingCards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = 'playingCards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # and add it to back of the pack
    deck.append(next_card)
    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card[0]


def calculate_score(hand):
    # calculate the total score of all cards in the list
    # only one ace can have the value 11, this will be reduce to 1 if the hand would bust
    score = 0
    ace = False
    # hand is array of integer(card_value)
    for card_value in hand:
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = calculate_score(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = calculate_score(dealer_hand)

        dealer_score_label.set(dealer_score)
        time.sleep(1)
        dealer_card_frame.update()

    player_score = calculate_score(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins")
        increment_dealer_win()
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!!")
        increment_player_win()
    elif dealer_score > player_score:
        result_text.set("Dealer wins!!")
        increment_dealer_win()
    else:
        result_text.set("Draw!!")


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = calculate_score(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")
        increment_dealer_win()


def increment_player_win():
    global player_win_label
    player_win = player_win_label.get() + 1
    player_win_label.set(player_win)


def increment_dealer_win():
    global dealer_win_label
    dealer_win = dealer_win_label.get() + 1
    dealer_win_label.set(dealer_win)


def initiate_game():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(calculate_score(dealer_hand))
    deal_player()


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def new_game():
    global dealer_hand
    global player_hand
    dealer_hand = []
    player_hand = []
    clear_frame(dealer_card_frame)
    clear_frame(player_card_frame)
    result_text.set("")
    player_score_label.set(0)
    dealer_score_label.set(0)
    initiate_game()


def shuffle():
    random.shuffle(deck)


def play():
    initiate_game()

    mainWindow.mainloop()


mainWindow = tkinter.Tk()
# set up the screen and frames for the dealer and player
mainWindow.title('Black Jack')
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_Frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_Frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_Frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_Frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_Frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_Frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_Frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_Frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

start_new_game_button= tkinter.Button(button_frame, text='New game', command=new_game)
start_new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text='shuffle', command=shuffle)
shuffle_button.grid(row=0, column=3)

player_win_label = tkinter.IntVar()
tkinter.Label(mainWindow, text='Player wins').grid(row=7, column=0, sticky='w')
player_count = tkinter.Label(mainWindow, textvariable=player_win_label)
player_count.grid(row=7, column=1, sticky='w')

dealer_win_label = tkinter.IntVar()
tkinter.Label(mainWindow, text='Dealer wins').grid(row=11, column=0, sticky='w')
dealer_count = tkinter.Label(mainWindow, textvariable=dealer_win_label)
dealer_count.grid(row=11, column=1, sticky='ws')

# load cards
cards = []
load_images(cards)
# :print(cards)
# create a new deck of cards and shuffle them
deck = list(cards) + list(cards)
shuffle()

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()