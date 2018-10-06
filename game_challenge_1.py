from aluLib import *

window_width = 1000
window_height = 500


# drawing rectangle left and right paddles
paddle_width = 20
paddle_height = 100
left_paddle_y = 0
right_paddle_y = 0


def paddles():

    global left_paddle_y, right_paddle_y, window_height, window_width
    disable_stroke()
    set_clear_color(0, 0.529, 0.318)
    clear()
    set_fill_color(1, 0, 0)

    # left paddle
    draw_rectangle(0, left_paddle_y, paddle_width, paddle_height)

    # right paddle
    draw_rectangle(window_width - paddle_width, right_paddle_y, paddle_width, paddle_height)

    # paddle movement

    # key "a" moves left paddle up
    if is_key_pressed("z"):
        if left_paddle_y < window_height - paddle_height:
            left_paddle_y += 3

    # key "z" moves left paddles down
    elif is_key_pressed("a"):
        if left_paddle_y > 0:
            left_paddle_y -= 3

    # key "k" moves right paddle up
    elif is_key_pressed("m"):
        if right_paddle_y < window_height - paddle_height:
            right_paddle_y += 3

    # key "m" moves right paddle down
    elif is_key_pressed("k"):
        if right_paddle_y > 0:
            right_paddle_y -= 3

# drawing the ball and its movement


ball_x = window_width // 2
ball_y = window_height // 2
min_x = 10
max_x = window_width - min_x
ball_r = 10
speed = 0
start_it = False
move_ball_x = 2
move_ball_y = 2


def ball():
    global start_it, ball_x, ball_y, ball_r, speed, move_ball_x, move_ball_y
    # drawing the ball
    draw_circle(ball_x, ball_y, ball_r)
    # when space bar is pressed make the game start
    if is_key_pressed(" "):
        start_it = True
        ball_x = window_width // 2
        ball_y = window_height // 2
    if start_it:
        ball_x += move_ball_x
        ball_y += move_ball_y

        # bouncing the ball back in diagonal manner in case of hitting the top or bottom of the window
        if ball_y == window_height or ball_y == 0:
            move_ball_y *= -1

        # make ball stop (game_over) in case of hitting right or left conner
        if ball_x == window_width or ball_x == 0:
            start_it = False
            speed = 0
            move_ball_x = 2

        # bouncing the ball back when it has hit any of the paddles
        if (ball_y >= right_paddle_y and ball_y <= right_paddle_y + paddle_height + ball_r) and ball_x == window_width - paddle_width:
            move_ball_x *= -1
            speed += 1
        if (ball_y >= left_paddle_y and ball_y <= left_paddle_y + paddle_height + ball_r) and ball_x == paddle_width:
            move_ball_x *= -1
            speed += 1

        # increasing the speed in case of bouncing from paddles 4 times
        if speed % 4 == 0 and speed != 0:
            move_ball_x += 1
            speed = 0
    # quiting the whole game
    if is_key_pressed("q"):
        cs1_quit()

def pong_game():
    paddles()
    ball()



start_graphics(pong_game, width=window_width, height=window_height, framerate=100)
