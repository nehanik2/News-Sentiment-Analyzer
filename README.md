# News-Sentiment-Analyzer

Data Science Project Topic – Predicting People’s Mood Based On Current Events
ReadMe File - 

This project is a modification of sentiment analysis, where the goal is to identify or predict the possible mood of a person or an individual when reading or viewing a particular event either in social media platforms and news channels.
Aim – The aim of the project is to provide better insight into the moods the people will feel when reading a particular article or news either on real-time broadcast or social media.
Scope - The project aims to collect data from over 150,000+ sources including international BBC, CNN, US national New York Times, Washington Post, Business Bloomberg and Wall Street Journal, Tech Techcrunch, Wired, Entertainment and sports. Thwe categories we are collecting in thsi project include politics, economy, health, technology, sports, entertainment, climate, crime and education. It is going to be covering only news in English language, the geographical content will be centered around US, UK, Cnanada and Australia. 

Possible Outcomes We Plan To Achieve –
1)	For the model to have the ability to affectively parse through the pre-existing textual articles and blogposts and predict a general mood of the content.
2)	To detect negative mood based on keywords and hate speech
3)	To monitor public sentiment regarding sensitive news materials
4)	To visualize trends in people’s moods and compare between different types of news
5)	To deduce or predict which type of news affects people’s moods the most.

Possible Applications Of The Project–
1)	This analysis will provide a better insight for marketing companies, and news channels to make the articles or news more engaging, to frame the news or piece of information more clearly and concisely to attract maximum target audience.
2)	The project can assist policy makers in creating stringent policies when it comes to circulating news related to sensitive matter or geopolitical content.

1) DATA COLLECTION 
Data for this project is collected and extracted from a public API NewsAPI from "https://newsapi.org/". The news data collector is getting or retrieiving articles from the API, for various cateogires. 
Total number of articles for each cateogry: 100 
Total number of categories: Politics, Economy, Health, Technology, Sports, Entertainment, Climate, Crime, Education 

The data collector automatically saves the data from 100 articles for each cateogry and saves it in raw_news_data.csv file. This data file includes all the raw data stored directly from the API.

Data summary is provided which shows the following: Articles per topic, Sample articles, title, topic, source. 

2) EXPLORATORY DATA ANALYSIS 


Once raw data is given and extracted, certain data exploration steps are carried out to understand the nature of the data. 
The dataset is properly loaded and the following is found by uisng the functions:
1) The information of the dataset
2) The description of the dataset
3) The number of rows and columns of the dataset - 900 rows and 9 columns
4) Shape of the dataset - (900,9)
5) Size of the dataset - 8100
6) Getting the number of features and list of features - 9 , ['title', 'description', 'content', 'full_text', 'url', 'source', 'published_at', 'topic', 'collected_at']
7) Datatypes in the dataset - title, object 

2.1) DATA VISUALIZATION AND TEXT LENGTH ANALYSIS 
Bar graph is created to display then number of columns and number of articles. X-axis contains topic, y-axis contains number of articles

Bar plots and histograms are created to understand the word count in each article and distribution of article length. 
Average article length - 437 characters 
Average word counts - 70 words 

2.2) SOURCE ANALYSIS 
Rouce analysis was done to identify the 15 top sources which were present in the data. A bar chart shows the number of articles per source. x - number of articles, y - source. This shows BBC news the first top source followed by The Verge and Gizmodo.com 

2.3) INTIIAL SENTIMENT ANALYSIS
Initial sentiment analysis is done using Vader. 
Initial sentiment distribution was given by creating a histogram.The histogram was divided by using compound sentiment score.

Compound sentiment score was chosen as the following: 
Positive articles  -score would be greater than or equal to 0.3 
Negative articles - score would be less than or equal to -0.3
Nutral articles - score will be greater than -0.3 and less than 0.3 

Positive articles - 430
Negative articles - 288
Neutral articles - 182

2.4) SENTIMENT DISTRIBUTION BY TOPIC 
This was done to identify which topic created which types of sentiment and how it influenced it. 
Sentiment is shown by topic by creating a histogram
x label - topic, y label - sentiment score 
Average sentiment by topic is:
crime           -0.510420
climate          0.020289
health           0.072735
education        0.101222
politics         0.103850
economy          0.166910
technology       0.271467
sports           0.319782
entertainment    0.360789

2.5) WORDCLOUD 
Wordclouds were used as another form of data visualizatiosn to check the frequency of each word.


2.6) TEMPORAL ANALYSIS 
Temporal analysis shows the number of articles for each cateogry produced over time 
x axis - date, y axis - Number of articles 

The graph shows peak number of articles realeased was for 5th november, 2025, and least was from 29th november to 1st decemnber. 

2.7) CHECKING MISSING VALUES 
Missing values for each feature is checked before data is pre-processed 
Missing count and percentage is given and bar chart is given 
Feautre description had the highest missing percentage of 0.55
Feature content has least missing percentage of 0.11 

2.8) EDA SUMMARY
EDA summary is given which gives the folllowing 

total_articles: 900
total_topics: 9
total_sources: 108
avg_text_length: 437.4611111111111
avg_word_count: 70.37666666666667
date_range: 2025-11-05 to 2025-12-04
positive_articles: 430
negative_articles: 288
neutral_articles: 182

