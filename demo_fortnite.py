import random

import pygame
import trackers.tracker_manager as mg
#color settings
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255,140,0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SILVER = (192,192,192)

#movement settings
JUMP_HEIGHT = 0.15
BUK_TRESHOLD = -1.6

#screen settings
HEIGHT = 900
WIDTH = 1440

#paddle settings
PAD_WIDTH = 30
PAD_HEIGHT = 130
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2

#ball settings
BALL_RADIUS  = 30


#needs cleanup
ball_pos = [0, 0]
ball_vel = [0.0, 0.0]

#paddle and position from all players
paddle1_vel = 0
paddle2_vel = 0

paddle1_status = True
paddle2_status = True

player_1_y = []
player_2_y = []

l_score = 0
r_score = 0

#path to images and fonts
FONT_MODERN = "assets/font/Roboto-Bold.ttf"
FONT_RETRO = "assets/font/bit9x9.ttf"

SPRING = "assets/img/happy.png"
BUK = "assets/img/crounching.png"

THEME1 = "assets/img/fortnite.jpg"
PADDLE1 = "assets/img/plank.png"
BALL1 = "assets/img/grenade.png"
BOUNCE_SOUND1 = "assets/sounds/test.wav"
SCORE_SOUND1 = "assets/sounds/synth_score.wav"

THEME2 = "assets/img/frozen.png"
PADDLE2 = "assets/img/tree.png"
BALL2 = "assets/img/pebbleFrozen.png"
BOUNCE_SOUND2 = "assets/sounds/test.wav"
SCORE_SOUND2 = "assets/sounds/synth_score.wav"

BOUNCE_SOUND3 = "assets/sounds/test.wav"
SCORE_SOUND3 = "assets/sounds/synth_score.wav"


