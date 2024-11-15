import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.argument("number", type=int)
@click.option(
    "-n",
    "--steps",
    default=1,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def sin(number,steps):
    for _ in range(steps):
        x = np.linspace(0, 2 * pi, number)
        df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.argument("number", type=int)
@click.option(
    "-n",
    "--steps",
    default=1,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def tan(number,steps):
    for _ in range(steps):
        x = np.linspace(0, 2 * pi, number)
        df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
        print(df)


if __name__ == "__main__":
    sin(10) #cmd_group()