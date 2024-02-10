# Import Modules
import pygame
import random
import numpy as np
import math


running = True

# Variables
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 15)
pSpeed = 0
Isle1 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle2 = Isle1[0] + random.randint(-120, 120), Isle1[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle2 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle3 = Isle2[0] + random.randint(-120, 120), Isle2[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle3 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle4 = Isle3[0] + random.randint(-120, 120), Isle3[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle4 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle5 = Isle4[0] + random.randint(-120, 120), Isle4[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle5 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle6 = Isle5[0] + random.randint(-120, 120), Isle5[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle6 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle7 = Isle6[0] + random.randint(-120, 120), Isle6[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle7 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle8 = Isle7[0] + random.randint(-120, 120), Isle7[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle8 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle9 = Isle8[0] + random.randint(-120, 120), Isle8[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle9 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle10 = Isle9[0] + random.randint(-120, 120), Isle9[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle10 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle11 = Isle10[0] + random.randint(-120, 120), Isle10[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle11 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle12 = Isle11[0] + random.randint(-120, 120), Isle11[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle12 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle13 = Isle12[0] + random.randint(-120, 120), Isle12[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle13 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle14 = Isle13[0] + random.randint(-120, 120), Isle13[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle14 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))
Isle15 = Isle14[0] + random.randint(-120, 120), Isle14[1] + random.randint(-120, 120), random.randint(5, 70)

if random.randint(1, 5) == 5:
    Isle15 = (random.randint(0, 1355), random.randint(0, 690), random.randint(5, 70))


info = font.render(" ", True, (0, 200, 100))
textpos = 0, 0
infoRect = info.get_rect()
colors = []
check = False
Genes_Global = [0, 0, 0, 0, 0, 0, 0, 0]


# DEFINE CLASSES_______________________________________________________________________________________________________|
class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, Speed, Size, Color, Range, Diet, Predatory, Weights):
        super(Creature, self).__init__()
        self.image = pygame.image.load("Creature.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        # Gene Mutations
        self.size = Size
        self.speed = Speed
        self.color = Color
        self.diet = Diet
        self.range = Range
        self.predatory = Predatory
        self.age = (random.randint(2000, 6000))
        self.weights = Weights
        # Render
        self.updates = 0
        self.tick = 0
        self.health = 40
        self.check = 1
        global colors
        r = self.color[0]
        b = self.color[1]
        g = self.color[2]
        self.color = r, g, b
        count = 0
        c = random.randint(1, 3)
        while self.color in colors:
            m = random.randint(-15, 15)
            if c == 1:
                r = self.find_color(r + m)
            elif c == 2:
                b = self.find_color(b + m)
            else:
                g = self.find_color(g + m)
            self.color = r, b, g
            count += 1
            if count > 999:
                break
        colors.append(self.color)
        for i in range(random.randint(1, 5)):
            genetype = random.randint(0, 4)
            if genetype == 0:
                mutate = round(random.uniform(0.1, 0.5), 1)
                self.mutatespeed = [0 - mutate, mutate]
                self.speed = self.speed + random.choice(self.mutatespeed)
                self.speed = round(self.speed, 1)
            elif genetype == 1:
                self.mutate = round(random.uniform(0.1, 0.5), 1)
                self.mutatesize = [0 - self.mutate, self.mutate]
                self.size = self.size + random.choice(self.mutatesize)
                if self.size < 0.1:
                    self.size = 0.1
                self.size = round(self.size, 1)
            elif genetype == 2:
                self.mutatediet = random.randint(1, 3)
                self.mutatediet = [0 - self.mutatediet, self.mutatediet]
                self.diet = self.diet + random.choice(self.mutatediet)
                self.diet = round(self.diet)
                if self.diet < -10:
                    self.diet = -10
                if self.diet > 10:
                    self.diet = 10
            elif genetype == 3:
                self.mutate = round(random.uniform(0.1, 0.3), 1)
                self.mutate = [0 - self.mutate, self.mutate]
                self.predatory = round(self.predatory + random.choice(self.mutate), 1)
                if self.predatory < -0.5:
                    self.predatory = -0.5
                if self.predatory > 0.5:
                    self.predatory = 0.5
            elif genetype == 4:
                self.mutate = random.randint(0, 1)
                if self.mutate == 0:
                    self.range += random.randint(1, 5)
                else:
                    self.range -= random.randint(-5, -1)
                    if self.range < 1:
                        self.range = 1
        for i in range(random.randint(1, 30)):
            index = random.randint(1, 17)
            m = round(random.uniform(10, 40))
            m = [0 - m, m]
            m = random.choice(m)
            self.weights[index][random.randint(0, 7)] += m
        # Gene Initialization
        self.scaleimage = pygame.transform.smoothscale(self.image, (self.size, self.size))
        self.image = self.scaleimage
        self.rect = self.image.get_rect()
        # Diet Gene
        docolor = True
        if self.diet < 0:
            herbivores.add(self)
        elif self.diet > -1:
            if self.predatory > 0:
                carnivores.add(self)
                predators.add(self)
                self.cimage = pygame.Surface(self.image.get_size()).convert_alpha()
                self.cimage.fill((225, 0, 0))
                self.image.blit(self.cimage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                docolor = False
            else:
                carnivores.add(self)
                self.cimage = pygame.Surface(self.image.get_size()).convert_alpha()
                self.cimage.fill((245, 135, 66))
                self.image.blit(self.cimage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                docolor = False
        # Color Gene
        if docolor:
            self.cimage = pygame.Surface(self.image.get_size()).convert_alpha()
            self.cimage.fill(self.color)
            self.image.blit(self.cimage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.htick = 0
        self.speedtick = 1
        self.tracked = False
        self.dir = random.randint(0, 360)
        self.outrotate = 0
        self.outvel = 0
        self.vel = 0
        self.saved_image = self.image
        self.rotatetick = 1
        self.rotate = 0
        self.lastdir = 0
        global Genes_Global
        Genes_Global = [self.speed, self.size, self.color, self.range, self.diet, self.predatory,
                        self.weights]
        self.go = True

    def find_color(self, r):
        if r > 225:
            r = random.randint(0, 225)
        if r < 0:
            r = random.randint(0, 225)
        return r


    def die(self):
        meat = Meat(self.x, self.y, self.size)
        meats.add(meat)
        self.kill()
        del self

    def move(self, steps):
        from math import sin, cos
        speedx = sin(self.dir) * steps
        speedy = cos(self.dir) * steps
        self.x = self.x + speedx
        self.y = self.y + speedy
        self.x, self.y = checkVoid((self.x, self.y), False)
        self.rect.x = self.x
        self.rect.y = self.y
        if pygame.sprite.spritecollideany(self, terrain):
            self.x = self.x - speedx
            self.y = self.y - speedy
            self.x, self.y = checkVoid((self.x, self.y), False)
            self.rect.x = self.x
            self.rect.y = self.y

    def clone(self):
        creature = Creature(self.x, self.y, self.speed, self.size, self.color, self.range,
                            self.diet, self.predatory, self.weights)
        creatures.add(creature)

    def think(self):
        idx = 1
        for plant in plants:
            distp = pygame.math.Vector2(self.x, self.y).distance_to((plant.x, plant.y))
            if idx == 1 or distp < shortdistp:
                shortdistp = distp
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
            rotatep = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            idx += 1
        if len(plants.sprites()) > 0 and shortdistp < self.range:
            distp = shortdistp
        else:
            distp, rotatep = 0, 0

        idx = 1
        for meat in meats:
            distm = pygame.math.Vector2(self.x, self.y).distance_to((meat.x, meat.y))
            if idx == 1 or distm < shortdistm:
                shortdistm = distm
            distp = pygame.math.Vector2(self.x, self.y).distance_to((plant.x, plant.y))
            if idx == 1 or distp < shortdistp:
                shortdistp = distp
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
            rotatem = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            idx += 1
        if len(meats.sprites()) > 0 and shortdistp < self.range:
            distm = shortdistm
        else:
            distm, rotatem = 0, 0

        idx = 1
        for herbivore in herbivores:
            disth = pygame.math.Vector2(self.x, self.y).distance_to((herbivore.x, herbivore.y))
            position = self.x, self.y
            herbposition = herbivore.x, herbivore.y
            if idx == 1 or disth < shortdisth and not position == herbposition:
                shortdisth = disth
            distp = pygame.math.Vector2(self.x, self.y).distance_to((plant.x, plant.y))
            if idx == 1 or distp < shortdistp:
                shortdistp = distp
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
            rotateh = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            idx += 1
        if len(herbivores.sprites()) > 0 and shortdistp < self.range:
            disth = shortdisth
        else:
            disth, rotateh = 0, 0

        idx = 1
        for carnivore in carnivores:
            distc = pygame.math.Vector2(self.x, self.y).distance_to((carnivore.x, carnivore.y))
            position = self.x, self.y
            carnposition = carnivore.x, carnivore.y
            if idx == 1 or distc < shortdistc and not position == carnposition:
                shortdistc = distc
            distp = pygame.math.Vector2(self.x, self.y).distance_to((plant.x, plant.y))
            if idx == 1 or distp < shortdistp:
                shortdistp = distp
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
            rotatec = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            idx += 1
        if len(carnivores.sprites()) > 0 and shortdistp < self.range:
            distc = shortdistc
        else:
            distc, rotatec = 0, 0

        inputs = distp, rotatep, disth, rotateh, distm, rotatem, distc, rotatec
        weights = self.weights
        layer1 = np.tanh((np.dot(inputs, weights[0]).T, np.dot(inputs, weights[1]).T,
                          np.dot(inputs, weights[2]).T, np.dot(inputs, weights[3]).T,
                          np.dot(inputs, weights[4]).T, np.dot(inputs, weights[5]).T,
                          np.dot(inputs, weights[6]).T, np.dot(inputs, weights[7]).T))
        inputs = layer1
        layer2 = np.tanh((np.dot(inputs, weights[8]).T, np.dot(inputs, weights[9]).T,
                          np.dot(inputs, weights[10]).T, np.dot(inputs, weights[11]).T,
                          np.dot(inputs, weights[12]).T, np.dot(inputs, weights[13]).T,
                          np.dot(inputs, weights[14]).T, np.dot(inputs, weights[15]).T))

        self.outvel = np.tanh((np.dot(layer2, weights[16])))
        self.outrotate = np.tanh((np.dot(layer2, weights[17])))
        self.rotate = 0
        self.vel += self.outvel
        self.dir += self.outrotate
        self.rotate = self.lastdir - self.dir
        self.rect = self.image.get_rect()
        if self.vel > self.speed:
            self.vel = self.speed
        if self.vel < 0 - self.speed:
            self.vel = 0 - self.speed
        if self.dir > 360:
            self.dir = 0
        if self.dir < 0:
            self.dir = 360


    def update(self):
        if self.go:
            self.updates += 0.5
            # DISPLAY__________________________________________________________________________________________________|
            global track
            if self.rect.collidepoint(pygame.mouse.get_pos()) and not track:
                self.tracked = True
                track = True
                d = f"{'Herbivore' if self.diet < 0 else 'Carnivore'}.{self.diet} Predatory: {self.predatory}"
                print(f"Health: {self.health} Speed: {self.speed} Size: {self.size} Diet: {d} Range: {self.range}"
                      f" Neural Network: {self.weights}")
            global info
            global textpos
            global font
            if self.tracked and track:
                info = font.render("Move: " + str(self.vel) + " Rotate: " + str(round(self.rotate, 1)) + " Health: " +
                                   str(round(self.health)), True,
                                   (0, 200, 100))
            if not track:
                self.tracked = False
            # MOVEMENT_________________________________________________________________________________________________|
            self.think()
            self.move(self.vel)
            self.lastdir = self.dir
            # LOSE ENERGY FOR HOMEOSTASIS______________________________________________________________________________|
            lossdividerspeed = 200
            lossdividersize = 200
            self.health -= round((self.vel / lossdividerspeed) + self.size / lossdividersize + 0.15, 2)
            # HERBIVORE COLLISIONS_____________________________________________________________________________________|
            if self.diet < 0:
                collided_plant = pygame.sprite.spritecollideany(self, plants)
                collided_predator = pygame.sprite.spritecollideany(self, predators)

                if collided_plant:
                    self.health += abs(self.diet) + 20
                    self.check = 0 if self.check > 3 else self.check + 1
                    for _ in range(random.randint(1, 2)):
                        self.clone() if self.check == 0 else None

                if collided_predator:
                    self.die()
            # PREDATOR COLLISIONS______________________________________________________________________________________|
            elif self.diet > -1 and self.predatory > 0:
                collided_meat = pygame.sprite.spritecollideany(self, meats)

                if collided_meat:
                    diet_value = 2 * self.diet
                    self.health += diet_value if diet_value >= 10 else 10
                    self.check = 0 if self.check > 4 else self.check + 1
                    if self.check == 0:
                        self.clone()
            # SCAVENGER COLLISIONS_____________________________________________________________________________________|
            elif self.diet > -1 and self.predatory > 0:
                collided_meat = pygame.sprite.spritecollideany(self, meats)
                collided_predator = pygame.sprite.spritecollideany(self, predators)
                if collided_meat:
                    diet_value = 2 * self.diet
                    self.health += diet_value if diet_value >= 10 else 10
                    self.check = 0 if self.check > 4 else self.check + 1
                    if self.check == 0:
                        self.clone()
                if collided_predator:
                    self.die()
            # DYING____________________________________________________________________________________________________|
            if self.updates > self.age or self.health < 1:
                self.die()


class Meat(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super(Meat, self).__init__()
        self.size = size - 1
        if self.size < 0:
            self.size = 0
        self.image = pygame.image.load("Meat.jpg").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.age = random.randint(80, 100)
        self.updates = 0
        self.end = False


    def update(self):
        self.updates += 1
        if self.end:
            self.kill()
        if pygame.sprite.spritecollideany(self, carnivores):
            self.end = True
        if self.updates == self.age:
            self.end = True
        if self.end:
            del self


class Plant(pygame.sprite.Sprite):
    def __init__(self, rec):
        super(Plant, self).__init__()
        self.check = 0
        choice = rec
        global Isle1, Isle2, Isle3, Isle4, Isle5, Isle6, Isle7, Isle8, Isle9, Isle10, Isle11, Isle12, Isle13, Isle14, \
            Isle15
        isles = Isle1, Isle2, Isle3, Isle4, Isle5, Isle6, Isle7, Isle8, Isle9, Isle10, Isle11, Isle12, Isle13, Isle14, \
            Isle15
        index = random.randint(0, 14)
        self.x, self.y = isles[index][0], isles[index][1]
        isle = isles[index][2]
        direction = random.randint(1, 5)
        self.x += random.randint(0 - isle, isle) * direction
        self.y += random.randint(0 - isle, isle) * direction
        self.x, self.y = checkVoid((self.x, self.y), False)
        isle = round(isle / 2)
        self.x += random.randint(0 - isle, isle) * direction
        self.y += random.randint(0 - isle, isle) * direction
        self.updates = 0
        global worldtype
        if worldtype == "Continents":
            self.size = 3
        elif worldtype == "Large":
            self.size = 5
        self.speed = pSpeed
        m = self.size/2
        self.size = self.size + round(random.uniform(0 - m, m), 1)
        if worldtype == "Continents":
            if self.size < 3:
                self.size = 3
        elif worldtype == "Large":
            if self.size < 3:
                self.size = 3
        # Gene Initialization
        # Size Gene
        self.image = pygame.image.load("Plant.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.scaleimage = pygame.transform.smoothscale(self.image, (self.size, self.size))
        self.image = self.scaleimage
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.isle = choice

    def die(self):
        self.kill()
        del self

    def clone(self):
        plant = Plant(self.isle)
        plants.add(plant)

    def update(self):
        global CLIMATE
        if random.randint(1, 80) == 5:
            self.clone()
        if (pygame.sprite.spritecollideany(self, herbivores) or self.updates > 4000 or
                random.randint(1, 90) == 20):
            self.die()
        self.updates += 1
        if len(plants.sprites()) > CLIMATE:
            if random.randint(0, 10) == 10:
                self.die()


class Terrain(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Terrain, self).__init__()
        self.image = pygame.image.load("Terrain.jpg").convert()
        size = random.randint(3, 8)
        self.image = pygame.transform.smoothscale(self.image, (size, size))
        self.x, self.y = checkVoid((x, y), True)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y


class Button(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Button, self).__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = 682.5, 340

    def update(self):
        global clicked
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            clicked = True
        else:
            clicked = False


# GLOBAL FUNCTIONS_____________________________________________________________________________________________________|
def checkVoid(sprite, offset):
    output = sprite
    if sprite[0] < 0 or sprite[0] > 1355 or sprite[1] < 0 or sprite[1] > 760:
        if sprite[0] < 0:
            output = 1350, output[1]
        if sprite[0] > 1355:
            output = 2, output[1]
        if sprite[1] < 0:
            output = output[0], 763
        if sprite[1] > 760:
            output = output[0], 5
    else:
        output = sprite
    if offset:
        output = output[0] + random.randint(-10, 10), output[1] + random.randint(-10, 10)
    return output


# INTRO________________________________________________________________________________________________________________|
flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
font = pygame.font.Font('freesansbold.ttf', 15)
screen = pygame.display.set_mode((1365, 700), flags, 8)
bg = pygame.image.load("Background.png").convert_alpha()
bg = pygame.transform.smoothscale(bg, (1000, 750))
pygame.display.set_caption("Cycles")
ICON = pygame.image.load("Icon.png")
pygame.display.set_icon(ICON)
buttons = pygame.sprite.Group()
button = Button("Button.png")
buttons.add(button)
clicked = False
track = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked and event.button == 1:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            screen = pygame.display.set_mode((1365, 770))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            screen = pygame.display.set_mode((1365, 800), flags, 8)
    screen.fill((0, 0, 75))
    screen.blit(bg, (1365/10, 700/45))
    buttons.update()
    buttons.draw(screen)
    font = pygame.font.Font('freesansbold.ttf', 100)
    ttext = font.render("Cycles", True, (100, 255, 100))
    ttextRect = ttext.get_rect()
    ttextRect.center = (1335 / 2 + 10, 100)
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render("Start", True, (20, 20, 20))
    textRect = text.get_rect()
    textRect.center = (1335 / 2 + 10, 200)
    screen.blit(text, textRect)
    screen.blit(ttext, ttextRect)
    pygame.display.flip()
    pygame.display.update()
del button, buttons
tickspeed = 100
# Setup
font = pygame.font.Font('freesansbold.ttf', 15)
textRect = text.get_rect()
textRect.center = (1355 // 2, 10)
screen = pygame.display.set_mode((1365, 700), flags, 1)
pygame.display.set_caption("Evolution Simulator")
ICON = pygame.image.load("Icon.png")
pygame.display.set_icon(ICON)
creatures = pygame.sprite.Group()
herbivores = pygame.sprite.Group()
carnivores = pygame.sprite.Group()
predators = pygame.sprite.Group()
meats = pygame.sprite.Group()
plants = pygame.sprite.Group()
terrain = pygame.sprite.Group()
running = True
worldtype = "Continents"
for i in range(random.randint(200, 250)):
    pos = [Isle1, Isle2, Isle3, Isle4, Isle5, Isle6, Isle7, Isle8, Isle9, Isle10, Isle11, Isle12, Isle13,
           Isle14,
           Isle15]
    pos = random.choice(pos)
    Speed = round(random.uniform(0.1, 1), 1)
    Size = random.randint(1, 4)
    Color = (random.randint(0, 226), random.randint(0, 226), random.randint(0, 226))
    Diet = random.randint(-5, 0)
    Predatory = round(random.uniform(-0.5, 0.5), 1)
    Range = random.randint(0, 20)
    Network = [[random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),
                random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),],
               [random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),
               random.randint(-10, 10), random.randint(-10, 10),]
               ]
    creature = Creature(pos[0] + random.randint(-10, 10), pos[1] + random.randint(-10, 10), Speed, Size, Color,
                        Range,
                        Diet, Predatory, Network)
    creatures.add(creature)
    for integer in range(3):
        plant = Plant(random.randint(1, 15))
        plants.add(plant)
rockx, rocky = random.randint(0, 1355), random.randint(0, 690)
for i in range(random.randint(500, 1000)):
    if random.randint(1, 300) == 25:
        rockx, rocky = random.randint(0, 1355), random.randint(0, 690)
    rockx += random.randint(-20, 20)
    rocky += random.randint(-20, 20)
    rockx, rocky = checkVoid((rockx, rocky), True)
    rock = Terrain(rockx, rocky)
    terrain.add(rock)
growth = random.randint(0, 2)
clock = pygame.time.Clock()
climatetick = 1
CLIMATE = random.randint(1100, 1500)
# Gameloop
restarts = 0
showstatistics = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Speed = round(random.uniform(0.1, 0.5), 1)
            Size = random.randint(1, 3)
            Color = (random.randint(0, 226), random.randint(0, 226), random.randint(0, 226))
            Diet = random.randint(-5, 0)
            Predatory = round(random.uniform(-0.5, 0.5), 1)
            Range = random.randint(0, 20)
            Sightmeat = [round(random.uniform(-0.5, 0.5), 1), round(random.uniform(-0.5, 0.5), 1)]
            mx, my = pygame.mouse.get_pos()
            Network = [[random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),]
                       ]
            creature = Creature(mx, my, Speed, Size, Color,
                                Range,
                                Diet, Predatory, Network)
            creatures.add(creature)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            track = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            screen = pygame.display.set_mode((1365, 700), flags, 8)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if showstatistics:
                showstatistics = False
            else:
                showstatistics = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            screen = pygame.display.set_mode((1365, 770))
    screen.fill((0, 0, 30))
    terrain.draw(screen)
    creatures.update()
    plants.update()
    meats.update()
    plants.draw(screen)
    meats.draw(screen)
    creatures.draw(screen)
    populationtext = font.render("Creatures: " + str(len(creatures.sprites())) + " | Plants: " +
                                 str(len(plants.sprites())),
                                 True, (100, 200, 225))
    iterationtext = font.render("Iteration: " + str(restarts + 1),
                                True, (200, 0, 100))
    iterationtextRect = iterationtext.get_rect()
    poptextRect = populationtext.get_rect()
    poptextRect.center = (1355 / 2, 12)
    infoRect.center = (10, 750)
    iterationtextRect.center = (47, 10)
    if showstatistics:
        screen.blit(populationtext, poptextRect)
        screen.blit(info, infoRect)
        screen.blit(iterationtext, iterationtextRect)
    fps = clock.get_fps()
    ftext = round(fps, 1)
    fpsfont = font.render("Fps: " + str(ftext), True, (225, 0, 225))
    fpsRect = fpsfont.get_rect()
    fpsRect.center = (1335 / 2, 28)
    if showstatistics:
        screen.blit(fpsfont, fpsRect)
    if len(creatures.sprites()) < 1:
        restarts += 1
        print("RESTART" + "[" + str(restarts) + "]")
        for i in range(random.randint(50, 100)):
            pos = [Isle1, Isle2, Isle3, Isle4, Isle5, Isle6, Isle7, Isle8, Isle9, Isle10, Isle11, Isle12, Isle13,
                   Isle14,
                   Isle15]
            pos = random.choice(pos)
            Speed = round(random.uniform(0.1, 0.5), 1)
            Size = random.randint(1, 3)
            Color = (random.randint(0, 226), random.randint(0, 226), random.randint(0, 226))
            Diet = random.randint(-5, -1)
            Predatory = round(random.uniform(-0.5, 0.5), 1)
            Range = random.randint(0, 20)
            Network = [[random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),],
                       [random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),
                        random.randint(-10, 10), random.randint(-10, 10),]
                       ]
            creature = Creature(pos[0], pos[1], Genes_Global[0], Genes_Global[1], Genes_Global[2], Genes_Global[3],
                                Genes_Global[4], Genes_Global[5], Genes_Global[6])
            creatures.add(creature)
    if len(plants.sprites()) < 1:
        restarts += 1
        print("RESTART" + "[" + str(restarts) + "]")
        for i in range(random.randint(10, 80)):
            plant = Plant(random.randint(1, 15))
            plants.add(plant)
    if check > 4:
        if climatetick > 20:
            CLIMATE = random.randint(1100, 1500)
            climatetick = 0
        else:
            climatetick += 1
        growth = random.randint(1, 5)

        Isle1 = (Isle1[0] + random.randint(0 - growth, growth), Isle1[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle1), False):
            Isle1 = checkVoid((Isle1), False)
            Isle1 = Isle1 + (random.randint(5, 70),)

        Isle2 = (Isle2[0] + random.randint(0 - growth, growth), Isle2[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle2), False):
            Isle2 = checkVoid((Isle2), False)
            Isle2 = Isle2 + (random.randint(5, 70),)

        Isle3 = (Isle3[0] + random.randint(0 - growth, growth), Isle3[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle3), False):
            Isle3 = checkVoid((Isle3), False)
            Isle3 = Isle3 + (random.randint(5, 70),)

        Isle4 = (Isle4[0] + random.randint(0 - growth, growth), Isle4[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle4), False):
            Isle4 = checkVoid((Isle4), False)
            Isle4 = Isle4 + (random.randint(5, 70),)

        Isle5 = (Isle5[0] + random.randint(0 - growth, growth), Isle5[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle5), False):
            Isle5 = checkVoid((Isle5), False)
            Isle5 = Isle5 + (random.randint(5, 70),)

        Isle6 = (Isle6[0] + random.randint(0 - growth, growth), Isle6[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle6), False):
            Isle6 = checkVoid((Isle6), False)
            Isle6 = Isle6 + (random.randint(5, 70),)

        Isle7 = (Isle7[0] + random.randint(0 - growth, growth), Isle7[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle7), False):
            Isle7 = checkVoid((Isle7), False)
            Isle7 = Isle7 + (random.randint(5, 70),)

        Isle8 = (Isle8[0] + random.randint(0 - growth, growth), Isle8[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle8), False):
            Isle8 = checkVoid((Isle8), False)
            Isle8 = Isle8 + (random.randint(5, 70),)

        Isle9 = (Isle9[0] + random.randint(0 - growth, growth), Isle9[1] + random.randint(0 - growth, growth),
                 random.randint(5, 70))
        if checkVoid((Isle9), False):
            Isle9 = checkVoid((Isle9), False)
            Isle9 = Isle9 + (random.randint(5, 70),)

        Isle10 = (Isle10[0] + random.randint(0 - growth, growth), Isle10[1] + random.randint(0 - growth, growth),
                  random.randint(5, 70))
        if checkVoid((Isle10), False):
            Isle10 = checkVoid((Isle10), False)
            Isle10 = Isle10 + (random.randint(5, 70),)

        Isle11 = (Isle11[0] + random.randint(0 - growth, growth), Isle11[1] + random.randint(0 - growth, growth),
                  random.randint(5, 70))
        if checkVoid((Isle11), False):
            Isle11 = checkVoid((Isle11), False)
            Isle11 = Isle11 + (random.randint(5, 70),)

        Isle12 = (Isle12[0] + random.randint(0 - growth, growth), Isle12[1] + random.randint(0 - growth, growth),
                  random.randint(5, 70))
        if checkVoid((Isle12), False):
            Isle12 = checkVoid((Isle12), False)
            Isle12 = Isle12 + (random.randint(5, 70),)

        Isle13 = (Isle13[0] + random.randint(0 - growth, growth), Isle13[1] + random.randint(0 - growth, growth),
                  random.randint(5, 70))
        if checkVoid((Isle13), False):
            Isle13 = checkVoid((Isle13), False)
            Isle13 = Isle13 + (random.randint(5, 70),)

        Isle14 = (Isle14[0] + random.randint(0 - growth, growth), Isle14[1] + random.randint(0 - growth, growth),
                  random.randint(5, 70))
        if checkVoid((Isle14), False):
            Isle14 = checkVoid((Isle14), False)
            Isle14 = Isle14 + (random.randint(5, 70),)

        Isle15 = (Isle15[0] + random.randint(0 - growth, growth), Isle15[1] + random.randint(0 - growth, growth),
                  random.randint(5, 70))
        if checkVoid((Isle15), False):
            Isle15 = checkVoid((Isle15), False)
            Isle15 = Isle15 + (random.randint(5, 70),)
        check = 0
    else:
        check += 1

    clock.tick(tickspeed)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
