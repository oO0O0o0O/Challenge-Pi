This program uses the random() function to calculate pi.

Area of a circle (A) = pi(r)^2
pi = A/(r)^2

Pi is equal to the proportion of the area of a circle
divided by the area of a square of length r. We can place this square
with one corner at the center of the circle and flush to the a/y axises,
thereby overlaping with the top-right quarter of the circle. This overlaping
area of the circle is represented by <i>a</i>.
pi = 4a/(r)^2

This proportion can be created by evenly placing dots in the square, dividing
the number of dots within the circle by the number in the circle and square, and
multiplying by four.

The random() function will be used to generate x/y coordinates for dots to be placed
in a square with coordinates (0,0) and (1,1). These dots will be counted as in or
outside the circle by calculating their distance to the origin. Since the square has length
1, the circle has radius 1, so any point further than 1.0 from the origin must be outside
the circle.

The number of points inside the circle divided by the number of total points times four
will equal approvimately pi, especially for larger numbers.

Source: https://youtu.be/pvimAM_SLic
