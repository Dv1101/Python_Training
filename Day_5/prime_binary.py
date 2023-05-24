def count_ones(number):
  """Counts the number of 1's in a prime number.

  Args:
    number: The prime number to count the 1's in.

  Returns:
    The number of 1's in the prime number.
  """

  # Create a lambda function to check if a digit is 1.
  is_one = lambda digit: digit == 1

  # Count the number of 1's in the binary representation of the number.
  count = 0
  while number > 0:
    if is_one(number % 2):
      count += 1
    number //= 2

  return count


def main():
  # Get a prime number from the user.
  number = int(input("Enter a prime number: "))

  # Count the number of 1's in the prime number.
  count = count_ones(number)

  # Print the number of 1's.
  print("The number of 1's in {} is {}".format(number, count))


if __name__ == "__main__":
  main()