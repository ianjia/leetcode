# Time Limit Exceeded
class Solution1(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        for i in range(2, n):
            if self.isPrime(i) == True:
                res += 1
        
        return res
        
    def isPrime(self, num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            
        return True

# Sieve of Eratosthenes
class Solution2(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i] == True:
                for j in range(i + i, n, i):
                    primes[j] = False

        return sum(primes) # count the number of "True"s in primes

# Sieve of Eratosthenes
class Solution3(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        res = n - 2
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            # makes all multiples of primes[i] False (not prime)
            if primes[i] == True:
                for j in range(i + i, n, i):
                    if primes[j] == False:
                        continue
                    primes[j] = False
                    res -= 1

        return res