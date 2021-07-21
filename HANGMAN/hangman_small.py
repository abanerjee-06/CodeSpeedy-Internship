import pygame,random


def ishang(word_guess):
    global word
    flag = False
    if (word_guess.lower() not in word.lower()):
        flag = True
    return flag

def get_word():
    f = open('words.txt')
    l = f.readlines()
    idx = random.randrange(0,len(l)-1)
    w = l[idx][:-1]
    return w

def currentWord(w,guess_word=[]):
    guessed_letter,spaced_w = guess_word,''
    for x in range(len(w)):
        if (w[x] == ' '):
            spaced_w += ' '
        elif (w[x] != ' '):
            spaced_w += '_ '
            for i in range(len(guessed_letter)):
                if (w[x].upper() == guessed_letter[i]):
                    spaced_w = spaced_w[:-2]
                    spaced_w += w[x].upper() + ' '
    return spaced_w

def buttonClick(x,y):
    for i in range(len(buttons)):
        if (x > buttons[i][1]-20 and x < buttons[i][1]+20):
            if (y > buttons[i][2]-20 and y < buttons[i][2]+20):
                return buttons[i][5]
    return None

def game_reset():
    global chances, guess_word, word
    chances,guess_word,word = 0,[],get_word()
    for i in range(len(buttons)):
        buttons[i][4] = True

def game_over(winner):
    prompts = ['You Lost, press any key to play again...','WINNER!, press any key to play again...']
    draw_window()
    pygame.time.delay(1000)
    window.fill(colors[1])

    if (not winner):
        text = fonts[2].render(prompts[0], 1, colors[0])
    else:
        text = fonts[2].render(prompts[1], 1, colors[0])
    
    word_guessed = fonts[2].render(word.upper(), 1, colors[0])
    word_actual = fonts[2].render('The phrase was: ', 1, colors[0])

    window.blit(word_guessed, (win_size[1]/2 - word_guessed.get_width()/2, 295))
    window.blit(word_actual, (win_size[1]/2 - word_actual.get_width()/2, 245))
    window.blit(text, (win_size[1]/2 - text.get_width()/2, 140))
    
    pygame.display.update()
    retry = True
    while(retry):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                retry = False
            if (event.type == pygame.QUIT):
                pygame.quit()
    game_reset()

def draw_window():
    global guess_word,hangmanstages,chances
    window.fill(colors[1])

    for i in range(len(buttons)):
        if (buttons[i][4]):
            pygame.draw.circle(window, colors[0], (buttons[i][1],buttons[i][2]), buttons[i][3])
            pygame.draw.circle(window, buttons[i][0], (buttons[i][1],buttons[i][2]), buttons[i][3]-2)
            text = fonts[0].render(chr(buttons[i][5]), 1, colors[0])
            window.blit(text, (buttons[i][1] - (text.get_width()/2), buttons[i][2] - (text.get_height()/2)))
        
    spaced_w = currentWord(word,guess_word)
    text1 = fonts[1].render(spaced_w, 1, colors[0])
    r = text1.get_rect()
    l = r[2]

    window.blit(text1,(win_size[1]/2 - l/2, 400))
    
    curr_stage = hangmanstages[chances]
    window.blit(curr_stage,(win_size[1]/2 - curr_stage.get_width()/2 + 20,150))
    pygame.display.update()


pygame.init()
win_size = [580,900]
colors = [(0,0,0),(100,255,100),(255,255,0),(102,255,255)]
window = pygame.display.set_mode((win_size[1],win_size[0]))
pygame.display.set_caption('Hangman Game in Python [Small Screen]')
fonts = [pygame.font.SysFont("ubuntu",20),pygame.font.SysFont("monospace",24),pygame.font.SysFont("ubuntu",45)]
hangmanstages = [pygame.image.load('./Photos/small_scr/Hangman.png'), pygame.image.load('./Photos/small_scr/Hangman(1).png'), pygame.image.load('./Photos/small_scr/Hangman(2).png'), pygame.image.load('./Photos/small_scr/Hangman(3).png'), \
pygame.image.load('./Photos/small_scr/Hangman(4).png'), pygame.image.load('./Photos/small_scr/Hangman(5).png'), pygame.image.load('./Photos/small_scr/Hangman(6).png')]
buttons,guess_word,word = [],[],''
chances = 0

increase = round(win_size[1] / 13)
init_vals = [25,60]
for i in range(26):
    if (i >= 13):
        y = init_vals[1] + 25
        x = init_vals[0] + (increase * (i - 13))
    else:
        y = init_vals[1] - 20
        x = init_vals[0] + (increase * i)
    buttons.append([colors[2],x,y,20,True,65+i])

word = get_word()
play_on = True

while (play_on):
    draw_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                play_on = False
        if (event.type == pygame.QUIT):
            play_on = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            coord = pygame.mouse.get_pos()
            alphabet = buttonClick(coord[0],coord[1])
            if (alphabet is not None):
                guess_word.append(chr(alphabet))
                buttons[alphabet - 65][4] = False
                if (ishang(chr(alphabet)) == False):
                    if (currentWord(word, guess_word).count('_') == 0):
                        game_over(True)
                else:
                    if (chances < 6):
                        chances += 1 
                    if (chances == 6):
                        game_over(False)
                    

pygame.quit()