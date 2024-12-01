import pgzrun
import random

WIDTH= 800
HEIGHT= 600

ITEMS= ["bag","battery","chips","bottle"]

GAME_STAGE= "start"
CURRENT_LEVEL= 1
FINAL_LEVEL= 6
START_SPEED= 10
items= []
animations= []

def display_message(msg):
    screen.draw.text(msg, fontsize= 45, center= (WIDTH/2, HEIGHT/2), color= "red")

def draw():
    global ITEMS, GAME_STAGE, CURRENT_LEVEL, FINAL_LEVEL, START_SPEED, items
    screen.clear()
    screen.blit("bground",(0,0))
    if GAME_STAGE == "over":
        display_message("Game Over!\n Try Again!")
    elif CURRENT_LEVEL == FINAL_LEVEL or GAME_STAGE == "win" :
        display_message("You Won! Well Done!")
    else:
        for h in items:
            h.draw()

def update():
    global items
    if len(items)== 0:
        items= make_item(CURRENT_LEVEL)

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
    '''print("update")'''
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
    for t in items_2_animate:
        duration= START_SPEED-CURRENT_LEVEL
        t.anchor= ("center", "bottom")
        a= animate(t, duration= duration, on_finished= handle_game_over, y= HEIGHT)
        animations.append(a)

def handle_game_over():
    global GAME_STAGE
    GAME_STAGE= "over"

def stop_animation(animations_2_stop):
    for w in animations_2_stop:
        print(w.running)
        if w.running:
            w.stop()

def handle_game_complete():
    global CURRENT_LEVEL, items, animations, GAME_STAGE
    stop_animation(animations)
    if CURRENT_LEVEL== FINAL_LEVEL:
        GAME_STAGE= "win"
    else:
        CURRENT_LEVEL= CURRENT_LEVEL+ 1
        animations= []
        items= []

def on_mouse_down(pos):
    #position is co-ordinates of mouse where it is clicked
    global items, CURRENT_LEVEL
    for x in items:
        if x.collidepoint(pos):
            if "paper" in x.image:
                handle_game_complete()
            else:
                handle_game_over()








pgzrun.go()