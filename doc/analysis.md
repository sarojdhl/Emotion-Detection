# __Problem Formulation__

|   Topic      | Prompt        | Answer |
| ------------- |:-------------:| -----:|
| Task        |WE want a model that can|Correctly classify emotional outcomes of the psychiatric patients.|
|Experience     |Using| User emotion dataset(ISEAR) |
| Performace        |As Measured by| Accuracy, F1 Score |
| Reason To solve        |The output will be used to | Cluster and treat patients at once|
| Sucess Criteria       |Sucess if |  accuracy  > 60%|
| Other     |Other Metrics |  Precision and recall|






## **Solution Formulation**

Manually, the problem could be solved as:
  * manually check the text answer for the emotion using human being.

It can be formulated as a ML Problem as:
  * classification of emotions of answer text
  * clustering of answer or response text

A similar ML task is:
  * Any classification task and natural language processing task that processes text

Our assumptions are
 * Emotional category of answer text gives us clue to psychological condition

A baseline approach could be:
  * Treating as classification task
  * Natural language processing by vectorizing sentences by word count
