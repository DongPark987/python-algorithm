import sys

input = sys.stdin.readline
print = sys.stdout.write

myTree = {}

sys.setrecursionlimit(10**6)


def circuit(node):
    global myTree
    if node == '.':
        return
    circuit(myTree[node][0])
    circuit(myTree[node][1])
    print(str(node)+"\n")


def insert(data):
    global myTree, root
    Next = root
    cursor = root
    while Next != '.':
        cursor = Next
        # print("next",Next)
        if data <= Next:
            # print("작다")
            Next = myTree[Next][0]
        else:
            # print("크다")
            Next = myTree[Next][1]
    myTree[data] = ['.', '.']
    if data <= cursor:
        myTree[cursor][0] = data
    else:
        myTree[cursor][1] = data


root = int(input())
myTree[root] = ['.', '.']
while True:
    # print(myTree)
    try:
        N = int(input().rstrip())
        # print(N)
        insert(N)
    except:
        break
circuit(root)
