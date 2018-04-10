# Technical Report for Capstone project
Raj Chakrabarty

The data used for this project was provided by the website Yummly, and is available at https://www.kaggle.com/c/whats-cooking.  

Cleaning and Natural Language Processing was done via the following process:

1. remove pluralizations - remove 's; from the end of each word, change words ending in 'oes' to end in 'o'.
2. Create a list of other words to be removed (peeled, fresh, ground, etc.) 
3. Remove non-alphabetic characters, and words referring to ingredients  ie, (20 oz.)
4. Save the 1000 most common ingredients to a csv file.
5. After inspecting the data, expand the list of words to be removed.
6. Standardize alternative spellings (anchovie/anchovy, yoghurt/yogurt)
7. Repeat the process until standardized list of one and two word ingredients emerges.

Descriptive analysis was done by calculating the prevalence of each ingredient in each cuisine, divided by the prevalence of the ingredient across all cuisines, with the cuisines being equally weighted). This was used to calculate the ‘most representative’ ingredients within each cuisine, and also the cosine similarity between cuisines.

Predictive modeling used the cuisine of each recipe as the outcome variable. As there were 20 different cuisines in the dataset, these were translated into integers between 0 and 19. The features of the model were built by count vectorizing the ingredients of each recipe using the custom stop word and vocabulary lists derived during preprocessing.

Random Forest, Logistic Regression, and KNN models were used. KNN was abandoned after the initial run due to bad performance. The other two models were grid searched to find the best parameters. The final model was Logistic Regression, which achieved 78% accuracy against the test data.

Possible future strategies:

Evaluation of different models, including Neural Network and Naive Bayes.

Application of the  same process to different datasets (such as New York Times or Epicurious recipes)

Hierarchical, K-means, and agglomerative clustering of cuisines.
 