import streamlit as st

st.title("Data Tren User Survey")

st.write("Angkatan 2011 - 2015")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
from statistics import mean
import math

st.write("Data Tren User Survey", st.session_state["Fakultas"], "Prodi", st.session_state["Jurusan"])
st.write("Angkatan 2011 - 2015")


#---------------------------------STATUS PEKERJAAN-------------------------------------------#
import pandas as pd

data_2018 = pd.read_excel(
    io="C:/Users/MSI/Downloads/Magang Tracer Study Script/Data Mentah Sortir_Analisis Tren_v3.xlsx",
    engine="openpyxl",
    sheet_name="2018",
    usecols="A:CP",
    nrows=3010,
)
data_2019 = pd.read_excel(
    io="C:/Users/MSI/Downloads/Magang Tracer Study Script/Data Mentah Sortir_Analisis Tren_v3.xlsx",
    engine="openpyxl",
    sheet_name="2019",
    usecols="A:CQ",
    nrows=3010,
)

data_2020 = pd.read_excel(
    io="C:/Users/MSI/Downloads/Magang Tracer Study Script/Data Mentah Sortir_Analisis Tren_v3.xlsx",
    engine="openpyxl",
    sheet_name="2020",
    usecols="A:CQ",
    nrows=3010,
)

data_2021 = pd.read_excel(
    io="C:/Users/MSI/Downloads/Magang Tracer Study Script/Data Mentah Sortir_Analisis Tren_v3.xlsx",
    engine="openpyxl",
    sheet_name="2021",
    usecols="A:CL",
    nrows=3010,
)

data_2022 = pd.read_excel(
    io="C:/Users/MSI/Downloads/Magang Tracer Study Script/Data Mentah Sortir_Analisis Tren_v3.xlsx",
    engine="openpyxl",
    sheet_name="2022",
    usecols="A:CL",
    nrows=3010,
)

#filter based on major
selected_major = st.session_state["Jurusan"]
dm18_filtered = data_2018[(data_2018['4. Program Studi']==selected_major)]
dm19_filtered = data_2019[(data_2019['4. Program Studi']==selected_major)]
dm20_filtered = data_2020[(data_2020['4. Program Studi']==selected_major)]
dm21_filtered = data_2021[(data_2021['Program Studi']==selected_major)]
dm22_filtered = data_2022[(data_2022['Program Studi']==selected_major)]



#waktu tunggu
wt18 = dm18_filtered.iloc[:, 75:94]
wt19 = dm19_filtered.iloc[:, 76:95]
wt20 = dm20_filtered.iloc[:, 76:95]
wt21 = dm21_filtered.iloc[:, 77:89]
wt22 = dm22_filtered.iloc[:, 77:89]


#sebelum lulus
sbl18 = []
sbl19 = []
sbl20 = []
sbl21 = []
sbl22 = []
#sesudah lulus
ssd18 = []
ssd19 = []
ssd20 = []
ssd21 = []
ssd22 = []

#tahun 2018
for i in range(len(wt18)):
    if wt18.iloc[i, 1] == 'sebelum lulus':
        sbl = wt18.iloc[i, 2]
        sbl18.append(sbl)
    elif wt18.iloc[i, 1] == 'sesudah lulus':
        ssd = wt18.iloc[i, 3]
        ssd18.append(ssd)

med18 = statistics.median(sbl18)
medsd18 = statistics.median(ssd18)
#tahun 2019
for i in range(len(wt19)):
    if wt19.iloc[i, 1] == 'sebelum lulus':
        sbl = wt19.iloc[i, 2]
        sbl19.append(sbl)
    elif wt19.iloc[i, 1] == 'sesudah lulus':
        ssd = wt19.iloc[i, 3]
        ssd19.append(ssd)
med19 = statistics.median(sbl19)
medsd19 = statistics.median(ssd19)
#tahun 2020
for i in range(len(wt20)):
    if wt20.iloc[i, 1] == 'sebelum lulus':
        sbl = wt20.iloc[i, 2]
        sbl20.append(sbl)
    elif wt20.iloc[i, 1] == 'sesudah lulus':
        ssd = wt20.iloc[i, 3]
        ssd20.append(ssd)
