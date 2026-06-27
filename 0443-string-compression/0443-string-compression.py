class Solution(object):
  def compress(self,chars):
    i = 0
    write = 0

    while i < len(chars):
        char = chars[i]
        count = 0

        # Count consecutive characters
        while i < len(chars) and chars[i] == char:
            i += 1
            count += 1

        # Write the character
        chars[write] = char
        write += 1

        # Write the count if greater than 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write
