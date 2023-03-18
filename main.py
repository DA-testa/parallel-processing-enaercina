import heapq
def parallel_processing(n, m, data):
    # initialize heap with the first n jobs
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    results = []

    for i in range(m):
        # get the earliest finishing thread
        start_time, thread = heapq.heappop(threads)
        # record the result
        results.append((thread, start_time))
        # add the next job to the thread
        heapq.heappush(threads, (start_time + data[i], thread))

    return results


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count
    # m - job count
    n = int(input())
    m = int(input())

    # second line - data
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))
    # TODO: create the function
    result = parallel_processing(n, m, data)

    # TODO: print out the results, each pair in it's own line
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
