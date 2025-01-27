import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv("googleplaystore.csv")  #READ THE DATA SET
"""print(df.info())""" #TAKE THE INFO ABAOUT TYPE AND COUNT OF COLUMNS

df.columns = df.columns.str.replace(" ","_")   # REMOVE THE SPACE FROM COLUMNS NAMES AND PLACED _ FOR READIBILITY 

sns.set_theme()
"""sns.set(rc={"figure.dpi":150, "figure.figsize":(4,3)})
sns.heatmap(df.isnull(),cbar=False)
plt.show()"""                                             # THE GRAPH OF MISSING VALUES  AND WE SEE RATING HAS MANY MISSING VALUE


#                                                     SOLVE MISSING VALUE PROBLEM
median_of_rating = df["Rating"].median()         
df["Rating"] = df["Rating"].fillna(median_of_rating )   # WE FILL MISING VALUE WITH MEDIAN OF RATING

df.dropna(inplace=True)  # WE DROPPED OTHER MISSING  VALUE BECAUSE OF LESS NUMBER



#--------------------------------------------CHANGE AND REPAIR THE COLUMNS DATA TYPE ----------------------------------------------------------------------

df["Rating"]=df["Rating"].astype("float64")     # RATING



df["Reviews"] = df["Reviews"].str.replace("M","") 
df["Reviews"] = df["Reviews"].astype("int64")         # CHANGE THE THE DATA TYPE OF REVIEWS



df["Size"] = df["Size"].str.replace("M","")    # REMOVE LETTER M FROM SIZE COLUMN FOR READIBILITY AND CHANGE DATA TYPE
df["Size"] = df["Size"].str.replace("k","") 
median_of_size = df[df["Size"]!="Varies with device"]["Size"].astype(float).median()
df["Size"] = df["Size"].str.replace("Varies with device",str(median_of_size))
df.Size = pd.to_numeric(df.Size)     # CHANGE THE DATA TYPE OF SIZE           




df["Installs"] = df["Installs"].str.replace("+","")  # REMOVE THE + FROM INSTALLS COLUMN FOR READIBILITY AND CHANGE DATA TYPE
df["Installs"] = df["Installs"].str.replace(",","")
df.Installs = pd.to_numeric(df.Installs) # CHANGE DATA TYPE OF INSTALLS


df["Price"] = df["Price"].str.replace("$","") # REMOVE THE $ FROM PRICE FOR CHANGE DATA TYPE
df.Price = pd.to_numeric(df.Price)            # CHANGE THE DATA TYPE OF PRICE   


df.Genres = df.Genres.str.split(";").str[0]   # SPLIT THE GENRES COLUMN BECAUSE OF OVERAGE
"""print(df.Genres.unique())"""
df.Genres = df.Genres.str.replace("Music & Audio","Music")  


df.Last_Updated = df.Last_Updated.str.replace(",","")
df.Last_Updated = pd.to_datetime(df.Last_Updated)   # CHANGE THE DATA TYPE OF LAST UPDATED COLUMN



#--------------------------------------------------------------------------------------DATA VISUALIZATION--------------------------------------------------------------------------------------------------------------------------------------

                                 
                                 
                                 
#                                                                        THE BAR CHART OF THE NUMBER OF THE APP BY GENRES

the_nunmber_of_App_by_Genres=df.App.groupby(df.Genres).count()            # THE NUMBER OF APP BY GENRES
"""
plt.figure(figsize=(16,9))
the_nunmber_of_App_by_Genres.plot(kind='bar',color='green',edgecolor="white")
plt.title('The Number of Apps by Genres'.upper(),fontsize=18,fontdict={'family': 'DejaVu Sans', 'size': 18, 'weight': 'bold'})
plt.xlabel("Genres",fontdict={'family':'DejaVu Sans', 'size': 14, 'weight': 'bold'})
plt.xticks(rotation=90,ha='center',fontsize=13,weight='bold')
plt.ylabel("The Number of Apps",fontsize=14,fontdict={'family': 'DejaVu Sans', 'weight': "bold"})
plt.yticks(weight='bold',fontsize=12)
plt.tight_layout()
plt.show()"""                   








#                                                                         THE BAR PLOT OF THE TOTAL INSTALLS OF THE APPLICATION BY GENRES


the_total_Installs_by_Genres =df.Installs.groupby(df.Genres).sum()               # TOTAL INSTALLS OF THE APPLICATION BY GENRES 
"""
plt.figure(figsize=(16,9))
sns.barplot(x=the_total_Installs_by_Genres.index,
           y=the_total_Installs_by_Genres.values,palette="viridis")
plt.title('Total Installs by Genres'.upper(), fontsize=18,fontdict={'family': 'DejaVu Sans', 'size': 18, 'weight': 'bold'})
plt.xlabel('Genres', fontsize=14,fontdict={'family': 'DejaVu Sans', 'size': 14, 'weight': 'bold'})
plt.ylabel('Total Installs', fontsize=14,fontdict={'family': 'DejaVu Sans', 'weight': "bold"})
plt.xticks(rotation=90, ha='center', fontsize=12,weight='bold',fontfamily="DejaVu Sans")
plt.yticks(range(0,35000000000,5000000000),[f'{y:,}' for y in range(0,35000000000,5000000000)],fontfamily='DejaVu Sans',fontsize=12,weight='bold')
plt.tight_layout()
plt.show() """                



#                                                                           THE BOX PLOT OF APP FREE OR NOT

