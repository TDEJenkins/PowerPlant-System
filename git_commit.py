from lib2to3.pytree import convert
from git import Repo
from requests import request
from sqlalchemy import false

#user inputs different watering levels to set what is over adn under watered for plant being sensored
overwater = (input("Enter over watering levels: "))
print("Overwatering level set to " + overwater)
underwater = (input("Enter under watering levels: "))
print("Underwatering level set to " + underwater)

#converts overwater and underwater variables to an integer
convert_underwater = int(underwater)
convert_overwater = int(overwater)

#test data list simulating sensor reader data
data = [325, 350, 325, 350, 375, 475, 525]

# function that sends files to github repository
PATH_OF_GIT_REPO = r'C:/Users/tayso/PowerPlant-System'  # make sure .git folder is properly configured on PC
COMMIT_MESSAGE = 'PowerPlant System Alert!'

def git_push():
    try:
        repo = Repo.init(PATH_OF_GIT_REPO) # initialize repository
        repo.index.add('PowerPlant-System/moisture_data.csv','PowerPlant-System/moisture_plot.png') #add files, configure correctly before use
        repo.index.commit(COMMIT_MESSAGE) # stages the commit with pre made message
        origin = repo.remote(name='origin') # define origin and remote location
        origin.push(force = True) # force pushes the commit to the repository
    except:
        print('Some error occured while pushing the code') # if error occurs



# code that reads the data list and sends discord alert if user over and water levels were reached while reading
if any(x <= convert_underwater for x in data):
    COMMIT_MESSAGE = 'Power Plant System Alert: Plant is Underwatered! Check for issue.'
    print('Power Plant System Alert: Plant is Underwatered! Check for issue.')
    git_push() # calls function
elif any(x >= convert_overwater for x in data):
    COMMIT_MESSAGE = 'Power Plant System Alert: Plant is Overwatered! Check for issue.'
    print('Power Plant System Alert: Plant is overwatered! Check for issue.')
    git_push() # calls function



