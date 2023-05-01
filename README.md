# Analyzing Story Graph Bot Analysis and Algorithm

## Installation

To run the analysis of storygraph-bot's current analysis, download both [storygraphbot](https://github.com/oduwsdl/storygraphbot) and [storygraph-toolkit](https://github.com/oduwsdl/storygraph-toolkit). Both modules have installation instructions as part of their repository. These two modules are used to download the observations of the current algorithm

## Exemplar Data Set

The [exemplar data set](data/exemplar_dataset.json) is a JSON file with 20 stories with varying qualities. Each dictionary represents a story. Characteristics include the story's title, duration, purity, highest degree, start, and end times. In the links component, there is a list of dictionaries that represent each connected component which is in 10 minute intervals. Each graph dictionary has the story graph link, the average degree of the connected component, and the index of the component as given by the website. 

To create the exemplar data set, I selected a variety of stories from the year in review from [2018](https://storygraph.cs.odu.edu/studies/2019-03/365-dots-in-2018/), [2019](https://storygraph.cs.odu.edu/studies/2019-12/365-dots-in-2019/), and [2020](https://storygraph.cs.odu.edu/studies/2021-01/366-dots-in-2020/). These graphs provided the link to the graph containing the highest degree connected component for the story. I started at this peak of the story and went back in 10 minute intervals until I saw the graph where the connected component first started, indicated by the time stamp where ten minutes before there were no articles related the given story.

Once I found the beginning of the story, I went graph to graph, recording the information included in the [exemplar data set](data/exemplar_dataset.json). This process continued until there were no longer any more connected components or articles refering to the given story.

## Toolkit files

In the folder [toolkit_files](data/toolkit_files) found in the [data folder](data), there are the output files from the storygraph-bot algortihm. The stories are denoted by their index, 0 to 19, which come from their position in the exemplar data set. In each file for a given story, the cache holds a json file for each data. This is where the information for the graphs the algorithm flagged are found in. 
