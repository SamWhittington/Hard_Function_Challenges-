#Challenge is: "Given two congruent circles a and b of radius r, return the area of their intersection rounded down to the nearest integer." In less than 128 chars..

##Answer:
from numpy import*;circleIntersection=lambda a,b,r:r*r*(lambda h:h<1and arccos(h)-h*(1-h*h)**.5)(hypot(*subtract(b,a))/r/2)//.5
