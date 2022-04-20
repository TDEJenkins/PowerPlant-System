


from git import Repo

PATH_OF_GIT_REPO = r'C:/Users/tayso/PowerPlant-System'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo.init(PATH_OF_GIT_REPO)
        repo.index.add('PowerPlant-System/moisture_data.csv','PowerPlant-System/moisture_plot.png')
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push(force = True)
    except:
        print('Some error occured while pushing the code')    

git_push()