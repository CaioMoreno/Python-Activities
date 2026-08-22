def hanoi_solver(n: int):
    rule = pow(2, n) - 1
    rod1 = [i for i in range(1, n+1)]
    rod2 = [0]
    rod3 = [0]
    result = ""
    for i in range(rule):
        result += str(rod1) + str(rod2) + str(rod3) + "\n"
        print(result)

        if len(rod3) == n+1:
            break

        if rod1[0] > rod3[0]:
            rod3.insert(0, rod1[0])
            del rod1[0]
        elif rod1[0] > rod2[0]:
            rod2.insert(0, rod1[0])
            del rod1[0]
        elif rod2[0] > rod3[0]:
            rod2.insert(0, rod3[0])
            del rod3[0]
        elif rod2[0] > rod1[0]:
            rod1.insert(0, rod2[0])
            del rod2[0]
        elif rod3[0] > rod2[0]:
            rod3.insert(0, rod2[0])
            del rod2[0]
        elif rod3[0] > rod1[0]:
            rod3.insert(0, rod1[0])
            del rod1[0]


hanoi_solver(3)
