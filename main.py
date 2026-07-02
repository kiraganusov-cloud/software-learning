# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print settings, characters, and context

print("\n India is widely known as one of the most populated countries in the world and a technology and undustrial hub. Poverty there is prominent, but reducing, and economic inequality is still a major issue. India's technological advancements make for a decent education system, but womens education still lags behind mens. Only around 55% of 22-year-old women have enrolled in higher education.")
print("\n Niger, a low-income, poverty-stricken country, has much lower education and literacy levels. Female primary school participation is just over 50%, which is an 8 year difference in education and learning. The lack of resources and encouragement for women in education leads to their lessened years of education. There are also has many obstructions, such as child marriage/early pregnancy, poverty and economic constraints, distance and infrastructure, and more.")

input("\n Press ENTER to continue")

print("\n  In Niger, there is not as high quality of education as there is in India, so women don’t have as many years of education. The poorness of the country also means significantly less households with electricity, which is visible on the graph,  but also limits the access to education and digital learning. ")
print("\n Women in India are likely to have more competition and interest in pursuing more years of education because they have more visible access to education. India is also a technology hub, so the education is likely more centered around electronics and technology, furthering their industry stance. Women in Niger tend to learn trades instead of pursuing an education like the women in India because it is much less available and not as important in their country’s economy.")

input("\n Press ENTER to view the graphed data and research question")

# graph:
print("Orange - Niger \nBlue - India")
listOfcountries = lwd["country_name"].unique()
# countries = india & niger

NigerCountryData = lwd.loc[lwd["country_name"] == "Niger"] # Orange
IndiaCountryData = lwd.loc[lwd["country_name"] == "India"] # blue


plt.scatter(data=IndiaCountryData, x="ED_educ_years_mean", y="EI_women_elec_p")
plt.scatter(data=NigerCountryData, x="ED_educ_years_mean", y="EI_women_elec_p")

plt.xlim(0,7)
plt.ylim(0,100)
plt.xlabel("Female average/median years of schooling")
plt.ylabel("Women living in an household with electricity (%)")
plt.title("Years of Schooling vs. Women Living with Electricity")

plt.show()

#research question
print("\nI believe that if women in Niger have more access to electricity, they will be able to access more education and their literacy rates and years of education will increase.")
print("\n My question: What innovative and accessible ways could women in Niger generate more electricity?")