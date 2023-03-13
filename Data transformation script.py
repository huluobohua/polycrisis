

#Locate file
import numpy as np
import pandas as pd
import openpyxl
f = 'https://github.com/huluobohua/polycrisis/blob/main/0.%20Polycrisis%20dashboard%20-%20Raw%20data%20for%20Mariana2.xlsx?raw=true'

"""### GBP indicator B"""

#Load xlsx sheet

df1 = pd.read_excel(f,
  sheet_name="GDP indicator B",
  skiprows=1,
  nrows=197,
  usecols="A:I"
);

df1.head()

#Replicate column C using A1 and A2
a1_gdpb = "IMF growth forecast for 2023 in Oct 21"
a2_gdpb = "IMF growth forecast for 2023 in Oct 22"

df1_c = ( df1[a2_gdpb] - df1[a1_gdpb] ) / abs(df1[a1_gdpb]) #operation


df1_c.head()

#Replicate column D using C

df1_d = df1_c + abs( df1_c.min() ) #operation

df1_d.head()

#Replicate column I using D

#normalisation
q1, q3 = df1_d.quantile(.25), df1_d.quantile(.75)
outlier_uppercut = q3 + 2*(q3-q1)
filter = df1_d.between(q1, outlier_uppercut, inclusive="both")
normalisation = pd.Series([
    #operation
     ((d-df1_d.min())/(df1_d[filter].max()-df1_d.min()) if d < outlier_uppercut
     else (1. if not np.isnan(d) else np.nan))
     for d in df1_d 
])

#reindexing
df1_i = 10 - 10*(normalisation)
df1_i.head()
df1["GDPindex"]=df1_i

"""### Food inflation indicator"""

#Load xlsx sheet
df2 = pd.read_excel(f,
  sheet_name="Food inflation indicator",
  skiprows=1,
  nrows=197,
  usecols="A:J"
);

df2.head()

#Replicate column B using A
a_fii = "Food inflation"
b_fii = "Food inflation shifted right"

df2_b = df2[a_fii] + abs(df2[a_fii].min()) #operation
assert all( df2_b.dropna() == df2[b_fii].dropna() ) #sanity check

df2_b.head()

#Replicate column I*10 using B
i_fii = "Normalized*10"

#normalisation
q1, q3 = df2_b.quantile(.25), df2_b.quantile(.75)
outlier_uppercut = q3 + 2*(q3-q1) 
#q3 + 2*(q3-q1) there is a manual override in the sheet
filter = df2_b.between(q1, outlier_uppercut, inclusive="both")
normalisation = pd.Series([
    #operation
     ((b-df2_b.min())/(df2_b[filter].max()-df2_b.min()) if b < outlier_uppercut
     else (1. if not np.isnan(b) else np.nan))
     for b in df2_b 
])

#reindexing
df2_i = 10*(normalisation)
df2_i
df2["FoodInfIndex"] = df2_i

"""### Credit Score indicator"""

#Load xlsx sheet
df3 = pd.read_excel(f,
  sheet_name="Credit Score indicator",
  skiprows=1,
  nrows=197,
  usecols="A:G"
);

df3.head()

#Replicate column B using A
a_csi = "Credit rating average"
b_csi = "Credit rating average inverted (to make more positive worse)"

df3_b = 21. - df3[a_csi] #operation
assert all( df3_b.dropna() == df3[b_csi].dropna() ) #sanity check

df3_b.head()

#Replicate column I*10 using B
i_csi = "Credit rating average normalized * 10 (values in red are imputted - exclude from indexation range)"

#normalisation
q1, q3 = df3[a_csi].quantile(.25), df3[a_csi].quantile(.75) #using column A
# q1, q3 = df3_b.quantile(.25), df3_b.quantile(.75) #using column B
outlier_uppercut = q3 + 2*(q3-q1)
filter = df3_b.between(q1, outlier_uppercut, inclusive="both")
normalisation = pd.Series([
    #operation
     ((b-df3_b.min())/(df3_b[filter].max()-df3_b.min()) if b < outlier_uppercut
     else (1. if not np.isnan(b) else np.nan))
     for b in df3_b 
])

#reindexing
df3_i = 10*(normalisation)
df3_i
df3["CreditRateIndex"] =df3_i







"""### External conflict risk"""


