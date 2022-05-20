#Count how many natural numbers have no duplicate digits.
#Inspired by https://github.com/PlummersSoftwareLLC/Primes/blob/drag-race/PrimePython/solution_3/PrimePY.py
import numpy as np

class NatSieve:
    """
    This is the main NatSieve class. 
    Call with a number you wish as an upper limit.
    """

    def __init__(self,limit):
        self._size = limit
        self._bits = np.ones(self._size + 1, dtype=np.bool_)

    def run_sieve(self):
        """Calculate to limit"""
        nat = 0 #the first natural number
        q = self._size
        bits_view = self._bits[nat:]
        while nat <= q:
            if not self._bits[nat]:
                nat+=1
                continue       
            """
            If a number is found to contain duplicate digits,
            skip all subsequent numbers that end in that.
            Step by the next highest power of 10
            """
            lst = [x for x in str(nat)]     #convert integer into list of integers

            if len(set(lst)) != len(lst):   #check that the list of integers is unique
                start = nat
                step = 10**len(str(nat))
                bits_view[start::step] = False
     
            nat += 1

    def count_nat(self):
        """
        Return the 1 bits that are still in the sieve, assuming you've run it already
        """
        return np.sum(self._bits)
    
    def get_nat(self):
        """
        Return a list of found natural numbers with no duplicate digits.
        Requires a prior run_sieve call        
        """
        nat = np.where(self._bits==False)[0]    #Show numbers with duplicate digits
        #nat = np.where(self._bits)[0]           #Show numbers without duplicate digits
        return nat

    def print_results(self, show_results, duration):
        """
        Display the count of natural numbers with no duplicate digits found
        """
        count = self.count_nat()

        if show_results:
            print("List of all natural numbers with no duplicate digits:")
            for num in self.get_nat():
                print(f"{num}")#, end=" ")
        print()
        print(f"Answer: {count}, Limit: {self._size}, Duration(s): {duration}")

#Main
if __name__ == "__main__":
    from argparse import ArgumentParser
    from timeit import default_timer

    default = 9876543210
    #default = 100000000

    parser = ArgumentParser(description="Python Natural Numbers With No Duplicate Digits Sieve")
    parser.add_argument("--limit","-l", help="Upper limit for calculating natural numbers with no duplicate digits", type=int,default=default)
    #parser.add_argument("--time","-t",help="Time limit", type=float, default=5)
    parser.add_argument("--show","-s", help="Print found natural numbers with duplicates digits", action="store_true")

    args = parser.parse_args()
    limit = args.limit
    #timeout = args.time
    show_results = args.show

    time_start = default_timer()
    sieve = NatSieve(limit)
    sieve.run_sieve()
    time_delta = default_timer() - time_start

    sieve.print_results(show_results, time_delta)

