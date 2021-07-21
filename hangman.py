import pygame
import random

pygame.init()
winHeight = 580
winWidth = 900
win=pygame.display.set_mode((winWidth,winHeight))
pygame.display.set_caption('Hangman Game in Python')
BLACK = (0,0, 0)
GREEN = (100,255,100)
WHITE = (255,255,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("ubuntu", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('ubuntu', 45)
word = ''
buttons = []
guessed = []
hangmanstages = [pygame.image.load('Hangman.png'), pygame.image.load('Hangman(1).png'), pygame.image.load('Hangman(2).png'), pygame.image.load('Hangman(3).png'), pygame.image.load('Hangman(4).png'), pygame.image.load('Hangman(5).png'), pygame.image.load('Hangman(6).png')]

tries = 0


def redraw_game_window():
    global guessed
    global hangmanstages
    global tries
    win.fill(WHITE)
    
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = currWord(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    win.blit(label1,(winWidth/2 - length/2, 400))

    stage = hangmanstages[tries]
    win.blit(stage, (winWidth/2 - stage.get_width()/2 + 20, 150))
    pygame.display.update()


def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def currWord(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
            

def buttonHit(x, y):
    for i in range(len(buttons)):
        if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
            if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
                return buttons[i][5]
    return None


def end(winner=False):
    global tries
    loses = 'You Lost, press any key to play again...'
    wins = 'WINNER!, press any key to play again...'
    redraw_game_window()
    pygame.time.delay(1000)
    win.fill(GREEN)

    if winner == True:
        label = lost_font.render(wins, 1, BLACK)
    else:
        label = lost_font.render(loses, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)

    win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()


def reset():
    global tries
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    tries = 0
    guessed = []
    word = randomWord()



# Setup buttons
increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])

word = randomWord()
gameon = True

while gameon:
    redraw_game_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameon = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            letter = buttonHit(clickPos[0], clickPos[1])
            if letter != None:
                guessed.append(chr(letter))
                buttons[letter - 65][4] = False
                if hang(chr(letter)):
                    if tries != 6:
                        tries += 1
                    else:
                        end()
                else:
                    # print(currWord(word, guessed))
                    if currWord(word, guessed).count('_') == 0:
                        end(True)

pygame.quit()

# always quit pygame when done!
