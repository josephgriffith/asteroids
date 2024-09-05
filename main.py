import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from random import randrange
from time import sleep

def main():
    print('Starting asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    frames = 0
    pygame.font.init()
    font = pygame.font.Font('/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf', 16)
    
    started = False
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    ordinance = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, rocks)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, ordinance)
    started = True

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    # print(player.containers)
    # sizes = [4,8,16,32]
    # asteroids = Asteroid(randrange(0, SCREEN_WIDTH), randrange(0, SCREEN_HEIGHT), randrange(8, 32, 8))



    #attempting to display a grid of colors with names and RGB
    clist = []                                  
    w, h, = 320, 16
    os = 0
    coord = (os,os)
    col, row = 0, 0
    for cname in colors:
        p = (coord[0]+col*w, coord[1]+row*h)
        row += 1
        rec = pygame.Rect(p[0], p[1], int(2*w), int(2*h))
        rgb = pygame.Color(cname)
        rgb = [rgb.r, rgb.g, rgb.b]
        # print((col, row), p, cname, rgb, row*h%SCREEN_HEIGHT, SCREEN_HEIGHT-h)
        print(cname, rgb)
        clist.append((p, cname, rec, rgb))
        if p[1] >= SCREEN_HEIGHT-h:
            row = 0
            col += 1
        if p[0] >= SCREEN_WIDTH-w-2*os:
            pass
            # break



    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        
        # frames += 1
        screen.fill('midnight blue')
        # screen.blit(font.render(str(frames), False, (32, 32, 32)), (20,20))
        # screen.blit(font.render(str(player.rotation), False, (32, 32, 32)), (20,50))

        # for u in updatables:
        #     u.update(dt)
        # for d in drawables:
        #     d.draw(screen)
        # for col in rocks:
        #     if player.collision(col):
        #         # fails to display YOU DIED unless ship is inside the asteroid or something??? 
        #         screen.blit(font.render('YOU DIED.', False, (255, 128, 128)), (SCREEN_WIDTH/2-20, SCREEN_HEIGHT/2-10))
        #         sleep(2)
        #         # sys.exit('Game over!')
        #     for b in ordinance:
        #         if col.collision(b):
        #             col.split()
        #             b.kill()

        # for s in ordinance:
        #     if player.collision(s):
        #         screen.blit(font.render('YOU DIED.', False, (255, 128, 128)), (SCREEN_WIDTH/2-20, SCREEN_HEIGHT/2-10))
        #         sleep(2)
        #         sys.exit('Game over!')
                

        # print(player.position)

        
        for c in clist:
            pygame.draw.rect(screen, c[1], c[2])
            #TODO: FONT COLOR THAT ALWAYS SHOWS UP
            rgb = c[3]
            
            d = 0
            # Counting the perceptive luminance - human eye favors green color...      
            luminance = (0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2])/255
            if luminance > 0.5:
                d = 32 # bright colors - black font
            # elif luminance > .33:
            #     d = 128
            else:
                d = 223 # dark colors - white font                        
            text = font.render(str(c[1])+", "+str(c[3]), False, pygame.Color(d, d, d))
            # text = font.render(str(c[1])+", "+str(c[3]), False, pygame.Color(255-rgb[0], 255-rgb[1], 255-rgb[2]))     #fails on mid greys
            w2 = text.get_rect().width
            screen.blit(text, (c[0][0]+.5*w-.5*w2, c[0][1]))

        pygame.display.flip()
        dt = clock.tick(5)/1000        #FPS

        # playing = False


def initGame(started):
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        rocks = pygame.sprite.Group()
        ordinance = pygame.sprite.Group()
        Player.containers = (updatables, drawables)
        Asteroid.containers = (updatables, drawables, rocks)
        AsteroidField.containers = (updatables)
        Shot.containers = (updatables, drawables, ordinance)









