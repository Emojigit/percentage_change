import sys
exit = sys.exit
def float2percent(f):
    return "{}%".format(f*100)

def main():
    if len(sys.argv) != 3:
        print("Usage: {} main.py <new value> <original value>".format(sys.executable))
        exit(1)
    try:
        n,o = float(sys.argv[1]),float(sys.argv[2])
    except ValueError:
        print("Usage: {} main.py <new value> <original value>".format(sys.executable))
        exit(1)
    print("           Change: {}".format(n - o))
    if o == 0:
        print("Original Value cannot be 0!")
        exit(2)
    PC = (n - o)/o
    print("Percenatge Change: {}".format(float2percent(PC)), end="")
    if PC > 0:
        print(" (Increase)")
    elif PC < 0:
        print(" (Decrease)")
    else:
        print(" (No Changes)")
    exit(0)

if __name__ == "__main__":
    main()
