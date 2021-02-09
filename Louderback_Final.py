#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# #This notebook is long, and though it has been edited to remove unnecessary mistakes, I have kept some code to show my work and thus my thinking as I worked through the various tasks.  

# Well done! Having spent years analyzing financial records for big banks, you've finally scratched your idealistic itch and joined the education sector. In your latest role, you've become the Chief Data Scientist for your city's school district. In this capacity, you'll be helping the  school board and mayor make strategic decisions regarding future school budgets and priorities.
# As a first task, you've been asked to analyze the district-wide standardized test results. You'll be given access to every student's math and reading scores, as well as various information on the schools they attend. Your responsibility is to aggregate the data to and showcase obvious trends in school performance.
# Your final report should include each of the following:
# 
# District Summary
# 
# Create a high level snapshot (in table form) of the district's key metrics, including:
# 
# Total Schools
# school_data["school_name"].nunique()
# Total Students
# len(student_data["Student ID"])
# Total Budget
# school_data["budget"].sum()
# Average Math Score
# student_data["math_score"].mean()
# Average Reading Score
# school_data_complete["reading_score"].mean()
# % Passing Math (The percentage of students that passed math.)
# student_data['passing_math'].value_counts()
# #True     29370
# #False     9800
# passing_math_total= 29370
# passing_math_pct= 29370/39170
# passing_math_pct
# #0.749808526933878
# % Passing Reading (The percentage of students that passed reading.)
# student_data['passing_read'].value_counts()
# #True     33610
# #False     5560
# passing_read_pct= 33610/39170
# passing_read_pct
# #0.8580546336482001
# % Overall Passing (The percentage of students that passed math and reading.)
# passing_both= student_data['passing_math'] & student_data['passing_read']
# student_data["passing_both"].value_counts()
# #True     25528
# #False    13642
# passing_both_pct= 25528/39170
# passing_both_pct
# #0.6517232575950983
# student_data["passing_both_value"]= (student_data["reading_score"]+student_data["math_score"])/200
# student_data["passing_both_value"]
# 
# 
# 
# 
# School Summary
# 
# Create an overview table that summarizes key metrics about each school, including:
# 
# School Name
# School Type
# Total Students
# Total School Budget
# Per Student Budget
# Average Math Score
# Average Reading Score
# % Passing Math (The percentage of students that passed math.)
# % Passing Reading (The percentage of students that passed reading.)
# % Overall Passing (The percentage of students that passed math and reading.)
# 
# 
# 
# 
# Top Performing Schools (By % Overall Passing)
# 
# Create a table that highlights the top 5 performing schools based on % Overall Passing. Include:
# 
# School Name
# School Type
# Total Students
# Total School Budget
# Per Student Budget
# Average Math Score
# Average Reading Score
# % Passing Math (The percentage of students that passed math.)
# % Passing Reading (The percentage of students that passed reading.)
# % Overall Passing (The percentage of students that passed math and reading.)
# 
# 
# 
# 
# Bottom Performing Schools (By % Overall Passing)
# 
# Create a table that highlights the bottom 5 performing schools based on % Overall Passing. Include all of the same metrics as above.
# 
# 
# Math Scores by Grade**
# 
# Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
# 
# Reading Scores by Grade
# 
# Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
# 
# Scores by School Spending
# 
# Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
# 
# Average Math Score
# Average Reading Score
# % Passing Math (The percentage of students that passed math.)
# % Passing Reading (The percentage of students that passed reading.)
# % Overall Passing (The percentage of students that passed math and reading.)
# 
# 
# 
# 
# Scores by School Size
# 
# Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).
# 
# 
# Scores by School Type
# 
# Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).
# 
# As final considerations:
# 
# Use the pandas library and Jupyter Notebook.
# You must submit a link to your Github/Git Lab repo that contains your Jupyter Notebook.
# You must include a written description of at least two observable trends based on the data.
# See Example Solution for a reference on the expected format.
# 
# 
# 
# 

# In[45]:





# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# In[46]:


school_data_complete


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[47]:


#District Summary


# In[ ]:





# In[48]:


tot_num_schools= school_data["school_name"].nunique()
tot_num_stds= len(student_data["Student ID"])
tot_dis_bgt= school_data["budget"].sum()
avg_dis_ms= student_data["math_score"].mean()
avg_dis_rs= student_data["reading_score"].mean()

school_data_complete["total_schools"]= tot_num_schools
school_data_complete["total_students"]= tot_num_stds
school_data_complete["total_budget"]= tot_dis_bgt

print(school_data_complete)


# In[49]:


