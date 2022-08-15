# nycpermits

Subway entrance data is out of date. 2010. Mostly they don't change, but is 2nd Ave line expansion included?

## A Note on Methodology For Complaints
Ideally, I'd like the window of complaints to be uniform for all of these permits. For instance, looking at the two years prior to the start of the job (or, ideally, 5 years, but I'd need to expand the nypd dataframe to do that). However, given how long it's taking to run this code as it is, I'm going to keep it simple and use the whole 5 year period for all entries. Because crime rates aren't totally elastic relative to the city as a whole, I don't think this is terrible, but it's less precise than I'd like to be as far as being able to predict where permits will happen.

# Subway Entrances
I decided to look at numbers of entrances within tenth, half, one, and 2.5 mile radii of the permit. I wanted to find the closest entrance, along with half mile, but that would be very calculation intensive and take too long to run.

# Distances to Parks
### Turning Distance Calcuation into Miles
This distance is in degrees. 1 degree latitude ~= to 69 miles. 1 degree longitude ~= 40 miles at NYC's latitude.

I'm going to treat a degree as equal to 54.5 miles for the purpose of these distance calculations. This means that my calculations of distance could be off by as much as 36.25%, if the change in position is actually only a change in longitude, latitude staying the same (in other words, 1 degree change actually equaling 40 miles). For a change only in latitude (longitude staying the same), the error rate is 21%.

Unfortunately, given the time line I'm on, I'm going to accept this level of imprecision. 

# Places for refinement or deeper analysis
note on distance from parks, above
eda -- looking at more park metrics, number within distance(see notes in eda)
random points -- I used an even distribution by borough. Would have been better to make the distribution proportional to area of borough. It would have been more precise.
use residential zoning for analysis, not (non-park) city area. _This is a positive sign, but warrants more research before drawing a conclusion. Ideally, one would use zoning data and eliminate random points that fall outside residential zoning. That would indicate whether new housing is being randomly distributed in residential zones or if the distribution leans towards or away from proximity to parks._

It might be worth looking at the proportion of the city encompassed by historic districts to get a more precise sense of the scale at which the districts are diminishing potential housing stock. That said, the rate at which random points fall in historic districts, at least by borough, gives us a good approzimation.

Looking at commuting times to central biz distances would be really interesting. Particularly relevant for SI -- is it actually farther?