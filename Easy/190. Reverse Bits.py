def reverseBits(slef, n: int) ->int:
  padded_binary='{:032b}'.format(n)
  reversed_binary=padded_binary[::-1]
  reversed_integer=int(reversed_binary,2)
  return reversed_integer