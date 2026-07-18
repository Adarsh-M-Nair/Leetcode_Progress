# Last updated: 7/18/2026, 8:32:14 PM
class Solution(object):
    def reverseBits(self, n):
        padded_binary = '{:032b}'.format(n)
        reversed_binary = padded_binary[::-1]
        reversed_integer = int(reversed_binary, 2)
        return reversed_integer
        