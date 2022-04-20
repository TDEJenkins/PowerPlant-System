
# import the PySerial module and other libraries
import serial
import time
from git import Repo

# expirement counter, tracks the number to make sure we do not overwrite files
replicate = 1

# set up the serial line
ser = serial.Serial('COM5', 9600) #('COM4', 9600)
time.sleep(2)


# Read and record the data
#runs for about 5 seconds while data is collected from the sensor. 
#If it seems like the loop is stuck, press [Ctrl] + [c].
data =[]                       # empty list to store the data
for i in range(50):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    flt = float(string)        # convert string to float
    print(flt)
    data.append(flt)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()

# show the data
for line in data:
    print(line)

# save data to a txt or csv file
with open("moisture_data" + str(replicate) + ".txt", "w") as out_file:      #opens a file and writes into the file
    for i in range(len(data)):                                              # for loop to count through the index of list 
        out_string = ""                                                     #builds string called "outstring" and is assigned an empty string
        out_string += str(data[i])                                          #turns 'data' list into a string and uses index 'i' to count
        out_string += '\n'                                                  # after reading each data point it creates a new line for better visablilty
        out_file.write(out_string)                                          #writes stringed data to output file 'out_file'


#plotting the data
import matplotlib.pyplot as plt
# if using a Jupyter notebook include %matplotlib inline

plt.plot(data)
plt.xlabel('Time (seconds)')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()

# save plot to a file
plt.savefig('moisture_plot' + str(replicate)+'.png')

# function that sends files to github repository

PATH_OF_GIT_REPO = r'C:/Users/tayso/PowerPlant-System'  # make sure .git folder is properly configured on PC
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo.init(PATH_OF_GIT_REPO) # initialize repository
        repo.index.add('PowerPlant-System/moisture_data.csv','PowerPlant-System/moisture_plot.png') #add files, configure correctly before use
        repo.index.commit(COMMIT_MESSAGE) # stages the commit with pre made message
        origin = repo.remote(name='origin') # define origin and remote location
        origin.push(force = True) # force pushes the commit to the repository
    except:
        print('Some error occured while pushing the code') # if error occurs
git_push() # calls function 