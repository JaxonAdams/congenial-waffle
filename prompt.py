# Function to ask questions and package up the data
def promptQuestions():
    # Set up empty dictionary for info
    projectInfo = {}

    # Prompt title and push info to dictionary
    projectTitle = input("Please enter your project's title: ")
    projectInfo["projectTitle"] = projectTitle

    # Prompt if description is wanted
    descriptionConfirm = input("Would you like to add a project description? y/n ").lower()
    # If yes, prompt description and push to dictionary 
    if descriptionConfirm == "y":
        print('Please enter the description below: ')
        description = input()
        projectInfo["description"] = description

    # Return the data
    return projectInfo

# Call function and store data in global variable
readmeInfo = promptQuestions()

# Template for README file
readmeTemplate = f'''
#{readmeInfo["projectTitle"]}
##{"Table of Contents" if "description" in readmeInfo or "installation" in readmeInfo or "usage" in readmeInfo or "contributions" in readmeInfo or "tests" in readmeInfo else ""}

'''

# If README not found in dist/ create one
# Write new README to the file
f = open("./dist/README.md", "w")
f.write(readmeTemplate)
f.close()