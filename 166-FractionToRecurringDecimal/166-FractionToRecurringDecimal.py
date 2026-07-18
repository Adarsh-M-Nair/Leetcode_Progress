# Last updated: 7/18/2026, 8:32:18 PM
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
    
        # Determine the sign
        sign = ""
        if (numerator < 0) ^ (denominator < 0):
            sign = "-"
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part
        integer_part = str(numerator // denominator)
        
        # Handle the remainder
        remainder = numerator % denominator
        if remainder == 0:
            return sign + integer_part
        
        # Fractional part
        fractional_part = []
        seen_remainders = {} # Map remainder to its position in the fractional part
        
        while remainder != 0 and remainder not in seen_remainders:
            seen_remainders[remainder] = len(fractional_part)
            remainder *= 10
            fractional_part.append(str(remainder // denominator))
            remainder %= denominator
            
        if remainder in seen_remainders:
            index = seen_remainders[remainder]
            fractional_part.insert(index, "(")
            fractional_part.append(")")
        
        return sign + integer_part + "." + "".join(fractional_part)