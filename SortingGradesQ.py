import pandas as pd

#Inputting random student score for my dataframe
student_scores = {'ID':[1,2,3],
    'NAME': ['Sid','Tom','Dick'],
    'SCORES': [98,90,85]
}

df = pd.DataFrame(student_scores)

score_output = df.sort_values(by = 'SCORES', ascending = False)

score_output

score_output.iloc[:,[0,1]]