# AutoDoc

Why write it twice?

AutoDoc is a python script used to create documentation(word documentation docx) from source code.

Mainly it will focus on Python scripts as a test.

The program only creates a skeleton of the documentation.Document formatting is default and the user will be able to add the parts necessary to format the document as he/she likes.

## Requirements
* Python 3
* docx - word library for python

## Features will include.
* *Reading source code* and filtering the code from the comments necessary to documentation
* *Creating a short brief documentation* (word document and markdown)
* *Creating logs for documented projects*

## Run
### Creating a new document from source

>python autoDoc.py document 'documentation_type' 'target_directory' 'project_name'

### *documentation_type*
Can either be *markdown* or *word*
### *target_directory*
Directory to the source code *root* folder
### *project_name*
Name of the project.

### Checking logs
>python autoDoc.py log 'project_name'

### *project_name*
View the logs of a certain prevously documented project
