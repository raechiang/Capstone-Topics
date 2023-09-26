Multilabel Text Classification of Research Articles
==============================

This is my second independent capstone project for Springboard.

## Introduction

Historically and in modern studies, people have observed that we have a growth rate of 3-4% in the number of article publications per year, with the total doubling every 15-17 years [^1][^2]. It does not appear to be slowing down, though interestingly, major economic crises and wars can pause or slow our growth for a time, shown in Figure 1. However, we tend to bounce back, and on the other hand, we can enter phases of faster growth following groundbreaking technological advancements, as seen in the 1809 to 1882 section, which is when the Industrial Revolution took place.

<p align="center">
  Scientific article growth (log publications vs year)
</p>
<p align="center">
  <img src="/reports/figures/numpubsperyear.png" alt="Plot of segmented unrestricted growth of scientific articles from four bibliographic databases (Bornmann, Haunschild, Mutz, 2021).">
</p>
<p align="center">
  <b>Figure 1</b>. Plot of segmented unrestricted growth of scientific articles from four bibliographic databases (Bornmann, Haunschild, Mutz, 2021).
</p>

Digitization and the Internet also have had an undeniable impact on increasing our ability to produce and share more articles. Surveys have shown that researchers value accessibility and many are enthusiastic about giving back, as models and concepts like Open Access, crowdsourcing, and expedited versions of the publishing systems grow in popularity [^3][^4][^5]. In theory, all of these should open the door for people without a lot of resources for subscriptions to access new information faster, and they in turn can contribute their work as well, and indeed, the number of articles in slightly less affluent areas has been increasing over time, as seen in Figure 2 [^6]. (There are other caveats and crises that the scholarly publishing communities are facing, but politics and economics are beyond the scope of this project.)

<p align="center">
  Science and engineering articles published (count vs year)
</p>
<p align="center">
  <img src="/reports/figures/numpubsperyear_byecon.png" alt="Plot of Science and engineering articles published per year by economic group in 1996-2020 (National Science Board, 2021).">
</p>
<p align="center">
  <b>Figure 2</b>. Plot of science and engineering articles published per year by economic group in 1996-2020 (National Science Board, 2021).
</p>

Thus, we have a problem: there are a lot of articles, and it may not be very realistic or reliable for people to manually tag or verify each article, and not all of them are categorized in the first place. Furthermore, new subjects and topics develop over time as we learn and discover more, so articles may even benefit from being categorized over and again. Researchers like the availability, and they want transparent, sophisticated search engines to assist in their research. This project aims to automatically categorize articles with at least 70-80% accuracy based off of an article's title and abstract. This alone is not sufficient for a search engine because researchers would want more granularity in their subject matter, but it may help in the organization and hierarchies of the articles.

