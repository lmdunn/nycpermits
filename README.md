# nycpermits

Subway entrance data is out of date. 2010. Mostly they don't change, but is 2nd Ave line expansion included?

## A Note on Methodology For Complaints
Ideally, I'd like the window of complaints to be uniform for all of these permits. For instance, looking at the two years prior to the start of the job (or, ideally, 5 years, but I'd need to expand the nypd dataframe to do that). However, given how long it's taking to run this code as it is, I'm going to keep it simple and use the whole 5 year period for all entries. Because crime rates aren't totally elastic relative to the city as a whole, I don't think this is terrible, but it's less precise than I'd like to be as far as being able to predict where permits will happen.

# Subway Entrances
I decided to look at numbers of entrances within tenth, half, one, and 2.5 mile radii of the permit. I wanted to find the closest entrance, along with half mile, but that would be very calculation intensive and take too long to run.