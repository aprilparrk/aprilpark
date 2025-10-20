# 1. Git is a version control system taht tracks files and manages code. It has abilites like branching, merging, and committing changes.
# Github is sort of a hosting service for Git repositories that enables collaborations and code sharing.

# 2. Terminal is where you type commands, and the commandline is where you enter and run the commands.

# 3. Local repository is stored on your computer, while remote is stored on public.

# 4. Version control records changes to files

# 5. Staging Area is where the changes to code are stored before being committed.

# 6. git add adds the changes and prepares to be committed.

# 7. git commit saves changes to local repository.

# 8. git push uploads the changes from local to remote repository.

# 9. git status shows to state of the working directory and the staging area.

# 10. git pull takes the updates from a remote repository into the local.

# 11. pwd shows the current location in the directory.

# 12. ls lists all of the files and folders in the directory.

# 13. cd changes from current to another directory.

# 14. nano enables editing code directly on terminal.

# 15. touch creates a new file

# 16. mv moves a file to another location.

# 17. rm removes/deletes files.

# 18. cat displays files.


#3.2
# 1. pwd
# 2. ls
# 3. cd ~/python_decal/brianna_repo
# git pull
# 4. mv homework.py ~/python_decal/judy_decal/homework/
# 5. cd ~/python_decal/judy_decal/homework/
# 6. cat homework.py
# 7. git add homework.py
# git commit -m "done with homework"
# git push
# 8. I ran into this error with homework4. There are new commits to GitHub that Judy has not synced yet. The error occurs
#because Judy tried to push the "old" changes. To fix it, Judy should git pull origin main and then git push origin main again.
# 9. cd ~/Recents/


#4.1 
def checkDataType(num):
    return type(num)

def evenOrOdd(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def sumWithLoops(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def duplicateList(list):
    new = []
    for i in list:
        new.append(i)
        new.append(i)
    return new

def square(num): #Add colon when defining a function
    return num * num

print(duplicateList(['h','e','l','l','o']))