"""plt.figure(figsize=(16,9))
sns.boxplot(x= "Type", y = "Rating" , data=df)
plt.title("THE RELATIONSHIP BETWEEN TYPE AND RATING",fontdict={'family':"DejaVu Sans"},weight="bold")
plt.xticks(family="DejaVu Sans",weight="bold")
plt.yticks(family="DejaVu Sans",weight="bold")
plt.xlabel("Type",weight="bold")
plt.ylabel("Rating",weight="bold")
plt.show() """               




#                                                                           THE HEAT MAP OF OUR DATA
"""plt.figure(figsize = (16,9))
subset_df = df[["Installs", "Price", "Rating", "Reviews", "Size"]]
corr = subset_df.corr()
sns.heatmap(corr, annot = True, linewidths = .5, fmt=".2f")
plt.title("Heat Map of Our Data".upper(),weight="bold",fontdict={'family':"DejaVu Sans",'size':18})
plt.xticks(weight="bold",family="DejaVu Sans")
plt.yticks(weight="bold",family="DejaVu Sans")
plt.show()"""




#                                                                           THE BOX PLOT OF BETWEEN CONTENT RATING AND RATING
"""
palette = sns.color_palette("Set2", n_colors=6)
plt.figure(figsize=(16,9))
sns.boxplot(x= "Content_Rating", y = "Rating", data = df,palette=palette)
plt.title("THE RELATIONSHIP BETWEEN CONTENT RATING AND RATING",fontdict={'family':"DejaVu Sans",'size':14},weight="bold")
plt.xticks(family="DejaVu Sans",weight="bold")
plt.yticks(family="DejaVu Sans",weight="bold")
plt.xlabel("Content Rating",weight="bold",family="DejaVu Sans",)
plt.ylabel("Rating",weight="bold",family="DejaVu Sans",)
plt.show()"""





#                                                                            THE PIE CHART OF NUMBER OF APP BY CONTENT

the_number_of_App_by_ContentRating = df.App.groupby(df.Content_Rating).count()   
"""
the_number_of_App_by_ContentRating.plot(kind="pie", figsize=(16, 9), autopct='%1.1f%%')
plt.ylabel('')  
plt.title('Number of Apps by Content Rating in Google Play Store'.upper(),fontdict={'family':"DejaVu Sans"},weight="bold")
plt.xticks(weight="bold",fontfamily="DejaVu Sans")  
plt.show()"""





#                                                                             THE BAR PLOT OF TOTAL INSTALLS BY CONTENT RATING

the_total_Installs_by_ContentRating = df.Installs.groupby(df.Content_Rating).sum()
"""
plt.figure(figsize=(16, 9))
sns.barplot(x=the_total_Installs_by_ContentRating.index, 
            y=the_total_Installs_by_ContentRating.values, 
            palette="viridis")
plt.title("Total Installs by Content Rating", fontsize=18,weight='bold',fontdict={'family':"DejaVu Sans"})
plt.xlabel("Content Rating", fontsize=14,weight='bold',fontfamily="DejaVu Sans")
plt.ylabel("Total Installs", fontsize=14,weight='bold',fontfamily="DejaVu Sans")
plt.xticks(rotation=0,weight='bold',fontfamily="DejaVu Sans")
plt.yticks(range(0,120000000000,30000000000),[f'{y:,}' for y in range(0,120000000000,30000000000)],weight='bold',fontfamily="DejaVu Sans")  
plt.show()"""




df["Evaluation"] = pd.cut(df["Rating"], bins=[1.0,2.0,3.0,3.5,4.0,4.5,5.0],labels=["Awful","Bad","Medium","Good","Very Good","Perfect"])    # THE NEW COLUMN FOR EVALUATE RATING OF APPS




#                                                                              THE HORIZONTAL BAR CHART OF EVALUATION OF APPS BY GENRES

the_evaluations_by_Genres = df.groupby(['Genres', 'Evaluation']).size().unstack(fill_value=0)

"""colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'][::-1]
the_evaluations_by_Genres.plot(
    kind='barh',
    stacked=True,
    figsize=(16, 9),
    color=colors[:the_evaluations_by_Genres.shape[1]],
    alpha=0.9
)                                

plt.title('Rating distribution of each genres'.upper(), fontsize=16,weight="bold",fontfamily="DejaVu Sans")
plt.xlabel('Number of Apps', fontsize=12,weight="bold",fontfamily="DejaVu Sans")
plt.ylabel('Genres', fontsize=12,weight="bold",fontfamily="DejaVu Sans")
plt.legend(title='Evaluation', title_fontsize=10,)
plt.xticks(rotation=90,weight="bold",fontfamily="DejaVu Sans",fontsize=10)
plt.yticks(weight="bold",fontfamily="DejaVu Sans")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()"""












#                                                                                    THE HORIZONTAL BAR CHART OF AVERAGE INSTALLS BY GENRES

the_average_Installs_by_Genres = df["Installs"].groupby(df.Genres).mean().sort_values(ascending=False)
"""plt.figure(figsize=(16, 9))
sns.barplot(
    y=the_average_Installs_by_Genres.index,
    x=the_average_Installs_by_Genres.values,
    palette="viridis"
)

plt.title("AVERAGE INSTALLS BY GENRES", fontsize=16, weight="bold", fontfamily="DejaVu Sans")
plt.xlabel("Average Installs", fontsize=12, weight="bold", fontfamily="DejaVu Sans")
plt.ylabel("Genres", fontsize=12, weight="bold", fontfamily="DejaVu Sans")
plt.xticks(
    range(0, 85000000, 10000000),
    [f'{y:,}' for y in range(0, 85000000, 10000000)],
    rotation=90,
    fontsize=10,
    weight="bold",
    fontfamily="DejaVu Sans"
)
plt.yticks(fontsize=10, weight="bold", fontfamily="DejaVu Sans")
plt.tight_layout()
plt.show()"""