med20 = statistics.median(sbl20)
medsd20 = statistics.median(ssd20)
#tahun 2021
for i in range(len(wt21)):
    if wt21.iloc[i, 1] == 'Sebelum lulus':
        sbl = wt21.iloc[i, 2]
        sbl21.append(sbl)
    elif wt21.iloc[i, 1] == 'Sesudah lulus':
        ssd = wt21.iloc[i, 3]
        ssd21.append(ssd)
med21 = statistics.median(sbl21)
medsd21 = statistics.median(ssd21)
#tahun 2022
for i in range(len(wt22)):
    if wt22.iloc[i, 1] == 'Sebelum lulus':
        sbl = wt22.iloc[i, 2]
        sbl22.append(sbl)
    elif wt22.iloc[i, 1] == 'Sesudah lulus':
        ssd = wt22.iloc[i, 3]
        ssd22.append(ssd)
med22 = statistics.median(sbl22)
medsd22= statistics.median(ssd22)


medsbl= [med18, med19, med20, med21, med22]
medssd = [medsd18, medsd19, medsd20, medsd21, medsd22]
#sebelum lulus
year = ['2018', '2019', '2020' , '2021' , '2022']

#set the plot
fig, ax = plt.subplots(figsize=(8,4))

# Set the border properties
ax.spines['left'].set_visible(True)    # Show left border
ax.spines['bottom'].set_visible(True)  # Show bottom border
ax.spines['right'].set_visible(True)   # Show right border
ax.spines['top'].set_visible(True)     # Show top border

# Customize the border style
border_style = {'linewidth': 0.5, 'edgecolor': 'black'}
for spine in ax.spines.values():
    spine.set(**border_style)
    
#give the marker
plt.plot(year, medsbl, color='blue', marker='o')
#set the grid
ax.set_facecolor("white")
plt.grid(color='black',axis='y',alpha=0.2)
#give the labels
for i in range(len(medsbl)):
        plt.text(i,medsbl[i]+0.5,medsbl[i],ha = 'center')
#plotting the line
plt.plot(year, medsbl, '#4F81BD', marker='o',linewidth=2.0)
plt.ylim((0,max(medsbl)+2))
plt.yticks(fontsize=12)
plt.title('Waktu Tunggu Sebelum Lulus (Median)')

st.pyplot(fig)

#sesudah lulus

#set the plot
fig2, ax2 = plt.subplots(figsize=(8,4))

# Set the border properties
ax2.spines['left'].set_visible(True)    # Show left border
ax2.spines['bottom'].set_visible(True)  # Show bottom border
ax2.spines['right'].set_visible(True)   # Show right border
ax2.spines['top'].set_visible(True)     # Show top border

# Customize the border style
border_style = {'linewidth': 0.5, 'edgecolor': 'black'}
for spine in ax2.spines.values():
    spine.set(**border_style)
    
#give the marker
plt.plot(year, medssd, color='blue', marker='o')
#set the grid
ax.set_facecolor("white")
plt.grid(color='black',axis='y',alpha=0.2)
#give the labels
for i in range(len(medssd)):
        plt.text(i,medssd[i]+0.5,medssd[i],ha = 'center')
#plotting the line
plt.plot(year, medssd, '#4F81BD', marker='o',linewidth=2.0)
plt.ylim((0,max(medssd)+2))
plt.yticks(fontsize=12)
plt.title('Waktu Tunggu Sesudah Lulus (Median)')
st.pyplot(fig2)



#pendapatan bekerja
pb18 = []
pb19 = []
pb20 = []
pb21 = []
pb22 = []
#pendapatan usaha
pu18 = []
pu19 = []
pu20 = []
pu21 = []
pu22 = []

def Average(lst):
    return sum(lst) / len(lst)

#grouping for bekerja and wirausaha category
#year 2018
for i in range(len(wt18)):
    if wt18.iloc[i, 0] == 'bekerja':
        x = wt18.iloc[i, 6]
        pb18.append(x)
    elif wt18.iloc[i, 0] == 'wirausaha':
        x = wt18.iloc[i, 15]
        pu18.append(x)
    elif wt18.iloc[i, 0] == 'bekerja dan wiraswasta':
        x = wt18.iloc[i, 11]
        pb18.append(x)

