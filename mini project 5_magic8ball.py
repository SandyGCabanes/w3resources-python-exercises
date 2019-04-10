#sandygcabanes
#practicepython.org
#mini project 5 magic 8 ball
''' Create a Python project of a Magic 8 Ball which is a toy used for
fortune-telling or seeking advice.
Allow the user to input their question.
Show an in progress message.
Create 10/20 responses, and show a random response.
Allow the user to ask another question/advice or quit the game'''

import random
def magic_8_ball():
    question_asked = input('Type in your question:')
    list_a = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy, try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
    random_answer_number= random.randint(1,20)
    random_answer = list_a[random_answer_number]
    print (random_answer)
    ask_again = input('Do you want to ask another question? Y/N')
    if ask_again == 'N' or 'n':
        print ('End')
    elif ask_again == 'Y' or 'y':
        magic_8_ball()
magic_8_ball()



