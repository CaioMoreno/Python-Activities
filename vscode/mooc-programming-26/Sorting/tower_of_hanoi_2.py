def hanoi_solver(n: int):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []

    def show():
        print(rod1, rod2, rod3)

    def move(disks, source, auxiliary, destination):
        if disks == 0:
            return

        # Move n-1 disks out of the way
        move(disks - 1, source, destination, auxiliary)

        # Move the remaining disk
        destination.append(source.pop())
        show()

        # Put the n-1 disks on top of it
        move(disks - 1, auxiliary, source, destination)

    show()
    move(n, rod1, rod2, rod3)


hanoi_solver(3)