school_data_complete["avg_dis_ms"]= avg_dis_ms
school_data_complete["avg_dis_rs"]= avg_dis_rs
#get boolean values for passing
pass_math=(school_data_complete["math_score"]>=70)
pass_read=(school_data_complete["reading_score"]>=70)
school_data_complete["pass_math"]= pass_math
school_data_complete["pass_read"]= pass_read

pass_both= school_data_complete['pass_math'] & school_data_complete['pass_read']
school_data_complete["pass_both"]= pass_both

#get numbers to find percentages
pass_math_total= school_data_complete['pass_math'].value_counts()
pass_math_pct= pass_math_total/tot_num_stds*100

pass_read_total= school_data_complete['pass_read'].value_counts()
pass_read_pct= pass_read_total/tot_num_stds*100

pass_both_total= school_data_complete["pass_both"].value_counts()
pass_both_pct= pass_both_total/tot_num_stds*100

school_data_complete["pass_math_pct"]= pass_math_pct
school_data_complete["pass_read_pct"]= pass_read_pct
school_data_complete["pass_both_pct"]= pass_both_pct


# In[50]:


print(school_data_complete)


# alculate the total number of schools
# 
# Calculate the total number of students
# 
# Calculate the total budget
# 
# Calculate the average math score
# 
# Calculate the average reading score
# 
# Calculate the percentage of students with a passing math score (70 or greater)
# 
# Calculate the percentage of students with a passing reading score (70 or greater)
# 
# Calculate the percentage of students who passed math and reading (% Overall Passing)
# 
# Create a dataframe to hold the above results

# In[51]:


district_data= school_data_complete.drop(columns=['size','grade','budget','Student ID','student_name','gender','school_name','reading_score','math_score','School ID','type','pass_math','pass_read','pass_both'])


# In[52]:


district_data_dropped= district_data.dropna()


# In[53]:


district_data_final= pd.DataFrame(district_data_dropped)
district_data_final = district_data_final.round(decimals=2)

district_data_final.to_csv('district_summary.csv', index=False, header=True)
type(district_data_final)
print(district_data_final)


# #DISTRICT DATA ABOVE 

# #SCHOOL DATA BELOW

# In[54]:


print(district_data)


# School Summary¶
# 
#     Create an overview table that summarizes key metrics about each school, including:
#         School Name
#         School Type
#         Total Students
#         Total School Budget
#         Per Student Budget
#         Average Math Score
#         Average Reading Score
#         % Passing Math
#         % Passing Reading
#         % Overall Passing (The percentage of students that passed math and reading.)
# 
#     Create a dataframe to hold the above results
# 
# 

# In[55]:


school_data_complete


# In[56]:


school_data


# In[57]:


school_data_complete['reading_score'][:2918] >= 70


# In[ ]:





# In[58]:


school_data_complete['reading_score'][2918:]


# In[59]:


listofRS= student_data["reading_score"]
listofmax= listofRS.to_list()
print(listofmax)


# In[ ]:





# In[60]:


hhsread.valuecounts()


# In[61]:


school_data["type"]


# In[62]:


typelist= school_data["type"]
listoftypes= typelist.to_list()
print(listoftypes)


# In[63]:


#school_data_sum = school_data.assign(e=pd.Series(np.random.randn(sLength)).values)
#df.assign(=df['temp_c'] * 9 / 5 + 32)


# In[64]:


#school_summary= school_data_complete.groupby(['school_name']).mean()
schools_summary=school_data_complete.drop(columns=['student_name','gender','grade','total_students','School ID','Student ID','avg_dis_ms','avg_dis_rs','total_schools','total_budget','pass_math','pass_math_pct','pass_read_pct','pass_read','pass_both','pass_both_pct'])
#schools_summary= school_data_complete.drop(columns=['grade','Student ID','student_name','gender','School ID','total_budget',"total_students','avg_dis_ms','avg_dis_rs','pass_math','pass_read','pass_both','total_schools'])
#ssdf=schools_summary.groupby(["school_name"]).mean()
#ssdf
schooldf= schools_summary.groupby(['school_name']).mean()
schooldf1 = schooldf.round(decimals=2)
#pass_both= finaldf['reading_score'] & finaldf['math_score'] >=70
#final_df["pass_both"]= pass_both
#finaldf[school_name[[Baily High School)]
#schooldf1.groupby(['school_name']).mean()
schooldf1.describe


# In[ ]:





# In[65]:


schooldf1.to_csv('school_brief.csv', index=False, header=True)


# In[66]:


DistinctCount=df["reading_score"].value_counts()
count=df["reading_score"].count()


