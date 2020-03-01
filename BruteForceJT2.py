### Test Python file created by James to test and improve python programming skills in VSCode
### date started: 26/02/2020
### importing useful modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
print("Done.")

### workspace area

# brute force hacker?
# simple random number creator-guesser
#passcode = 555
passcode = np.random.randint(9999)
attempt = 1
solved = False

while solved == False:
    test = np.random.randint(9999)
    print("testing:", test)

    if test == passcode:
        solved = True
        print("Correct code was", test)
    else:
        attempt += 1
print("number of attempts:", attempt)

#random number creator, guessing without repeats this time - more complicated to code