from git import Repo
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