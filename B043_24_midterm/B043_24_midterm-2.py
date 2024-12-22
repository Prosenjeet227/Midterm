import numpy as np
daily_screen =[]
num_app =[]
gender=[]
file_open =open('D:\\New folder (2)\\mobile_usage_behavioral_analysis.csv','r')
heading = file_open.readline()
line_file = file_open.readline()

while (len(line_file) > 0):
    arr = line_file.strip().split(',')
    gender.append(arr[2])
    daily_screen.append(float(arr[4]))
    num_app.append(float(arr[5]))
    line_file = file_open.readline()

file_open.close()
print(gender)

print(daily_screen)
print(num_app)

daily_screen_list = np.array(daily_screen)
print(daily_screen_list.mean())
print(daily_screen_list.max())
print(daily_screen_list.min())
num_app_list = np.array(num_app)
print(num_app_list.mean())
print(num_app_list.max())
print(num_app_list.min())