#year 2019
for i in range(len(wt19)):
    if wt19.iloc[i, 0] == 'bekerja':
        x = wt19.iloc[i, 6]
        pb19.append(x)
    elif wt19.iloc[i, 0] == 'wirausaha':
        x = wt19.iloc[i, 15]
        pu19.append(x)
    elif wt19.iloc[i, 0] == 'bekerja dan wiraswasta':
        x = wt19.iloc[i, 11]
        pb19.append(x)

#year 2020
for i in range(len(wt20)):
    if wt20.iloc[i, 0] == 'bekerja':
        x = wt20.iloc[i, 6]
        pb20.append(x)
    elif wt20.iloc[i, 0] == 'wirausaha':
        x = wt20.iloc[i, 15]
        pu20.append(x)
    elif wt20.iloc[i, 0] == 'bekerja dan wiraswasta':
        x = wt20.iloc[i, 11]
        pb20.append(x)
        
#year 2021
for i in range(len(wt21)):
    if wt21.iloc[i, 0] == 'Bekerja':
        x = wt21.iloc[i, 7]
        pb21.append(x)
    elif wt21.iloc[i, 0] == 'Wirausaha':
        x = wt21.iloc[i, 9]
        pu21.append(x)
    elif wt21.iloc[i, 0] == 'Bekerja dan wiraswasta':
        x = wt21.iloc[i, 7]
        pb21.append(x)
        
#year 2022
for i in range(len(wt22)):
    if wt22.iloc[i, 0] == 'Bekerja':
        x = wt22.iloc[i, 7]
        pb22.append(x)
    elif wt22.iloc[i, 0] == 'Wirausaha':
        x = wt22.iloc[i, 9]
        pu22.append(x)
    elif wt22.iloc[i, 0] == 'Bekerja dan wiraswasta':
        x = wt22.iloc[i, 7]
        pb22.append(x)

#convert into dataframe
pb18 = pd.DataFrame(pb18)
pb19 = pd.DataFrame(pb19)
pb20 = pd.DataFrame(pb20)
pb21 = pd.DataFrame(pb21)
pb22 = pd.DataFrame(pb22)

#calculate the statistics descriptive
pbd18 = pb18.describe()
pbd19 = pb19.describe()
pbd20 = pb20.describe()
pbd21 = pb21.describe()
pbd22 = pb22.describe()
#calculation for the table (bekerja)
#calculate the count
mean_pb18 = pbd18.loc['mean', 0]
median_pb18 = pbd18.loc['50%', 0]


bc_18 = "{} orang".format(len(pb18))
bc_19 = "{} orang".format(len(pb19))
bc_20 = "{} orang".format(len(pb20))
bc_21 = "{} orang".format(len(pb21))
bc_22 = "{} orang".format(len(pb22))


#calculate mean
mean_pb18 = "Rp {:,.2f}".format(pbd18.loc['mean', 0])
mean_pb19 = "Rp {:,.2f}".format(pbd19.loc['mean', 0])
mean_pb20 = "Rp {:,.2f}".format(pbd20.loc['mean', 0])
mean_pb21 = "Rp {:,.2f}".format(pbd21.loc['mean', 0])
mean_pb22 = "Rp {:,.2f}".format(pbd22.loc['mean', 0])
#calculate the lowest value
min_pb18 = "Rp {:,.2f}".format(pbd18.loc['min', 0])
min_pb19 = "Rp {:,.2f}".format(pbd19.loc['min', 0])
min_pb20 = "Rp {:,.2f}".format(pbd20.loc['min', 0])
min_pb21 = "Rp {:,.2f}".format(pbd21.loc['min', 0])
min_pb22 = "Rp {:,.2f}".format(pbd22.loc['min', 0])

