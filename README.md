# News-Sentiment-Analyzer

Data Science Project Topic – Predicting People’s Mood Based On Current Events
ReadMe File - 

Youtube Video : https://youtu.be/PIPiPAXLnJI

Data Science Project: News Sentiment Analyzer
1. Data Source
The dataset is composed of news headlines collected from the New York Times Archive API (publicly available REST service) of the period from Jan 2024 to June 2024.
API : https://api.nytimes.com/svc/archive/v1/2020/3.json?api-key=#####
2. Nature of the Data
The data is pre-existing (secondary data), downloaded directly from an online API. 
No synthetic or generated samples are included.
3. Aim of the Data
This dataset is used to build and demonstrate an automated classifier that predicts the mood of the reader of a news article based on its headline text.
4. Number of Rows and Columns
Rows: 23,887 (each representing a single news article headline)
Columns: 20 (headline, abstract, web_url, keywords, section, pub_date, label)
5. Shape of the Data
Tabular, shape: (23,887, 20)
6. Values in Data
Contains both textual (headline, abstract, keywords, section) and numerical values (binary/multi-class target label, word count).


7. Features and Attributes

Attribute Name
Description
Data Type (based on 2nd row)
headline
Text string of the article headline
dict (contains multiple headline fields such as main, print_headline, seo, etc.)
abstract
Short summary of the article content
str
web_url
Link to the news article
str
snippet
Short extract or snippet of the article
str
lead_paragraph
Opening paragraph of the article
str
print_section
Section identifier for print edition (e.g., "A", "B")
str
print_page
Page number where the article appears in print
int or str
source
News source (e.g., “The New York Times”)
str
multimedia
List of dictionaries describing media assets (images, videos)
list
keywords
List of key topics identified by NYT editors
list
pub_date
Publication date in ISO format
str (datetime)
document_type
Type of article document (e.g., “article”, “brief”)
str
news_desk
Editorial desk that produced the story
str
section_name
Main section category (e.g., “Business”, “World”)
str
subsection_name
Subcategory within the section
str
byline
Dictionary containing author information
dict
type_of_material
Type of content (e.g., “News”, “Editorial”, “Review”)
str
_id
Unique article identifier
str
word_count
Number of words in the article
int
uri
Permanent NYT URI reference for the article
str










7. DATA EXPLORATION
This include identifying number of rows and columns
Identifying the shape of data
Identifying the size of the data

    DATA PREPROCESSING 
This includes finding the missing values 
Finding the redundant values 
Replacing missing values with suitable methods 

Finding Missing values 
      Total 8 features had major missing values 
      After calculating the percentage of missing values for each feature, whichever feature had missing value greater than 50% was eliminated.
Subsection_name feature was eliminated

Replacing missing values 
     Since our data included both text, numerical and categorical data, different methods were used to replace the missing values.
For text data - the missing values were filled with “unknown”
For numerical data - median approach was used to fill the missing values 


Finding redundancy 
     df.duplicated() method was used to find duplicacy or redundancy in data, the duplicacy was zero. 

10. STEP 3 - FEATURE SELECTION AND DATA VISUALIZATION
The data included numerical, text and categorical data, hence to find the relation between different features, three methods were used. 

10. Visualization of the Data
Initial exploratory data analysis (EDA) includes:
Heatmaps showing feature correlations
Sample confusion matrix for classifier predictions


Text data- TF-IDF was used to vectorize the text data and cosine similarity was used, threshold was 0.6, after which the features with similarity greater than threshold were selected. The correlation coefficient was created with two features (print_page, word_count)

Numerical data - Pearson correlation coefficient was calculated 

Categorical data - Categorical data was converted to numerical data and the correlation coefficient and heatmap was generated. 


8. Outcome of the Data
Output variable (label) binary. Common examples are:
0 = 'Positive'
1 = 'Negative'

11. Demo Classification using Random Forests
The project demonstrates news category prediction by:
Converting headlines to bigram-based numerical features using Bag-of-Words/CountVectorizer.
Training a RandomForestClassifier with n_estimators=200 and criterion='entropy'.
Reporting validation accuracy and misclassification rate.
12. Data Science Project Lifecycle




This project is a modification of sentiment analysis, where the goal is to identify or predict the possible mood of a person or an individual when reading or viewing a particular event either in social media platforms and news channels.
Aim – The aim of the project is to provide better insight into the moods the people will feel when reading a particular article or news either on real-time broadcast or social media.
Scope – Since the scope and variety of real-time news and content on social media is vast, this project aims to tailor down to the most crucial types of news such as geopolitical news relating to US (United States) and EU (European Union) and entertainment news related to Western music and Hollywood.
Language Of Content – Since, this project focuses on sentiment analysis and uses NLP tools, for ease of training the model, we are limiting all the textual content to English language. This textual content will include data from news articles, blogs, and public comments from social media platform Twitter.

Possible Outcomes We Plan To Achieve –
1)	For the model to have the ability to affectively parse through the pre-existing textual articles and blogposts and predict a general mood of the content.
2)	To detect negative mood based on keywords and hate speech
3)	To monitor public sentiment regarding sensitive news materials
4)	To visualize trends in people’s moods and compare between different types of news namely geopolitical news and entertainment news.
5)	To deduce or predict which type of news affects people’s moods the most.

Possible Applications Of The Project–
1)	This analysis will provide a better insight for marketing companies, and news channels to make the articles or news more engaging, to frame the news or piece of information more clearly and concisely to attract maximum target audience.
2)	The project can assist policy makers in creating stringent policies when it comes to circulating news related to sensitive matter or geopolitical content.

Data Collection For The Project –
We aim to collect data for the project in two phases, one having primary data including surveys and questionnaires targeting public and young adults and recording their sentiments on past events or most relevant information. We are going to collect data from individuals of age group 20-30, and will have a sample size of approximately 200 to 300 individuals. The secondary data will refer to data being collected from two distinct news channels namely “New York Times” and “CNN” and one social media platform “Twitter” by using their open-source API and this data will be used to train the model or different parameters to predict the mood and will use extensive NLP techniques to increase efficiency of the model. The testing data for this model will comprise of an unknown news channel “ABC News” and one unused social media or blog platform such as “Reddit” only.

Team Members Information - 
1)	Name – Neha Nikam, BU ID – U88786364
2)	Name – Shrishty Gupta, BU ID – U41123810
3)	Name – Visista Jayanti, BU ID – U59259052





