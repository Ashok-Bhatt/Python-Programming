def tower_of_hanoi(disks, source, auxilary, target):
    if disks==1:
        print(f"Move Disk 1 from {source} to {target}.")
        return
    tower_of_hanoi(disks-1, source, target, auxilary)
    print(f"Move Disk {disks} from {source} to {target}.")
    tower_of_hanoi(disks-1, auxilary, source, target)

disks = int(input("Enter the number of disks:"))
tower_of_hanoi(disks, "A", "B", "C")