# In[67]:


ssdf.columns


# In[ ]:





# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[68]:


district_df= pd.DataFrame(school_data_complete)
dfclean= district_df.drop(columns=['type','grade','student_name','gender', 'School ID','Student ID'])

tot_num_schools= school_data["school_name"].nunique()
tot_num_stds= len(student_data["Student ID"])
tot_dis_bgt= school_data["budget"].sum()
avg_dis_ms= student_data["math_score"].mean()
avg_dis_rs= student_data["reading_score"].mean()


school_data_complete["avg_dis_ms"]= avg_dis_ms
school_data_complete["avg_dis_rs"]= avg_dis_rs
#get boolean values for passing
pass_math=(school_data_complete["math_score"]>=70)
pass_read=(school_data_complete["reading_score"]>=70)
school_data_complete["pass_math"]= pass_math
school_data_complete["pass_read"]= pass_read

pass_both= school_data_complete['pass_math'] & school_data_complete['pass_read']
school_data_complete["pass_both"]= pass_both

#get numbers to find percentages
pass_math_pct= pass_math_total/tot_num_stds*100
pass_math_total= school_data_complete['pass_math'].value_counts()

pass_read_pct= pass_read_total/tot_num_stds*100
pass_read_total= school_data_complete['pass_read'].value_counts()

pass_both_pct= pass_both_total/tot_num_stds*100
pass_both_total= school_data_complete["pass_both"].value_counts()


sch_type= school_data_complete["type"]
#sch_size= school_data_complete["size"]
#tot_sch_bgt= school_data_complete["budget"]
per_st_bgt= school_data_complete["budget"]/school_data_complete["size"]
school_data_complete["per_st_bgt"]= per_st_bgt

#stread= school_data_complete["reading_score"].mean()
#stmath= school_data_complete["math_score"].mean()


# School Summary
# 
#     Create an overview table that summarizes key metrics about each school, including:
#         School Name
#         School Type
#         Total Students
#         Total School Budget
#         Per Student Budget
#         Average Math Score
#         Average Reading Score
#         % Passing Math
#         % Passing Reading
#         % Overall Passing (The percentage of students that passed math and reading.)
# 
#     Create a dataframe to hold the above results
# 
# 

# In[69]:


school_sum_df= school_data_complete.groupby(['school_name']).mean()
school_sum_df


# In[70]:


school_sum_df_clean = school_sum_df.drop(columns=['total_schools','total_students','total_budget','avg_dis_ms','avg_dis_rs','Student ID','School ID','pass_math_pct','pass_read_pct','pass_both_pct'])
#district_data= school_data_complete.drop(columns=['size','grade','budget','Student ID','student_name','gender','school_name','reading_score','math_score','School ID','type','pass_math','pass_read','pass_both'])


# In[71]:


indv_school_summaries= school_sum_df_clean.round(decimals=2)
print(indv_school_summaries)


# In[ ]:





# In[72]:


indv_school_summaries.to_csv('school_summaries.csv', index=True, header=True)


# In[73]:


iss_df=indv_school_summaries


# In[74]:


print(iss_df)


# 
# sch_type= school_data_complete["type"]
# sch_size= school_data_complete["size"]
# tot_sch_bgt= school_data_complete["budget"]
# per_st_bgt= school_data["budget"]/school_data["size"]
# stread= school_data_complete["reading_score"].mean()
# stmath= school_data_complete["math_score"].mean()
# 
# sdf= pd.DataFrame({'': [390., 350., 30., 20.]},
# 
#                   index=index)

# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[92]:


overpasslist= iss_df["pass_both"]


# In[93]:


overpasslist.sort_values(ascending=False)


# In[94]:


overpasslist.sort_values(ascending=False).head()


# In[ ]:





# In[ ]:






# In[ ]:





# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[95]:


overpasslist.sort_values(ascending=True)


# In[97]:


overpasslist.sort_values(ascending=True).head()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[130]:


#grade data
nine_gd_df=school_data_complete.loc[school_data_complete["grade"]=="9th" , :]
ten_gd_df=school_data_complete.loc[school_data_complete["grade"]=="10th" , :]
eleven_gd_df=school_data_complete.loc[school_data_complete["grade"]=="11th" , :]
twelve_gd_df=school_data_complete.loc[school_data_complete["grade"]=="12th" , :]


# In[132]:


print(nine_gd_df)


# In[133]:


#mean score
nine_math=nine_gd_df.groupby(["school_name"])["math_score"].mean()
ten_math=ten_gd_df.groupby(["school_name"])["math_score"].mean()
eleven_math=eleven_gd_df.groupby(["school_name"])["math_score"].mean()
twelve_math=twelve_gd_df.groupby(["school_name"])["math_score"].mean()

