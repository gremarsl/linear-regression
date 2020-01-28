def createLine(p1, p2):
    # y=mx+c
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]
    m = delta_y / delta_x
    c = p1[1] - m * p1[0]
    return m, c


def main():
    data = [(0, 5), (1, 6), (2, 7), (3, 8)]

    # create m with first and last
    mList = []
    cList = []
    while len(data) > 1:
        print(data)
        m, c = createLine(data[0], data[-1])

        # if required it is possible here to weight the m's and the c's
        # with: (m1*k-factor + m2*j-factor)/(k+j)
        mList.append(m)
        cList.append(c)
        del data[-1]

    m_mean = sum(mList) / len(mList)
    c_mean = sum(cList) / len(cList)

    print(
        "Monday\t\t=\t0\nTuesday\t\t=\t1\nWednesday\t=\t2\nThursday\t=\t3\nFriday\t\t=\t4\nSaturday\t=\t5\nSunday\t\t=\t6")

    while True:
        INPUT = input("Enter the day (see respective number above) you want to predict the sales: ")

        try:
            Input = int(INPUT)
            if Input >6:
                print("Your value: {} is higher then the maximum valid value 6".format(Input))
                continue

        except ValueError:
            if INPUT=='':  # the only False String is an empty string:
                print("Your input was empty! Try again - Enter a number from 0-6")

            else:
                print("That wasn't a number! - Try again")
            # return to start of the loop
            continue
        else:
            break

    prediction = m_mean * Input + c_mean
    print(prediction)


if __name__ == "__main__":
    main()
