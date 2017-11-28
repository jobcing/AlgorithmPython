import heapq

def doubleHeapq():
    n = int(input())
    queue = []

    for i in range(n):
        inputstr = input().split(" ")
        command = inputstr[0]
        num = int(inputstr[1])

        if(command == 'I'):
            heapq.heappush(queue, num)
        else:
            if(not queue):
                continue
            elif(num == -1):
                heapq.heappop(queue)
            else:
                queue.remove(max(queue))

    return queue

if __name__ == "__main__":
    testcase = int(input())
    result = []

    for i in range(testcase):
        resultque = doubleHeapq()
        result.append(resultque)

    for i in result:
        if not i:
            print("EMPTY")
        else:
            print("%d %d" % (max(i), min(i)))
