import pygame, random, time

class App:
    def __init__(self):
        self.screen = None
        self.running = None
        self.clock = None
        self.body = None
        self.direction = None
        self.expand = None
        self.head = None
        self.tail = None
        self.posFood = None

    def init(self):
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 100)
        pygame.mixer.music.load("backgroundsound.wav")
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode([1200, 800])
        pygame.display.set_caption("gayaya Vs snakegaya")
        self.running = True
        self.clock = pygame.time.Clock()
        self.body = [pygame.Vector2(10, 10), pygame.Vector2(9, 10), pygame.Vector2(8, 10), pygame.Vector2(7, 10), pygame.Vector2(6, 10)]
        self.direction = [1, 0]
        self.expand = False
        self.posFood = [random.randint(0, 29), random.randint(0, 19)]

    def renderFood(self):
        self.screen.blit(pygame.transform.scale(pygame.image.load("gayaya.png").convert_alpha(), (30, 30)), pygame.Rect(self.posFood[0] * 40, self.posFood[1] * 40, 40, 40))


    def renderSnake(self):
        if self.body[1][0] - self.body[0][0] == 1 and self.body[1][1] - self.body[0][1] == 0:
            self.head = pygame.transform.scale(pygame.image.load("headleft.png").convert_alpha(), (40, 40))
        elif self.body[1][0] - self.body[0][0] == -1 and self.body[1][1] - self.body[0][1] == 0:
            self.head = pygame.transform.scale(pygame.image.load("headright.png").convert_alpha(), (40, 40))
        elif self.body[1][0] - self.body[0][0] == 0 and self.body[1][1] - self.body[0][1] == 1:
            self.head = pygame.transform.scale(pygame.image.load("headup.png").convert_alpha(), (40, 40))
        elif self.body[1][0] - self.body[0][0] == 0 and self.body[1][1] - self.body[0][1] == -1:
            self.head = pygame.transform.scale(pygame.image.load("headdown.png").convert_alpha(), (40, 40))
        if self.body[-2][0] - self.body[-1][0] == 1 and self.body[-2][1] - self.body[-1][1] == 0:
            self.tail = pygame.transform.scale(pygame.image.load("tailright.png").convert_alpha(), (40, 40))
        elif self.body[-2][0] - self.body[-1][0] == -1 and self.body[-2][1] - self.body[-1][1] == 0:
            self.tail = pygame.transform.scale(pygame.image.load("tailleft.png").convert_alpha(), (40, 40))
        elif self.body[-2][0] - self.body[-1][0] == 0 and self.body[-2][1] - self.body[-1][1] == 1:
            self.tail = pygame.transform.scale(pygame.image.load("taildown.png").convert_alpha(), (40, 40))
        elif self.body[-2][0] - self.body[-1][0] == 0 and self.body[-2][1] - self.body[-1][1] == -1:
            self.tail = pygame.transform.scale(pygame.image.load("tailup.png").convert_alpha(), (40, 40))

        for i in self.body:
            if self.body.index(i) == 0:
                self.screen.blit(self.head, pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))
            elif self.body.index(i) == len(self.body) - 1:
                self.screen.blit(self.tail, pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))
            else:
                if [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][0] == [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][0]:
                    self.screen.blit(pygame.transform.scale(pygame.image.load("bodyvertical.png").convert_alpha(), (40, 40)), pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))
                elif [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][1] == [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][1]:
                    self.screen.blit(pygame.transform.scale(pygame.image.load("bodyhorizontal.png").convert_alpha(), (40, 40)), pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))
                else:
                    if [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][0] == -1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][1] == -1 or [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][1] == -1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][0] == -1:
                        self.screen.blit(pygame.transform.scale(pygame.image.load("cornerdownright.png").convert_alpha(), (40, 40)), pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))
                    elif [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][0] == -1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][1] == 1 or [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][1] == 1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][0] == -1:
                        self.screen.blit(pygame.transform.scale(pygame.image.load("cornerupright.png").convert_alpha(), (40, 40)), pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))
                    elif [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][0] == 1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][1] == -1 or [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][1] == -1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][0] == 1:
                        self.screen.blit(pygame.transform.scale(pygame.image.load("cornerdownleft.png").convert_alpha(), (40, 40)), pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))
                    elif [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][0] == 1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][1] == 1 or [self.body[self.body.index(i) + 1][0] - i[0], self.body[self.body.index(i) + 1][1] - i[1]][1] == 1 and [self.body[self.body.index(i) - 1][0] - i[0], self.body[self.body.index(i) - 1][1] - i[1]][0] == 1:
                        self.screen.blit(pygame.transform.scale(pygame.image.load("cornerupleft.png").convert_alpha(), (40, 40)), pygame.Rect(i[0] * 40, i[1] * 40, 40, 40))

    def updateSnake(self):
        if self.expand:
            temp = self.body[:]
            temp.insert(0, temp[0] + self.direction)
            self.body = temp[:]
            self.expand = False
        else:
            temp = self.body[:-1]
            temp.insert(0, temp[0] + self.direction)
            self.body = temp[:]

    def update(self):
        self.updateSnake()
        self.collisionSnake()

        if not 0 <= self.body[0][0] < 30 or not 0 <= self.body[0][1] < 20:
            self.gameOver()

        for i in self.body[1:]:
            if i == self.body[0]:
                self.gameOver()

    def render(self):
        self.screen.blit(pygame.transform.scale(pygame.image.load("font.png").convert_alpha(), [1200, 800]), [0, 0])
        pygame.draw.line(self.screen, "red", [0, 0], [1200, 0], 5)
        pygame.draw.line(self.screen, "red", [0, 0], [0, 800], 5)
        pygame.draw.line(self.screen, "red", [0, 800], [1200, 800], 7)
        pygame.draw.line(self.screen, "red", [1200, 800], [1200, 0], 7)
        self.renderFood()
        self.renderSnake()
        self.screen.blit(pygame.font.Font("freesansbold.ttf", 20). render(("score: " + str(len(self.body) - 5)), True, pygame.Color("white")), pygame.font.Font("freesansbold.ttf", 20). render(("score: " + str(len(self.body) - 5)), True, pygame.Color("white")). get_rect(center = [45, 20]))
        self.clock.tick(60)
        pygame.display.flip()

    def collisionSnake(self):
        if self.posFood == self.body[0]:
            self.posFood = [random.randint(0, 29), random.randint(0, 19)]
            self.expand = True
            pygame.mixer.Sound("frogdeath.wav").play()

    def gameOver(self):
        pygame.mixer.Sound("crashsound.wav").play()
        time.sleep(0.2)
        self.running = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.USEREVENT:
                self.update()

            if pygame.key.get_pressed()[pygame.K_UP] and self.direction[1] != 1 or pygame.key.get_pressed()[pygame.K_w] and self.direction[1] != 1:
                self.direction = [0, -1]

            elif pygame.key.get_pressed()[pygame.K_DOWN] and self.direction[1] != -1 or pygame.key.get_pressed()[pygame.K_s] and self.direction[1] != -1:
                self.direction = [0, 1]

            elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.direction[0] != -1  or pygame.key.get_pressed()[pygame.K_d] and self.direction[0] != -1:
                self.direction = [1, 0]

            elif pygame.key.get_pressed()[pygame.K_LEFT] and self.direction[0] != 1  or pygame.key.get_pressed()[pygame.K_a] and self.direction[0] != 1:
                self.direction = [-1, 0]

    @staticmethod
    def cleanUp():
        pygame.quit()

    def run(self):
        self.init()
        while self.running:
            self.events()
            self.render()
        self.cleanUp()



if __name__ == "__main__":
    app = App()
    app.run()