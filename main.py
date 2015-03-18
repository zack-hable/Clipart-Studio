#
# Clipart Studio 0.5.1
# Zack Hable
# Python 3.4 & PyGame 1.9.2 Alpha
#


# please note that all print statements are NOT shown in the program window, as pygame makes its own window for graphics
# these are simply left for debug purposes

import pygame, time, os


def resetboxcolor():
            circlebox = pygame.draw.rect(menu, (0, 255, 0), (10, 37, 80, 20))
            boxbox = pygame.draw.rect(menu, (0, 255, 0), (10, 67, 80, 20))
            hold1box = pygame.draw.rect(menu, (0, 255, 0), (10, 97, 80, 20))
            hold2box = pygame.draw.rect(menu, (0, 255, 0), (10, 127, 80, 20))
            hold3box = pygame.draw.rect(menu, (0, 255, 0), (10, 157, 80, 20))
            hold4box = pygame.draw.rect(menu, (0, 255, 0), (10, 187, 80, 20))
            linebox = pygame.draw.rect(menu, (0, 255, 0), (10, 7, 80, 20))
            menu.blit(linetext, (20, 10))
            menu.blit(circletext, (20, 40))
            menu.blit(boxtext, (20, 70))
            menu.blit(hold1text, (20, 100))
            menu.blit(hold2text, (20, 130))
            menu.blit(hold3text, (20, 160))
            menu.blit(hold4text, (20, 190))
            menu.blit(linetext, (20, 10))

def save():
    global work
    export = "EXPORT\export" + str(time.clock()) + ".png"
    print(export)
    pygame.image.save(work, export)

def clear():
    global work,screen,temp,displaynum
    work = pygame.Surface(work.get_size())
    work = work.convert()
    work.fill((255, 255, 255))
    screen.blit(work, (100, 0))
    temp = []
    displaynum = -1
    pygame.display.flip()

pygame.init()  # initialize pygame

os.environ['SDL_VIDEO_WINDOW_POS'] = str('0,19')  # set pygame window to fill entire screen, this should work on any pc
size = [pygame.display.Info().current_w, pygame.display.Info().current_h]  # set screen resolution, this is in pixels
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Paint V0.5 | Zack Hable")  # screen window title

work = pygame.Surface((pygame.display.Info().current_w-100, pygame.display.Info().current_h))  # this is the user work area
work = work.convert()
work.fill((255, 255, 255))  # set work area to white

menu = pygame.Surface((100, pygame.display.Info().current_h))  # this is the menu for paint tools
menu = menu.convert()
menu.fill((50, 50, 50))

font = pygame.font.SysFont("Arial", 15)  # setup font, this can be changed and is applied program wide

# these are program strings/text

linetext = font.render("Line Tool", 1, (10, 10, 10))
circletext = font.render("Circle Tool", 1, (10, 10, 10))
boxtext = font.render("Box Tool", 1, (10, 10, 10))
hold1text = font.render("Flood Tool", 1, (10, 10, 10))
hold2text = font.render("Pencil Tool", 1, (10, 10, 10))
hold3text = font.render("Triangle", 1, (10, 10, 10))
hold4text = font.render("Text", 1, (10, 10, 10))
colortext = font.render("Colors", 1, (0, 255, 0))
thicktext = font.render("Thickness", 1, (0, 255, 0))
thick1text = font.render("1", 1, (10, 10, 10))
thick2text = font.render("2", 1, (10, 10, 10))
thick3text = font.render("3", 1, (10, 10, 10))
thick4text = font.render("4", 1, (10, 10, 10))
thick5text = font.render("5", 1, (10, 10, 10))
thick6text = font.render("6", 1, (10, 10, 10))
cleartext = font.render("Clear Image", 1, (10, 10, 10))
savetext = font.render("Save Image", 1, (10, 10, 10))

# these are the boxes the user can click on for each tool
# "holdboxes" were not implemented right away but were already programmed so it was
# too late to change the variable names

