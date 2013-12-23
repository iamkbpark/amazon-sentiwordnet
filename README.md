Sentiwordnet analysis of Amazon review Datasets 
===================

Amazon reviews datasets study through extended sentiwordnet domain



```r

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


Pictures below show the labeled annotation distribution of each sentiword

```
> p1 <- ggplot(data, aes(x = pos)) + geom_density() + ylim(c(0.0,2.7)) + ggtitle("Positive labeled")
> p2 <- ggplot(data, aes(x = neg)) + geom_density() + ylim(c(0.0,2.7)) + ggtitle("Negative labeled")
> multiplot(p1, p2, cols=1)
```





