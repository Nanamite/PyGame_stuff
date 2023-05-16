import pygame
from random import randint
from sys import exit

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

black_surface = pygame.Surface((500, 500))
black_surface.fill((0, 0, 0))

class character:
    def __init__(self, pos, idx, color, font_size):
        self.color = color
        self.pos = pos
        self.idx = idx
        self.font = pygame.font.SysFont('couriernew', bold = True, size = font_size)
        self.t = 0

    def draw(self, time):
        if self.t < 4 and time < 4:
            self.text = self.font.render(chr(randint(33, 126)), True, self.color).convert()
        else:
            self.text = self.font.render(chr(randint(33, 126)), True, self.color).convert_alpha()

        self.rect = self.text.get_rect(midtop = (self.pos[0], self.pos[1]))
        screen.blit(self.text, self.rect)

    def fall(self, fall):
        self.pos = (self.pos[0], self.pos[1] + fall)
        self.t += 1
    
class string_row:
    def __init__(self, N, pos):
        self.characters = []
        self.pos = pos
        self.N = N
        self.fall = randint(10, 40)
        self.i = 0
        self.font_size = randint(10, 25)
    
    def gen_characters(self):
        for i in range(self.N):
            if i == 0:
                col = (200, 255, 200)
            else:
                col = (200 - min(200, 100*i), 255 - 20*i, 255 - min(200, 100*i))
            self.characters.append(character(self.pos, i, col, self.font_size))
    
    def draw_char(self, time):
        if self.i > 0:
            for k in range(self.i):
                self.characters[k].fall(self.fall)

        if self.i != self.N:
            for k in range(self.i + 1):
                self.characters[k].draw(time)
            self.i += 1
        else:
            for character in self.characters:
                character.draw(time)

strings = []
pos = []
time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(black_surface, (0, 0))

    for i in range(int(time*10)):
        if i < 4:
            if randint(0, 100)%2 == 0:
                rand_pos = (randint(10, 450), randint(0, 70))
                N = randint(3, 12)
                if len(strings) > 1 and len(pos) > 1:
                    if (rand_pos in pos and strings[pos.index(rand_pos)].i == strings[pos.index(rand_pos)].N):
                        #continue
                        pos.append(rand_pos)
                        strings.append(string_row(N, rand_pos))
                        strings[-1].gen_characters()
                    else:
                        pos.append(rand_pos)
                        strings.append(string_row(N, rand_pos))
                        strings[-1].gen_characters()

                else:
                    pos.append(rand_pos)
                    strings.append(string_row(N, rand_pos))
                    strings[-1].gen_characters()

    for string in strings:
        string.draw_char(time)

        if string.characters[-1].pos[1] > 800:
            idx = strings.index(string)
            strings.pop(idx)
            pos.pop(idx)

    pygame.display.update()
    clock.tick(8)
    time += 0.1

