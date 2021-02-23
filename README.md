# Friends-API-creation
API creation of the series Fiends with Flask
Welcome to the Friends API!! Ever wanted to change the world´s favourite sitcom? wanted to be part of the Friends Family? well this is your way to go. For this you have three main endpoints: characters, lines and episodes. In each you find the following info:

1- http://127.0.0.1:5000/characters 

    -name, personality and job


2- http://127.0.0.1:5000/lines

    -line,  name, and episode


3- http://127.0.0.1:5000/episodes

    -episode, name 




**Note:**
-In **/characters** you´ll find a brief description  of all the characters, with **name, job and personality as obligatory params**. 

-In **/lines** you find all the scripts of episodes 2,3 and 7. The choice of this episodes has been done after analyzing a csv on the people´s ratings of every Friends episode. These three were ranked in top ten. **Line, name and episode are obliigatory params**.

-In **/episodes** you find a  list with all the characters in each episode 2,3 and 7. **Episode and name are obligatory params.**




With each endpoints you can perform the CRUD operations:

     -Create here is == Insert (in which you need to add the parameters stated above).


     -Read is the plain url of one of the three options; to get more details insert the id. 


     -Update here is == Edit in which you need to pass the id as a parameter and the changes in at least one of the mandatory parameters. 


**C(reate)**:
YES, you can finally consider yourself part of the Friends family by adding yourself as a new character of the serie. For this, you´ll need to pass your **name, personality and job as a parameter into this url**:
http://127.0.0.1:5000/characters/insert


**R(read)**:
http://127.0.0.1:5000/characters you´ll find a list with all the characters names and their id. 
**Use this id as a parameter** in order to get more details of said id in this url:
http://127.0.0.1:5000/characters/details


**U(pdate)**:
http://127.0.0.1:5000/characters/edit you need to pass the **id of the given object you want to modify, as well as pass a dictionary with at least one of the mandatory parameters as keys** *(in characters is name, personality and/or job)*, and the **new value**. 



**D(delete)**:
As well, you can also delete the existence of a character if you ever wanted a plot twist by **passing the id of said character as a parameter to the url**:
http://127.0.0.1:5000/characters/delete 


Protective programming is in place, which you can find in checking.py. Meaning that in case user has not passed mandatory parameters, she/he will be informed.  




