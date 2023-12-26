from time import sleep
from ursina import *
import random as r
import os

filename = 'highest_score.txt'

colors = [color.white, color.black, color.gray, color.light_gray, color.dark_gray, color.red, color.green, color.blue,
          color.cyan, color.magenta, color.yellow, color.orange, color.olive, color.lime, color.pink, color.gold,
          color.turquoise, color.violet]


def get_highest_score():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            score_str = file.readline().strip()  # Remove whitespace and newlines
            try:
                # Convert to float and round to nearest integer
                score = round(float(score_str))
                return score
            except ValueError:
                return 0  # Handle non-numeric input
    else:
        return 0


def update_highest_score(score):
    with open(filename, 'w') as file:
        file.write(str(score))


app = Ursina()

music = Audio('audios/flappy.mp3', loop=True, autoplay=True)

highest_score = get_highest_score()
bird = Animation('models\\img',
                 scale=(2, 2, 2),
                 y=10)

box = Animation('models/box',
                collider='box',
                scale=(1.2, 1.2, 1),
                y=10, enabled=False)

camera.orthographic = True
camera.fov = 20

level = 1

delay = 2.5
speed = 5
jump = 6
gravity = 20

vsp = 0
score = 0

score_text = Text(
    text=f"Dro3: {int(score)}\nHighest: {int(highest_score)}", position=(-0.85, 0.4), scale=2)

music_on = Animation('models/on',
                     scale=(1, 1, 1),
                     y=9, x=-16.5, enabled=True)
music_off = Animation('models/off',
                      scale=(1, 1, 1),
                      y=9, x=-16.5, enabled=False)
game_over_text = Text(text='m', position=(0, 0), scale=2,
                      origin=(16.5, -9))

ahh = Audio('audios/ahhh.mp3', autoplay=False, loop=False)
pas = Audio('audios/pass.mp3', autoplay=False, loop=False)
pas.volume = 1

pipes = []

pipe = Entity(model='quad',
              color=color.white33,
              texture='white_cube',
              position=(20, 10),
              scale=(3, 15, 1),
              collider='box')

pipe.passed = False

game_over = False
game_over_text = Text(
    text='Press R to restart\n\n Press Esc to Quit', position=(
        0, 0), scale=2, enabled=False, origin=(
        0, 0))


def reset_game():
    global vsp, score, pipes, game_over, level
    level = 1
    vsp = 0
    score = 0
    score_text.text = f"Dro3: {int(score)}\nHighest: {int(highest_score)}"

    for p in pipes:
        destroy(p)
    pipes = []

    bird.position = (0, 10)
    bird.y = 10
    bird.rotation = (0, 0, 0)
    bird.animate_position((0, 0), duration=0.5, curve=curve.out_expo)
    bird.animate_scale((2, 2, 2), duration=0.5, curve=curve.out_expo)
    bird.animate_rotation_z(360, duration=0.5, curve=curve.out_expo)

    game_over = False
    game_over_text.enabled = False


def update():
    global vsp, score, speed, game_over, gravity, level, delay, jump, highest_score
    if score > 19:
        for p in pipes:
            p.color = random.choice(colors)

    if score > highest_score:
        # Update the highest score with the player's score
        highest_score = score
        # Write the updated highest score to the file
        update_highest_score(highest_score)

    if level == 1:
        delay = 2.5
        speed = 5
        jump = 6
        gravity = 20

    if score == 18:
        delay = 4

    if score == 19:
        jump = 9

    if score == 38:
        delay == 3

    if score == 39:
        jump = 15

    if level == 2:
        delay = 1.5
        speed = 15
        jump = 9
        gravity = 20

    if level == 3:
        delay = 1
        speed = 20
        jump = 15
        gravity = 30

    if score == 20:
        level = 2
    if score == 40:
        level = 3
    box.y = bird.y
    box.x = bird.x
    if not game_over:
        vsp -= gravity * time.dt
        bird.y += vsp * time.dt
        for p in pipes:
            p.x = p.x - speed * time.dt
            if p.x < bird.x and not p.passed:
                p.passed = True
                score += 0.5
                pas.play()
                if score <= highest_score:
                    score_text.text = f"Dro3: {int(score)}\nHighest: {int(highest_score)}"
                else:
                    score_text.text = f"Dro3: {int(score)}\nHighest: {int(highest_score) + 1}"
        touch = box.intersects()
        if touch.hit or bird.y < -10 or bird.y > 10:
            game_over_text.text = 'Press R to restart\n\n Press Esc to Quit'
            if music_on.enabled:
                music.volume = 0

            ahh.play()
            sleep(2)
            ahh.stop()

            if music_on.enabled:
                music.volume = 1
            game_over = True
            game_over_text.enabled = True


def input(key):
    global vsp
    if key == 'm':
        toggle_music()
    if not game_over:
        if key == 'space':
            vsp = jump
    if game_over:
        if key == 'r' or key == 'space':  # Pressing 'r' resets the game
            reset_game()
        if held_keys['escape']:
            application.quit()


def newPipe():
    global delay, colors
    y = r.randint(4, 16)
    new1 = duplicate(pipe, y=y)
    new2 = duplicate(pipe, y=y - 22)
    pipes.extend((new1, new2))
    if score == 18:
        new1.color = color.red
        new2.color = color.red

    setattr(new1, 'passed', False)
    setattr(new2, 'passed', False)
    invoke(newPipe, delay=delay)


def toggle_music():
    if music.volume == 0:
        music_off.enabled = False
        music_on.enabled = True
        music.volume = 1

    else:
        music_off.enabled = True
        music_on.enabled = False
        music.volume = 0


game_over = True
game_over_text = Text(text='Start', position=(0, 0), scale=2,
                      origin=(0, 0))


def main():
    newPipe()

    app.run()


if __name__ == "__main__":
    main()
