'''In the last mission, we worked with just one data set, the 2015 World Happiness Report, to explore data aggregation. However, it's very common in practice to work with more than one data set at a time.
Often, you'll find that you need additional data to perform analysis or you'll find that you have the data, but need to pull it from mulitiple sources. In this mission, we'll learn a couple of different techniques for combining data using pandas to easily handle situations like these.
We'll use what we learned in the last mission to analyze the 2015, 2016, and 2017 World Happiness Reports. Specifically, we'll look to answer the following question:
Did world happiness increase, decrease, or stay about the same from 2015 to 2017?
As a reminder, these reports assign each country a happiness score based on a poll question that asks respondents to rank their life on a scale of 0 - 10, so "world happiness" refers to this definition specifically.
Below is a preview of the 2015 report:
Country	Region	Happiness Rank	Happiness Score	Standard Error	Economy (GDP per Capita)	Family	Health (Life Expectancy)	Freedom	Trust (Government Corruption)	Generosity	Dystopia Residual
0	Switzerland	Western Europe	1	7.587	0.03411	1.39651	1.34951	0.94143	0.66557	0.41978	0.29678	2.51738
1	Iceland	Western Europe	2	7.561	0.04884	1.30232	1.40223	0.94784	0.62877	0.14145	0.43630	2.70201
2	Denmark	Western Europe	3	7.527	0.03328	1.32548	1.36058	0.87464	0.64938	0.48357	0.34139	2.49204
3	Norway	Western Europe	4	7.522	0.03880	1.45900	1.33095	0.88521	0.66973	0.36503	0.34699	2.46531
4	Canada	North America	5	7.427	0.03553	1.32629	1.32261	0.90563	0.63297	0.32957	0.45811	2.45176
Below are descriptions for some of the columns:
Country - Name of the country
Region - Name of the region the country belongs to
Happiness Rank - The rank of the country, as determined by its happiness score
Happiness Score - A score assigned to each country based on the answers to a poll question that asks respondents to rate their happiness on a scale of 0-10
Let's start by reading the 2015, 2016, and 2017 reports into a pandas dataframe and adding a Year column to each to make it easier to distinguish between them.

Instructions

We've already read the World_Happiness_2015.csv file into a dataframe called happiness2015.
Use the pandas.read_csv() function to read the World_Happiness_2016.csv file into a dataframe called happiness2016 and the World_Happiness_2017.csv file into a dataframe called happiness2017.
Add a column called Year to each dataframe with the corresponding year. For example, the Year column in happiness2015 should contain the value 2015 for each row.'''
import pandas as pd
import numpy as np

happiness_2015 = pd.read_csv("World_Happiness_2015.csv")
happiness_2016 = pd.read_csv("World_Happiness_2016.csv")
happiness_2017 = pd.read_csv("World_Happiness_2017.csv")

'''Añadimos columnas a los df'''

happiness_2015['Year'] = 2015
happiness_2016['Year'] = 2016
happiness_2017['Year'] = 2017

'''Let's start by exploring the pd.concat() function. The concat() function combines dataframes one of two ways:
Stacked: Axis = 0 (This is the default option.)
Concat_Updated
Side by Side: Axis = 1
Concat_Axis1
Since concat is a function, not a method, we use the syntax below:
Concat_syntax
In the next exercise, we'll use the concat() function to combine subsets of happiness2015 and happiness2016 and then debrief the results on the following screen.
Below are the subsets we'll be working with:
head_2015 = happiness2015[['Country','Happiness Score', 'Year']].head(3)
Country	Happiness Score	Year
0	Switzerland	7.587	2015
1	Iceland	7.561	2015
2	Denmark	7.527	2015
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)
Country	Happiness Score	Year
0	Denmark	7.526	2016
1	Switzerland	7.509	2016
2	Iceland	7.501	2016
Let's use the concat() function to combine head_2015 and head_2016 next.

Instructions

We've already saved the subsets from happiness2015 and happiness2016 to the variables head_2015 and head_2016.
Use the pd.concat() function to combine head_2015 and head_2016 along axis = 0. Remember to pass the head_2015 and head_2016 into the function as a list. Assign the result to concat_axis0.
Use the pd.concat() function to combine head_2015 and head_2016 along axis = 1. Remember to pass head_2015 and head_2016 into the function as a list and set the axis parameter equal to 1. Assign the result to concat_axis1.
Use the variable inspector to view concat_axis0 and concat_axis1.
Assign the number of rows in concat_axis0 to a variable called question1.
Assign the number of rows in concat_axis1 to a variable called question2.'''

head_2015 = happiness_2015[['Country','Happiness Score', 'Year']].head(3)
head_2016 = happiness_2016[['Country','Happiness Score', 'Year']].head(3)

concat_axis0 = pd.concat([head_2015, head_2016], axis = 0)
concat_axis1 = pd.concat([head_2015, head_2016], axis = 1)
question1 = 6
question2 = 3