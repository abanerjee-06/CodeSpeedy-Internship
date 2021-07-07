import pygame,random
pygame.init()


winsize = (900,580)
colors = [(0,0,0),(100,255,100),(255,255,255),(102,255,255)]
fonts = [pygame.font.SysFont("ubuntu",20),pygame.font.SysFont("monospace",24),pygame.font.SysFont("ubuntu",45)]
word = ''
buttons,guess = [],[]
hangmanpics = [pygame.image.load('Hangman.png'), pygame.image.load('Hangman(1).png'), pygame.image.load('Hangman(2).png'), pygame.image.load('Hangman(3).png'), pygame.image.load('Hangman(4).png'), pygame.image.load('Hangman(5).png'), pygame.image.load('Hangman(6).png')]
tries = 0

window = pygame.display.set_mode(winsize)
pygame.display.set_caption('Hangman Game in Python')


def currentWord(word,guess=[]):
    wordnow = ''
    for i in range(len(word)):
        if (word[i] != ' '):
            wordnow += '_ '
            for j in range(len(guess)):
                if (word[i].upper() == guess[j]):
                    wordnow = wordnow[:-2]
                    wordnow += word[i].upper() + ' '
        elif (word[i] == ' '):
            wordnow += ' '
    return wordnow

def draw_gamewin():
    global guess,hangmanpics,tries
    window.fill(colors[2])
    for i in range(len(buttons)):
        if (buttons[i][4]):
            pygame.draw.circle(window, colors[0], (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(window, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            text = fonts[0].render(chr(buttons[i][5]), 1, colors[0])
            window.blit(text, (buttons[i][1] - (text.get_width() / 2), buttons[i][2] - (text.get_height() / 2)))
        
    wordshow = currentWord(word,guess)
    text = fonts[2].render(wordshow,1,colors[0])
    rect = text.get_rect()
    level = hangmanpics[tries]
    window.blit(text,(winsize[0]/2  - level.get_width()/2 + 20, 150))
    pygame.display.update()

def inpword():
    f = open("words.txt")
    l = f.readlines()
    i = random.randrange(0,len(l)-1)
    return l[i][:-1]

def hanging(guess):
    global word
    if (guess.lower() in word.lower()):
        return False
    else:
        return True

def getbutton(x,y):
    for i in range(len(buttons)):
        if ((y-20 < buttons[i][2]) and (y+20 > buttons[i][2])):
            if ((x-20 < buttons[i][1]) and (x+20 > buttons[i][1])):
                return buttons[i][5]
    return None

def game_reset():
    global guess,buttons,word,tries
    for i in range(len(buttons)):
        buttons[i][4] = True
    tries,guess = 0,[]
    word = inpword()
    

def end(winner):
    global tries
    draw_gamewin()
    pygame.time.delay(1000)
    window.fill(colors[1])

    if (not winner):
        text = fonts[2].render('You Lost, Press any key to play again....',1,colors[0])
        print('The correct word is: ',word.upper())
    else:
        text = fonts[2].render('WINNER!! Press any key to play again....',1,colors[0])
    actual_word = fonts[2].render(word.upper(),1,colors[0])
    disp_word = fonts[2].render('The word was: ',1,colors[0])

    window.blit(actual_word,(winsize[0]/2 - actual_word.get_width()/2, 295))
    window.blit(disp_word, (winsize[0]/2 - disp_word.get_width()/2, 245))
    window.blit(text, (winsize[0]/2 - text.get_width()/2, 140))
    pygame.display.update()

    play_again = True
    while (play_again):
        for event in pygame.event.get():
            if (event.type() == pygame.QUIT):
                pygame.quit()
            elif (event.type() == pygame.KEYDOWN):
                play_again = False
    game_reset()


inc,val = round(winsize[0]/13),0
for i in range(26):
    if (i >= 13):
        y = 85
        val = inc * (i-13)
    else:
        y = 40
        val = inc * i
    x = 25+val
    buttons.append([colors[3],x,y,20,True,65+i])

word = inpword()
play_game  = True
while (play_game):
    draw_gamewin()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            play_game = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.ESCAPE):
                play_game = False
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            coord = pygame.mouse.get_pos()
            key = getbutton(coord[0],coord[1])
            if (key != None):
                guess.append(chr(key))
                buttons[key-65][4] = False
                if (hanging(chr(key))):
                    if (tries >= 6):
                        end(False)
                    else:
                        tries += 1
                else:
                    if (currentWord(word,guess).count('_') == 0):
                        end(True)
pygame.quit()
