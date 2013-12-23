data <- read.csv('/Users/rmaestre/Projects/amazon-datasets/data/output/results.tsv', header=TRUE, sep="\t")


p1 <- ggplot(data, aes(x = pos)) + geom_density() + ylim(c(0.0,2.7)) + ggtitle("Positive labeled")
p2 <- ggplot(data, aes(x = neg)) + geom_density() + ylim(c(0.0,2.7)) + ggtitle("Negative labeled")
multiplot(p1, p2, cols=1)


p1 <- ggplot(data, aes(x = neg, y = X1.0)) + geom_point() + geom_smooth(method = "loess", formula = y ~ x) + ylim(c(-0.8,1.3))
p2 <- ggplot(data, aes(x = neg, y = X5.0)) + geom_point() + geom_smooth(method = "loess", formula = y ~ x) + ylim(c(-0.8,1.3))
p3 <- ggplot(data, aes(x = pos, y = X1.0)) + geom_point() + geom_smooth(method = "loess", formula = y ~ x) + ylim(c(-0.8,1.3))
p4 <- ggplot(data, aes(x = pos, y = X5.0)) + geom_point() + geom_smooth(method = "loess", formula = y ~ x) + ylim(c(-0.8,1.3))
multiplot(p1, p2, p3, p4, cols=2)





multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  require(grid)

  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)

  numPlots = length(plots)

  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                    ncol = cols, nrow = ceiling(numPlots/cols))
  }

 if (numPlots==1) {
    print(plots[[1]])

  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))

    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))

      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}
