![Post Length (Characters) Bar Chart](/images/post_length.png "Mean and median post lengths")# Complaints

# Parks
I looked at how the boroughs compare to each other in respect to their proportion of parks. I also examined how the distance to parks for the permits compared to what one would expect from a random distribution of permits, both at the city and borough level.

## Distribution of Parks Throughout the City
First, I examined how parks are distributed throughout the boroughs by area: 

![Park Area versus Borough Area as Percentage of City Total](/images/par_distr_area.png "Parks by Area")

Second, I looked at the distribution by number:

![Park Number versus Borough Area as Percentage of City Total](/images/par_distr_num.png "Parks by Number")

What's clear from both metrics is that the Bronx "overperforms" when it comes to parks. It has a higher proportion of parks as measured by both number and area. Queens, on the other hand, "underperforms". It has a lower proportion of parks by both number and area. **This suggests that the city should prioritize developing parkland in Queens.**

Staten Island is interesting because it has a far lower percentage of parks by number but a far higher percentage of parkland by area when compared to it's proportion of city area. Given that Staten Island is less densely developed than the rest of the city and has more single family homes (with yards, etc. **NOTE: I'm speaking anecdotally as of the moment. Ultimately, this warrants finding data to support it**), this seems unsurprising.

Brooklyn has a higher proportion of parks by number but a lower proportion of parkland by area when compared to it's share of the city's area. I believe that while it would be ideal for both to be proportional, it's preferable to have a greater number of parks, as that makes it more likely there are more parks accessible to more people even though they may be smaller parks.

Manhattan, perhaps unsurprisingly, has a disproportionate share of parks by both number and area when compared to its share of city area. Central Park certainly contributes a lot to park area. I hypothesize that Manhattan is historically the wealthiest borough (**NOTE: Again, this is anecdotal at the moment. It would be ideal to find statistics to back this up.**) and has had the most parkland to cater to its wealthier residents.

## Permits and Parks
Actual permits fall closer to parks than random points. Two notes: the distribution of permits/random points aren't the same so city-wide v borough percent differences don't line up. Also, this analysis could be made more precise by randomly selecting points in areas zoned for housing.

![Mean Parks City-Wide, Random versus Actual](/images/city_parks_rando_actual.png "City-wide Park Distance")

![Mean Parks By Borough, Random versus Actual](/images/boros_parks_rando_actual.png "Park Distance by Borough")

This is a positive sign, but comparing the permits to random points that fall in residential zoning would offer a more precise metric. For example, a skew away from parks among the random points may very well reflect points falling in commercial or industrial zones that don't have parks nearby.

## City-Wide Rates of Permits in Historic Districts
As expected, the rate of permits in historic districts (.6%) is 84.8% lower than the rate among the randomly distributed points(3.9%). This is, of course, one of the purposes of a historic district, but it's worth considering when we look at building more housing in NYC. In particular, why are the districts located where they are? Do they contribute to inequity in housing opportunities?

![Rates of Location in Historical Districts City-Wide, Random versus Actual Permits](/images/city_historical_rando_actual.png "Rates of Historical District Location")



