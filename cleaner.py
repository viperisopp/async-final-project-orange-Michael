import pandas as pd
import numpy as np

# wdi = pd.read_csv("datasets/world_development_indicator/wdi_data.csv")
# def simplify_years(years):
#     years = years.split()[0]
#     return years
# wdi = wdi.drop("Series Code",axis="columns")
# wdi = wdi.melt(id_vars=["Country Name","Country Code","Series Name"], var_name = "Years", value_name = "Values")
# wdi["Years"] = wdi["Years"].apply(simplify_years).astype(int)
# wdi = wdi[wdi["Values"] != '..']
# wdi = wdi.reset_index(drop=True)
# wdi.to_csv("wdi.csv",index=False)

# sdg_seven = pd.read_csv("datasets/sustainable_development_goals/Goal7.csv")
# sdg_seven = sdg_seven[["SeriesDescription","GeoAreaName","TimePeriod","Value","Location"]]
# print(sdg_seven[sdg_seven["TimePeriod"] == sdg_seven["Time_Detail"]]) check if time detail is redundant
# print(sdg_seven["Units"].unique()) check if units is redundant
# sdg_seven = sdg_seven[sdg_seven["Value"].notnull()]
# sdg_seven.to_csv("sdg_seven.csv",index=False)

# sdg_nine = pd.read_csv("datasets/sustainable_development_goals/Goal9.csv")
# sdg_nine = sdg_nine[["SeriesDescription","GeoAreaName","TimePeriod","Value","Mode of transportation","Location","Units"]]
# print(sdg_nine[sdg_nine["TimePeriod"] == sdg_nine["Time_Detail"]]) check if time detail is redundant
# print(sdg_nine["Units"].unique()) check if units is redundant
# sdg_nine.to_csv("sdg_nine.csv",index=False)

# sdg_eleven = pd.read_csv("datasets/sustainable_development_goals/Goal11.csv")
# print(sdg_eleven[sdg_eleven["TimePeriod"] == sdg_eleven["Time_Detail"]]) check if time detail is redundant
# print(sdg_eleven["Units"].unique()) check if units is redundant
# sdg_eleven = sdg_eleven[["SeriesDescription","GeoAreaName","TimePeriod","Value","Location"]]
# sdg_eleven.to_csv("sdg_eleven.csv",index=False)

# lpi = pd.read_csv("datasets/logistics_preformance_index/lpi_data.csv")
# lpi = lpi.drop("Series Code",axis="columns")
# lpi = lpi.melt(id_vars=["Country Name","Country Code","Series Name"], var_name = "Years", value_name = "Values")
# lpi["Years"] = lpi["Years"].apply(simplify_years).astype(int)
# lpi = lpi[lpi["Values"] != '..']
# lpi.to_csv("lpi.csv",index=False)

# df = pd.read_csv("datasets/intermediate_indicators/inter_indicator_data.csv")
# df = df.drop("Series Code",axis="columns")
# df = df.melt(id_vars=["Country Name","Country Code","Series Name"], var_name = "Years", value_name = "Values")
# df["Years"] = df["Years"].apply(simplify_years).astype(int)
# df = df[df["Values"] != '..']
# df.to_csv("inter_ind_data.csv",index=False)

# df = pd.read_csv("cleaned/country_gdp.csv")
# df = df[["Country Name","Country Code","2020"]]
# df.to_csv("cleaned/country_gdp.csv",index=False)