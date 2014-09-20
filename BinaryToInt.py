def bin_to_int(binary):
  """
  Convert a binary to an integer.
  Runs O(log n).
  """
  
    x = str(binary)
    power = 0
    sum = 0
    for i in range(1, len(str(binary))+1):
        if x[-i] == str(1):
            sum += 2**power
        power += 1
    return int(sum)

def test_cases():
  assert bin_to_int(1001) == 9
  assert bin_to_int(0001) == 1
  assert bin_to_int(1110) == 14
  assert bin_to_int(010010101110) == 512
  
def main():
  test_cases()
  
if __name__ == '__main__':
  main()
