class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        PHI = 1140  
        def mod_exp(base: int, exp: int, mod: int) -> int:
            result = 1
            base = base % mod
            while exp > 0:
                if (exp % 2) == 1:
                    result = (result * base) % mod
                exp = exp >> 1
                base = (base * base) % mod
            return result

        
        def compute_exponent_mod(b: List[int], mod: int) -> int:
            exponent = 0
            for digit in b:
                exponent = (exponent * 10 + digit) % mod
            return exponent

       
        exp_mod = compute_exponent_mod(b, PHI)
        
        if exp_mod == 0:
            exp_mod = PHI
        

        return mod_exp(a, exp_mod, MOD)
