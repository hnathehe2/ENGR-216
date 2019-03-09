import csv
import matplotlib.pyplot as plt
import numpy as np


def velocity(d1, d2, t1, t2):
    v = (d2-d1)/(t2-t1)
    return v


def acceleration(v1, v2, t1, t2):
    a = (v2-v1)/(t2-t1)
    return a


def average(lists):
    summ = 0
    for i in range(len(lists)):
        summ += lists[i]
    avg = summ / len(lists)
    return avg


def repeat_point(point, length):
    points = []
    for i in range(length):
        points.append(point)
    return points


file_name = 'trial3-lab2.csv'
px_to_cm = 0.0967
theta = 3.7
x = []
y = []
first_line = True
went_back = False
start = False
wrongspeed = False
index = 0
first_y = 0
time = []
time_mid = []
time_mid_mid = []
vel_x = []
vel_y = []
acc_x = []
acc_y = []

with open(file_name, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if first_line:
            first_line = False
        else:
            if not went_back:
                if index == 0:
                    x.append(float(row[3])*px_to_cm)
                    y.append(float(row[4])*px_to_cm)
                    time.append(float(row[1])/1000)
                    index += 1
                else:
                    if (start==False):
                        if float(row[4])*px_to_cm-y[0]>2*px_to_cm:
                            start=True
                    elif float(row[4])*px_to_cm - y[index - 1] > -2*px_to_cm:
                        x.append(float(row[3]) * px_to_cm)
                        y.append(float(row[4]) * px_to_cm)
                        time.append(float(row[1]) / 1000)
                        index += 1
                    else:
                        went_back = True

check=True
for i in range(len(x) - 1):
    if check:
        vel_x.append(velocity(x[i], x[i+1], time[i], time[i+1]))
        vel_y.append(velocity(y[i], y[i+1], time[i], time[i+1]))
        if len(vel_y)>3:
            q=len(vel_y)
            if (vel_y[q-1]-vel_y[q-2]<-10):
                check=False
        time_mid.append((time[i+1] + time[i])/2)

for i in range(len(vel_x) - 1):
    acc_x.append(acceleration(vel_x[i], vel_x[i+1], time_mid[i], time_mid[i+1]))
    acc_y.append(acceleration(vel_y[i], vel_y[i + 1], time_mid[i], time_mid[i + 1]))
    time_mid_mid.append((time_mid[i+1] + time_mid[i])/2)

avg_acc_x = average(acc_x)
avg_acc_y = average(acc_y)

plt.subplot(211)
plt.plot(time_mid, vel_x, 'r-')
plt.title('Velocity X (cm/s)')
plt.xlabel('Time (s)', x=0, horizontalalignment='left')
plt.ylabel('Velocity (cm/s)')

plt.subplot(212)
plt.plot(time_mid, vel_y, 'b-')
plt.title('Velocity Y (cm/s)')
plt.xlabel('Time (s)', x=0, horizontalalignment='left')
plt.ylabel('Velocity (cm/s)')
plt.show()

plt.subplot(211)
plt.plot(time_mid_mid, acc_x, 'r-', label='')
plt.plot(time_mid_mid, repeat_point(avg_acc_x, len(time_mid_mid)), 'g-', label='Average Acceleration')
plt.annotate(str(avg_acc_x) + ' cm/s^2', xy=(time_mid_mid[0], avg_acc_x + 10))
plt.legend()
plt.title('Acceleration X (cm/s^2)')
plt.xlabel('Time (s)', x=0, horizontalalignment='left')
plt.ylabel('Acceleration (cm/s^2)')

plt.subplot(212)
plt.plot(time_mid_mid, acc_y, 'b-', label='')
plt.plot(time_mid_mid, repeat_point(avg_acc_y, len(time_mid_mid)), 'g-', label='Average Acceleration')
plt.annotate(str(avg_acc_y) + ' cm/s^2', xy=(time_mid_mid[0], avg_acc_y + 10))
plt.legend()
plt.title('Acceleration Y (cm/s^2)')
plt.xlabel('Time (s)', x=0, horizontalalignment='left')
plt.ylabel('Acceleration (cm/s^2)')
plt.show()

print('Velocity Y:', vel_y)
print(avg_acc_y)
print('Gravity:', avg_acc_y / np.sin(np.deg2rad(theta)))
