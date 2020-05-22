'''In this mission, we'll learn a couple other string cleaning tasks such as:

Finding specific strings or substrings in columns, extracting substrings from unstructured data, removing strings or substrings from a series.
We'll work with the 2015 World Happiness Report again and additional economic data from the World Bank.

Below are descriptions for the columns we'll be working with:

ShortName - Name of the country
Region - The region the country belongs to
IncomeGroup - The income group the country belongs to, based on Gross National Income (GNI) per capita
CurrencyUnit - Name of country's currency
SourceOfMostRecentIncomeAndExpenditureData - The name of the survey used to collect the income and expenditure data
SpecialNotes - Contains any miscellaneous notes about the data
To start, let's read the data sets into pandas and combine them.

Instructions

We've already read World_Happiness_2015.csv into a dataframe called happiness2015
and World_dev.csv into a dataframe called world_dev.

Use the pd.merge() function to combine happiness2015 and world_dev. Save the resulting dataframe to merged. 
As a reminder, you can use the following syntax to combine the dataframes: pd.merge(left=df1, right=df2, how='left', left_on='left_df_Column_Name', right_on='right_df_Column_Name').
Set the left_on parameter to the Country column from happiness2015 and the right_on parameter to the ShortName column from world_dev.
Use the DataFrame.rename() method to rename the SourceOfMostRecentIncomeAndExpenditureData column in merged to IESurvey (because we don't want to keep typing that long name!).
We've already saved the mapping to a dictionary named col_renaming.
Make sure to set the axis parameter to 1.'''

import pandas as pd
import numpy as np

happiness_2015 = pd.read_csv("World_Happiness_2015.csv")
world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
merged = pd.merge(left = happiness_2015, right = world_dev, how = 'left', left_on = 'Country', right_on = 'ShortName')
merged = merged.rename(col_renaming, axis = 1)

'''Instructions

Write a function called extract_last_word with the following criteria:
The function should accept one parameter called element.
Use the string.split() method to split the object into a list. First convert element to a string as follows: str(element).
Return the last word of the list.
Use the Series.apply() method to apply the function to the CurrencyUnit column. Save the result to merged['Currency Apply'].
Use the Series.head() method to print the first five rows in merged['Currency Apply'].'''

def extract_last(element):
    element = str(element).split()
    return(element[-1])

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last)

'''In fact, pandas has built in a number of vectorized methods that perform the same operations for strings in series as Python
 string methods.
Below are some common vectorized string methods, but you can find the full list here:

Method	Description
Series.str.split()	Splits each element in the Series.
Series.str.strip()	Strips whitespace from each string in the Series.
Series.str.lower()	Converts strings in the Series to lowercase.
Series.str.upper()	Converts strings in the Series to uppercase.
Series.str.get()	Retrieves the ith element of each element in the Series.
Series.str.replace()	Replaces a regex or string in the Series with another string.
Series.str.cat()	Concatenates strings in a Series.
Series.str.extract()	Extracts substrings from the Series matching a regex pattern.
We access these vectorized string methods by adding a str between the Series name and method name:

Syntax
The str attribute indicates that each object in the Series should be treated as a string, without us having to explicitly 
change the type to a string like we did when using the apply method.

Instructions

Use the Series.str.split() method to split the CurrencyUnit column into a list of words and then use the Series.str.get() method to select just the last word. Assign the result to merged['Currency Vectorized'].
Use the Series.head() method to print the first five rows in merged['Currency Vectorized'].'''

merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)
merged['Currency Vectorized'].head(5)

lengths = merged['CurrencyUnit'].str.len()
value_counts = lengths.value_counts(dropna = False)

'''In pandas, regular expression is integrated with vectorized string methods to make finding and extracting patterns of characters easier. However, the rules for creating regular expressions can be quite complex, so don't worry about memorizing them. In this mission, we'll provide guidance on how to create the regex we need to use for the exercises, but you can also follow along using this documentation.

Instructions

We've already saved the regex to a variable called pattern. The brackets, [], indicate that either "national accounts" or "National accounts" should produce a match.

Use the Series.str.contains() method to search for pattern in the SpecialNotes column. Assign the result to national_accounts.
Use the Series.head() method to print the first five rows in national_accounts.'''

pattern = r'[Nn]ational accounts'
national_accounts = merged['SpecialNotes'].str.contains(pattern, na = False)
national_accounts.head()
merged_national_accounts = merged[national_accounts]
merged_national_accounts.head(5)