[^1]: Bornmann, L., Haunschild, R., & Mutz, R., "Growth rates of modern science: a latent piecewise growth curve approach to model publication numbers from established and new literature databases". *Humanit Soc Sci Commun* 8, 224 (2021). [https://doi.org/10.1057/s41599-021-00903-w](https://doi.org/10.1057/s41599-021-00903-w).
[^2]: Amnet, "Scholarly Publishing: Challenges, Opportunities, and Trends". *Amnet* (2022). [https://amnet-systems.com/scholarly-publishing-challenges-opportunities-and-trends/](https://amnet-systems.com/scholarly-publishing-challenges-opportunities-and-trends/).
[^3]: Sandusky, R., Tenopir, C., & Casado, M., "Figure and table retrieval from scholarly journal articles: User needs for teaching and research". *Asis&t* 44: 1-33 (2008). [https://doi.org/10.1002/meet.1450440390](https://doi.org/10.1002/meet.1450440390)).
[^4]: ScienceEditor, "The Future of Academic Publishing: Emerging Trends You Should Know". *ServiceScape* (2021). [https://www.servicescape.com/blog/the-future-of-academic-publishing-emerging-trends-you-should-know](https://www.servicescape.com/blog/the-future-of-academic-publishing-emerging-trends-you-should-know).
[^5]: Singh, S., "2022 in review: Key developments shaping scholarly publishing". *Editage insights* (2023). [https://www.editage.com/insights/2022-in-review-key-developments-shaping-scholarly-publishing](https://www.editage.com/insights/2022-in-review-key-developments-shaping-scholarly-publishing).
[^6]: White, K., "Publication Output by Country, Region, or Economy and Scientific Field". *Science and Engineering Indicators*, National Science Board, National Science Foundation (2021). [https://ncses.nsf.gov/pubs/nsb20214/publication-output-by-country-region-or-economy-and-scientific-field](https://ncses.nsf.gov/pubs/nsb20214/publication-output-by-country-region-or-economy-and-scientific-field).


### The Dataset

The dataset contained 20,972 articles, labeled with one to three of the six categories: Computer Science, Physics, Mathematics, Statistics, Quantitative Biology, and Quantitative Finance. It was found on Kaggle, and it was scraped by Analytics Vidhya, which is a community of data professionals ([link](https://www.kaggle.com/datasets/blessondensil294/topic-modeling-for-research-articles)). The 20,972 articles were part of the "train.csv" file, which originally had nine columns: the unique ID, the title, the abstract, and the six topic columns. The topic columns were populated by a 1 or 0 to indicate if the article belongs to or does not belong to the corresponding category. There was also a "test.csv" file, containing 8989 articles, which contained the same first three columns as the "train.csv" file, but these articles were unlabeled.

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## Data Wrangling and Exploratory Data Analysis

[Notebook link](notebooks/1.1-rc-data-wrangling-eda.ipynb).

### Data wrangling

At this step, I verified the data and sought to establish a broad understanding of the data. There were no missing values and almost no problems in the overall statistics of the values, and the inputs that would be expected to be unique were unique. There was one suspicious sample, which contained only five words total between its title and abstract, so it was dropped. The titles and abstracts were concatenated with one another, and some light text cleaning and preprocessing were conducted. Using gensim and NLTK, the texts were converted to lowercase tokens, the stop words were removed, and the resulting pruned lists of words were lemmatized. The process took about 15-20 minutes over both input files.

### Exploratory Data Analysis

First, the distributions of the labels and words were examined. The dataset was imbalanced, with Quantitative Biology and Quantitative Finance having very few samples, and Statistics also had relatively few samples compared to the remaining three. Computer Science was the biggest class.

<p align="center">
  <img src="/reports/figures/1-1_num-articles-per-topic.png" alt="Bar chart of the number of articles per topic.">
</p>

<details>
  <summary>Articles per topic.</summary>

| Topic | Count | % |
| --- | --- | --- |
| Computer Science | 8594 | 40.9% |
| Physics | 6013 | 28.7% |
| Mathematics | 5618 | 26.7% |
| Statistics | 5206 | 24.8% |
| Quantitative Biology | 587 | 2.8% |
| Quantitative Finance | 249 | 1.2% |

</details>

There was a total of 26,267 labels, so there were 5295 more labels than there were articles. Most of the articles were tagged with only one topic.

<p align="center">
  <img src="/reports/figures/1-1_num-topics.png" alt="Bar chart of the number of articles tagged with exactly 1, 2, or 3 topics.">
</p>

<details>
  <summary>Number of articles with exactly 1, 2, or 3 topics.</summary>

| Num Topics | Count | % |
| --- | --- | --- |
| 1 | 15928 | 76% |
| 2 | 4793 | 23% |
| 3 | 251 | 1% |

</details>

Overall, there was an average of 166 total words per sample with their titles and abstracts combined, and the minimum length was 12 and the maximum was 467. There were slight differences in the distributions of quantity of words per topic, with Mathematics generally falling in the lowest range and Quantitative Biology having the highest range. The rest of the topics intuitively arranged themselves between these two, with topics that would be more similar to Mathematics having lower distributions and topics that would be more similar to Biology having higher distributions.

<p align="center">
  <img src="/reports/figures/1-1_distrib-words-per-article.png" alt="Histogram of the number of words per article.">
  <img src="/reports/figures/1-1_boxplots-words-per-topic.png" alt="Box plot of number of words in a sample for each topic.">
</p>

Then, I looked at the most common tokens in both "train.csv" and "test.csv". The "train.csv" had the top ten most common tokens as model, data, method, network, system, result, problem, based, time, and show, and "test.csv" had a similar top ten results. All of the tokens seem to relate to science. When examining the top tokens per topic, the same words appeared a lot, so when constructing word clouds, I filtered the 30 most common global words so that the top 200 words per category might be more expressive of their topic.

<p align="center">
  <img src="/reports/figures/1-1_filtered-wc-0-cs.png" alt="Word cloud of 200 words without 30 most common global words for Computer Science.">
  <img src="/reports/figures/1-1_filtered-wc-1-ph.png" alt="Word cloud of 200 words without 30 most common global words for Physics.">
  <img src="/reports/figures/1-1_filtered-wc-2-ma.png" alt="Word cloud of 200 words without 30 most common global words for Mathematics.">
  <img src="/reports/figures/1-1_filtered-wc-3-st.png" alt="Word cloud of 200 words without 30 most common global words for Statistics.">
  <img src="/reports/figures/1-1_filtered-wc-4-qb.png" alt="Word cloud of 200 words without 30 most common global words for Quantitative Biology.">
  <img src="/reports/figures/1-1_filtered-wc-5-qf.png" alt="Word cloud of 200 words without 30 most common global words for Quantitative Finance.">
</p>

## Preprocessing and Modeling

[Notebook link](notebooks/2.0-rc-preprocessing-modeling.ipynb).

This step can be divided into two broad problems: one dealing with single-label categorization and one dealing with multilabel categorization. The former was done with scikit-learn, using TF-IDF vectorizers and Naive Bayes classifiers on four and six categories, and the latter was done using spaCY pipelines on four categories.

### Single-Label categorization

The first six classifiers used a TF-IDF vectorizer that conducted some basic text preprocessing, such as stripping accents, lowercasing before tokenizing, and removing scikit-learn’s default English stop words. The minimum document frequency was two, and both unigrams and bigrams were accepted. Prediction labels were encoded to numbers 0 to 5, and the articles that were marked with multiple categories were dropped, so the resulting dataset contained 15,927 articles (76% of the original). This set was then split into 80% and 20% training and testing sets.

Two Naive Bayes classifiers were used out-of-the-box to get an idea of how the models would perform, MultinomialNB and ComplementNB. The latter performed slightly better, but overall, the class imbalance was clearly problematic for both of these. The confusion matrices showed that little to no articles were predicted to belong to Statistics, Quantitative Biology, and Quantitative Finance. The feature spaces for these were very large, exceeding 130,000, so SelectKBest reduced the number of features to 20000, which turned out to work well across all four classifiers.

The two strongly underrepresented classes, Quantitative Biology and Quantitative Finance, were dropped for the next part of this single-label categorization phase. Combined, these two categories only accounted for 651 articles in the single-label subset, so the remaining dataset contained 15,276 articles. The first six classifiers used the same TF-IDF vectorizer, but the final two used a slightly different one, which was selected using RandomizedSearchCV. The document frequency parameters were the only differences, with `max_df=0.2` and `min_df=5`, whereas the first version used a `max_df=1.0` and `min_df=2`.

Overall, the ComplementNB classifiers tended to perform better, and filtering K-best features improved each of the models. Dropping the two underrepresented labels improved the models' recall slightly across the remaining labels, and it improved precisions slightly for the three majority labels (Computer Science, Physics, and Mathematics). Every model predicted Statistics poorly, with each ComplementNB variation having precision and recall floating around 0.85 and 0.37 for Statistics. Below is a table of these Naive Bayes classifiers' balanced accuracy and macro F1, which were chosen due to the class imbalance.

| Model | Num Classes | K-best? | Balanced Accuracy | Macro F1 |
| --- | --- | --- | --- | --- |
| MultinomialNB | 6 | No | 0.4576 | 0.4318 |
| ComplementNB | 6 | No | 0.5546 | 0.5778 |
| MultinomialNB | 6 | Yes | 0.4689 | 0.4522 |
| ComplementNB | 6 | Yes | 0.6427 | 0.6789 |
| MultinomialNB | 4 | No | 0.6928 | 0.6687 |
| ComplementNB | 4 | No | 0.7585 | 0.7715 |
| MultinomialNB | 4 | Yes | 0.7450 | 0.7531 |
| ComplementNB | 4 | Yes | 0.7914 | 0.8082 |

<details>
  <summary>Balanced Accuracy and Macro F1 table as bar graphs</summary>
  <p align="center">
    <img src="/reports/figures/2-0-nb_bacc.png" alt="Bar graph for balanced accuracies of Multinomial and Complement Naive Bayes classifiers for the single-label categorization problem.">
    <img src="/reports/figures/2-0-nb_f1.png" alt="Bar graph for macro F1 of Multinomial and Complement Naive Bayes classifiers for the single-label categorization problem.">
  </p>
</details>

The classifier that performed the best from this set was the ComplementNB on four classes using SelectKBest, and it used the second version of the TF-IDF vectorizer, with the two document frequencies `max_df=0.2` and `min_df=5`. Its confusion matrix illustrates that it is pretty good at predicting the three bigger classes, but bad at predicting Statistics. The precision for all four of the classes exceeds 0.80, and the recall is 0.91 or higher for the three majority classes, but for statistics, it is only 0.39.

<p align="center">
  <img src="/reports/figures/2-0-cmatrix_ComplementNB_1_4ck.png" alt="Confusion matrix for Complement Naive Bayes classifier with Select K-Best.">
</p>

### Multilabel Categorization

The multilabel dataset allows for articles that are tagged with 1-3 categories. This subset of the original 20,971 articles comprised of 20,316 articles because 655 (3%) of the articles were labeled with only Quantitative Biology, only Quantitative Finance, or exactly both of these, and thus dropped.

Preprocessing the text involved the typical steps, for which spaCY's NLP "en_cor_web_sm" pipeline was used along with a bit of regular expressions to help with cleaning. For compatibility with spaCY's multilabel text categorizer, the dataset had to be split into three parts: a training set (75%), a dev set (15%), and a test set (10%), and converted into serialized forms accepted by the categorizer.

Three models were created: a unigram bag-of-words model, a bigram bag-of-words model, and a convolutional neural network model. Their results were similar, but the CNN model was the slowest to train, and the unigram model was the fastest to train, and the unigram model performed generally better than the bigram model. The table below displays the three spaCY models' evaluations with a scorer threshold of 0.5 and no rules on the number of categories to return. Slight variations to the parameters of the unigram model were tested, but they did not yield different enough results or valuable enough improvements. The only model that attained better scores had a slower learning rate, causing the time to train to increase, but because the improvement was very small, the change was deemed not worth the extra time.

<p align="center">
  <img src="/reports/figures/2-0-spacy_models_prf_s0.5.png" alt="Three spaCY models' precision, recall, and f1-score for each of the four categories, using a scorer threshold of 0.5.">
</p>

When the models predict, they return scores for each category. To be considered as part of a category, its corresponding score has to exceed a specific threshold value. Adjusting this threshold improved the unigram bag-of-words model in terms of recall, and mostly it impacted the Statistics predictions. A threshold of 0.45 to 0.50 would attain a decent range of 0.74 to 0.93 precision and recall across every subject. The exact threshold to use would depend on the application, with a more lenient (lower) threshold value increasing the recall at the cost of precision and with a less lenient (higher) threshold value increasing the precision at the cost of recall. Thus, this is also a balancing act because heavily favoring one over the other would likely not be desired in any application of this article categorization problem. Even though an empty search result or recommendation section could be undesirable, returning too many incorrect articles could reduce users' trust in the system.

One issue that this simple of a scorer ran into is that some articles were too uncertain to pass as any category, given any reasonable threshold value--for example, if the scores were all under 0.30, then any reasonable threshold value would probably return no category (or a prediction of 0000). However, every article should have at least one category. Thus, the scorer was given an extra step: if no category exceeded the threshold value, then the highest scored category would be returned true. Doing this also increased the recall of the model, but the precision was slightly lower.

The classification report below is for the unigram bag-of-words model, using a threshold of 0.45, and requiring at least the one highest label to be returned.

| | Precision | Recall | F1-score |
| --- | --- | --- | --- |
| *Computer Science* | 0.85 | 0.90 | 0.87 |
| *Physics* | 0.91 | 0.85 | 0.88 |
| *Mathematics* | 0.84 | 0.84 | 0.84 |
| *Statistics* | 0.74 | 0.83 | 0.78 |
| | | | |
| *Micro Avg* | 0.84 | 0.86 | 0.85 |
| *Macro Avg* | 0.84 | 0.85 | 0.84 |
| *Weighted Avg* | 0.84 | 0.86 | 0.85 |
| *Samples Avg* | 0.88 | 0.89 | 0.86 |

Every spaCY model performed weakest in predicting Statistics, but it is still a big improvement over the Naive Bayes classifiers. A precision and recall of 0.74 and 0.83 are not too bad, given the class imbalance. Below is the confusion matrix for the same unigram bag-of-words model. The model tended to be the most successful with articles that should have only one label. It tended to label more articles as Computer Science than was true, which can be seen in the darker squares along the predicted Computer Science columns not lying along the diagonal, but this might be expected because Computer Science had the highest representation in the dataset. In particular, Statistics and Physics had some fuzziness with Computer Science. Glancing over some problem cases revealed that some of the excessive labeling of Computer Science articles may also be because terms relating to software, technology, and computers tend to show up in all kinds of articles. I speculate that the tools and approaches may have been mentioned in the abstract; advanced computing technology is likely instrumental in furthering our research. Also, for Statistics, recall that the word clouds from the exploratory data analysis section revealed that Computer Science and Statistics seemed to have a lot of overlapping words.

<p align="center">
  <img src="/reports/figures/2-0-cmatrix_ubow.png" alt="Confusion matrix for fourteen label combinations for the unigram bag-of-words model using a scorer threshold of 0.45 and requiring at least one category returned as true.">
</p>

Using 100 of the samples from the test set, we can examine some of the tokens that the model found important on average per category with mean SHAP values. The number of features is high, and the subjects of the articles were probably very broad, so it cannot represent every article, but it is still interesting to see how the model seemed to value certain tokens and the strengths that it attributed to each. The top words, seen below, seem relevant to each category, but each category seems a bit different from the rest, broadly speaking. In the top ten, Computer Science has goal-oriented tokens, physics has subject domain tokens, mathematics has a lot of tool-related tokens, and statistics has technique-related tokens. It also seems to me that for the most part, the model found that the actual topics within the categories seemed less important, whereas the types of problems that researchers for each category tended to pursue were more important when the model was trying to determine which category the article belonged to. The Physics category does not support this observation as well as the others because many of its top tokens appear to be the specific domains that were probably covered in each article. This leads me to think that author information, citations, and references could also aid in categorization, and especially would be useful for search engines or recommendation systems.

| Computer Science | Physics | Mathematics | Statistics |
| --- | --- | --- | --- |
| Reachability | Mechanic | Prove | Bayesian |
| Bit | Calculation | Operator | Sequential |
| Inability | Sky | Sharp | Statistical |
| Improvement | Symmetry | Article | Recommender |
| Communication | Detector | Homotopy | Clustering |
| Robot | Molecular | Theorem | Approximate |
| Attempt | Galaxy | Perturb | Trial |
| Segmentation | Hydrodynamic | Mathematical | Parametric |
| Principled | Spacecraft | Category | Learning |
| Validate | Removal | Conic | Explanation |

### Comparisons and Evaluations

In terms of the preprocessing steps, scikit-learn's TF-IDF vectorizer was the fastest, taking only about five seconds to preprocess the documents, whereas spaCY's pipeline took three to four minutes. That being said, spaCY's pipeline was more sophisticated in that it also considered word meanings and usages, though the term frequency and document infrequency were not considered at this point of the process. However, more work or different features can be extracted with spaCY, so practice of it may be useful for wider applications. Neither of these methods was as slow as using NLTK and gensim, which took 10 to 15 minutes to preprocess the text.

Although the scikit-learn Naive Bayes and spaCY classifiers sought to solve different problems, the spaCY models performed better than the Naive Bayes classifiers. The Naive Bayes classifiers had especially poor recall when trying to predict Statistics, whereas the spaCY unigram bag-of-words model had higher recall for Statistics without sacrificing too much precision. The four-class ComplementNB model had precision, recall, and F1 scores of 0.84, 0.39, and 0.53 for Statistics, whereas the unigram bag-of-words model had 0.74, 0.83, and 0.78. The scores of the ComplementNB classifier were better for the larger classes, but I believe that it should be easier to correctly classify single labels versus multiple labels because there are not as many things that need to be predicted correctly. The correct prediction for a single label problem requires a true value for exactly one category per article, whereas the correct prediction for the multilabel problem can contain a true value for any one to three categories per article. In other words, a single label guess would have a 1 in 4 chance to randomly pick the correct answer, but a multilabel guess would have a 1 in 16 chance to randomly pick the correct answer, and two of those 16 choices will never be the correct answer in this article dataset.

In terms of the time taken to train, training the Naive Bayes classifiers was very fast, whereas training any of the spaCY models took longer. If there is a lot of training and retraining that needs to take place, then it may be harder to support using the spaCY models. There are other multilabel categorization models that still could be examined.

Overall, the unigram bag-of-words model would be the best model for this problem, especially since it does address the multilabel aspect of the problem. Its accuracy was good, and it can attain decent precision and recall across all categories. The threshold to use may depend on the application because different use cases may prefer more precision or more recall, but using a threshold around 0.45 to 0.50 will land precision and recall across all categories in the range of 0.75 to 0.93. It may be better to force the interpreter to return at least one category if no category meets the threshold because every article needs at least one label anyway.

## Conclusion and Future Work

Text categorization can help facilitate organization and information retrieval, which can help people and software find information more quickly and conveniently so people can focus on discovery and learning. This project sought to create a model that classifies articles into categories, and the unigram bag-of-words model can be used to automatically tag new or unlabeled articles with the four categories to fairly good precision and recall, especially for the three major categories, and especially when the articles have only one label. However, it should not be ignored that this model may categorize too many articles with Computer Science and too few articles with Statistics, and there will probably be some fuzziness with interdisciplinary articles. This project addressed one aspect of the larger applications of recommendation or search engines that would likely want to continue deeper into more specific topics.

There were two main problems with the model: the category imbalance and the scorer. The category imbalance was known from the beginning. Three of the six categories were represented decently. Two of the original six categories, Quantitative Biology and Quantitative Finance, were dropped altogether. Statistics had the smallest presence in the dataset, but the final model was not too bad at predicting it, so attempts to balance the classes were not pursued in this project.

A common approach to balance the classes would be to try to resample the dataset, which in this case would mean to consider downsampling Computer Science and to consider upsampling Statistics. A more involved approach that expands the project in a different direction could be to consider using different categories. The four categories were broad, and it seemed like Data Science topics appeared often in both Computer Science and Statistics, which was demonstrated in the EDA section and when looking at samples that were mislabeled by the model. Perhaps this project could be turned into an unsupervised and supervised problem: find similar groups, determine what these categories probably are or should be, and then try to teach a classifier based on the new categories. This would also make use of the other ~9000 articles from the "test.csv".

The other problem was the scorer, which was not exactly a problem, but it has its weaknesses. It was a basic scorer, since it had a single threshold value, but ultimately it failed to solve the problem because every article should have at least one topic. In this project, the workaround was to simply force the scorer to return the category that had the highest score if no score met the threshold, but this method meant that the uncertain articles would only belong to exactly one category, yet we know that an article could belong to more than one category.

Perhaps implementing a more sophisticated scorer or using a different type of scorer could be considered. Without changing too much to the function of the scorer, a slightly more sophisticated scorer could be one that dynamically interprets scores depending on the current distribution of scores. For example, if the scores were [0.18, 0.16, 4e-6, 0.03], it would return [1, 1, 0, 0], instead of [0, 0, 0, 0] given a threshold of 0.5, or [1, 0, 0, 0] given the same threshold and a requirement that the maximum category is set to true if no category met the threshold. This could help with overcoming the issue of an uncertain batch of prediction scores never labeling an article with more than one category, and it may also help when scores are almost meeting the threshold but failing to return a second category as true despite also being relatively highly recommended. For example, [0.51, 0.49, 0.01, 0.01] with a threshold of 0.5 would return [1, 0, 0, 0], even though the predictions were close and not very strong. Otherwise, perhaps scoring could be remade: instead of being a classification problem with binary prediction results, in which categories are each only true or false, it could be a recommendation problem, in which the model's predictions are treated more as a ranking of category by relevance. How useful this is may depend on the application.
