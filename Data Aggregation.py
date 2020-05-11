'''The data set is a CSV file called World_Happiness_2015.csv. Below are descriptions for some of the columns we'll be working with:

Country - Name of the country.
Region - Name of the region the country belongs to.
Happiness Rank - The rank of the country, as determined by its happiness score.
Happiness Score - A score assigned to each country based on the answers to a poll question that asks respondents to rate their happiness on a scale of 0-10.
Family - The estimated extent to which family contributes to the happiness score.
Freedom - The estimated extent to which freedom contributes to the happiness score.
Generosity - The estimated extent to which generosity contributes to the happiness score.
To start, let's read our data set into a pandas dataframe and inspect it.'''

import pandas as pd
import numpy as np



happiness_2015 = pd.read_csv("World_Happiness_2015.csv")
first_5 = happiness_2015[:5]
first_5.info

'''First, let's visualize the happiness score of each country in happiness2015:

happiness2015['Happiness Score'].plot(kind='bar', title='Happiness Scores', ylim=(0,10))
World Happiness Scores
Plotting the data in its current form isn't helpful at all! There are so many data points that we can't see any of the values or labels.

You may have noticed that each country in the happiness2015 dataframe is assigned to a region, specified in the Region column. We can use the Series.unique() method to confirm the unique regions:

happiness2015['Region'].unique()
array(['Western Europe', 'North America', 'Australia and New Zealand',
       'Middle East and Northern Africa', 'Latin America and Caribbean',
       'Southeastern Asia', 'Central and Eastern Europe', 'Eastern Asia',
       'Sub-Saharan Africa', 'Southern Asia'], dtype=object)
Let's try plotting just one region next:

so_asia = happiness2015[happiness2015['Region'] == 'Southern Asia']
so_asia.plot(x='Country', y='Happiness Score', kind='barh', title='Southern Asia Happiness Scores', xlim=(0,10))
Southern Asia Happiness
It's much easier to read this visualization - we can clearly see the labels and values. However, we wouldn't know if the Southern Asia region is representative of the entire world unless we look at the other regions. What we really want is to create a visualization that uses one number, a summary statistic like the mean, to summarize the data for each region.

Mean Happiness
In this mission, we'll learn how to perform different kinds of aggregations, applying a statistical operation to groups of our data, and create visualizations like the one above.

Recall that in the Pandas Fundamentals course, we learned a way to use loops for aggregation. Our process looked like this:

Identify each unique group in the data set.
For each group:
Select only the rows corresponding to that group.
Calculate the average for those rows.
Let's use the same process to find the mean happiness score for each region.

Instructions

Create an empty dictionary named mean_happiness to store the results of this exercise.
Use the Series.unique() method to create an array of unique values for the Region column.
Use a for loop to iterate over the unique region values from the Region column.
Assign the rows belonging to the current region to a variable named region_group.
Use the Series.mean() method to calculate the mean happiness score for region_group.
Assign the mean value to the mean_happiness dictionary, using the region name as the key and the mean happiness score as the value.'''

mean_happiness = {}
for i in happiness_2015['Region']:
    region_group = happiness_2015[happiness_2015['Region'] == i]
    region_mean = region_group['Happiness Score'].mean()
    mean_happiness[i] = region_mean

'To create a GroupBy object, we use the DataFrame.groupby() method: df.groupby('col') where col is the column you want to use to group the data set. Note that you can also group the data set on multiple columns by passing a list into the DataFrame.groupby() method. However, for teaching purposes, we'll focus on grouping the data by just one column in this mission.
'When choosing the column, think about which columns could be used to split the data set into groups. To put it another way, look at columns with the same value for multiple rows.'''

'Instructions
'Use the df.groupby() method to group happiness2015 by the Region column. Assign the result to grouped.
'Use the GroupBy.get_group() method to select the data for the Australia and New Zealand group only. Assign the result to aus_nz.'

grouped = happiness_2015.groupby('Region')
aus_nz = grouped.get_group('Australia and New Zealand')

'We can also use the GroupBy.groups attribute to get more information about the GroupBy object:'
grouped = happiness_2015.groupby('Region')
grouped.groups
'The result is a dictionary in which each key corresponds to a region name.'
'Notice that the values include the index for each row in the original happiness2015 dataframe with the corresponding region name'
'For the following exercise, use the result from the dictionary returned by grouped.groups shown below:

