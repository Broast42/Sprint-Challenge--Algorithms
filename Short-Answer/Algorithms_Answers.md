#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(log(n)) While at first glance this function appears to be O(n^3) because n multiplies itself 3 times. Upon further review we see that for every stop in the loop we are incrementing a by +a * n^2. This means that with each step in the loop we are skipping a bunch of places meaning we never really stop at every place in the loop. So at worst our runtime would be O(log(n))


b) O(n log(n)) -- the for loop will run n times O(n) and the while loop incriments j by 2 meaning it runs at half of n times O(log(n)) making the total O(n log(n)).


c) O(n) -- every time the function recurses its addig 2 to the return value in a liniar fashion meaning that the function will only be called n times or in this case bunnies times.

## Exercise II

If we were to preform this experiment in real life we would first need to determine what data we arte looking for. In this case we are looking for the value of f. So we are looking for what floor eggs begin to break. Preforming this out in real life we would start at floor one and drop and egg if it didnt break we would move up a floor and begin the process again until we either reached the top floor or until an egg breaks whichever comes first is the value of f. Assuming we only drop one egg a floor we would have only lost one egg. 

a psudo code algorithm would look like this:

floor_eggs_break(n) --n being the number of floors the building has.
    floor = 1
    while floor is less than n
        if the egg breaks
            return floor
        else
            add 1 to floor --move up a floor and drop again

the run time for this algorithm would at worst be O(n) as we would only need to visit each floor one time.
