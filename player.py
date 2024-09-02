import pygame 
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAY_SHOOT_INTERVAL
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
            #self.velocity
            #self.radius
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        fwidth = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius/1.1
        bwidth = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius 
        a = self.position + forward * 1.5*self.radius - fwidth
        b = self.position + forward * 1.5*self.radius + fwidth
        c = self.position - forward * self.radius - bwidth
        d = self.position - forward * self.radius + bwidth
        # return [a, b, c, d]     #hourglass
        # return [a, b, d, c]     #trapezoid
        return [a, d, b, c]     #nacelles
        # return [d, c, b, a]     #hourglass
        # return [a, c, b, d]     #hourglass
        # return [a, d, c, b]     #hourglass
    
    def draw(self, screen):
        c = "light goldenrod"
        pygame.draw.circle(screen, c, self.position, PLAYER_RADIUS)
        pygame.draw.polygon(screen, c, self.triangle())

    def rotate(self, dt):
        self.rotation += int(PLAYER_TURN_SPEED*dt)      #TODO: figure out restricting to 0-360?

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward*PLAYER_SPEED*dt

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer <= 0:
            b = Shot(self.position[0], self.position[1], SHOT_RADIUS)
            b.velocity = self.velocity*PLAYER_SHOOT_SPEED               #lays stationary mine
            # b.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.timer = PLAY_SHOOT_INTERVAL




