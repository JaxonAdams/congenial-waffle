# Function to ask questions and package up the data
def promptQuestions():
    # Set up empty dictionary for info
    projectInfo = {}

    # Prompt user info for questions section
    userGithub = input("(required) Please enter your GitHub username: ")
    projectInfo["userGithub"] = userGithub
    userEmail = input("(required) Please enter your email address: ")
    projectInfo["userEmail"] = userEmail

    # Prompt title and push info to dictionary
    projectTitle = input("(required) Please enter your project's title: ")
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

## Table of Contents
{" - [Description](#description)" if "description" in readmeInfo else ""}
{" - [Installation](#installation)" if "installation" in readmeInfo else ""}
{" - [Usage](#usage)" if "usage" in readmeInfo else ""}
{" - [Contributions](#contributions)" if "contributions" in readmeInfo else ""}
{" - [Tests](#tests)" if "tests" in readmeInfo else ""}
 - [Questions](#questions)

{"## Description" if "description" in readmeInfo else ""}
{readmeInfo["description"] if "description" in readmeInfo else ""}



## Questions
Have any questions? You can reach me through my [github account](https://github.com/{readmeInfo["userGithub"]}) or email me at [{readmeInfo["userEmail"]}](mailto:{readmeInfo["userEmail"]}).
'''
# End template for README file

# If README not found in dist/ create one
# Write new README to the file
f = open("./dist/README.md", "w")
f.write(readmeTemplate)
f.close()

print("README written. Find it in the dist/ folder of this directory.")