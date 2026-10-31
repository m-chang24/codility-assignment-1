   # Assignment 1 - PassingCars (Codility Lesson 5)
   # Michael Chang
   # AI used: Claude (Anthropic) helped pick the problem and explain the approach.

   def solution(A):
       east = 0     # how many east cars (0s) we've seen so far
       pairs = 0    # total passing pairs

       for car in A:
           if car == 0:
               east = east + 1
           else:
               # this west car meets every east car before it
               pairs = pairs + east
               if pairs > 1000000000:
                   return -1

       return pairs
