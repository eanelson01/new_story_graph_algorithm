## Description of the Exemplar Dataset

| Characteristic Title | Description                                                                                                                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| story_title          | The assigned title for the story being tracked.                                                                                                                                                                | 
| exemplar_story_link  | The link to the graph where the story has the largest degree (the peak of the story).                                                                                                                          | 
| duration             | A binary classification of single or mutli day depending on how long the story went for.                                                                                                                       | 
| purity               | A binary classification of pure or impure based on if more than half of the news articles in the connected component are related to the tracked story.                                                         | 
| degree_category      | A description of how popular that news story was based on the degree of the exemplar connected component. Connected components are labeled low for degrees less than 7.5 and high for degrees greater than 7.5. | 
| degree_value         | The degree of the story's connected component at its peak.                                                                                                                                                     | 
| story_start_time     | The start time for the story pulled from the time and date found in the URI for the first graph of the story.                                                                                                  |
| story_end_time       | The end time for the story pulled from the time and date found in the URI for the last graph of the story.                                                                                                     |
| links                | A list of dictionaries that each represent graphs that makes up the story in chronological order.                                                                                                              |
| graph_link           | The link to the individual graph on the story graph website.                                                                                                                                                   | 
| cc_degree            | The degree of the connected component related to the given story found in the individual graph.                                                                                                                |
| cc_index  | The index of the selected connected component. Indices start at 1 in this exemplar dataset to match the output on the story graph website.                                                                     |