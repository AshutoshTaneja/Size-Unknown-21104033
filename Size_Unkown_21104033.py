# a sorted array
array = sorted([3,7,3,12,56,63,2,5,43,65,23,6,24,75,42,75,3,74,23,764,25,5724,765,23,74,32,65,248,96,83,42,75,2,745,21,75,2,752,7])
print(f"The sorted array is : {array}")

def binarySearchUnknownLength(start, array, find):

  # sets the front to be the index of the start of the array which is given
  front = start

  end = 1
  while(True):

    # exception handling using try: ... except: ...
    # the code under try: will be excecuted first but if the mentioned exception occurs
    # the code under except: will be excecuted

    try:


      # doubles the index till the array element is less than the required number
      if array[front + end - 1] < find:
        end *= 2

      # if the required number is found the loop breaks
      elif array[front + end - 1] == find:
        break

      # in case the array element is greater than the required number
      # front is set to the last place end was at and the loop continues again on the sub-array whose starting index is front
      else:
        front += int(end/2) -1
        end = 1

      # incase the index exceeds the length of the array the exception IndexError will be thrown
      # instead of giving the error the following code will be excecuted
    except IndexError:

      # the front to the last place end was at and the loop continues again on the sub-array whose starting index is front
      front += int(end/2) - 1
      end = 1

      # exception handling incase the element does not exist in the array
      try:
        if array[front+1]:
          pass

      # incase the elemnt is not in the array the following exception runs
      except IndexError:
        front = 0
        end = -1
        print("The element required does not exist in the array.")
        break

  print(f"The required number {find} is at {front + end}th position in the array.")



def linearSearchUnknownLength(start, array, find):

  while(True):
    try:
      if array[start] == find:
        print(f"The required number {find} is at {start+1}th position in the array.")
        break
      start += 1
    except IndexError:
      print("The element required does not exist in the array.")
      break


binarySearchUnknownLength(0, array, 7)
linearSearchUnknownLength(0, array, 7)