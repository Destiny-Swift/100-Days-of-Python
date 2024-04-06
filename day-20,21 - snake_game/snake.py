from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('green')

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())  # an astute way of doing things

    def move(self):
        snake_segments = self.segments
        for seg_index in range(len(snake_segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            new_heading = self.segments[seg_index - 1].heading()

            self.segments[seg_index].goto(new_x, new_y)
            snake_segments[seg_index].setheading(new_heading)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN and -10 < (self.head.ycor() - self.segments[1].ycor()) < 10:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP and -10 < (self.head.ycor() - self.segments[1].ycor()) < 10:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT and -10 < (self.head.xcor() - self.segments[1].xcor()) < 10:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT and -10 < (self.head.xcor() - self.segments[1].xcor()) < 10:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.setposition(1000, 1000)
        self.__init__()
        #
        # self.segments.clear()
        # self.create_snake()
        # self.head = self.segments[0]
        # self.head.color('green')

    '''
    For the extra conditional statements attached to the control functions, they're to tackle the fast hands who can
    by pass the first statement by giving the controls really fast and getting the snake to turn on itself.
    And -10 to + 10 range is quite a large range to contain the drifts without affecting anything else. 
    '''
