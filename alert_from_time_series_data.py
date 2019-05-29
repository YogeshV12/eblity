import sqlite3
import pandas as pd
import numpy as np
import time
import dateutil
import calendar


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
print("Opened database successfully")
c = conn.execute('SELECT UserName, StudentName, Grade, TimeSeries, Concept, ConceptProgress, SubConcept, SubConceptProgress, TotalProblemSolvingTime, QuestionsAttempted, PerSolved, AverageTimePerQuestion,  LearningGapsDetected, LearningGapsResolved from stitched_time_series_data WHERE SiteName = "Home" AND Concept <> "" GROUP BY Username, TimeSeries, Concept, SubConcept ORDER BY Grade')
# for row in c:
#     print(row)
headers = []
headers.append("UserName")
headers.append("StudentName")
headers.append("Grade")
headers.append("TimeSeries")
headers.append("Concept")
headers.append("ConceptProgress")
headers.append("SubConcept")
headers.append("SubConceptProgress")
headers.append("TotalProblemSolvingTime")
headers.append("QuestionsAttempted")
headers.append("PerSolved")
headers.append("AverageTimePerQuestion")
headers.append("LearningGapsDetected")
headers.append("LearningGapsResolved")
df = []
# # print(headers)

# curr_username = "asdf"
# for row in c:
#     global curr_username
#     curr_username = row[0]
#     break
# print(curr_username)
df = []
for i, row in enumerate(c):
    # print(i)
    record = []
    for col in row:
        record.append(col)
        # print(col)
    df.append(record)
# clusters = []
# print(df[:])
# for row in c:
#     global clusters
#     if (curr_username != row[0]):
#         df.append(clusters)
#         clusters = []
#         columns = []
#         for cols in row:
#             columns.append(cols)
#         clusters.append(columns)
#         curr_username = row[0]
#     else:
#         columns = []
#         for cols in row:
#             columns.append(cols)
#         clusters.append(columns)
        
# print(len(df))


df = pd.DataFrame(data=np.array(df), columns=headers)
# print(len(dfs))
print(df.head())

list_of_alerts = []
# for df in dfs:
#     print(df)
    # df['TimeSeries']=pd.to_datetime(df['TimeSeries'])
    # df.sort_values(by=['TimeSeries'], inplace=True, ascending=True)

    # alert on % Learning gap resolved
for UserName, StudentName, Grade, TimeSeries, Concept, ConceptProgress, SubConcept, SubConceptProgress, PerSolved, AverageTimePerQuestion, LGD, LGR in zip(df['UserName'], df['StudentName'], df['Grade'], df['TimeSeries'], df['Concept'], df['ConceptProgress'], df['SubConcept'], df['SubConceptProgress'], df['PerSolved'], df['AverageTimePerQuestion'], df['LearningGapsDetected'], df['LearningGapsResolved']):
    if LGD != '' and LGR != '' and int(LGD) != 0 and int(LGR) != 0:
        if (int(LGR) / int(LGD))*100 <= 75:
            alert = []
            alert.append(UserName)
            alert.append(StudentName)
            alert.append(Grade)
            alert.append(TimeSeries)
            alert.append(Concept)
            alert.append(ConceptProgress)
            alert.append(SubConcept)
            alert.append(SubConceptProgress)
            alert.append(PerSolved)
            alert.append(AverageTimePerQuestion)
            alert.append(LGD)
            alert.append(LGR)
            alert.append(str((int(LGR) / int(LGD))*100) + "%")
            alert.append("Percentage Learning gap is below 75%")
            list_of_alerts.append(alert)

    # if average time per question  is greater than 10 minutes % ^-^ alert
            if AverageTimePerQuestion != '' and int(AverageTimePerQuestion) >= 7:
                    alert = []
                    alert.append(UserName)
                    alert.append(StudentName)
                    alert.append(Grade)
                    alert.append(TimeSeries)
                    alert.append(Concept)
                    alert.append(ConceptProgress)
                    alert.append(SubConcept)
                    alert.append(SubConceptProgress)
                    alert.append(PerSolved)
                    alert.append(AverageTimePerQuestion)
                    alert.append(LGD)
                    alert.append(LGR)
                    alert.append(str((int(LGR) / int(LGD))*100) + "%")
                    alert.append("average time per question  is greater than 7 minutes")
                    list_of_alerts.append(alert)

alert_df = pd.DataFrame(data = np.array(list_of_alerts), columns = ["UserName", "StudentName", "Grade", "TimeSeries", "Concept", "ConceptProgress", "SubConcept", "SubConceptProgress", "PerSolved", "AverageTimePerQuestion", "LGD", "LGR", "PerLearningGapResolved", "comment"])

alert_df.to_csv("all_alerts.csv", index = False)