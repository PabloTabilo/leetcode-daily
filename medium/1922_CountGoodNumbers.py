class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # range per digit : 0 - 9
        # primes: 2, 3, 5, 7 -> odd position
        # even: 0, 2, 4, 6, 8
        # n = 1, pos = 0
        # n = 2, pos = 0, 1
        # odd position 0, 1, 2, 3, 4, 5, 6

        # n = 1 -> 0, 2, 4, 6, 8
        # n = 2 -> _ _, [0-8][2-7]
        # n = 3 -> _ _ _, [0-8][2-7][0-8] = 5*4*5 -> n/2 = 1, 3-1 = 2 -> 5^2 * 4^1
        # n = 4 -> _ _ _ _, 5*4*5*4
        p = n // 2
        q = n - p
        #print(f"p = {p}, q = {q}")
        MOD = 10**9 + 7
        def mod_exp(base, expo):
            res = 1
            while expo > 0:
                if(expo % 2 == 1):
                    res = ((res % MOD) * (base % MOD)) % MOD 
                    expo -= 1
                expo /= 2
                base = ((base % MOD) * (base % MOD)) % MOD 
            return res
        return ((mod_exp(5, q) % MOD) * (mod_exp(4, p) % MOD)) % MOD