'''North America': Int64Index([4, 14], dtype=int64'''
'''Prove that the values for the North America group in the dictionary returned by grouped.groups above correspond to countries in North America in the happiness2015 dataframe.
Use the snippet above to identify the indexes of the countries in happiness2015 that belong to the North America group.
Use the indexes to assign just the countries in North America in happiness2015 to north_america.
Use the GroupBy.get_group() method to select the data for the North America group only. Assign the result to na_group.
Use the following code to compare north_america and na_group: north_america == na_group. Assign the result to equal.'''

north_america = happiness_2015.iloc[[4,14]]

na_group = grouped.get_group('North America')

equal = north_america == na_group

'''Methods	Description
mean()	Calculates the mean of groups.
sum()	Calculates the sum of group values.
size()	Calculates the size of the groups.
count()	Calculates the count of values in groups.
min()	Calculates the minimum of group values.
max()	Calculates the maximum of group values.'''

means = grouped['Happiness Score'].mean()

'''Select by Label	Syntax
Single column	GroupBy["col1"]
List of columns	GroupBy[["col1", "col2"]]'''

'''Instructions

Select just the Happiness Score column from grouped. Assign the result to happy_grouped.
Use the GroupBy.mean() method to compute the mean of happy_grouped. Assign the result to happy_mean.'''

happy_grouped = grouped['Happiness Score']
happy_mean = happy_grouped.mean()

'''For example, suppose we wanted to calculate both the mean and maximum happiness score for each region. Using what we learned so far, we'd have to first calculate the mean, like we did above, and then calculate the maximum separately.
Luckily, however, the GroupBy.agg() method can perform both aggregations at once. We can use the following syntax:
Agg_Syntax
Note that when we pass the functions into the agg() method as arguments, we don't use parentheses after the function names. For example, when we use np.mean, we refer to the function object itself and treat it like a variable, whereas np.mean() would be used to call the function and get the returned value.
The function names can also be passed in as strings, but we won't cover that explicitly in this mission. You can refer to this documentation for more information on this topic.
Let's practice using the agg() method next.
Apply the GroupBy.agg() method to happy_grouped. Pass a list containing np.mean and np.max into the method. Assign the result to happy_mean_max.
As noted above, passing 'mean' and 'max' into the GroupBy.agg() method will also return the same results. However, for answer checking purposes, 
you'll have to use np.mean and np.max.
We've also created a custom function named dif to calculate the difference between the mean and maximum values. Pass dif into the GroupBy.agg() method.
Assign the result to mean_max_dif.'''
def dif(group):
    return (group.max() - group.mean())

happy_mean_max = happy_grouped.agg([np.mean, np.max])
mean_max_dif = happy_grouped.agg(dif)

'''If you're an Excel user, you may have already drawn comparisons between the groupby operation and Excel pivot tables. If you've never used Excel, don't worry! No prior knowledge is needed for this mission. We'll demonstrate the pivot_table() method next.
Below, we use the df.pivot_table() method to perform the same aggregation as above.
Keep in mind that this method returns a dataframe, so normal dataframe filtering and methods can be applied to the result. For example, let's use the DataFrame.plot() method to create a visualization. Note that we exclude aggfunc below because the mean is 
the default aggregation function of df.pivot_table().'''

pv_happiness = happiness_2015.pivot_table(values = 'Happiness Score', index = 'Region', aggfunc = np.mean)

pv_happiness.plot(kind = 'barh', title = 'Mean Happiness Scores by Region', 
xlim = (0, 10), legend = False)

'''The pivot_table method also allows us to aggregate multiple columns and apply multiple functions at once.
Below, we aggregate both the 'Happiness Score' and 'Family' columns in happiness2015 and group by the 'Region' column:'''


happiness_2015.pivot_table(['Happiness Score', 'Family'], 'Region')

'''To apply multiple functions, we can pass a list of the functions into the aggfunc parameter:'''

happiness_2015.pivot_table('Happiness Score', 'Region', aggfunc = [np.mean, np.min, np.max],
margins = True)



grouped = happiness_2015.groupby('Region')[['Happiness Score', 'Family']]

happy_family_stats = grouped.agg([np.min, np.max, np.mean])
pv_happy_family_stats = happiness_2015.pivot_table(['Happiness Score', 'Family'], 'Region', aggfunc = [np.mean, np.max, np.min], 
margins = True)