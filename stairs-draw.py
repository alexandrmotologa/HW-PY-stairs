# Dicționarul de simboluri utilizate în afișarea scării
symbols = {
    "line": "━",
    "left": "┓",
    "right": "┗",
    "inverse_left": "┛",
    "inverse_right": "┏",
}

# Funcția pentru afișarea scării
def print_stairs(num_steps):
    # Afișează treptele scării în ordinea crescătoare
    for steps in range(num_steps):
        # Calculează spațiul necesar pentru a alinia simbolurile
        space = " " * steps * 2
        # Afișează prima treaptă a scării cu simbolurile corespunzătoare
        if steps == 0:
            print(space + symbols["line"] * 2 + symbols["left"])
        # Afișează treptele intermediare ale scării
        else:
            print(space + symbols["right"] + "━" + symbols["left"])
    # Afișează treptele scării în ordinea descrescătoare
    for step in range(num_steps):
        # Calculează spațiul necesar pentru a alinia simbolurile
        space = " " * (num_steps - step - 1) * 2
        # Afișează ultima treaptă a scării cu simbolurile corespunzătoare
        if step == num_steps-1:
            print(space + symbols["line"] * 2 + symbols["inverse_left"])
        # Afișează treptele intermediare ale scării inverse
        else:
            print(space + symbols["inverse_right"] +
                  symbols["line"] + symbols["inverse_left"])


# Solicită utilizatorului să introducă numărul de trepte al scării
print_stairs(int(input("Scrie numarul d edrepte al scarii: ")))