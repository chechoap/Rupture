import time

script = open('story.txt')


def introtext():
    with open('story.txt') as t:
        line = t.readline()
        if "***** intro *****" in line:
            line = "\n"
            while line:
                if "***** end intro ****" in line:
                    line = "\n"
                    break
                else:
                    print(line.strip())
                    line = t.readline()
                    time.sleep(0.5)
                    

def choices():

    uc = input
    print("a. Go left (Stairs to the second floor).\nb. Go right.(Deeper into the first floor")

    # validation to receive either "a" or "b"
    while uc != "a" or uc != "b":
        if (uc == "a" or uc == "b"):
            break
        else:
            print("Pick a or b.")
            uc = input()

    with open('story.txt') as t:
        # Reads the first line on the txt so "line" is not blank and the next while can work.
        line = t.readline()

        if uc == "a":
            while line:
                line = t.readline()
                if "***** left *****" in line:
                    line = "\n"
                    while line:
                        print((line.strip()))
                        line = t.readline()
                        time.sleep(0.5)
                        if "***** end left *****" in line:
                            break
        else:
            while line:
                line = t.readline()
                if "***** right *****" in line:
                    line = "\n"
                    while line:
                        print((line.strip()))
                        line = t.readline()
                        time.sleep(0.5)
                        if "***** end right *****" in line:
                            break