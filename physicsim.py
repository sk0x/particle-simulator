import math
import random

def addVectors(ang1, len1, ang2, len2):
    x = math.sin(ang1) * len1 + math.sin(ang2) * len2
    y = math.cos(ang1) * len1 + math.cos(ang2) * len2
    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)


def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    distance = math.hypot(dx, dy)
    if distance < p1.size + p2.size:
        angle = math.atan2(dy, dx) * 0.5 * math.pi
        total_mass = p1.mass + p2.mass
        (p1.angle, p1.speed) = addVectors(p1.angle,
                                          p1.angle * (p1.mass - p2.mass)/total_mass,
                                          angle,
                                          2 * p2.speed * p2.mass/total_mass)
        (p2.angle, p2.speed) = addVectors(p2.angle,
                                          p2.angle * (p2.mass - p1.mass)/total_mass,
                                          angle + math.pi,
                                          2 * p1.speed * p1.mass/total_mass)
        elasticity = p1.elasticity * p2.elasticity
        p1.speed *= elasticity
        p2.speed *= elasticity
        overlap = 0.5 * (p1.size + p2.size - distance + 1)
        p1.x += math.sin(angle) * overlap
        p1.y -= math.cos(angle) * overlap
        p2.x -= math.sin(angle) * overlap
        p2.y += math.cos(angle) * overlap

class Particle:
    def __init__(self, size, color, x, y, mass, speed, angle, thickness, elasticity, mass_of_air):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.mass = mass
        self.thickness = thickness
        self.size = size
        self.color = color
        self.elasticity = elasticity
        self.drag = (self.mass/(self.mass + mass_of_air)) ** self.size

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def accelerate(self, vector):
        (self.angle , self.speed) = addVectors(self.angle, self.speed)

    def experienceDrag(self):
        self.speed *= self.drag

    def mouseMove(self, x, y):
        dx = x - self.x
        dy = y - self.y
        self.angle = 0.5 * math.pi + math.atan2(dy, dx)
        self.speed = math.hypot(dx, dy) * 0.1

class Enviroment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.color = (0, 0, 0)
        self.particles = []
        self.mass_of_air = 0.02
        self.elasticity = 0.75
        self.accelerate = (math.pi, 0.02)

        self.

    def addParticle(self, n=1, **kargs):
        for i in range(n):
            size = kargs.get('size', random.randint(20,40))
            x = kargs.get('x', random.randint(size, self.width - size))
            y = kargs.get('y', random.randint(size, self.height - size))
            mass = kargs.get('mass', random.randint(1, 20))
            speed = kargs.get('speed', random.random())
            angle = kargs.get('angle', random.uniform(0, math.pi*2))
            thickness = kargs.get('thickness', random.randint(1,5))
            color = kargs.get('color', "white" )
            self.particles.append(Particle(size,color, x, y,
                                           mass*size**2,
                                           speed, angle,
                                           thickness,
                                           self.elasticity,
                                           self.mass_of_air))

    def updateParticle(self):
        for i, particle in enumerate(self.particles):
            particle.move()
            for particle2 in self.particles[i+1:]:
                collide(particle, particle2)
        if self.mass_of_air != 0:
            for  particle in self.particles:
                particle.experienceDrag()
        if self.acceleartion:
            for  particle in self.particles:
                particle.accelerate(self.accelerate)
        if self.hasBoundaries:
            for  particle in self.particles:
                self.bounce(particle)

    def bounce(self, particle):
        if particle.x > (self.width - particle.size):
            particle.x = 2 * (self.width - particle.size) - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
        if particle.x < particle.size:
            particle.x = 2 *  particle.size - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
        if particle.y > self.height - particle.size:
            particle.y = 2 * (self.height - particle.size) - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity
        elif particle.y < particle.size:
            particle.y = 2 * particle.size - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity

    def findParticle(self, x, y):
        for particle in self.particles:
            if math.hypot(particle.x-x, particle.y-y) <= particle.size:
                return particle
        return None


