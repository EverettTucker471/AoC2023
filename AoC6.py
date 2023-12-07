"""
Let t be the given time
Let d be the given record distance

we wish to find the range of k in [0, n] that satisfies k(n - k) > d

You can solve the quadratic to produce the roots, which gives you the range
I did both parts of this on Desmos

The function, by the way, is

ANS = 1 + floor(1/2(n + sqrt(n^2 - 4d))) - ceil(1/2(n - sqrt(n^2 - 4d)))
For record, this function misses the correct answer by 1 if these functions result in a perfect square.
However, this doesn't happen in our input data
"""