print(nine_math)


# In[134]:


#Summary DF 
gd_sum_df=school_data_complete.groupby(["school_name"]).mean()
gd_sum_df["9th Grade"]=nine_math
gd_sum_df["10th Grade"]=ten_math
gd_sum_df["11th Grade"]=eleven_math
gd_sum_df["12th Grade"]=twelve_math

print(gd_sum_df["12th Grade"])


# In[135]:


math_gd_sum_df=gd_sum_df[["9th Grade", "10th Grade", "11th Grade", "12th Grade"]]
math_gd_sum_df
math_gd_sum_df.index.name=None 
#Math Scores by Grade
print(math_gd_sum_df)


# In[ ]:





# In[112]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[ ]:


#grade data
nine_gd_df=school_data_complete.loc[school_data_complete["grade"]=="9th" , :]
ten_gd_df=school_data_complete.loc[school_data_complete["grade"]=="10th" , :]
eleven_gd_df=school_data_complete.loc[school_data_complete["grade"]=="11th" , :]
twelve_gd_df=school_data_complete.loc[school_data_complete["grade"]=="12th" , :]
print(eleven_gd_df)


# In[137]:


#mean scores read
nine_read=nine_gd_df.groupby(["school_name"])["reading_score"].mean()
ten_read=ten_gd_df.groupby(["school_name"])["reading_score"].mean()
eleven_read=eleven_gd_df.groupby(["school_name"])["reading_score"].mean()
twelve_read=twelve_gd_df.groupby(["school_name"])["reading_score"].mean()
print(nine_read)


# In[ ]:


#Summary DF read
gd_sum_df=school_data_complete.groupby(["school_name"]).mean()
gd_sum_df["9th Grade"]=nine_read
gd_sum_df["10th Grade"]=ten_read
gd_sum_df["11th Grade"]=eleven_read
gd_sum_df["12th Grade"]=twelve_read

read_gd_sum_df=gd_sum_df[["9th Grade", "10th Grade", "11th Grade", "12th Grade"]]
read_gd_sum_df
read_gd_sum_df.index.name=None 


# In[138]:


print(read_gd_sum_df)


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[ ]:





# In[229]:


#this dataframe gives asked for inforation with per student budget in no particular order
iss_df_sbs= iss_df.drop(columns=['size','budget'])
iss_df_sbs


# In[222]:


#code below gives school name and per student budget from low to high only
#iss_df_psb1= iss_df_sbs["per_st_bgt"].sort_values(ascending=True)
#iss_df_psb1


# In[225]:


#code below gives school name and per student budget from high to low only
#iss_df_psb2= iss_df_sbs["per_st_bgt"].sort_values(ascending=False)
#iss_df_psb2


# In[230]:


#give us all data asked for with "per student budget" listed from lowest to highest
iss_df_psbindex=iss_df_sbs.sort_values("per_st_bgt")
iss_df_psbindex


# In[209]:


iss_df_psbfinal= iss_df_sbs.sort_values(["per_st_bgt"])
iss_df_psbfinal


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[164]:


iss_df_sizehigh= iss_df["size"].sort_values(ascending=False)
iss_df_sizehigh


# In[165]:


iss_df_sizelow= iss_df.sort_values("size")
iss_df_sizelow


# In[203]:


print(iss_df["size"])


# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[ ]:





# In[197]:


listoftypes


# In[198]:


school_data


# In[184]:


iss_df


# In[200]:


typelist= school_data["type"]
listoftypes= typelist.to_list()
print(listoftypes)


# In[ ]:





# In[199]:


merge_df = pd.merge(school_data, iss_df, on="budget")
merge_df


# 
#     Average Math Score
#     Average Reading Score
#     % Passing Math
#     % Passing Reading
#     Overall Passing Rate (Average of the above two)
# 

# In[241]:


merge_df.sort_values(["school_name","type"])


# In[242]:


schl_data_type= merge_df.drop(columns=['size_x','size_y','budget','School ID','per_st_bgt'])
schl_data_type


# In[249]:


short_type_df= schl_data_type.groupby("type").mean()
short_type_df


# In[258]:


schl_data_type2=schl_data_type.set_index("type")
schl_data_type2


# In[260]:


schl_data_type2.loc[["District", "Charter"]]


# In[262]:


schl_data_type2.loc[["District"]].mean()


# In[263]:


schl_data_type2.loc[["Charter"]].mean()


# In[ ]:




