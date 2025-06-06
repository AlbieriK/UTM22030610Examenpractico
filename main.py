import pandas as pd
import numpy as np
################################
df = pd.read_csv("dt.csv")
df = pd.read_csv("dt.csv")
#######################################################
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["discount"] = pd.to_numeric(df["discount"], errors="coerce") #converts to numbers and if there is something strange it puts NAN
#################################################
df["order_date"] = pd.to_datetime(df["order_date"]) #change the format to date
#############################################
df["sales_filled"] = df["sales"].fillna(0)#replaces empty values ​​with 0
#########################################
df["discount"] = df["discount"].mask(df["discount"] < 0, np.nan)#replace negative numbers with NAN
##############################
df_cleaned = df.dropna(subset=["sales", "discount"], how="all")#ELIMINATE SALES AND DISCOUNTS
#########################

west_missing_sales = df[(df["region"] == "West") & (df["sales"].isna())]#Filter empty sales from west 
mean_discount = df["discount"].mean()
df["discount"] = df["discount"].fillna(mean_discount)
discount_index_2 = df.loc[2, "discount"]

df.loc[df["sales"].notna() & df["discount"].notna(), "net_sales"] = df["sales"] * (1 - df["discount"] / 100)
######################
filtered_sales_discount = df[(df["sales"] >= 200) & (df["discount"] <= 10)] #filter data greater than two hundred with a specific discount xd

######################
sorted_sales = df[df["sales"].notna()].sort_values("order_date", ascending=False) #order the dates in specific order


df["weekday"] = df["order_date"].dt.day_name()

df = df.dropna(axis=1, how="all")#This is to delete all empty columns in general xd











#
#

#






















#print("Nueva columna sales_filled:\n", df[["sales", "sales_filled"]])
#print("\nFilas con descuentos negativos reemplazados por NaN:\n", df["discount"])
#print("\nDataFrame sin filas donde sales y discount están ambos vacíos:\n", df_cleaned)
#print("\nFilas donde region es West y sales es NaN:\n", west_missing_sales)
#print(f"\nValor en discount del índice 2 después de llenar con promedio: {discount_index_2}")
#print("\nColumna net_sales:\n", df[["sales", "discount", "net_sales"]])
#print("\nFiltrado por sales >= 200 y discount <= 10:\n", filtered_sales_discount)
#print("\nOrdenado por order_date descendente (sales no NaN):\n", sorted_sales)
#print("\nColumna weekday:\n", df[["order_date", "weekday"]])
#print("\nDataFrame final sin columnas completamente vacías:\n", df)
