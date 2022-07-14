queue = []


def push():                                       # push operation
    e = int(input("enter the length of queue"))
    i=0
    while(i < e):
        element = int(input("enter the elements of queue"))
        queue.append(element)
        i = i + 1

    print(queue)

def pop():                                        # pop operation
    if len(queue) == 0:                           # if queue is empty
        print("queue is empty")
    else:
        queue.pop(0)
        print(queue)


    # e = input("enter the length of stack")
while(True):
    choice = int(input("enter the choices 1 to push, 2 to pop, 3 to quit"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    else:
        print("you quit")
        break
