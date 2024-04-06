import pandas as pd
import turtle
import timer


FONT = ('Courier', 12, 'normal')


screen = turtle.Screen()
screen.setup(width=725, height=477)
screen.title('Nigeria States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.tracer(0)

turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# initialize timer
timer = timer.Timer(200, 200)


# timer display mechanism - recursion
def timer_running():
    if len(labelled_states) < 37:
        screen.update()
        timer.update()
        turtle.ontimer(fun=timer_running, t=1000)  # so we can turn off timer when done


# read csv
data = pd.read_csv('36_states.csv')


labelled_states = []  # store states rightly guessed


screen.update()
while len(labelled_states) < 37:

    # get state input
    try:
        answer_state = turtle.textinput(title=f'{len(labelled_states)}/37 States Correct',
                                        prompt="What's another state's name?").title().strip()  # Dang PEP
    except AttributeError:
        missing_states = [state for state in data.states.to_list() if state not in labelled_states]
        # List comprehension baby 👆😁

        # export missed states to csv file
        pd.Series(missing_states, name='States').to_csv('states_to_learn.csv', index=False)

        break

    else:
        timer_running()  # call function inside loop for smooth integration

        # check if state exists in database; then label map with state
        if answer_state in data.states.to_list() and answer_state not in labelled_states:
            state = data[data.states == answer_state]

            pen.goto(int(state.x.item()), int(state.y.iloc[0]))

            # label map
            labelled_states.append(answer_state)
            answer_state = answer_state.replace(' ', '\n')  # further modifications for states with spaces
            pen.write(answer_state, align='center', font=FONT)

if len(labelled_states) == 37:
    screen.exitonclick()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tNow that's how it's done 😎")

# calculate time spent on quiz
time_spent = timer.initial_minutes * 60 - timer.time_seconds

seconds_spent = str(time_spent % 60)
minutes_spent = time_spent // 60

if len(seconds_spent) == 1:
    seconds_spent = f'0{seconds_spent}'

if len(str(minutes_spent)) < 2:
    minutes_spent = f'0{minutes_spent}'

print(f'\t\t\t\t\t\t\t\t\t\t\t\t\tTime Taken: {minutes_spent}:{seconds_spent}')
