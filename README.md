Analysis of the Location of New York City New Residential Building Permits
-----
New York City is one of the most expensive cities to live in, worldwide. According to [CNBC](https://www.cnbc.com/2019/03/07/heres-the-share-of-income-that-goes-to-rent-in-cities-across-the-us.html), in 2019, the average rent ($2100 USD) was 40% of the average income (62,870 USD). Generally, anything over 30% of income is considered unaffordable (this figure has it's basis in the cap that the US Federal government places on what share of income residents can pay towards affordable housing: see [Fortune](https://fortune.com/2015/08/04/housing-30-percent-rule/) and [Earnest.com](https://www.earnest.com/blog/rent-and-the-30-percent-rule/) for two discussions of this rate). 

To further illustrate, the average Manhattan rent recently broke $5,000 USD/month for the first time, in July of 2022 [NY Post](https://nypost.com/2022/07/14/average-manhattan-rent-breaks-5000-for-the-first-time/).

The following analysis is designed to help address this challenge in two ways: first, by providing insight to the city on where new building is happening and suggest possiblities as to why; two, provide builders insight on potential patterns in where buildings are currently being permitted to help them locate the most promising opportunities for new construction.

# Data Dictionary
-----
This analysis used the following data sets, all but one to be found at [NYC Open Data](https://opendata.cityofnewyork.us/):
- [data on building permits](https://data.cityofnewyork.us/Housing-Development/DOB-Permit-Issuance/ipu4-2q9a)
- [subway entrance locations](https://data.cityofnewyork.us/Transportation/Subway-Entrances/drex-xx56)
- [boundaries of historic districts](https://data.cityofnewyork.us/Housing-Development/Historic-Districts/xbvj-gfnw)
- [map of criminal complaints](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i)
- [map of city parks](https://nycopendata.socrata.com/Recreation/Parks-Properties/enfh-gkve)
- [2020 Census tracts boundaries](https://data.cityofnewyork.us/City-Government/2020-Census-Tracts-Mapped/weqx-t5xr)
- [2020 Census data](https://www1.nyc.gov/site/planning/planning-level/nyc-population/2020-census.page##2020-census-results) (this is from the NYC Dept. of City Planning; [this link](https://www1.nyc.gov/assets/planning/download/office/planning-level/nyc-population/census2020/nyc_decennialcensusdata_2010_2020_change.xlsx?r=3) autodownloads the data)

Data from these sets were combined into the final data set:

|Feature|Type|Description|
|---|---|---|
|borough|obj|borough permit is located in|
|bin_no|int|Building Identification Number. A unique number used by NYC Dept of City Planning and Dept of Building to track each building|
|house_no|obj|Street address number|
|street_name|obj|Name of street permit is located on|
|job_no|int|Number assigned to job filing by DOB|
|zip_code|int|Address zip code. 99999 indicates the zip code was missing|
|job_start_date|obj|Date the job started|
|owners_business_type|obj|Type of business or individual that owns the building|
|non-profit|obj|1 indicates the owner is a non-profit. 0 indicates it is not|
|latitude|float|Degrees latitude of location|
|longitude|float|Degrees longitude of location|
|point|obj|Longitude and latitude for conversion into a `shapely` point|
|bct2020|int|Borough Census Tract 2020 number|
|total_complaints|int|Total complaints within .1 mile of the permit, 08/02/2014-08/02/2020|
|closest_subway|float|The distance in miles to the closest subway entrance. This data is dated 2010 but includes both the Hudson Yards 7 line extension and the 2nd Ave line to 96th Street|
|closest_subway_line|obj|The subway line(s) accessible by the closest subway entrance|
|subway_count_tenth_mi|int|The number of subway entrances within .1 miles of the permit|
|subway_count_half_mi|int|The number of subway entrances within .5 miles of the permit|
|subway_count_one_mi|int|The number of subway entrances within 1 mile of the permit|
|subway_count_two_five_mi|int|The number of subway entrances within 2.5 miles of the permit|
|hist_dist_name|obj|The name of the historic district the permit is located in or `none` if not located in a historic district|
|in_hist_dist|int|1 indicates the permit is in a historic district. 0 indicates it is not|
|closest_park|float|The distance to the closest park. NOTE: as of 08/16/22 this is an approximation, equating 1 degree of distance to 54.5 miles, the average distance of one degree latitude and 1 degree longitude at NYC's latitude|
|name_closest_park|obj|The name of the park closest to the permit|
|park_count_tenth_mi|int|The number of parks within .1 miles of the permit|
|park_count_half_mi|int|The number of parks within .5 miles of the permit|
|park_count_one_mi|int|The number of parks within 1 mile of the permit|
|park_count_two_five_mi|int|The number of parks within 2.5 miles of the permit|
|pop_20|int|float|The number of people counted in the permit's Boro Census Tract for the 2020 census|
|hhpop_20p|float|The percentage of people living in a household in the permit's Boro Census Tract for the 2020 census|
|gq_20p|float|The percentage of people living in a group home in the permit's Boro Census Tract for the 2020 census|
|instgq_20p|float|The percentage of people who are institutionalized within the permit's Boro Census Tract for the 2020 census|
|avhhsz_20|float|The average household size within the permit's Boro Census Tract for the 2020 census|
|popu18_20p|float|Percentage of the population under 18 within the permit's Boro Census Tract for the 2020 census|
|hsp_20p|float|Hispanic percentage of the population within the permit's Boro Census Tract for the 2020 census|
|wnh_20p|float|White non-Hispanic percentage of the population within the permit's Boro Census Tract for the 2020 census|
|bnh_20p|float|Black non-Hispanic percentage of the population within the permit's Boro Census Tract for the 2020 census|
|anh_20p|float|Asian non-Hispanic percentage of the population within the permit's Boro Census Tract for the 2020 census|
|onh_20p|float|Other non-Hispanic percentage of the population within the permit's Boro Census Tract for the 2020 census|
|nh2pl_20p|float|2 or more races, non-Hispanic percentage of the population within the permit's Boro Census Tract for the 2020 census|
|hunits_20|int|Number of units of housing within the permit's Boro Census Tract for the 2020 census|
|ochu_20p|float|Percent of occupied housing units within the permit's Boro Census Tract for the 2020 census|
|vachu_20p|float|Percent of vacant housing units within the permit's Boro Census Tract for the 2020 census|

# Brief Summary of Analysis
## Data Cleaning and Feature Engineering
While some cleaned data lives in the repository, most of the data for this analysis is available at [this Google Drive folder](https://drive.google.com/drive/folders/1JsxNW6hqSInCaDFb5RAN6UfVsiBRKuox?usp=sharing). To most easily replicate this analysis, please put the four data folders (`data_large_sets`, `data_nypd_by_year`, `data_permits_by_boro`, and `data_permits_w_nypd`) data in the parent directory to the `nycpermits` repository.


The data was cleaned to put it in a useable form and recover or eliminate nulls/other unusable data. Most notably, the permits data set was reduced to contain only the first permit for new residential buildings with a job start date between 08/02/2016 and 08/02/2022.

Feature engineering consisted of connecting the permits to relevant data from other data sets. In addition, versions with and without dummified categorical data columns were also generated.

Noteworthy is the computational power/time necessary to identify the number of criminal complaints within .1 miles of the permit. For that reason, AWS servers were used for much of that work and a folder with .py files is included in the repository. In the original analysis, for some reason Brooklyn in 2014 was difficult to run and was broken out into a separate task by rewriting the 2014 .py file accordingly. This shouldn't be necessary, but is fairly easy to do.

To replicate this part of the analysis on a remote server, load the `data_permits_by_boro` and `data_nypd_by_year` folders into the home of that server and run the .py files from there. Otherwise, the .py files can be run on your computer from the same directory that holds these folders, though you'll need to move the files from their current place in the repository to have them in the same directory as these folders.

## EDA
### Randomly Selected Points
At several points in EDA, randomly selected points were used to compare what we'd expect permits to look like if they were evenly distributed through the boroughs versus what they actually looked like.

1000 points were selected randomly from each of the 5 boroughs. Points that fell in parks were eliminated. Of the original 5000 points, 4253 were left, still roughly evenly distributed across the boroughs

### Permits versus Relative Borough Density
Note: relative borough density was calulated using the percent of city total area and city total population for each borough. Therefore, while the proportions are correct, which is all that's needed for this analysis, the actual values don't translate to meaningful numbers.

The boroughs are not proportionally represented among the permits relative to their density.

This shows the percentages of actual permits compared to relative density.

![Percent of Total Permits versus Relative Density by Borough](/images/perms_v_density_boro.png "% Permits v. Relative Density by Borough")

This shows what we'd expect for the percentage of permits if it was inversely related to density.

![Expected Percent of Total Permits Relative to Density by Borough](/images/perms_expected_v_density_boro.png "% Permits v. Relative Density by Borough")

## Parks
### Comparison of Parks by Borough
Queens has proportionally fewer parks than the other boroughs as compared to its share of the city's area, whether measured by the number of parks or the area of the parks within the borough. 

By park area:
![Park Area versus Borough Area as Percentage of City Total](/images/par_distr_area.png "Parks by Area")

By park number:
![Park Number versus Borough Area as Percentage of City Total](/images/par_distr_num.png "Parks by Number")

This suggests that the city should develop more parkland in Queens.

Two notes:

While borough population is a valid alternative metric to borough area, as the idea is to consider long term development, area was the preferred metric. Parkland is limited by available area and area suggests the number/size of parks necessary to provide residents with equal access. 

Additionally, borough area does not take into account zoning. The hypothesis, which warrants further exploration, is that different proportions of industrial zoning will only marginally affect the relative areas of the boroughs. It's worth noting that zoning is a political choice, so this selection of random choices that doesn't take zoning into account provides valuable insight, but taking zoning into account would also likely provide valuable insights. 

### Proximity to Parks Relative to Expected Distribution
Actual permits fall closer to parks than randomly chosen points (that don't fall in parkland), both by city and by borough. 

Citywide:
![Mean Parks City-Wide, Random versus Actual](/images/city_parks_rando_actual.png "City-wide Park Distance")

By borough:
![Mean Parks By Borough, Random versus Actual](/images/boros_parks_rando_actual.png "Park Distance by Borough")

The relative proximity of actual permits to parks when compared to expectations is a potentially positive sign, as proximity to parks is desireable for quality of life reasons. However, comparing the permits to random points that fall in residential zoning would offer a more precise metric. For example, a skew away from parks among the random points may very well reflect points falling in commercial or industrial zones that don't have parks nearby.

Two notes:
One: distance to parks was calulated using the `shapely` package. The distance was calculated in degrees (from degrees longitude and latitude). However, degrees of longitude and latitude are not the same distance length. A degree of latitude is roughly 69 miles and a degree of longitude at New York City's latitude is about 40 miles. These distances were calculated at a rate of 54.5 miles per degree, the average of these two values. At it's most extreme, a change of longitude on exactly the same latitude, this could represent an error of as much as 36.25%. A more exact distance like those used elsewhere could be calculated by finding the exact point on the park that is closest to the permit and calculating that with the distance function used elsewhere.

Two: the citywide and borough percent differences don't directly compare because the randomly-selected points were not distributed across the boroughs in the same proportions as the actual permits were. This helps to examine what permits would look like if they were evenly distributed throughout the boroughs. Each graph is valid in itself, but the numbers won't add up if compared to each other.

### Distribution of Outlier Parks By Borough
Queens, perhaps unsurprisingly, has by far the highest proportion of parks that were an outlier distance (>.375 miles) away from the closest park:

![Permits with Outlier Distances from Parks by Borough](images/outlier_park_dist.png "Number of Permits with Outlier Park Distances by Borough")

Again, this reinforces the need for more parks in Queens and may also suggest that more should be done to encourage construction near existing parks.

## Historic Districts
As expected, the city-wide rate of permits in historic districts (.6%) is 84.8% lower than the rate among the randomly distributed points(3.9%). This is, of course, one of the purposes of a historic district, but it's worth considering when we look at building more housing in NYC. In particular, why are the districts located where they are? Do they contribute to inequity in housing opportunities?

![Rates of Location in Historical Districts City-Wide, Random versus Actual Permits](/images/city_historical_rando_actual.png "Rates of Historical District Location")

This dynamic is the same across boroughs and on a nominal measure most affects Manhattan, which has the largest share of its land taken up by historic districts, as represented by the higher proportion of random points falling in historic districts.

![Rates of Location in Historical Districts by Borough, Random versus Actual Permits](/images/boros_historic_rando_actual.png "Rates of Historical District Location by Borough, Random v. Actual")

## Criminal Complaints
Each borough's share of criminal complaints within .1 mile of its actual permits was compared to the boroughs share of all criminal complaints across the city, from 08/02/2014-08/02/2020.

![#Share of Permit Complaints Compared to All Complaints by Borough](images/perm_complaints_v_crime_boro.png "Share of Permit Complaints v. All Complaints, by Borough")

Brooklyn and Staten Island have disproportionately high shares of complaints in proximity to permits relative to their overall share of criminal complaints. This suggests that new construction is happening in relatively high crime areas of those boroughs.

Each borough's share of permits with outlier numbers of criminal complaints(>1084 complaints) within .1 mile was compared to the boroughs share of all criminal complaints across the city, from 08/02/2014-08/02/2020.

![Borough Share of Crime v Borough's Share of High Crime Permits](images/outlier_complaints__v_crime_boro.png "Permits w/Outlier Criminal Complaints versus Overall Crime Rates by Borough")

Likewise, each borough's share of permits with outlier numbers of criminal complaints(>1084 complaints) within .1 mile waas compared to the borough's share of criminal complaints within .1 of a permit across the city, again from 08/02/2014-08/02/2020.

![# of Permits with Outlier Levels of Criminal Complaints Compared to Permit Rates, by borough](images/outlier_complaints_v_perms_boro.png "Permits w/Outlier Criminal Complaints versus Overall Permit Rates by Borough")

In both cases, the Bronx and Manhattan have a disproportionate share of the permits with outlier numbers of criminal complaints. This suggests that while the Brooklyn is more likely to have new construction in a relatively high crime area compared to the rest of the borough, it's more likely that a new building in an extraordinarly high crime area falls in the Bronx or Manhattan.

Two notes:
One, because there's a lead time to start construction, the analysis examined criminal complaints starting and ending 2 years before the start and end time of the permit data unde examination. This roughly accounts for the criminal complaints at the time the decision to build was being made. More data on how long it takes from planning to permitting would help to refine this number, but especially given the relative stickiness of crime rates and relative rates of crime across the city over the short term, this rough estimate was considered adequate. 

Two, per the Open Data NYC site, crimes occurring anywhere other than an intersection are geo-located to the middle of the block. 

# Subway Entrances
I decided to look at numbers of entrances within tenth, half, one, and 2.5 mile radii of the permit. I wanted to find the closest entrance, along with half mile, but that would be very calculation intensive and take too long to run.

# Modeling



# Conclusions
- It would be advisable for the city to examine why development is not happening inversely proportionally to density and in the absence of good reasons for that, find ways to support more development in less dense boroughs.
- The city should examine why there's less parkland and, absent a good reason otherwise, develop more parks in Queens.
- It's possible that the lack of proximity to parks in Queens at least partly reflects difficulty in building near them. For a builder considering building in Queens looking for relative ease in getting approval, this warrants further exploration.
- The city should be very careful about expanding the number and/or size of historic districts as they do appear to impede the building of new residential buildings at a very high rate. It's also worth considering whether or not it may be possible to ease the path to new development in historic districts while still maintaining their historic character (for example, by easing approval and/or allowing the preservation of existing facades with new construction behind and above them for buidings that are not, themselves, considered historically significant.)
- Builders should be wary of trying to build in New York City Historic Districts.
- The city should examine why new construction is going up primarily in relatively high crime parts of Brooklyn and Staten Island. It's possible this reflects important economic development of underserved areas. Alternatively, it could reflect NIMBYism in lower crime areas. 
- The city should examine why there are so many permits at extremely high crime locations in Manhattan and the Bronx. Again, there may or may not be beneficial reasons behind this pattern.
- Builders considering Brooklyn and Staten Island should examine whether or not the trends there reflect relative ease of building in those relatively higher crime areas or another cause.

# Points for Refinement or Further Analysis
This analysis, as with most, has several points at which it could be refined or at which further analysis could be completed. Here are some that have been identified:
- use residential zoning as a factor in additional analyses involving borough area and the distribution of random points to see what insights are gleaned from that, especially in comparison to the analysis that doesn't include zoning.
- greater precision in closest park distance, as noted above.
- examining whether the number of parks within given radii (.1, .5, 1, 2.5 miles) reveals anything of value
- finding data on commuting times to central business distances from different parts of the boroughs could potentially add an interesting dimension to this analysis. For example, how long is the commute from different parts of Staten Island (thought of as being farther away but also less densely developed) into Manhattan and how does it compare to those of the other boroughs?