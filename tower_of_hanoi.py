# Problem 2 #

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from rod {source} to rod {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)
def bubble_sort(arr):
    n = len(arr)
    iteration = 1
    while True:
        swapped = False
        for i in range(n - 1):
            print(f"Items compared: [{arr[i]}, {arr[i+1]}]", end=" ")
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                print(f"➔ swapped {arr}")
            else:
                print("➔ not swapped")
        if not swapped:
            break
        print(f"Iteration #{iteration} {arr}")
        iteration += 1

def main():
    n = int(input("Enter the number of disks: "))
    tower_of_hanoi(n, 'A', 'B', 'C')
    arr = [5, 2, 6, 4, 1]
    print(f"Input values = {arr}")
    bubble_sort(arr)
    print(f"Output values = {arr}")
if __name__ == "__main__":
    main()