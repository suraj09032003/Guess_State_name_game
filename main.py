import turtle
import pandas


screen = turtle.Screen()
screen.title("India states game")
image = "Mapa-de-India-color-scaled-1024x1024-2.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Download india_states_final_coordinates.csv")
all_states = data.state.to_list()
guessed_states=[]

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 states correct"
                                    , prompt="whats another states name?").title()

    if answer_state == "Exit":
        missing_state =[]
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.GUESS_STATE")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item() ,state_data.y.item())
        t.write(answer_state)


