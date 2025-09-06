# modifiable values
MAX_X: int = 30
MAX_Y: int = 30

# static values
ORIGO: int = 0


# renders a coordinate system and optionally a graph based on a k and m value
def Render(k: float | None = None, m: float | None = None):

    if (k is not None) and (m is not None):
        print(f"k: {k}\n\nm: {m}\n")

    for x in range(MAX_X + 1, ORIGO, -1):
        for y in range(ORIGO, MAX_Y + 1, 1):
            if x == 1 and y == 0:
                print(" ORIGO ", end="")
            elif x == 1:
                print(f" X+{y:03} ", end="")
            elif y == 0:
                print(f" Y+{(x-1):03} ", end="")
            elif (k is not None) and (m is not None) and (y == (1 / k) * (x - 1) + m):
                print(" ##### ", end="")
            else:
                print(" ..... ", end="")
        print("\n", end=None)


# runs once
def Init() -> None:
    Render()


# runs continuously
def Loop(loop_should_break: bool) -> bool:
    print("\nENTER YOUR LINEAR FUNCTION (y = kx + m)")
    k: float = float(input("k: "))
    m: float = float(input("m: "))

    Render(k=k, m=m)

    q = input("")

    if q == ":q":
        loop_should_break = True

    return loop_should_break


# program main entry point
def Main():
    loop_should_break = False

    Init()

    while not loop_should_break:
        loop_should_break = Loop(loop_should_break)


if __name__ == "__main__":
    Main()