#calculate the highest value
max_pb18 = "Rp {:,.2f}".format(pbd18.loc['max', 0])
max_pb19 = "Rp {:,.2f}".format(pbd19.loc['max', 0])
max_pb20 = "Rp {:,.2f}".format(pbd20.loc['max', 0])
max_pb21 = "Rp {:,.2f}".format(pbd21.loc['max', 0])
max_pb22 = "Rp {:,.2f}".format(pbd22.loc['max', 0])

#calculate the median
med_b18 = "Rp {:,.2f}".format(pbd18.loc['50%', 0])
med_b19 = "Rp {:,.2f}".format(pbd19.loc['50%', 0])
med_b20 = "Rp {:,.2f}".format(pbd20.loc['50%', 0])
med_b21 = "Rp {:,.2f}".format(pbd21.loc['50%', 0])
med_b22 = "Rp {:,.2f}".format(pbd22.loc['50%', 0])
#calculate standard deviation
std_b18 = "Rp {:,.2f}".format(pbd18.loc['std', 0])
std_b19 = "Rp {:,.2f}".format(pbd19.loc['std', 0])
std_b20 = "Rp {:,.2f}".format(pbd20.loc['std', 0])
std_b21 = "Rp {:,.2f}".format(pbd21.loc['std', 0])
std_b22 = "Rp {:,.2f}".format(pbd22.loc['std', 0])
# std_b21 = "Rp{:,}".format(statistics.pstdev(pb21))
# std_b22 = "Rp{:,}".format(statistics.pstdev(pb22))

countb = [bc_18, bc_19, bc_20, bc_21, bc_22]
minb = [min_pb18, min_pb19, min_pb20, min_pb21, min_pb22]
maxb = [max_pb18, max_pb19, max_pb20, max_pb21, max_pb22]
medb = [med_b18, med_b19, med_b20, med_b21, med_b22]
meanb = [mean_pb18, mean_pb19, mean_pb20, mean_pb21, mean_pb22]
stdb = [std_b18, std_b19, std_b20, std_b21, std_b22]



df1 = pd.DataFrame(
    [countb, minb, maxb, medb, meanb, stdb],
    columns=('2018', '2019', '2020', '2021', '2022'), 
    index=['Count', 'Min', 'Max', 'Median', 'Mean', 'Standard Deviation'])

st.table(df1)


#calculation for the table (wirausaha)
#calculate the count
bu_18 = "{} orang".format(len(pu18))
bu_19 = "{} orang".format(len(pu19))
bu_20 = "{} orang".format(len(pu20))
bu_21 = "{} orang".format(len(pu21))
bu_22 = "{} orang".format(len(pu22))

#calculate mean
mean_pu18 = "Rp {:,.2f}".format(Average(pu18))
mean_pu19 = "Rp {:,.2f}".format(Average(pu19))
mean_pu20 = "Rp {:,.2f}".format(Average(pu20))
mean_pu21 = "Rp {:,.2f}".format(np.nanmean(pu21))
mean_pu22 = "Rp {:,.2f}".format(1)
#calculate the lowest value
min_pu18 = "Rp {:,.2f}".format(np.nanmin(pu18))
min_pu19 = "Rp {:,.2f}".format(np.nanmin(pu19))
min_pu20 = "Rp {:,.2f}".format(np.nanmin(pu20))
min_pu21 = "Rp {:,.2f}".format(np.nanmin(pu21))
min_pu22 = "Rp {:,.2f}".format(np.nanmin(1))

#calculate the highest value
max_pu18 = "Rp {:,.2f}".format(np.nanmax(pu18))
max_pu19 = "Rp {:,.2f}".format(np.nanmax(pu19))
max_pu20 = "Rp {:,.2f}".format(np.nanmax(pu20))
max_pu21 = "Rp {:,.2f}".format(np.nanmax(pu21))
max_pu22 = "Rp {:,.2f}".format(np.nanmax(1))
# max_pu22 = "Rp{:,.2f}".format(max(pu22))