This summary is then saved as a json file named eda_summary.json. 


3) DATA CLEANING 
Data cleaning was done in the following steps 
Identifying the missing values 
Cleaning the missing values
Checking the duplicate values or redundancy 

A class texprocessor was created which performed the following operations on the textual data 
a) Identifying and eliminating the stopwords and keeping the self.keep_words =  'not', 'no', 'never', 'neither', 'nobody', 'nothing','very', 'too', 'most', 'more', 'less', 'few', 'much','many', 'really', 'quite', 'rather', 'fairly'

b) The text was cleaned by following the steps:
Converting text to string 
Converting all the text to lowercase 
Removing the URL
Removing the tags 
Removing email addresses
Removing special characters
Removing whitespace

Tokenization and lemmatization was carried out 
If you had to remove stopwords, it would then create new tokens with it, if it had to lemmatize, then lemmatization method would be called.

c) Fixing missing values 
Missing values were fixed for the following attributes as they had the highest percentage of the same namely 'content', 'description' and 'title'. 
After removing the missing values new shape of the dataset is (843, 10)

d) Duplicacy is calculated

Duplicates based on URL: 0
Duplicates based on title: 5
Duplicacy percentage based on URL: 0.0%
Duplicacy percentage based on title: 0.5931198102016607%

After removing duplicates: 843 articles

e) Tokenization is applied
Token statistics:
count    843.000000
mean      73.169632
std       11.828382
min       31.000000
25%       64.000000
50%       72.000000
75%       81.000000
max      111.000000

The threshold of tokens is 50 

f) Cleaned data visualization
Once the data is completely cleaned, the visualziatons were created to compare and show the following

i) original text legth
ii) cleaned text length
iii) token count distribution
iv) before and after comparison 

Histograms were create for the following 

g) Saving the cleaned data 
The cleaned data summary is given 

Original articles: 834
Average tokens per article: 73
Min tokens: 50
Max tokens: 111
Articles by topic:
topic
politics         99
sports           98
health           95
economy          94
technology       93
crime            93
climate          91
entertainment    88
education        83

This data was then saved as 'cleaned_news_data.csv'

4) FEATURE ENGINEERING 
For discussing which features contribute the most and for selecting the most appropriate features the following approaches were used. 

Emotion lexicons
toxicity classification
Sentiment lexicon features were given and included positive_word_count, negative_word_count, positive_ratio, negative_ratio, sentiment_balance

Vader was used for initial sentiment analysis

TF-IDF was used and all dominant features were merged

Visualizations used to understand the correlation between different features was:
a) Wordclouds 
b) Correlation heatmap 
c) Sentiment vs emotion heatmap
d) Dominant emotion distribution
e) Emotion radar chart

5) MODEL SELECTION AND TRAINING 
The models used for the project include Logistic regression, and Random forests 
Logistic regression is used because:
Reasons: 
a) Handles mixed features
b) Works well with negative values
c) Good for text classification
d) Handles multiple classes. 

Random forests is used because:
Reasons:
a)It handles all types of features
b)No feature scaling is required
c)Captures non linear relationship
d)Robust to outliers 

Naive bayes is used:
Reason: Because it handles test classification well 

Sentiment distribution per topic, Emotion probability distribution per topic and Dominant mood per topic is done.

sentiment_pred  Negative  Neutral  Positive
topic                                      
climate             42.9      9.5      47.6
crime               80.0      0.0      20.0
economy             45.5      0.0      54.5
education           46.7      6.7      46.7
entertainment       26.7     13.3      60.0
health              34.8      4.3      60.9
politics            42.9      7.1      50.0
sports              16.0      8.0      76.0
technology           8.3     33.3      58.3

Confusuon matrix, and box plot visualizations have been done to check sentiment composition by topic. 

Bar chart showing overall emotion distribution shows that neutral emotion is highest and disgust emotion is lowest.

To identify which cateogires of news correspond to which maximum emoiton, bar chart for each individual emotion is created. 

Crime - Highest anger component 
Technology - Highest anticipation component
All cateogries - zero disgust
Economy - highest fear component 
Politics - highest joy component
Entertainment - highest neutral component 
Crime - highest sadness component 
Crime - highest surprise component 
Economy - highest trust component 

Training, testing and splitting: Trainign data is given 80% and testing data is given 20%

Cross validation is used, 5 folds are taken on training dataset 

6) MODEL EVALUATION 
The evaluation metrices used is confusuion matrix, accuracy score, F1 score
Macro F1 score is chosen 
F1 score is preferred because of its ability to handle imbalanced dataset

Naive bayes accuracy - 70%
Logistic regression accuracy - 91.2%
Random forest accuracy - 97.01%
Ensemble accuracy - 97.01%

Visualziations used is confusion matrix and probability confidence distribution

POTENTIAL CHALLENGES AND ISSUES WE FACED
1) Scale of the data, downscaling the data was an issue, since the data was huge.
2) Selecting appropriate text features for predicting the mood and checking which ones highly affect it was challenging. 
3) Selecting appropriate models checkign that it it adaptable to both numerical and text features was important


Team Members Information - 
1)	Name – Neha Nikam, BU ID – U88786364
2)	Name – Shrishty Gupta, BU ID – U41123810
3)	Name – Visista Jayanti, BU ID – U59259052


