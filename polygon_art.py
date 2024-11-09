import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()

        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self, new_location):
        self.location = new_location
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])


class PolygonArt:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def run(self):
        choice = int(input("Which art do you want to generate? Enter a number between 1-9: "))

        for i in range(30):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            border_size = random.randint(1, 10)
            num_levels = 2
            reduction_ratio = 0.618

            if choice == 1:
                num_sides = 3
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 2:
                num_sides = 4
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 3:
                num_sides = 5
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 4:
                num_sides = random.randint(3, 5)
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 5:
                num_sides = 3
                embedded = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 6:
                num_sides = 4
                embedded = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 7:
                num_sides = 5
                embedded = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 8:
                num_sides = random.randint(3, 5)
                embedded = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 9:
                num_sides = random.randint(3, 5)
                embedded = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels,
                                           reduction_ratio)
                embedded.draw()
                new_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                polygon = Polygon(num_sides, size, orientation, location, new_color, border_size)
                polygon.draw()

        turtle.done()


class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        Polygon.__init__(self, num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        while self.num_levels > 0:
            Polygon.draw(self)
            self.size *= self.reduction_ratio
            self.location[0] += self.size * (1 - self.reduction_ratio) / 2
            self.location[1] += self.size * (1 - self.reduction_ratio) / 2
            self.num_levels -= 1


polygon_art = PolygonArt()
polygon_art.run()
