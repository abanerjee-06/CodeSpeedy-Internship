import pygame,random

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
                    spaced_w += w[x].upper()+' '
    return spaced_w


        


def draw_window():
    global guess_word,hangmanstages,chances
    window.fill(colors[2])

    for i in range(len(buttons)):
        if (buttons[i][4]):
            pygame.draw.circle(window,colors[0],(buttons[i][1],buttons[i][2]),buttons[i][3])
            pygame.draw.circle(window,buttons[i][0],(buttons[i][1],buttons[i][2]),buttons[i][3]-2)
            text = fonts[0].render(chr(buttons[i][5]),1,colors[0])
            window.blit(text,(buttons[i][1]-(text.get_width()/2),buttons[i][2]-(text.get_height()/2)))
            spaced_w = currentWord(word,guess_word)
            text1 = fonts[1].render(spaced_w,1,colors[0])
            r = text1.get_rect()
            l = r[2]
            window.blit(text1,(win_size[1]/2-l/2,400))
            curr_stage = hangmanstages[chances]
            window.blit(curr_stage,(win_size[1]/2 - curr_stage.get_width()/2+20,150))
            pygame.display.update()


win_size = [580,900]
colors = [(0,0,0),(100,255,100),(255,255,255),(102,255,255)]

pygame.init()
window = pygame.display.set_mode((win_size[1],win_size[0]))
pygame.display.set_caption('Hangman Game in Python')
fonts = [pygame.font.SysFont("ubuntu",20),pygame.font.SysFont("monospace",24),pygame.font.SysFont("ubuntu",45)]
hangmanstages = [pygame.image.load('Hangman.png'), pygame.image.load('Hangman(1).png'), pygame.image.load('Hangman(2).png'), pygame.image.load('Hangman(3).png'), pygame.image.load('Hangman(4).png'), pygame.image.load('Hangman(5).png'), pygame.image.load('Hangman(6).png')]
buttons,guess_word,word = [],[],''
chances = 0

increase = round(win_size[1] / 13)
x = 25
for i in range(26):
    if (i >= 13):
        y = 85
        x += (increase * (i - 13))
    else:
        y = 40
        x += (increase * i)

word = get_word()

    spaced_w = ''play_on = True

while (play_on):
    draw_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (even.key == pygame.K_ESCAPE):
                play_on = False
        if (event.type == pygame.QUIT):
            play_on = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
        

pygame.quit()