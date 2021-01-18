#!/usr/bin/env python
# coding: utf-8

# In[214]:



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


# In[215]:


#Your final report should include each of the following:

#District Summary

#Create a high level snapshot (in table form) of the district's key metrics, including:

#Total Schools
#sum number of schools
#15 schools
#Total Students
#sum number of students
#39170
#Total Budget
school_data["budget"].sum()
#Average Math Score
#total number of test takers divided by scores
#Average Reading Score
#total number of test takers divided by scores
#% Passing Math (The percentage of students that passed math.)
#sum of test takers with scores at or above the passing number
#% Passing Reading (The percentage of students that passed reading.)
#sum of test takers with scores at or above the passing number
#% Overall Passing (The percentage of students that passed math and reading.)
#sum of test takers with scores at or above the passing number for both subjects





#School Summary

#Create an overview table that summarizes key metrics about each school, including:

#School Name
#School Type
#Total Students
#Total School Budget
#Per Student Budget
#Average Math Score
#Average Reading Score
#% Passing Math (The percentage of students that passed math.)
#% Passing Reading (The percentage of students that passed reading.)
#% Overall Passing (The percentage of students that passed math and reading.)




#Top Performing Schools (By % Overall Passing)

#Create a table that highlights the top 5 performing schools based on % Overall Passing. Include:

#School Name
#School Type
#Total Students
#Total School Budget
#Per Student Budget
#Average Math Score
#Average Reading Score
#% Passing Math (The percentage of students that passed math.)
#% Passing Reading (The percentage of students that passed reading.)
#% Overall Passing (The percentage of students that passed math and reading.)




#Bottom Performing Schools (By % Overall Passing)

#Create a table that highlights the bottom 5 performing schools based on % Overall Passing. Include all of the same metrics as above.


#Math Scores by Grade**

#Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


#Reading Scores by Grade

#Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


#Scores by School Spending

#Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:

#Average Math Score
#Average Reading Score
#% Passing Math (The percentage of students that passed math.)
#% Passing Reading (The percentage of students that passed reading.)
#% Overall Passing (The percentage of students that passed math and reading.)




#Scores by School Size

#Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).


#Scores by School Type

#Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).

#As final considerations:

#Use the pandas library and Jupyter Notebook.
#You must submit a link to your Github/Git Lab repo that contains your Jupyter Notebook.
#You must include a written description of at least two observable trends based on the data.
#See Example Solution for a reference on the expected format.
#school_data_complete.describe
budget_total=0
school_total= school_data["school_name"].unique()
sc=0
#district_per_st_budget=24649428/39169
#school_data["budget"].sum()=24649428
studatread= float
passing_math=bool
pm=0
passboth=0
passing_read=0

#school_data["school_name"].nunique()
#15
#len(student_data["Student ID"])
#39170
#school_data["budget"].sum()
#$24,649,428
#student_data["math_score"].mean()
#78.98537145774827
#school_data["reading_score"].mean()
#81.87784018381414
#student_data['passing_math'].value_counts()
#yes,passing_math=     29370
#no,passing_math= 9800
#student_data['passing_read'].value_counts()
#yes,passing_reading= 33610
#no,passing_reading= 5560


# In[222]:


print(school_data_complete)


# In[ ]:





# In[216]:


type(school_data_complete["reading_score"])


# In[217]:


school_data["budget"].sum()


# In[139]:


sc=school_data["school_name"].unique()
print(sc)


# In[140]:


#school_data["school_count"]
    #Syntax: pandas.unique(Series)
    #Syntax: Dataframe.nunique (axis=0/1, dropna=True/False)
    #Syntax: Dataframe.col_name.nunique()
    #Syntax: Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)

school_data["school_name"].nunique()


# In[141]:


len(school_data["school_name"])


# In[142]:


print(student_data)


# In[143]:


len(student_data["Student ID"])


# In[144]:


student_data["student_name"].nunique()


# In[145]:


24649428/39169


# In[146]:


school_data["budget"]


# In[147]:


school_data["budget"]/school_data["size"]


# In[148]:


studatread= student_data["reading_score"].mean()
print(studatread)


# In[149]:


student_data["math_score"].mean()


# In[150]:


school_data_complete["reading_score"].mean()


# In[151]:


print(student_data[["math_score", "reading_score"]])


# In[152]:


type(student_data["math_score"])


# In[ ]:





# In[171]:


student_data["math_score"].bool >=70:


# In[195]:


passing_math=(student_data["math_score"]>=70)
passing_read=(student_data["reading_score"]>=70)


# In[196]:


print(passing_math)


# In[197]:


student_data["passing_math"]= passing_math
student_data["passing_read"]= passing_read
student_data.head()


# In[198]:


student_data['passing_math'].value_counts()


# In[199]:


student_data['passing_read'].value_counts()


# In[211]:


student_data["reading_score"]=pd.to_numeric(student_data["reading_score"])


# In[208]:


student_data["math_score"]=pd.to_numeric(student_data["math_score"])


# In[213]:


for row in student_data["reading_score"]:
    if student_data["reading_score"]>= 70:
        passing_read=passing_read+1


# In[56]:


print(student_data)


# In[57]:


print(school_data_complete)


# In[218]:


print(school_data)


# In[220]:


#Let's set the index to First Name. For this to stick you have to save it to a dataframe
ind_student_data=student_data.set_index("school_name")

#Notice how the columns are off-set now.  First Name is in a different position.
ind_student_data


# In[39]:


school_data.iloc[0:]


# In[221]:


school_data_complete.describe


# In[33]:


student_data[["reading_score","math_score"]].head()


# In[17]:


print(student_data.iloc[2])


# In[18]:


print(school_data.iloc[3])


# In[47]:


print(school_data).loc['total students']


# In[49]:



print(student_data[["reading_score","math_score"]])


# In[63]:



            


# In[59]:


student_data["reading_score"].describe


# In[64]:


student_percent= student_data["reading_score"]/100
student_percent


# In[69]:


school_data(passing)


# In[ ]:


student_data_complete