colors = [
"white",
"gray",
"darkgray",
"darkgrey",
"dimgray",
"dimgrey",
"black",
"gray0",
"gray1",
"gray2",
"gray3",
"gray4",
"gray5",
"gray6",
"gray7",
"gray8",
"gray9",
"gray10",
"gray11",
"gray12",
"gray13",
"gray14",
"gray15",
"gray16",
"gray17",
"gray18",
"gray19",
"gray20",
"gray21",
"gray22",
"gray23",
"gray24",
"gray25",
"gray26",
"gray27",
"gray28",
"gray29",
"gray30",
"gray31",
"gray32",
"gray33",
"gray34",
"gray35",
"gray36",
"gray37",
"gray38",
"gray39",
"gray40",
"gray41",
"gray42",
"gray43",
"gray44",
"gray45",
"gray46",
"gray47",
"gray48",
"gray49",
"gray50",
"gray51",
"gray52",
"gray53",
"gray54",
"gray55",
"gray56",
"gray57",
"gray58",
"gray59",
"gray60",
"gray61",
"gray62",
"gray63",
"gray64",
"gray65",
"gray66",
"gray67",
"gray68",
"gray69",
"gray70",
"gray71",
"gray72",
"gray73",
"gray74",
"gray75",
"gray76",
"gray77",
"gray78",
"gray79",
"gray80",
"gray81",
"gray82",
"gray83",
"gray84",
"gray85",
"gray86",
"gray87",
"gray88",
"gray89",
"gray90",
"gray91",
"gray92",
"gray93",
"gray94",
"gray95",
"gray96",
"gray97",
"gray98",
"gray99",
"gray100",


"floralwhite",
"ghostwhite",
"whitesmoke",
"antiquewhite1",
"antiquewhite",
"navajowhite",
"navajowhite1",
"antiquewhite2",
"navajowhite2",
"antiquewhite3",
"navajowhite3",
"antiquewhite4",
"navajowhite4",

"tan",
"lightsalmon",
"lightsalmon1",
"tan1",
"sandybrown",
"orange",
"orange1",
"palevioletred1",
"lightsalmon2",
"salmon1",
"tan2",
"salmon",
"orange2",
"sienna1",
"palevioletred2",
"coral",
"salmon2",
"darkorange",
"chocolate1",
"coral1",
"darkorange1",
"indianred1",
"sienna2",
"lightsalmon3",
"palevioletred",
"peru",
"tan3",
"chocolate2",
"coral2",
"tomato",
"tomato1",
"indianred2",
"darkorange2",
"orange3",
"palevioletred3",
"salmon3",
"tomato2",
"violetred1",
"sienna3",
"chocolate",
"indianred",
"chocolate3",
"coral3",
"darkorange3",
"violetred2",
"brown1",
"indianred3",
"orangered",
"orangered1",
"tomato3",
"brown2",
"firebrick1",
"orangered2",
"violetred3",
"firebrick2",
"sienna",
"lightsalmon4",
"tan4",
"violetred",
"brown3",
"orange4",
"palevioletred4",
"orangered3",
"salmon4",
"firebrick3",
"sienna4",
"mediumvioletred",
"crimson",
"saddlebrown",
"chocolate4",
"coral4",
"indianred4",
"darkorange4",
"brown",
"tomato4",
"firebrick",
"red",
"red1",
"red2",
"violetred4",
"brown4",
"orangered4",
"red3",
"firebrick4",
"darkred",
"red4",
"darkgreen",
"darkolivegreen",
"darkolivegreen1",
"darkolivegreen2",
"darkolivegreen3",
"darkolivegreen4",
"darkseagreen",
"darkseagreen1",
"darkseagreen2",
"darkseagreen3",
"darkseagreen4",
"forestgreen",
"green",
"green1",
"green2",
"green3",
"green4",
"greenyellow",
"lawngreen",
"lightgreen",
"lightseagreen",
"limegreen",
"mediumseagreen",
"mediumspringgreen",
"palegreen",
"palegreen1",
"palegreen2",
"palegreen3",
"palegreen4",
"seagreen",
"seagreen1",
"seagreen2",
"seagreen3",
"seagreen4",
"springgreen",
"springgreen1",
"springgreen2",
"springgreen3",
"springgreen4",
"yellowgreen",
"aliceblue",
"blue",
"blue1",
"blue2",
"blue3",
"blue4",
"blueviolet",
"cadetblue",
"cadetblue1",
"cadetblue2",
"cadetblue3",
"cadetblue4",
"cornflowerblue",
"darkblue",
"darkslateblue",
"deepskyblue",
"deepskyblue1",
"deepskyblue2",
"deepskyblue3",
"deepskyblue4",
"dodgerblue",
"dodgerblue1",
"dodgerblue2",
"dodgerblue3",
"dodgerblue4",
"lightblue",
"lightblue1",
"lightblue2",
"lightblue3",
"lightblue4",
"lightskyblue",
"lightskyblue1",
"lightskyblue2",
"lightskyblue3",
"lightskyblue4",
"lightslateblue",
"lightsteelblue",
"lightsteelblue1",
"lightsteelblue2",
"lightsteelblue3",
"lightsteelblue4",
"mediumblue",
"mediumslateblue",
"midnightblue",
"navyblue",
"powderblue",
"royalblue",
"royalblue1",
"royalblue2",
"royalblue3",
"royalblue4",
"skyblue",
"skyblue1",
"skyblue2",
"skyblue3",
"skyblue4",
"slateblue",
"slateblue1",
"slateblue2",
"slateblue3",
"slateblue4",
"steelblue",
"steelblue1",
"steelblue2",
"steelblue3",
"steelblue4",
"aqua",
"aquamarine",
"aquamarine1",
"aquamarine2",
"aquamarine3",
"aquamarine4",
"azure",
"azure1",
"azure2",
"azure3",
"azure4",
"beige",
"bisque",
"bisque1",
"bisque2",
"bisque3",
"bisque4",
"blanchedalmond",
"burlywood",
"burlywood1",
"burlywood2",
"burlywood3",
"burlywood4",
"chartreuse",
"chartreuse1",
"chartreuse2",
"chartreuse3",
"chartreuse4",
"cornsilk",
"cornsilk1",
"cornsilk2",
"cornsilk3",
"cornsilk4",
"cyan",
"cyan1",
"cyan2",
"cyan3",
"cyan4",
"darkcyan",
"darkgoldenrod",
"darkgoldenrod1",
"darkgoldenrod2",
"darkgoldenrod3",
"darkgoldenrod4",
"darkkhaki",
"darkmagenta",
"darkorchid",
"darkorchid1",
"darkorchid2",
"darkorchid3",
"darkorchid4",
"darksalmon",
"darkslategray",
"darkslategray1",
"darkslategray2",
"darkslategray3",
"darkslategray4",
"darkslategrey",
"darkturquoise",
"darkviolet",
"deeppink",
"deeppink1",
"deeppink2",
"deeppink3",
"deeppink4",
"fuchsia",
"gainsboro",
"gold",
"gold1",
"gold2",
"gold3",
"gold4",
"goldenrod",
"goldenrod1",
"goldenrod2",
"goldenrod3",
"goldenrod4",
"honeydew",
"honeydew1",
"honeydew2",
"honeydew3",
"honeydew4",
"hotpink",
"hotpink1",
"hotpink2",
"hotpink3",
"hotpink4",
"indigo",
"ivory",
"ivory1",
"ivory2",
"ivory3",
"ivory4",
"khaki",
"khaki1",
"khaki2",
"khaki3",
"khaki4",
"lavender",
"lavenderblush",
"lavenderblush1",
"lavenderblush2",
"lavenderblush3",
"lavenderblush4",
"lemonchiffon",
"lemonchiffon1",
"lemonchiffon2",
"lemonchiffon3",
"lemonchiffon4",
"lightcoral",
"lightcyan",
"lightcyan1",
"lightcyan2",
"lightcyan3",
"lightcyan4",
"lightgoldenrod",
"lightgoldenrod1",
"lightgoldenrod2",
"lightgoldenrod3",
"lightgoldenrod4",
"lightgoldenrodyellow",
"lightgray",
"lightgrey",
"lightpink",
"lightpink1",
"lightpink2",
"lightpink3",
"lightpink4",
"lightslategray",
"lightslategrey",
"lightyellow",
"lightyellow1",
"lightyellow2",
"lightyellow3",
"lightyellow4",
"lime",
"linen",
"magenta",
"magenta1",
"magenta2",
"magenta3",
"magenta4",
"maroon",
"maroon1",
"maroon2",
"maroon3",
"maroon4",
"mediumaquamarine",
"mediumorchid",
"mediumorchid1",
"mediumorchid2",
"mediumorchid3",
"mediumorchid4",
"mediumpurple",
"mediumpurple1",
"mediumpurple2",
"mediumpurple3",
"mediumpurple4",
"mediumturquoise",
"mintcream",
"mistyrose",
"mistyrose1",
"mistyrose2",
"mistyrose3",
"mistyrose4",
"moccasin",
"navy",
"oldlace",
"olive",
"olivedrab",
"olivedrab1",
"olivedrab2",
"olivedrab3",
"olivedrab4",
"orchid",
"orchid1",
"orchid2",
"orchid3",
"orchid4",
"palegoldenrod",
"paleturquoise",
"paleturquoise1",
"paleturquoise2",
"paleturquoise3",
"paleturquoise4",
"papayawhip",
"peachpuff",
"peachpuff1",
"peachpuff2",
"peachpuff3",
"peachpuff4",
"pink",
"pink1",
"pink2",
"pink3",
"pink4",
"plum",
"plum1",
"plum2",
"plum3",
"plum4",
"purple",
"purple1",
"purple2",
"purple3",
"purple4",
"rosybrown",
"rosybrown1",
"rosybrown2",
"rosybrown3",
"rosybrown4",
"seashell",
"seashell1",
"seashell2",
"seashell3",
"seashell4",
"silver",
"slategray",
"slategray1",
"slategray2",
"slategray3",
"slategray4",
"slategrey",
"snow",
"snow1",
"snow2",
"snow3",
"snow4",
"teal",
"thistle",
"thistle1",
"thistle2",
"thistle3",
"thistle4",
"turquoise",
"turquoise1",
"turquoise2",
"turquoise3",
"turquoise4",
"violet",
"wheat",
"wheat1",
"wheat2",
"wheat3",
"wheat4",
"yellow",
"yellow1",
"yellow2",
"yellow3",
"yellow4",
]






if __name__ == "__main__":
    main()