class Pong_demo():
    def __init__(self,mode = "time", players=1, theme=1, ball_speed=5, paddle_speed=4 ,ball_speedup= 1.0006, play_time=120, win_score = 2):
        self.mode = mode
        self.players = players
        self.ball_speed = ball_speed
        self.ball_speedup = ball_speedup
        self.paddle_speed = paddle_speed
        self.play_time = play_time
        self.win_score = win_score
        self.time_start = 0
        self.theme = theme

        self.buk = BUK
        self.jump = SPRING

        self.font = FONT_MODERN
        self.color_text = BLACK

        #set theme images
        if self.theme == 1:
            self.background = THEME1
            self.paddle = PADDLE1
            self.ball = BALL1
            self.sound_paddle = BOUNCE_SOUND1
            self.sound_score = SCORE_SOUND1

        elif self.theme == 2:
            self.background = THEME2
            self.paddle = PADDLE2
            self.ball = BALL2
            self.sound_paddle = BOUNCE_SOUND2
            self.sound_score = SCORE_SOUND2

        else:
            self.theme = 3
            self.sound_paddle = BOUNCE_SOUND3
            self.sound_score = SCORE_SOUND3
            self.color_text = BLACK
            self.font = FONT_RETRO

        self.start()


    #init method to set up the ball, decide wich direction it is going to start off in
    def ball_init(self, right):
        global ball_pos, ball_vel
        ball_pos = [WIDTH // 2, HEIGHT // 2]

        horz = self.ball_speed

        direction = random.randrange(0,2)
        ran = random.randrange(3,6)

        if direction == 0:
            vert = ran
        else: vert = -ran


        if right == False:
            horz = - horz

        ball_vel = [horz, -vert]


    def init_paddles_and_ball(self):
        global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, l_score, r_score  # these are floats
        global score1, score2  # these are ints
        paddle1_pos = [HALF_PAD_WIDTH - 1, HEIGHT // 2]
        paddle2_pos = [WIDTH + 1 - HALF_PAD_WIDTH, HEIGHT //2]
        l_score = 0
        r_score = 0
        if random.randrange(0, 2) == 0:
            self.ball_init(True)
        else:
            self.ball_init(False)

    def draw_hitbox(self, canvas):
        pygame.draw.circle(canvas, BLACK, ball_pos, BALL_RADIUS, 0)

        pygame.draw.polygon(canvas, BLACK, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT],
                                            [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
                                            [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
                                            [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)

        pygame.draw.polygon(canvas, BLACK, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],
                                            [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
                                            [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
                                            [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)



    def draw(self, canvas):
        global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score, paddle1_status, paddle2_status

        ball_vel[0] = ball_vel[0] * self.ball_speedup
        ball_vel[1] = ball_vel[1] * self.ball_speedup


        if self.theme == 3:
            canvas.fill(WHITE)
            pygame.draw.line(canvas, BLACK, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
            self.draw_hitbox(canvas)

        else:
            canvas.blit(self.background, [0,0])


        #checks paddle for possible movement
        if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
            paddle1_pos[1] += paddle1_vel

        if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
            paddle2_pos[1] += paddle2_vel
        elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
            paddle2_pos[1] += paddle2_vel
        elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
            paddle2_pos[1] += paddle2_vel


        ball_pos[0] += int(ball_vel[0])
        ball_pos[1] += int(ball_vel[1])






        #botsing met muur onder
        if int(ball_pos[1]) <= BALL_RADIUS:
            ball_vel[1] = - ball_vel[1]
        #botsing met muur boven
        if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
            ball_vel[1] = -ball_vel[1]


        if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT,
                                                                                     paddle1_pos[1] + HALF_PAD_HEIGHT, 1):
            #links paddle botsen
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= self.ball_speedup
            ball_vel[1] *= self.ball_speedup

            s = pygame.mixer.Sound(self.sound_paddle)
            s.set_volume(1)
            ch = s.play()

            #bal bottste tegen paddle, geef de speler een opdracht dat hij moet doen
            ran = random.randrange(0,2)
            if ran == 0:
                paddle1_status = "buk"


            else:
                paddle1_status = "spring"


            if paddle1_status == "buk":
                canvas.blit(self.buk, [200, HEIGHT/2])

            elif paddle1_status == "spring":
                canvas.blit(self.jump, [200, HEIGHT/2])

            if self.players == 2:
                if paddle2_status == "buk":
                    canvas.blit(self.buk, [1000, HEIGHT/2])

            elif paddle2_status == "spring":
                canvas.blit(self.jump, [1000, HEIGHT/2])






        elif int(ball_pos[0]) <= BALL_RADIUS:
            r_score += 1
            s = pygame.mixer.Sound(self.sound_score)
            s.set_volume(0.4)
            ch = s.play()
            paddle1_status = True
            paddle2_status = True
            self.ball_init(True)

        if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(ball_pos[1]) in range(
                paddle2_pos[1] - HALF_PAD_HEIGHT, paddle2_pos[1] + HALF_PAD_HEIGHT, 1):

            #rechter paddle botsen
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= self.ball_speedup
            ball_vel[1] *= self.ball_speedup
            #speel geluid
            s = pygame.mixer.Sound(self.sound_paddle)
            s.set_volume(1)
            ch = s.play()

            ran = random.randrange(0, 2)
            if ran == 0:
                paddle2_status = "buk"


            else:
                paddle2_status = "spring"


        elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS:
            l_score += 1
            s = pygame.mixer.Sound(self.sound_score)
            s.set_volume(0.4)
            ch = s.play()
            paddle1_status = True
            paddle2_status = True
            self.ball_init(False)

            # hitbox
            # self.draw_hitbox(canvas)
        if self.theme != 3:
            canvas.blit(self.paddle, [paddle2_pos[0] - 60, paddle2_pos[1] - HALF_PAD_HEIGHT])
            canvas.blit(self.paddle, [paddle1_pos[0] - 60, paddle1_pos[1] - HALF_PAD_HEIGHT])
            canvas.blit(self.ball, [ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS])

        label1 = self.font.render(str(l_score), 1, self.color_text)
        label2 = self.font.render(str(r_score), 1, self.color_text)



        canvas.blit(label2, (WIDTH-100, 100))
        canvas.blit(label1, (50, 100))




        if self.mode == "time":
            current_time = pygame.time.get_ticks()
            time_since_beginning = (current_time - self.time_start) / 1000
            time_remaining = "{:.0f}".format(self.play_time - time_since_beginning)
            label3 = self.font.render(time_remaining, 1, self.color_text)
            canvas.blit(label3, (WIDTH / 2 - 60, HEIGHT - 200))

            if self.play_time- time_since_beginning < 0:
                print("Time mode: time is up")
                pygame.display.quit()
                pygame.quit()

        elif self.mode == "score":
            win_score = self. win_score
            if l_score >=  win_score:
                print("Score mode: left player won")
                pygame.display.quit()
                pygame.quit()
            elif r_score >= win_score:
                print("Score mode: right player won")
                pygame.display.quit()
                pygame.quit()

        #self.draw_hitbox(canvas)





    #need to make this more precise
    def update_paddle_player(self,player):
        global paddle1_pos, paddle2_pos, player_1_y, player_2_y,paddle1_status, paddle2_status

        try:
            player_pos = mg.get_position("tracker_"+str(player))
            player_x = player_pos["x"]
            player_y = player_pos["y"]

            if player == 1:
                player_1_y.append(float(player_y))
                player_1_y = player_1_y[-60:]

                min_y = min(player_1_y)
                max_y = max(player_1_y)

                if max_y - min_y > JUMP_HEIGHT and paddle1_status == "spring" :
                    paddle1_status = True

                elif player_y < BUK_TRESHOLD and paddle1_status == "buk":
                    paddle1_status = True

                if paddle1_status == "buk" or paddle1_status == "spring":
                    paddle1_pos[1] = 3000

                elif paddle1_status == True:
                    paddle1_pos[1] = 900 - int((player_x + 1.6) * 300)

            elif player == 2:
                player_2_y.append(float(player_y))
                player_2_y = player_2_y[-60:]

                min_y = min(player_2_y)
                max_y = max(player_2_y)

                if max_y - min_y > JUMP_HEIGHT and paddle2_status == "spring":
                    paddle2_status = True

                elif player_y < BUK_TRESHOLD and paddle2_status == "buk":
                    paddle2_status = True

                if paddle2_status == "buk" or paddle2_status == "spring":
                    paddle2_pos[1] = 3000

                elif paddle2_status == True:
                    paddle2_pos[1] = 900 - int((player_x + 1.6) * 300)

        except TypeError as e:
            pass



    def update_paddle_ai(self):
        global paddle2_vel, paddle2_pos, ball_pos, ball_vel



        if paddle2_pos[1] > ball_pos[1]+40 and ball_pos[0] > WIDTH-1000 and ball_vel[0] > 0:
            paddle2_vel = -self.paddle_speed

        elif paddle2_pos[1] < ball_pos[1]-40 and ball_pos[0] > WIDTH-1000 and ball_vel[0] > 0:
            paddle2_vel = self.paddle_speed

        elif ball_vel[0] < 0 and (paddle2_pos[1] < HEIGHT/2-70 or paddle2_pos[1] > HEIGHT/2+70):
            if (paddle2_pos[1] < HEIGHT/2-50):
                paddle2_vel = +self.paddle_speed
            else: paddle2_vel = -self.paddle_speed

        else: paddle2_vel = 0


    def update_paddles(self):
        if self.players == 1:
            self.update_paddle_player(1)
            self.update_paddle_ai()

        else:
            self.update_paddle_player(1)
            self.update_paddle_player(2)




    def start(self):
        pygame.mixer.pre_init(22100, -16, 2, 64)
        pygame.mixer.init()

        pygame.init()
        fps = pygame.time.Clock()
        # init ball and paddles
        self.init_paddles_and_ball()
        # set pygame screen settings and fonts
        window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 32)


        self.jump = pygame.image.load(self.jump).convert_alpha()
        self.buk = pygame.image.load(self.buk).convert_alpha()


        #set theme
        if self.theme != 3:
            self.background =  pygame.image.load(self.background).convert()
            self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

            self.paddle =  pygame.image.load(self.paddle).convert_alpha()


            self.ball =  pygame.image.load(self.ball).convert_alpha()
            self.ball = pygame.transform.scale(self.ball, (55, 55))


        #set font
        self.font = pygame.font.Font(self.font, 100)

        # opens the game windows and sets the tittle
        pygame.display.set_caption('Project II - Pong')
        self.time_start  = pygame.time.get_ticks()
        # start game loop

        while True:
            self.update_paddles()
            self.draw(window)
            pygame.display.flip()
            fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                        pygame.quit()




Pong_demo(paddle_speed=6, theme=2, play_time=10, players=1, ball_speed=12, mode="time")
