Extended Sentiwordnet analysis of Amazon review Datasets 
===================

We use an extended and manually annotated Sentiwordnet with a specific domain (electronics) to analyse the Amazon reviews dataset.
A copy of the Amazon dataset can be downloaded from the  [Stanford Large Network Dataset Collection](http://snap.stanford.edu/data/web-Amazon.html "Snap"), the extended Sentowordnet annotated dataset can be downloaded from this repository for further testing.

The Amazon reviews dataset has the next distribution of reviews attached of one of the next labels:

 * 1.0:  14675
 * 2.0:  7566
 * 3.0:  8719
 * 4.0:  17717
 * 5.0:  30253
 
The matchings distribution of Sentiwordnets are:

 * 1.0: 42538 
 * 2.0: 32496 
 * 3.0: 41045 
 * 4.0: 93482 
 * 5.0: 126337

Once we have process the Amazon Datasets linking reviews, label reviews (from 1.0 to 5.0) and manual positive and negative scores from extended Sentiwordnet (from 0.0 to 1.0), we can summarize the result dataset

```R

> data <- read.csv('/Users/rmaestre/Projects/amazon-datasets/data/output/results.tsv', header=TRUE, sep="\t")
> summary(data)
            word          pos               neg              X1.0              X2.0        
 able         :  1   Min.   :0.00000   Min.   :0.0000   Min.   :0.00000   Min.   :0.00000  
 abrupt       :  1   1st Qu.:0.00000   1st Qu.:0.0000   1st Qu.:0.02832   1st Qu.:0.00000  
 acceptable   :  1   Median :0.07125   Median :0.0000   Median :0.11567   Median :0.09345  
 accessible   :  1   Mean   :0.26748   Mean   :0.2376   Mean   :0.18213   Mean   :0.12130  
 accommodating:  1   3rd Qu.:0.52712   3rd Qu.:0.4744   3rd Qu.:0.24049   3rd Qu.:0.16276  
 accomplished :  1   Max.   :0.99477   Max.   :0.9960   Max.   :1.00000   Max.   :1.00000  
 (Other)      :504                                                                         
      X3.0              X4.0             X5.0       
 Min.   :0.00000   Min.   :0.0000   Min.   :0.0000  
 1st Qu.:0.05231   1st Qu.:0.1106   1st Qu.:0.1543  
 Median :0.11543   Median :0.2476   Median :0.3207  
 Mean   :0.14834   Mean   :0.2274   Mean   :0.3208  
 3rd Qu.:0.16667   3rd Qu.:0.3115   3rd Qu.:0.4605  
 Max.   :1.00000   Max.   :1.0000   Max.   :1.0000

```

Pictures below show the labeled annotation distribution of each sentiword. We can see two main distributions near 0.0 and near 0.5 because each word has a negative and positive score annotation, e.g.: "limited" has +0.0 and -0.325.

```
> p1 <- ggplot(data, aes(x = pos)) + geom_density() + ylim(c(0.0,2.7)) + ggtitle("Positive labeled")
> p2 <- ggplot(data, aes(x = neg)) + geom_density() + ylim(c(0.0,2.7)) + ggtitle("Negative labeled")
> multiplot(p1, p2, cols=1)
```


![Labeled distribution](https://raw.github.com/rmaestre/amazon-sentiwordnet/master/images/word_labeled_dist.jpg?token=145687__eyJzY29wZSI6IlJhd0Jsb2I6cm1hZXN0cmUvYW1hem9uLXNlbnRpd29yZG5ldC9tYXN0ZXIvaW1hZ2VzL3dvcmRfbGFiZWxlZF9kaXN0LmpwZyIsImV4cGlyZXMiOjEzODg0MTc2MTZ9--3f2e8016d671a25bd75603132bc4f8edc8480535 "Labeled distribution")


To perform the analysis, we calculate the frecuency of each sentiword in each review clasifying each review as a vector with one label from 1.0 to 5.0 (the common rating). E.g.: the probability to find the sentiword "limited" (with +0.0 and -0.325 score manual labels) in each band label is the follow one:

*   p(limited|1.0)=0.12456344586728754
*   p(limited|2.0)=0.13736903376018628
*   p(limited|3.0)=0.15366705471478465
*   p(limited|4.0)=0.30151338766006985
*   p(limited|5.0)=0.2828870779976717


In order to visualize the relation between the annotated score of Sentiwordnet and the probability to find the word in a determinate review label, we print below the each relationship between "neg" and "pos" values and review labels.

![Correlation](https://raw.github.com/rmaestre/amazon-sentiwordnet/master/images/correlation_word_label.jpg?token=145687__eyJzY29wZSI6IlJhd0Jsb2I6cm1hZXN0cmUvYW1hem9uLXNlbnRpd29yZG5ldC9tYXN0ZXIvaW1hZ2VzL2NvcnJlbGF0aW9uX3dvcmRfbGFiZWwuanBnIiwiZXhwaXJlcyI6MTM4ODQxOTEwM30%3D--a826cb9530f29fdaefa63766862b5b836172874c "Correlation")

Therefore, we can see a positive correlation line betweem X1 and "neg" and X5 and "pos" as well as negative correlation between X1 and "pos" and X5 and "neg".

In order, to create a random distribution to compare results, we create a Random Sentiwordnet

```python
if np.random.uniform(0,1) > 0.5:
   sw_pos = 0.0
   sw_neg = np.random.uniform(0,1)
else:
    sw_neg = 0.0
    sw_pos = np.random.uniform(0,1)
```

Thus, picture below shows the previous random sampling.

![Random test](https://raw.github.com/rmaestre/amazon-sentiwordnet/master/images/random_test.jpg?token=145687__eyJzY29wZSI6IlJhd0Jsb2I6cm1hZXN0cmUvYW1hem9uLXNlbnRpd29yZG5ldC9tYXN0ZXIvaW1hZ2VzL3JhbmRvbV90ZXN0LmpwZyIsImV4cGlyZXMiOjEzODg0MTk5OTF9--49e176cf0454f308e34d08a4338467b30b885283 "Random test")
 
 
Future work and improvements
===================
* Working in n-grams (n=2) in order to define context and word; i.e.: in the hotel domain, the word cold has not the same polarity of you are talking bout the hotel staff or the drink in the room. Better precision, worst recall.
* Improve the recall of the extended Sentiwordnet
* Compare the main [Sentiwordnet](http://sentiwordnet.isti.cnr.it/ "Sentiwordnet") with a domain specific one

