#!/usr/bin/env python

import pandas as pd
from collections import Counter
from typing import List


# Set the oppropriate filenames for input and output
input_file = r".\emails.csv"
output_file =r".\common_domains.csv"


# read the data into a pandas dataframe
df = pd.read_csv(input_file)


# Select the column required as a pandas data series
emails = df["Email"]
domains= [email.split('@')[1] for email in emails]

# How many occurrences of each domain
counter = Counter(domains)

# Create a new pandas dataframe with the domain and counts tallied, in ascending order
ordered_domains = pd.DataFrame(counter.items(), columns=['Domain', 'Count']).sort_values(by='Count', ascending=False)

# Grab the top 3 entries
data = ordered_domains.head(3)
print(data)


# write to a new CSV file
data.to_csv(output_file, index=False)

