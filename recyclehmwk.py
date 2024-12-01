import pgzrun
import random

WIDTH= 800
HEIGHT= 600

ITEMS= ["byron","mortis","EMZ","frank"]

GAME_STAGE= "start"
CURRENT_LEVEL= 1
FINAL_LEVEL= 6
START_SPEED= 10
items= []
animations= []

def display_message(msg):
    screen.draw.text(msg, fontsize= 45, center= (WIDTH/2, HEIGHT/2), color= "red")


def draw():
    global ITEMS, GAME_STAGE, CURRENT_LEVEL, FINAL_LEVEL, START_SPEED
    screen.clear()
    screen.blit("desert",(0,0))
    if GAME_STAGE == "over":
        display_message("Game Over!/n Try Again!")
    elif CURRENT_LEVEL == FINAL_LEVEL or GAME_STAGE == "win" :
        display_message("You Won!/n Well Done!")


def make_item(number_of_extra_items):
    items_to_create= get_option_to_create(number_of_extra_items)
    new_items= create_items(items_to_create)
    layout_items(new_items)
    animate_item(new_items)
    return new_items

def get_option_to_create (number_of_extra_items):
    items_to_create= ["paper"]
    for i in range(number_of_extra_items):
        option= random.choice(ITEMS)
        items_to_create.append(option)
    return items_to_create

def create_items(items_to_create):
    new_items= []
    for u in (items_to_create):
        item= Actor(u+ "img" )
        new_items.append(item)
    return new_items

def layout_items(items_layout):
    number_of_gaps= len(items_layout)+1
    gap_size= WIDTH/number_of_gaps
    random.shuffle(items_layout)
    for i, item in enumerate(items_layout):
      posx= (i+ 1)* gap_size
      item.x= posx

def animate_item(items_2_animate):
    global animations
    for t in items_2_animate():
        duration= START_SPEED-CURRENT_LEVEL
        t.anchor= ("center", "bottom")
        a= animate(t, duration= duration, on_finished= handle_game_over, y= HEIGHT)
        animations.append(a)

def handle_game_over():
    global GAME_STAGE
    GAME_STAGE= "over"     
pgzrun.go()