---
layout: default
---

## You are what you eat ...

You are what you eat - an idiom surely most of us have already heard at some point in our life. Be it as a child when we did not want to eat the broccoli our mother lovingly prepared, or from your colleague at work who just discovered veganism.
This idiom simply states that "the food one eats has a bearing one one's state of mind and health." [[1]](https://www.phrases.org.uk/meanings/you-are-what-you-eat.html)
Very few would argue this, however, we want to take this idiom literally: are you really what you eat?

This question immediately leads to another question: what are you exactly?
We do not want to make this question any more phylosophical than it already is, therefore, we assume that groups of people can be defined by their external properties: age, religion, ethnicity, wealth, and so on.
There certainly exist multiple ways of defining a person, however, the aforementioned values can easily be captured by population demographics, and thus, are of interest for us.

## Our Goal

We are interested in the influence of demographic data on food composition.
Can food consumption habits be mapped to certain groups of people?
In this data story, we are going to answer this question in two parts: first, we will explore relations between each individual demographic marker and food consumption habits.
Afterward, we will investigate how well we can predict food consumption habits from demographic markers.
These analyses are interesting, but not really useful without a specific usecase.
Therefore, we are going to apply our newly-gained understanding and develop a marketing strategy for a new protein bar!

## Introducing the Data Sets

In this data story we explore the relation between food consumption habits and population demographics in the year 2015 in London.
For our analyses we use two data sets: the [Tesco 1.0 Grocery](https://www.nature.com/articles/s41597-020-0397-7) data set and the [ward profiles](https://data.london.gov.uk/dataset/ward-profiles-and-atlas) published in 2015 by the government of the United Kingdom.
The Tesco data set captures provides an aggregated view of food purchases for the year 2014 in Tesco supermarkets in London.
For every ward, it contains the nutrient content of the typical food product - in other words, all purchased products of 2014 are aggregated to yield the "average" food product of a ward.
<div id="images"> 
	<img src="assets/images/pie.png">
	<div class="caption">Nutrients of the average food product in the ward "Gascoigne". Looks yummy, doesn't it?</div>
</div>

The ward profiles provide a range of demographic data, such as population age distribution, ethnicities, general fertility rate, ambulance callouts and many more.
The ward profiles provide 1000 features! We therefore limit our analyses to the following features: *age distribution*, *ethnicity*, *religion*, *qualification*, *household income*, *happiness*, *Health*, and *Happiness*. 
However, one problem arises: most of these indicators were either collected in 2013, or with the nationwide census of 2011.
The tesco data set contains grocery data from 2014, that's a 1- or 3-year difference!
Does that make a difference?

## Did the population demographics change between 2011 and 2014?

Before we can start exploring the relation between food and demographcis, we need to first investigate how the time of survey influences the demographics.
To do this, we calculate the change in population for 2011 and 2013 in relation to 2014 for every ward.
<div id="images"> 
	<img src="assets/images/pop_diff.png">
	<div class="caption">Relative population difference of all wards between 2011/2014 and 2013/2014.</div>
</div>
The difference in population of wards for 2014 and 2013 is small, only 11 wards show more than a 5% change in population count.
However, 111 wards show a difference larger than 5% for 2011.
With this, we conclude that the population in those 111 wards changed significantly.
This change in population might also influence other demographic factors.
Therefore, we exclude these wards for the following analyses.
The remaining wards do not seem to have changed much in terms of population numbers.
Thus, we assume that other demographic markers did not significantly change as well.

## Teenagers love Carbs

<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~aglavac/7.embed">
</iframe>

Looking at the contour plot, we can see some interesting correlations.
Interestingly, the amount of carbohydrates consumed in a ward seems to be positively correlated with the number of people with lower qualifications and with younger people under the age of 15.
Furthermore, wealthier wards (indicated by a higher median and mean household income) seem to consume more protein, wards with more non-religious seem to consume more alcohol.
These findings are quite intereting, thus, we want to explore these correrlations further.

## Correlating Demographics and Food Habits

The qualitative analysis is interesting, but as Data Scientists, we love numbers and hard facts.
Thus, we calculate the Spearman Rank coefficient between the nutrients and the demographic markers and their corresponding p-values, to estimate whether the correlations are actually significant.
<div id="images"> 
	<img src="assets/images/feat_corrs.png">
	<div class="caption">Spearman Rank correlations of demographic markers vs. nutrients (left) and their corresponding p-values (right). Significant p-values are indicated with blue.</div>
</div>
Judging by the p-values, most correlations are significant.
`Well-Being` is not a demographic marker showing significant correlations with nutrients, a similar conclusion can be made for `Aged 65+` and `Born in UK`.
The prevalence of `White` is positively correlated with the energy provided by protein, alcohol and fibre.
Wards with less religious people (indicated by a higher fraction of `No religion`) seem to consume more alcohol, more fibre and more protein.
All in all, the nutrients show many significant correlations with demographic markers.
However, it is difficult to judge which demographic markers can actually best predict each nutrient.
To find the most important demographic markers, we build a prediction model for each nutrient using the demographics as independent variables.

## Finding the most important features

## A Case Study: Developing a Marketing Strategy

Some sort of chicken product: ward with high protein and low fat consumption




 








