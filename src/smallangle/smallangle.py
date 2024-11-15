import click
import numpy as np
from numpy import pi
import pandas as pd
import math as mt

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def sin(number):
    """ Generates list with NUMBER and sin(NUMBER).
    
    Generates a list of NUMBER(S) between 0 en 2pi, with the sin of these NUMBER(S).
    """
    for _ in range(number):
        x = np.linspace(0, 2 * pi, number)
        df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def tan(number):
    """ Generates list with NUMBER and tan(NUMBER).

    Generates a list of NUMBER(S) between 0 en 2pi, with the tan of these NUMBER(S).
    """
    for _ in range(number):
        x = np.linspace(0, 2 * pi, number)
        df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
        print(df)


@cmd_group.command()
@click.argument("epsilon", type=float)
def biggest_angle(epsilon):
    """Gives biggest angle for chosen EPSILON with |x-sin(x)| <= EPSILON.

    For chosen EPSILON value check the biggest angle for which
    |x-sin(x)| <= EPSILON, rounded by 3 decimals.  
    """
    x = 0
    step = 0.001
    while abs(x - mt.sin(x)) <= epsilon:
        x = x + step
    result = round(x - step, 3)
    print(f"For an accuracy of {epsilon}, the small-angle approximation holds up to x = {result}.")

if __name__ == "__main__":
    cmd_group()