#Locate file
import numpy as np
import pandas as pd
import openpyxl
f = 'https://github.com/huluobohua/polycrisis/blob/main/0.%20Polycrisis%20dashboard%20-%20Raw%20data%20for%20Mariana2.xlsx?raw=true'


#Load xlsx sheet
df4 = pd.read_excel(f,
  sheet_name="External conflict risk",
  skiprows=1,
  nrows=197,
  usecols="A:J"
);

df4.head()

#Replicate column C123 using A1, A2  and A3
a1_ecr = "GPI Militarization 2022"
a2_ecr = "GPI Relationship with neighbors 2022"
a3_ecr = "Current external conflict (5 if current; 3 if probable or stand-off; 0 if none)"
c123_ecr = "GPI External Components"

df4_c123 = ( df4[a1_ecr]+df4[a2_ecr]+df4[a3_ecr] )/3 #operation
assert all( df4_c123.dropna() == df4[c123_ecr].dropna() ) #sanity check

df4_c123.head()

#Replicate column I using C123
i_ecr = "GPI external components normalized"

#normalisation
q1, q3 = df4_c123.quantile(.25), df4_c123.quantile(.75) #using column C123
outlier_uppercut = q3 + 2*(q3-q1)
filter = df4_c123.between(q1, outlier_uppercut, inclusive="both")
normalisation = pd.Series([
    #operation
     ((c-df4_c123.min())/(df4_c123[filter].max()-df4_c123.min()) if c < outlier_uppercut
     else (1. if not np.isnan(c) else np.nan))
     for c in df4_c123 
])

#reindexing
df4_i = 10*(normalisation)
df4_i
df4["ExternalConflictIndex"] = df4_i





#Locate file
import numpy as np
import pandas as pd
import openpyxl
f = 'https://github.com/huluobohua/polycrisis/blob/main/0.%20Polycrisis%20dashboard%20-%20Raw%20data%20for%20Mariana2.xlsx?raw=true'


"""### Political stability abs conf"""

#Load xlsx sheet
df5 = pd.read_excel(f,
  sheet_name="Political stability abs conf",
  skiprows=1,
  nrows=197,
  usecols="A:J"
)

df5.head()

#Replicate column I using A
a_psac = "2021 WGI Political stability"
i_psac = "WGI normalized"

#normalisation
q1, q3 = df5[a_psac].quantile(.25), df5[a_psac].quantile(.75) #using column A
outlier_uppercut = q3 + 2*(q3-q1)
filter = df5[a_psac].between(q1, outlier_uppercut, inclusive="both")
normalisation = pd.Series([
    #operation
     ((a-df5[a_psac].min())/(df5[a_psac][filter].max()-df5[a_psac].min()) if a < outlier_uppercut
     else (1. if not np.isnan(a) else np.nan))
     for a in df5[a_psac]
])

#reindexing
df5_i = 10 - 10*(normalisation)
df5_i
df5["PolStabIndex"] = df5_i





"""### Climate indicator"""

import numpy as np
import pandas as pd
import openpyxl
f = 'https://github.com/huluobohua/polycrisis/blob/main/0.%20Polycrisis%20dashboard%20-%20Raw%20data%20for%20Mariana2.xlsx?raw=true'

#Load xlsx sheet
df6 = pd.read_excel(f,
  sheet_name="Climate indicator",
  skiprows=1,
  nrows=197,
  usecols="A:K"
);

df6.head()

#Replicate column I using A
a_ci = "ND-GAIN Climate Vulnerability Index"
i_ci = "Climate index taken to 10 point scale"

#normalisation
q1, q3 = df6[a_ci].quantile(.25), df6[a_ci].quantile(.75)
outlier_uppercut = q3 + 2*(q3-q1)
q1,q3,outlier_uppercut
filter = df6[a_ci].between(q1, outlier_uppercut, inclusive="both")
normalisation = pd.Series([
    #operation
     ((a-df6[a_ci].min())/(df6[a_ci][filter].max()-df6[a_ci].min()) if a < outlier_uppercut
     else (1. if not np.isnan(a) else np.nan))
     for a in df6[a_ci]
])

#reindexing
df6_i = 10*(normalisation)
df6_i
df6["ClimateIndex"] = df6_i

df1.head()

df2.head()

df3.head()

df4.head()

df5.head()

df6.head()