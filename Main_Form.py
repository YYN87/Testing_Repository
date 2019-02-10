# Copyrights Yasas Y Nonis
import turtle
import math
import random
import winsound
import tkMessageBox
import keyboard

# region Screen Settings. Testing Comment
wn = turtle.Screen()
wn.title("Monkey Hunting  V 1.0")
wn.bgcolor("green")
wn.bgpic("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\spaceImage.gif")

# endregion " ",

# region Registering the shapes
turtle.register_shape("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\player.gif")
turtle.register_shape("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\invader.gif")

# endregion


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\player.gif")
        self.speed(0)
        self.setposition(0, -280)
        self.speed = 10

    def move_right(self):
        x = self.xcor()
        x += self.speed
        self.setx(x)
        if x > 280:
            self.setx(280)

    def move_left(self):
        x = self.xcor()
        x -= self.speed
        self.setx(x)
        if x < -280:
            self.setx(-280)

    def speed_increase(self):
        self.speed += 10

    def speed_decrease(self):
        self.speed -= 10


class Enemy(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.speed = 0.1 # x direction speed
        self.speedY = 0.1 # y direction speed
        self.shape("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\invader.gif")
        x = random.randint(-275, 275)
        y = random.randint(200, 275)
        self.setposition(x, y)
        self.heightDiff = 40

    def enemy_motion(self):

        # Moving enemy
        x = self.xcor()
        y = self.ycor()

        # Checking for borders
        if x > 280:
            self.speed *= -1
            y -= self.heightDiff
        elif x < -280:
            self.speed *= -1
            y -= self.heightDiff

        x += self.speed
        self.setposition(x, y)

    def enemy_motion_2(self):
        
        # if scoring.Points() < 100:
        x = self.xcor()
        y = self.ycor()

        if self.speed > 0:
            y -= self.speed
        else:
            y += self.speed
            
        self.setposition(x, y)
        if y < -300:
            x1 = random.randint(-275, 275)
            y1 = random.randint(200, 275)
            self.setposition(x1, y1)

    def enemy_motion_3(self):
        x = self.xcor()
        y = self.ycor()
        x -= self.speed
        y -= self.speedY
        self.setposition(x, y)
        # Checking for borders
        if x > 280:
            self.speed *= -1
            # y -= self.heightDiff
        elif x < -280:
            self.speed *= -1
            # y -= self.heightDiff
        if y < -300:
            x2 = random.randint(-275, 275)
            y2 = random.randint(200, 275)
            self.setposition(x2, y2)


class Border(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(3)
        
    def draw_borders(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()

        for side in range(4):
            self.fd(600)
            self.lt(90)
        self.penup()

    def draw_score_border(self):
        self.penup()
        self.goto(302, 200)
        self.color("black")
        self.pendown()

        for side in range(4):
            self.fd(100)
            self.lt(90)
        self.penup()


class Bullet(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("triangle")
        self.color("yellow")
        self.penup()
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.speed = 1
        self.hideturtle()

    def bullet_position(self):
        x = player.xcor()
        y = player.ycor() + 10
        self.setposition(x, y)
        self.showturtle()
        winsound.PlaySound("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\laser.wav", winsound.SND_ASYNC)

    def isBulletPassed(self):

        if self.ycor() > 280:
            return True
        else:
            return False

    def bullet_motion(self):
        # if self.isBulletPassed == True:
        if self.ycor() > 280:
            self.hiding_bullet()
        else:
            y1 = self.ycor()
            y1 += self.speed
            self.sety(y1)

    # def remaining_bullets(self):
        # rem_bullets = self.no_of_bullets - keypress.shot_pressed
        # return rem_bullets

    def hiding_bullet(self):
        # if isCollision(enemy, bullet) == True:
        self.hideturtle()
        self.setposition(0, 400)


class Score(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.speed(0)
        self.penup()
        self.setposition(-300, 300)
        self.score = 0
        scorestring = "Score : %s" % self.score
        self.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
        self.hideturtle()

    def Points(self):
    
        if Collision().isCollision(bullet, enemy) == True:
            self.score += 10
            scorestring = "Score : %s" % self.score
            self.clear()
            self.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        return self.score

    def return_score(self):
        return self.score

    def check_score(self):
        if self.score < 150:
            return "motion_1"
        elif self.score >= 150 and self.score < 300:
            return "motion_2"
        else:
            return "motion_3"

    def speed_tracking(self):
        if self.score % 100 == 0 and self.score != 0:  # and self.score < 200:
            bullet.speed += 0.1
            if enemy.speed > 0:
                enemy.speed += 0.1
                enemy.speedY += 0.1
            else:
                enemy.speed -= 0.1
                enemy.speedY += 0.1


class Levels(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.speed(0)
        self.penup()
        self.setposition(305, 250)
        self.no_of_bullets = 20
        self.no_of_level = 1
        bullets = "Bullets : %s \n" % self.no_of_bullets
        level = "Level : %s " % self.no_of_level
        self.write(bullets + level, False, align="left", font=("Arial", 14, "normal"))
        self.hideturtle()

    def remaining_bullets(self):
        global youLost
        global rem_bullets

        if rem_bullets < 0:
            youLost = "True"
        else:
            if scoring.return_score() != 0 and scoring.return_score() % 100 == 0 and rem_bullets <= 20:
                rem_bullets += self.no_of_bullets
                bullets = "Bullets : %s \n" % rem_bullets
                self.clear()
                self.write(bullets, False, align="left", font=("Arial", 14, "normal"))

            else:

                bullets = "Bullets : %s \n" % rem_bullets
                self.clear()
                self.write(bullets, False, align="left", font=("Arial", 14, "normal"))


class Collision:

    def isCollision(self, a1, a2):
        dist_x = a1.xcor()-a2.xcor()
        dist_y = a1.ycor()-a2.ycor()
        distance = math.sqrt(math.pow(dist_x, 2)+math.pow(dist_y, 2))
        if distance < 15:
            winsound.PlaySound("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\explosion.wav", winsound.SND_ASYNC)
            return True
        else:
            return False


def pause():

    tkMessageBox.showinfo("Paused", "Press ENTER to continue")


class Key_Press:

    def __init__(self):
        self.shot_pressed = 0
        self.was_pressed = False

    def key_count(self):
        global rem_bullets
        if keyboard.is_pressed('space'):
            if not self.was_pressed:
                self.shot_pressed += 1
                rem_bullets = rem_bullets - 1
                self.was_pressed = True
        else:
            self.was_pressed = False


# region Create objects and Main Variables
player = Player()
bullet = Bullet()
scoring = Score()
Border().draw_borders()
Border().draw_score_border()
levels = Levels()
youLost = "False"
keypress = Key_Press()

rem_bullets = 20

no_of_enemies = 8
enemies = []
for i in range(no_of_enemies):
    enemies.append(Enemy())

enemy = enemies[no_of_enemies-1]
# endregion

# region Keyboard bindings
turtle.listen()
turtle.onkey(player.move_right, "Right")
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.speed_increase, "Up")
turtle.onkey(player.speed_decrease, "Down")
turtle.onkey(bullet.bullet_position, "space")
turtle.onkey(pause, "Escape")
# endregion

wn.tracer(0)

# region Main Loop
while True:

    wn.update()

    for enemy in enemies:

        scoring.Points()
        if scoring.check_score() == "motion_1":
            enemy.enemy_motion()
        elif scoring.check_score() == "motion_2":
            enemy.enemy_motion_2()
        else:
            enemy.enemy_motion_3()

        if Collision().isCollision(enemy, bullet) == True:
            
            bullet.hiding_bullet()
            x = random.randint(-200, 200)
            y = random.randint(200, 250)
            enemy.setposition(x, y)

            # scoring.Points()
            # #Can I make any modifications to increase the efficiency ????
            for enemy in enemies:
                scoring.speed_tracking()
 
        if Collision().isCollision(enemy, player) == True: #or enemy.ycor() <= player.ycor():
            player.hideturtle()
            for enemy in enemies:
                enemy.hideturtle()
            tkMessageBox.showinfo("GAME OVER", "YOU LOST")
            winsound.PlaySound("C:\Users\yasas\Desktop\Python\Space_Invaders_with_Classes\Game_Over.wav", winsound.SND_ASYNC)
            youLost = "True"
            break

    if bullet.isBulletPassed == True:
        bullet.bullet_position()
    bullet.bullet_motion()
    keypress.key_count()

    levels.remaining_bullets()

    if youLost == "True":
        break
# endregion

turtle.done()