#calculate the median
med_u18 = "Rp {:,.2f}".format(np.nanmedian(pu18))
med_u19 = "Rp {:,.2f}".format(np.nanmedian(pu19))
med_u20 = "Rp {:,.2f}".format(np.nanmedian(pu20))
med_u21 = "Rp {:,.2f}".format(np.nanmedian(pu21))
med_u22 = "Rp {:,.2f}".format(np.nanmedian(pu22))
# med_u22 = "Rp{:,.2f}".format(statistics.median(pu22))
#calculate standard deviation
std_u18 = "Rp {:,.2f}".format(np.nanstd(pu18))
# std_u19 = "Rp{:,}".format(statistics.pstdev(pu19))
std_u19 = "Rp {:,.2f}".format(np.nanstd(pu19))
std_u20 = "Rp {:,.2f}".format(np.nanstd(pu20))
std_u21 = "Rp {:,.2f}".format(np.nanstd(pu21))
std_u22 = "Rp {:,.2f}".format(np.nanstd(pu22))
# std_u21 = "Rp{:,}".format(statistics.pstdev(pu21))
# std_u22 = "Rp{:,}".format(statistics.pstdev(pu22))

countu = [bu_18, bu_19, bu_20, bu_21, bu_22]
minu = [min_pu18, min_pu19, min_pu20, min_pu21, min_pu22]
maxu = [max_pu18, max_pu19, max_pu20, max_pu21, max_pu22]
medu = [med_u18, med_u19, med_u20, med_u21, med_u22]
meanu = [mean_pu18, mean_pu19, mean_pu20, mean_pu21, mean_pu22]
stdu = [std_u18, std_u19, std_u20, std_u21, std_u22]



df2 = pd.DataFrame(
    [countu, minu, maxu, maxu, meanu, stdu],
    columns=('2018', '2019', '2020', '2021', '2022'), 
    index=['Count', 'Min', 'Max', 'Median', 'Mean', 'Standard Deviation'])

st.table(df2)


# line plot 
# bekerja
#define the value
categories = ['Median','Mean']
# med_bb = [med_b18, med_b19, med_b20, med_b21, med_b22]
# mean_bb = [mean_pb18, mean_pb19, mean_pb20, mean_pb21, mean_pb22]

med_bb = [med_b18, med_b19, med_b20, med_b21, med_b22]
mean_bb = [mean_pb18, mean_pb19, mean_pb20, mean_pb21, mean_pb22]
#data label
# def addlabels(x,y):
#     for i in range(len(x)):
#         plt.text(i+0.3,y[i]+100000,y[i],ha = 'center')
#         return a
#plotting
fig3,ax3 = plt.subplots(figsize=(11,6))
ax3.set_facecolor("white")

# Set the border properties
ax3.spines['left'].set_visible(True)    # Show left border
ax3.spines['bottom'].set_visible(True)  # Show bottom border
ax3.spines['right'].set_visible(True)   # Show right border
ax3.spines['top'].set_visible(True)     # Show top border

# Customize the border style
border_style = {'linewidth': 0.5, 'edgecolor': 'black'}
for spine in ax3.spines.values():
    spine.set(**border_style)
    
#plot the line
plt.plot(year, med_bb, '#4F81BD', marker='o',linewidth=2.0,label = "median")
plt.plot(year, mean_bb, '#C0504D', marker='o',linewidth=2.0,label = "mean")
plt.grid(color='black',axis='y',alpha=0.2)

#set the y limit
# val = 5000000
# ax3.set_yticks((0, val, 2*val, 3*val, 4*val, 5*val, 6*val))
# plt.ylim((-1000000, 32000000))

#formatting the y ticks
# current_values = plt.gca().get_yticks()
# plt.gca().set_yticklabels(['Rp{:,}'.format(x) for x in current_values])

# ##set the data label
# for i in range(len(med_bb)):
#         plt.text(i,med_bb[i]-2000000, 'Rp{:,}'.format(float(med_bb[i])),ha = 'center')
# for i in range(len(mean_bb)):
#         plt.text(i,mean_bb[i]+1000000,'Rp{:,}'.format(float(mean_bb[i])),ha = 'center')


#setting the legend
ax3.legend(categories,fontsize="14",loc='lower left', bbox_to_anchor=(0.25, -0.25),facecolor="white",edgecolor="white",ncol=2)
st.pyplot(fig3)
