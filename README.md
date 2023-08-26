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

TODO

## Conclusion and Future Work

TODO
