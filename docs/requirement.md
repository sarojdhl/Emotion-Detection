# __Requirement Gathering__

## About the Company


| Name        | Details           | 
| ------------- |:-------------:|
| Company Name      | Sk Pscyology| 
| Location     |Lalitpur| 
| Compnay type     |Private Clinic| 
| Employees   |35| 



What does your business do?

* Recognize the possible emotional outcomes of the psychiatric patients based on a different background, physiological, and behavioral variables.

What product or service are you selling?

* Treating psychiatric patients 


What are your mission and vision?
* Recognize  the  possible  emotional  outcomes of the psychiatric patients





## Context on the product
Why do you need this new system? What is the business need?

* Recognize the possible emotional outcomes of the psychiatric patients so that manual identification is automated and we can save time.

* Clustering the people of similar emotions and psychological symptoms and treating them accordingly. 

Is there a system in place to do it right now (even if manual)? If so, how is it done right now? Is the process documented? 

__Current system__

* Manual reading of patients answers
* No measure to perform accuracy test.
* No documentation



What features don't you like about the current system?
* It's a manual process
* Depends on controllers(who classify sentiments) sentiment.

Are there other systems this system will interface with?
* No

Are there any dependencies on other project/systemin completing the project/system? Who will deliver the inputs for this system?

* No. Our controller will give input in the form of text. 

Who will receive the outputs of the feature?
* Admin/controller will receive the output of this feature.

Who else should talk to?

| Name        | Phone           | Email(@gmail.com)  |
| ------------- |:-------------:| -----:|
| Saroj Dahal      | 98*** | saroj.dahal |
| Kshitiz Regmi     | 98** | kshitiz.regmi |


Does the current system do things that this system will not do?
* No



How will we know this is complete?
* It should be more than 60% accurate.

## About the new system

__Functional Requirements__

* On making a request for a patient's mental condition, the system shall classify all the input text as sentiment in a bunch or one by one.

* If clicked  find emotional outcomes, the UI shall return sentiment of every answer as input.

* The admin/controller who uses the system shall have a login id and password.

* The user interface shall run on windows and Linux pc.




__Nonfunctional requirement__

* The system should be easy to use  and should be
organized in such a way that user error is minimized.

* Controllers shall be able to use all the system functions after a total of
three hours' training. After this training, the average number of errors made by
The controller shall not exceed two per day.

* TIme to restart after failure shall be less than 1 minute.

* The analysis shall take less than 1 minute to give bar chart if sentiments.



## System usage

* The system shall use MongoDB if required
* The system shall use less than 1 GB of memory.
* Admin/controller only uses the system.
* Application shall be web-based



## **About the Data**

What data do you have that might be related, in any way, to the problem being
solved? Also, describe data.     
  * The data that will be used is ISEAR data. The data contains 7446 sentences, with seven categories of emotions: anger, disgust, fear, joy, sadness, shame, and disgust. 





## **Caveats**

What are the constraints on the system being built (resourcing, timing, etc.)?


  * The constraint on the system being built is the problem of few data. Also, the timing is an issue; the product has to be built within a small period of time.


What is the strategy for your organization?[One year, five years]. Are there considerations that need to be taken into account?      
  * The strategy is to use the system for some period and improve it as we learn and get more data. So, the system has to be opened for further enhancement.



## **General**

Do you have a timeline in mind?        
  * Yes, the product should be ready to be used within two weeks. 


