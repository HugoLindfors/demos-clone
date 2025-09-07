from tkinter import *  # type: ignore

# modifiable values
MAX_X: int = 60
MAX_Y: int = 60

# static values
ORIGO: int = 0


# used to draw graphs that can be put on the equation y = kx + m
def DrawLinearGraph(window: Tk, k: float | None = None, m: float | None = None) -> None:
    for x in range(MAX_X + 1, ORIGO, -1):
        for y in range(ORIGO, MAX_Y + 1, 1):

            if x == 1 and y == 0:
                Frame(master=window, bg="white", width=10, height=10).grid(
                    column=x, row=y
                )
            elif x == 1 and y % 2 == 0:
                Frame(master=window, bg="white", width=10, height=10).grid(
                    column=x, row=y
                )
            elif MAX_Y - y == 0 and x % 2 == 0:
                Frame(master=window, bg="red", width=10, height=10).grid(
                    column=x, row=y
                )
            elif x == 1 and y % 2 != 0:
                Frame(master=window, bg="green", width=10, height=10).grid(
                    column=x, row=y
                )
            elif MAX_Y - y == 0 and x % 2 != 0:
                Frame(master=window, bg="white", width=10, height=10).grid(
                    column=x, row=y
                )
            elif (k is not None) and (m is not None) and (MAX_Y - y == k * (x - 1) + m):
                Frame(master=window, bg="blue", width=10, height=10).grid(
                    column=x, row=y
                )
            else:
                Frame(master=window, bg="black", width=10, height=10).grid(
                    column=x, row=y
                )


def Init(window: Tk) -> Tk:
    window.title(string="FORM")

    return window


def Loop(loop_should_break: bool, window: Tk) -> bool:

    DrawLinearGraph(window=window, k=1, m=0)

    window.mainloop()

    return loop_should_break


def Main() -> int:
    window = Tk()
    window = Init(window=window)

    loop_should_break: bool = False

    while not loop_should_break:
        loop_should_break = Loop(loop_should_break=loop_should_break, window=window)

    return 0


if __name__ == "__main__":
    if Main() != 0:
        print("ERROR")
