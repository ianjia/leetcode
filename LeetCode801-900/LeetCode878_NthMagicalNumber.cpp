// Math
class Solution1 {
public:
    int nthMagicalNumber(int N, int A, int B) {
        int modNum = 1e9 + 7;
        int lcm = (A / gcd(A, B)) * B;
        int magicalNums = (lcm/A) + (lcm/B) - 1;
        
        long rounds = N / magicalNums, remainders = N % magicalNums;
        long long res = rounds * lcm;
        if (remainders == 0) {
            return res % modNum;
        }
        
        int aSum = A, bSum = B;
        for (int i = 0; i < remainders - 1; i++) {
            if (aSum <= bSum) {
                aSum += A;
            }
            else {
                bSum += B;
            }
        }
        res += min(aSum, bSum);
        return res % modNum;
    }
    
    int gcd(int a, int b) {
        if (a == 0) {
            return b;
        }
        return gcd(b % a, a);
    }
};

// Binary Search
class Solution2 {
public:
    int nthMagicalNumber(int N, int A, int B) {
        int modNum = 1e9 + 7;
        int lcm = (A / gcd(A, B)) * B;
        
        long start = 0;
        long end = (long)N * min(A, B);
        while (start + 1 < end) {
            long mid = start + (end - start) / 2;
            int cur = mid/A + mid/B - mid/lcm;
            if (cur < N) {
                start = mid;
            }
            else {
                end = mid;
            }
        }
        
        int temp = start/A + start/B - start/lcm;
        
        if (temp == N) { // If there are not enough magic numbers below mid
            return start % modNum;
        }
        else {
            return end % modNum;
        }
    }
    
    int gcd(int a, int b) {
        if (a == 0) {
            return b;
        }
        return gcd(b % a, a);
    }
};
