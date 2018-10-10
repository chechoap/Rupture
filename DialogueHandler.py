import time

script = open('story.txt')


def introtext():
    with open('story.txt') as t:
        line = t.readline()
        if "***** intro ****" in line:
            line = "\n"
            while line:
                if "***** end intro ****" in line:
                    line = "\n"
                    break
                else:
                    print(line.strip())
                    line = t.readline()
                    time.sleep(0.5)
                    


def choices(uc):
    with open('story.txt') as t:
        # Reads the first line on the txt so "line" is not blank and the next while can work.
        line = t.readline()
        if uc == "a":
            # Reads the entire txt file.
            while line:
                line = t.readline()
                if "***** left *****" in line:
                    line = "\n"
                    # Reads the txt file from "file" until it reaches "**** end left ****" statement, then it exits while loop.
                    while line:
                        line = "\n"
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