'''With regular expressions, we use the following syntax to indicate a character could be a range of 
numbers:
pattern = r"[0-9]"

And we use the following syntax to indicate a character could be a range of letters:

#lowercase letters
pattern1 = r"[a-z]"
​
#uppercase letters
pattern2 = r"[A-Z]"

We could also make these ranges more restrictive. For example, if we wanted to find a three character substring in a column that starts with a number between 1 and 6 and ends with two letters of any kind, we could use the following syntax:

pattern = r"[1-6][a-z][a-z]"
If we have a pattern that repeats, we can also use curly brackets { and } to indicate the number of times it repeats:

pattern = r"[1-6][a-z][a-z]" = r"[1-6][a-z]{2}"

Instructions

Create a regular expression that will match years and assign it to the variable pattern. 
Note: we've already set up the pattern variable. Insert your answer inside the parantheses: 
"(your_answer)".
Use pattern and the Series.str.extract() method to extract years from the SpecialNotes column. 
Assign the resulting Series to years.'''

pattern =r"([1-2][0-9]{3})"
years = merged['SpecialNotes'].str.extract(pattern)

'''Instructions

Use pattern and the Series.str.extract() method to extract years from the SpecialNotes column again,
but this time, set the expand parameter to True to return the results as a dataframe. Assign the 
resulting dataframe to years.'''

pattern = r"([1-2][0-9]{3})"
years = merged['SpecialNotes'].str.extract(pattern, expand = True)

'''In the last screen, we learned we could use the Series.str.extract() method to extract a pattern of characters from a column as a dataframe by setting the expand parameter equal to True. However, the Series.str.extract() method will only extract the first match of the pattern. If we wanted to extract all of the matches, we can use the Series.str.extractall() method.

We'll demonstrate this method but, first, let's make the results easier to read by using the df.set_index() method to set the Country column as the index.

merged = merged.set_index('Country')
Next, let's use the same regular expression from the last screen to extract all the years from the Special Notes column, except this time, we'll use a named capturing group. Using a named capturing group means that we can refer to the group by the specified name instead of just a number. We can use the following syntax to add a name: (?P<Column_Name>...).

Below, we name the capturing group Years:

pattern = r"(?P<Years>[1-2][0-9]{3})"
merged['SpecialNotes'].str.extractall(pattern)

Instructions

We've already set the Country column as the index and saved the regular expression used to extract years
in the pattern variable.

Use the Series.str.extractall() method to extract all of the years in the IESurvey. Assign the result to
years.
Use the Series.value_counts() method to create a list of the unique years, along with the count. Assign
the result to value_counts. Print value_counts.'''

pattern = r"(?P<Years>[1-2][0-9]{3})"
years = merged['IESurvey'].str.extractall(pattern)
value_counts = years['Years'].value_counts()
print(value_counts)

Let's add those two groups to our regex and try to extract them again:

pattern = r"(?P<First_Year>[1-2][0-9]{3})(/)?(?P<Second_Year>[0-9]{2})?"
years = merged['IESurvey'].str.extractall(pattern)


'''Note that we also added a question mark, ?, after each of the two new groups to indicate that a
match for those groups is optional. This allows us to extract years listed in the yyyy format AND the 
yyyy/yy format at once. 
The dataframe returned has three columns - one for each capturing group specified in pattern. Because 
we didn't name the second group, (/), the capturing group number, 1, was used as the column name.'''

'''Instructions

We've already created a regular expression that extracts the pattern "yyyy/yy" and saved it to a variable
called pattern. Notice that we didn't enclose /? in parantheses so that the resulting dataframe will only
contain a First_Year and Second_Year column.

Use the Series.str.extractall() method to extract pattern from the IESurvey column. Assign the result to
years.
Use vectorized slicing to extract the first two numbers from the First_Year column in years (For example,
extract "20" from "2000"). Assign the result to first_two_year.
Add first_two_year to the Second_Year column in years, so that Second_Year contains the full year
(ex: "2000"). Assign the result to years['Second_Year'].'''

pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"
years = merged['IESurvey'].str.extractall(pattern)
first_two_year = years['First_Year'].str[0:2] #Extraemos los dos primeros numeros de la columna FirstYear para añadirlo en la SecondYear
years['Second_Year'] = first_two_year + years['Second_Year'] #unimos el paso anterior a la columna Second Year para dejar el año complejo es decir 2011


merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(' income', '').str.replace(':', '').str.upper()
pv_incomes = merged.pivot_table(index = 'IncomeGroup', values = 'Happiness Score')
pv_incomes.plot(kind = 'bar', rot = 30, ylim = (0, 10))

