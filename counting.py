
ham = int(input("what do you what to count: "))
   
if __name__ == '__main__':
    
    def print_consecutive_numbers(n):
        for i in range(1, n + 1):
            print(i, sep=("-"))
        
    n = ham
    print_consecutive_numbers(n)