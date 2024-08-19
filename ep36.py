from util import decimal_to_binary

number = 0
# Example usage
upperlimit=1_000_000
for i in range (upperlimit):
    if str(i)==str(i)[::-1]:
        bin_i=decimal_to_binary(i)
        if str(bin_i)==str(bin_i)[::-1]:
            print(f"the base10 palindrome {i} = base2 palindrome {bin_i}")
            number+=i

print(f"The sum of the palindromes is {number}")