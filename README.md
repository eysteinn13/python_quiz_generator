The Quiz Generator!
===================

The Quiz Generator is a web-page that allows a user to generate questions from a few categories. The user can decide how many categories he picks and how many questions he want's to generate.
After the user has picked the categories and the number of questions he will be presented a list of questions. The user can than decide to make a pdf-file from the questions, answer the questions and see his results or generate new random questions if he is unhappy with the current questions.


To run the Quiz Generator you must be in the source folder of the project, have Django installed on your computer, install the PyPi package ReportLab and type:
python3 manage.py runserver

You can then open a browser and go to http://localhost:8000/home/ 

All the questions are from this API: http://jservice.io/
