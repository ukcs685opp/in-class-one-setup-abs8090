import matplotlib.pyplot as plt
import numpy as np

print("plot figures here")
q_list = []
x_line = []
y_line = []
num_list = []
nn_list = []
# default_scenario_ContactTimesReport.txt
# default_scenario_MessageDelayReport.txt

f = open("reports/default_scenario_ContactTimesReport.txt")
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")    
for i in range(len(lines)):
    l = lines[i].split(" ")
    x_line.append(float(l[0]))
    y_line.append(float(l[1]))
print(x_line)
print(y_line)

plt.title("length of contact times")
plt.xlabel("time")
plt.ylabel("number of contact")
plt.plot(x_line,y_line)
plt.show()

x_line = []
y_line = []

f = open("reports/default_scenario_MessageDelayReport.txt")
lines2 = f.readlines()
for i in range(len(lines2)):
    lines2[i] = lines2[i].rstrip("\n")    

for i in range(1,len(lines2)):
    l = lines2[i].split(" ")
    x_line.append(float(l[0]))
    y_line.append(float(l[1]))
print(x_line)
print(y_line)

plt.title("message delay")
plt.xlabel("time")
plt.ylabel("cumulative probability")
plt.plot(x_line,y_line)
plt.show()
# ############################

# f = open("sarsa.txt")
# lines = f.readlines()
# for i in range(len(lines)):
#     lines[i] = lines[i].rstrip("\n")
#     num_list.append(i)

# for line in lines:
#     sarsa_list.append(float(line)) # this is cumulative value, not individual

   
# ############################

# f = open("rmax.txt")
# lines = f.readlines()
# for i in range(len(lines)):
#     lines[i] = lines[i].rstrip("\n")
#     # num_list.append(i)


# ############################
# # f = open("nn.txt")
# # lines = f.readlines()
# # for i in range(len(lines)):
# #     lines[i] = lines[i].rstrip("\n")    

# # for line in lines:
# #     nn_list.append(float(line))



# ###########################
# for line in lines:
#     rmax_list.append(float(line))

# plt.title("after 30K episodes")
# plt.xlabel("episodes")
# plt.ylabel("mean reward")
# plt.plot(num_list,q_list, color = 'black', label="Q-Learning")
# plt.plot(num_list,sarsa_list, c = 'blue', label="SARSA")
# plt.plot(num_list,rmax_list, c = 'red',label="RMAX")
# legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')

# ############################
# #print(eps_list)
# #print(ucb_list)
# #print(tho_list)
# plt.show()