linebox = pygame.draw.rect(menu, (0, 255, 0), (10, 7, 80, 20))
circlebox = pygame.draw.rect(menu, (0, 255, 0), (10, 37, 80, 20))
boxbox = pygame.draw.rect(menu, (0, 255, 0), (10, 67, 80, 20))
hold1box = pygame.draw.rect(menu, (0, 255, 0), (10, 97, 80, 20))
hold2box = pygame.draw.rect(menu, (0, 255, 0), (10, 127, 80, 20))
hold3box = pygame.draw.rect(menu, (0, 255, 0), (10, 157, 80, 20))
hold4box = pygame.draw.rect(menu, (0, 255, 0), (10, 187, 80, 20))

redbox = pygame.draw.rect(menu, (255, 0, 0), (15, 277, 30, 20))
bluebox = pygame.draw.rect(menu, (0, 0, 255), (55, 277, 30, 20))
orangebox = pygame.draw.rect(menu, (255, 102, 0), (15, 307, 30, 20))
greenbox = pygame.draw.rect(menu, (0, 255, 0), (55, 307, 30, 20))
yellowbox = pygame.draw.rect(menu, (255, 255, 0), (15, 337, 30, 20))
purplebox = pygame.draw.rect(menu, (128, 0, 128), (55, 337, 30, 20))
whitebox = pygame.draw.rect(menu, (255, 255, 255), (15, 367, 30, 20))
blackbox = pygame.draw.rect(menu, (1, 1, 1), (55, 367, 30, 20))
cyanbox = pygame.draw.rect(menu, (0, 255, 255), (15, 397, 30, 20))
pinkbox = pygame.draw.rect(menu, (255, 182, 193), (55, 397, 30, 20))

thick1box = pygame.draw.rect(menu, (0, 255, 0), (15, 447, 30, 20))
thick2box = pygame.draw.rect(menu, (0, 255, 0), (55, 447, 30, 20))
thick3box = pygame.draw.rect(menu, (0, 255, 0), (15, 477, 30, 20))
thick4box = pygame.draw.rect(menu, (0, 255, 0), (55, 477, 30, 20))
thick5box = pygame.draw.rect(menu, (0, 255, 0), (15, 507, 30, 20))
thick6box = pygame.draw.rect(menu, (0, 255, 0), (55, 507, 30, 20))

clearbox = pygame.draw.rect(menu, (0, 255, 0), (10, 540, 80, 20))
savebox = pygame.draw.rect(menu, (0, 255, 0), (10, 570, 80, 20))

# this is 'blitting' or attaching each box/text to the menu

menu.blit(linetext, (20, 10))
menu.blit(circletext, (20, 40))
menu.blit(boxtext, (20, 70))
menu.blit(hold1text, (20, 100))
menu.blit(hold2text, (20, 130))
menu.blit(hold3text, (20, 160))
menu.blit(hold4text, (20, 190))
menu.blit(colortext, (30, 250))
menu.blit(thicktext, (15, 430))
menu.blit(thick1text, (27, 450))
menu.blit(thick2text, (67, 450))
menu.blit(thick3text, (27, 480))
menu.blit(thick4text, (67, 480))
menu.blit(thick5text, (27, 510))
menu.blit(thick6text, (67, 510))
menu.blit(cleartext, (15, 545))
menu.blit(savetext, (15, 575))
screen.blit(menu, (0, 0))
screen.blit(work, (100, 0))

pygame.display.flip()  # this renders the "blitted" actions done above
# this line above is very important to understand with pygame
# you MUST display.flip for your items to appear/render, NOT like TB

