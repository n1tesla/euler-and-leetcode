
def longest_collatz_seq():
    max_len=1

    for i in range(2,1000000):
        t=i
        seq_len=1
        while t!=1:
            if t%2==0:
                t= t/2
                seq_len+=1
            else:
                t=t*3+1
                seq_len+=1
        if seq_len>max_len:
            max_len=seq_len
            longest_chain_starting_number=i

    return longest_chain_starting_number,max_len

if __name__ == '__main__':
    import time
    start=time.perf_counter()
    print(longest_collatz_seq())
    print(f"ended in {(time.perf_counter()-start)*1000}")

