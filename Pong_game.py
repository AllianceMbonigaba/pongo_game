from aluLib import *

window_width = 500
window_height = 500


# drawing rectangle left and right paddles
paddle_width = window_width / 9
paddle_height = window_height / 7
left_paddle_y = 0
right_paddle_y = 0
min_y = 10
max_y = window_height - min_y



def paddles():

    global left_paddle_y, right_paddle_y, min_y, min_x, window_height
    disable_stroke()
    clear()
    set_fill_color(1, 0, 0)

    # left paddle
    draw_rectangle(0, left_paddle_y, paddle_width, paddle_height)

    # right paddle
    draw_rectangle(window_width - paddle_width, right_paddle_y, paddle_width, paddle_height)

    # paddle movement

    # key "a" moves left paddle up
    if is_key_pressed("a"):
        if left_paddle_y < window_height - paddle_height:
            left_paddle_y += 3

    # key "z" moves left paddles down
    elif is_key_pressed("z"):
        if left_paddle_y > 0:
            left_paddle_y -= 3

    # key "k" moves right paddle up
    elif is_key_pressed("k"):
        if right_paddle_y < window_height - paddle_height:
            right_paddle_y += 3

    # key "m" moves right paddle down
    elif is_key_pressed("m"):
        if right_paddle_y > 0:
            right_paddle_y -= 3

# drawing the ball and its movement


ball_x = window_width / 2
ball_y = window_width / 2
min_x = 10
max_x = window_width - min_x
move_ball = 1


def ball():
    global ball_x, ball_y, min_x, max_x, move_ball, max_y, min_y, try_again
    draw_circle(ball_x, ball_y, 10)

    if ball_x > min_x and ball_x < max_x:
        ball_x += 1
        ball_y += 0.3
    # defining how to fail in the game
    elif ball_x > min_x or ball_x > max_x:
        clear()


    elif ball_x == max_y or ball_x == min_x:
        ball_x -= 2
        ball_y += 0.3


def paddle_contact():
    global ball_x, ball_y, right_paddle_y, left_paddle_y
    if right_paddle_y >= ball_y or ball_y <= paddle_height and ball_x == (window_width - paddle_width):
        ball_x -= 2
        ball_y -= 0.3

    elif left_paddle_y >= ball_y or ball_y <= paddle_height and ball_x == window_width - paddle_width:
        ball_x -= 2
        ball_y -= 0.3












def pong_game():

    paddles()
    ball()
    paddle_contact()


start_graphics(pong_game, width=window_width, height=window_height, framerate= 100)
