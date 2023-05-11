# Generate binary numbers between 1 to `n` using a queue
# Google Translate Icon
# Given a positive number n, efficiently generate binary numbers between 1 and n using the queue data structure in linear time.

# For example, for n = 16, the binary numbers are:

# 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000


from queue import Queue

def generate_binary_numbers(n):
    q = Queue()

    q.put("1")

    while n>0:
        n-= 1
        s1 = q.queue[0]
        q.get()
        print(s1, end=" ")

        s2 = s1
        q.put(s1+"0")
        q.put(s2+"1")

generate_binary_numbers(16)