# setting default application values
mode = 0
color = [1, 1, 1]
thick = 2
text = ""
mod = 0
displaynum = -1
temp = []

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:  # if user presses "X" in top right
        pygame.quit()
    elif ev.type == pygame.KEYDOWN:  # if user presses a key
        while True:
            ev2 = pygame.event.poll()
            if ev2.type == pygame.KEYDOWN:  # SPECIAL FUNCTION KEY COMBOS
                key = str(pygame.key.name(ev2.key))
                mod = pygame.key.get_mods()
                print(key, mod)
                if mod == 64 or mod == 128:  # CTRL KEYS, 64 = left, 128 = right
                    if key == "z":  # this is the "CRTL Z" support, to undo your last action
                        # this works by making a new window every time a user adds a line/box/etc and then is saved to a list
                        # so we just loop from the beginning window to the current window
                        print("UNDO", displaynum)
                        work = pygame.Surface((pygame.display.Info().current_w-100, pygame.display.Info().current_h))
                        work = work.convert()
                        work.fill((255, 255, 255))
                        for i in range(0, displaynum):
                            work.blit(temp[i], (0, 0))
                            print(i, "ADDED!")
                        print("DONE!")
                        if displaynum > -1: displaynum -= 1
                        screen.blit(work, (100, 0))
                        pygame.display.flip()
                    elif key == "s":
                        save()
                    elif key == "w":
                        clear()
                    break
    elif ev.type == pygame.MOUSEBUTTONDOWN:  # if user pressed their mouse
        mosx = pygame.mouse.get_pos()[0]  # getting mouse x/y coordinates
        mosy = pygame.mouse.get_pos()[1]  # another very important note, pygame works up -> down, so (1,1) is in the top left
        print(mosx, mosy)
        # these statements turn the corresponding box from green to blue
        # it also sets the other boxes back to green, in a newer update I plan to just make them into a function to save space
        # then enable that "mode" for the tool the user selected
        if mosx >= 10 and mosx <= 90 and mosy >= 7 and mosy <= 27:
            resetboxcolor()
            linebox = pygame.draw.rect(menu, (0, 0, 255), (10, 7, 80, 20))
            menu.blit(linetext, (20, 10))
            screen.blit(menu, (0, 0))
            pygame.display.flip()
            mode = 1
            print("LINE MODE!")
        elif mosx >= 10 and mosx <= 90 and mosy >= 37 and mosy <= 57:
            resetboxcolor()
            circlebox = pygame.draw.rect(menu, (0, 0, 255), (10, 37, 80, 20))
            menu.blit(circletext, (20, 40))
            screen.blit(menu, (0, 0))
            pygame.display.flip()
            mode = 2
            print("CIRCLE MODE!")
        elif mosx >= 10 and mosx <= 90 and mosy >= 67 and mosy <= 87:
            resetboxcolor()
            boxbox = pygame.draw.rect(menu, (0, 0, 255), (10, 67, 80, 20))
            menu.blit(boxtext, (20, 70))
            screen.blit(menu, (0, 0))
            pygame.display.flip()
            mode = 3
            print("BOX MODE!")
        elif mosx >= 10 and mosx <= 90 and mosy >= 97 and mosy <= 117:
            resetboxcolor()
            hold1box = pygame.draw.rect(menu, (0, 0, 255), (10, 97, 80, 20))
            menu.blit(hold1text, (20, 100))
            screen.blit(menu, (0, 0))
            pygame.display.flip()
            mode = 4
            print("FLOOD MODE!")
        elif mosx >= 10 and mosx <= 90 and mosy >= 127 and mosy <= 147:
            resetboxcolor()
            hold2box = pygame.draw.rect(menu, (0, 0, 255), (10, 127, 80, 20))
            menu.blit(hold2text, (20, 130))
            screen.blit(menu, (0, 0))
            pygame.display.flip()
            mode = 5
            print("PENCIL MODE!")
        elif mosx >= 10 and mosx <= 90 and mosy >= 157 and mosy <= 177:
            resetboxcolor()
            hold3box = pygame.draw.rect(menu, (0, 0, 255), (10, 157, 80, 20))
            menu.blit(hold3text, (20, 160))
            screen.blit(menu, (0, 0))
            pygame.display.flip()
            mode = 6
            print("TRIANGLE MODE!")
        elif mosx >= 10 and mosx <= 90 and mosy >= 187 and mosy <= 207:
            resetboxcolor()
            hold4box = pygame.draw.rect(menu, (0, 0, 255), (10, 187, 80, 20))
            menu.blit(hold4text, (20, 190))
            screen.blit(menu, (0, 0))
            pygame.display.flip()
            mode = 7
            print("HOLD MODE!")
        # these are the color choices, once clicked they change the current color of the tool
        elif mosx >= 15 and mosx <= 45 and mosy >= 277 and mosy <= 297:
            color = [255, 0, 0]
        elif mosx >= 55 and mosx <= 85 and mosy >= 277 and mosy <= 297:
            color = [0, 0, 255]
        elif mosx >= 15 and mosx <= 45 and mosy >= 307 and mosy <= 327:
            color = [255, 102, 0]
        elif mosx >= 55 and mosx <= 85 and mosy >= 307 and mosy <= 327:
            color = [0, 255, 0]
        elif mosx >= 15 and mosx <= 45 and mosy >= 337 and mosy <= 357:
            color = [255, 255, 0]
        elif mosx >= 55 and mosx <= 85 and mosy >= 337 and mosy <= 357:
            color = [128, 0, 128]
        elif mosx >= 15 and mosx <= 45 and mosy >= 367 and mosy <= 387:
            color = [255, 255, 255]
        elif mosx >= 55 and mosx <= 85 and mosy >= 367 and mosy <= 387:
            color = [1, 1, 1]
        elif mosx >= 15 and mosx <= 45 and mosy >= 397 and mosy <= 417:
            color = [0, 255, 255]
        elif mosx >= 55 and mosx <= 85 and mosy >= 397 and mosy <= 417:
            color = [255, 182, 193]
        # these change line thickness
        elif mosx >= 15 and mosx <= 45 and mosy >= 447 and mosy <= 467:
            thick = 1
        elif mosx >= 55 and mosx <= 85 and mosy >= 447 and mosy <= 467:
            thick = 2
        elif mosx >= 15 and mosx <= 45 and mosy >= 477 and mosy <= 497:
            thick = 3
        elif mosx >= 55 and mosx <= 85 and mosy >= 477 and mosy <= 497:
            thick = 4
        elif mosx >= 15 and mosx <= 45 and mosy >= 507 and mosy <= 527:
            thick = 5
        elif mosx >= 55 and mosx <= 85 and mosy >= 507 and mosy <= 527:
            thick = 6
        # this statement clears the screen, sets it back to default values
        elif mosx >= 10 and mosx <= 90 and mosy >= 540 and mosy <= 560:
            clear()
        # this currently exports the image, I have plans to make it more user friendly
        # as of now to avoid overwriting other projects I export the image as
        # "export" + the current time (very unlikely there are any files with this name)
        elif mosx >= 10 and mosx <= 90 and mosy >= 570 and mosy <= 590:
            save()
        # this is when the user clicks inside the "work" window
        elif mosx >= 100 and mosx <= pygame.display.Info().current_w and mosy >=0 and mosy <= pygame.display.Info().current_h:
            print("DRAW")
            while True:
                ev = pygame.event.poll()
                if ev.type == pygame.MOUSEBUTTONUP:
                    mosx2 = pygame.mouse.get_pos()[0]
                    mosy2 = pygame.mouse.get_pos()[1]
                    temp.append(0)
                    displaynum += 1  # out current display number/window indice
                    print("DISPLAY:", displaynum)
                    temp[displaynum] = pygame.Surface((pygame.display.Info().current_w-100, pygame.display.Info().current_h), pygame.SRCALPHA, 32)
                    temp[displaynum] = temp[displaynum].convert_alpha()  # making our work windows transparent, used in my CRTL Z concept
                    if mode == 1:  # draw a line
                        pygame.draw.line(temp[displaynum], color, (mosx-100, mosy), (mosx2-100, mosy2), thick)
                    elif mode == 2:  # draw a circle
                        op1 = abs(mosx2 - mosx)  # I had to use ABS due to a user moving backward on the x/y axis
                        op2 = abs(mosy2 - mosy)
                        if op1 > op2:
                            pygame.draw.circle(temp[displaynum], color, (mosx-100, mosy), op1)
                        else:
                            pygame.draw.circle(temp[displaynum], color, (mosx-100, mosy), op2)
                    elif mode == 3:  # draw a rectangle
                        pygame.draw.rect(temp[displaynum], color, (mosx-100, mosy, mosx2-mosx, mosy2 - mosy))
                    elif mode == 4:  # fill the entire screen with a color
                        temp[displaynum].fill(color)
                    elif mode == 5:  # pencil tool, keeps adding dots until user lets go of their mouse
                        while True:
                            ev2 = pygame.event.poll()
                            if ev2.type == pygame.MOUSEBUTTONUP or ev2.type == pygame.MOUSEBUTTONDOWN:
                                break
                            mosx2 = pygame.mouse.get_pos()[0]
                            mosy2 = pygame.mouse.get_pos()[1]
                            pygame.draw.line(temp[displaynum], color, (mosx2-100, mosy2), (mosx2-100, mosy2), thick)
                            screen.blit(temp[displaynum], (100, 0))
                            pygame.display.flip()
                    elif mode == 6:  # this is the triangle tool, making use of pygame's custom ploygon function
                        pygame.draw.polygon(temp[displaynum], color, [(mosx-100, mosy), (mosx2-100, mosy), (mosx2-100, mosy2), (mosx-100, mosy)])
                    elif mode == 7:  # this is the text input, as of now it works, but not fully (for example no shift support)
                        while True:
                            ev2 = pygame.event.poll()
                            if ev2.type == pygame.KEYDOWN:
                                key = str(pygame.key.name(ev2.key))
                                if key == "return":
                                    text = ""
                                    break
                                elif key == "delete" or key == "backspace":
                                    text = text[0:len(text)-1]
                                    # screen.blit(work, (100, 0))
                                    pygame.display.flip()
                                    print("SPECIAL KEY NOT SUPPORTED!")
                                elif key == "right shift" or key == "left shift":
                                    print("SPECIAL KEY NOT SUPPORTED!", pygame.key.get_mods())
                                elif key == "space":
                                    text += " "
                                    mess = font.render(text, 1, color)
                                    temp[displaynum].blit(mess, (mosx-100, mosy))
                                    # screen.blit(work, (100, 0))
                                    pygame.display.flip()
                                else:
                                    text += key
                                    mess = font.render(text, 1, color)
                                    temp[displaynum].blit(mess, (mosx-100, mosy))
                                    #screen.blit(work, (100, 0))
                                    pygame.display.flip()
                                    mod = 0
                            work.blit(temp[displaynum], (0,0))
                            screen.blit(work, (100, 0))
                            pygame.display.flip()
                    # this applies all of the updates the user has done above          
                    work.blit(temp[displaynum], (0, 0))
                    screen.blit(work, (100, 0))
                    pygame.display.flip()
                    break

    elif ev.type == pygame.VIDEORESIZE:  # if user changes the window size
        if ev.w > 800 and ev.h > 600:
            size = ev.size
            work = pygame.Surface((ev.w-100, ev.h))  # this is the user work area
            work = work.convert()
            work.fill((255, 255, 255))  # set work area to white
            for i in range(0, displaynum+1):
                print("DISPLAY RESTORED:", i)
                temp[i] = pygame.transform.scale(temp[i], (ev.w-100, ev.h))
                work.blit(temp[i], (0, 0))
            screen.blit(work, (100, 0))
            # IMPORTANT: I need to resize the 'menu' window here, support for work area is complete
            pygame.display.flip()
            print("RESIZED!")
        else:  # if user tries to go below our needed resolution we go back to last known good resolution
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            pygame.display.set_caption("Paint V0.5 | Zack Hable")  # screen window title
            screen.blit(menu, (0, 0))
            screen.blit(work, (100, 0))
            pygame.display.flip()
