from sg_story_vects import cluster_stories_for_dates
import json

def create_collection(dates, cutoff, vector_dim, story_id):
    
    # generate the clusters using the new algorithm function

    story_vectors = cluster_stories_for_dates(dates, min_cosine_sim=cutoff, story_vect_dim=vector_dim, cmp_only_event_con_comps=False)

    # create the JSON file
    story_json = json.dumps(story_vectors)

    # save the json file
    with open(f"data/new_algorithm_files/story_{story_id}/story_{story_id}_dimension_{vector_dim}.json", "w") as outfile:
        outfile.write(story_json)

cutoff = 0.9

# list of dimension to be tested
dimension_values = [10, 50, 100, 500, 1500, 2000]

# story 0
# '2018-06-11'
# '2018-06-12'
# '2018-06-13'


for vector_dim in dimension_values:
    create_collection(['2018-06-11', '2018-06-12', '2018-06-13'], cutoff, vector_dim, 0)


#story 1
# '2018-02-07'
# '2018-02-08'

for vector_dim in dimension_values:
    create_collection(['2018-02-07', '2018-02-08'], cutoff, vector_dim, 1)

#story 2
# '2018-07-05'
# '2018-07-06'

for vector_dim in dimension_values:
   create_collection(['2018-07-05', '2018-07-06'], cutoff, vector_dim, 2)

# story 3
# '2018-10-27'
# '2018-10-28'
# '2018-10-29'

for vector_dim in dimension_values:
    create_collection(['2018-10-27', '2018-10-28', '2018-10-29'], cutoff, vector_dim, 3)

#story 4
# '2018-12-13'
# '2018-12-14'

for vector_dim in dimension_values:
    create_collection(['2018-12-13', '2018-12-14'], cutoff, vector_dim, 4)

#story 5
# '2018-12-01'
# '2018-12-02'

for vector_dim in dimension_values:
    create_collection(['2018-12-01', '2018-12-02'], cutoff, vector_dim, 5)

# story 8
# '2019-02-16'
# '2019-02-17'

for vector_dim in dimension_values:
    create_collection(['2019-02-16', '2019-02-17'], cutoff, vector_dim, 8)

# story 9
# '2019-03-30'

for vector_dim in dimension_values:
    create_collection(['2019-03-30'], cutoff, vector_dim, 9)

# story 11
# '2019-12-29'
# '2019-12-30'

for vector_dim in dimension_values:
    create_collection(['2019-12-29', '2019-12-30'], cutoff, vector_dim, 11)

# story 16
# '2020-12-28'

for vector_dim in dimension_values:
    create_collection(['2020-12-28'], cutoff, vector_dim, 16)

# story 17
# '2020-07-18'
# '2020-07-19'

for vector_dim in dimension_values:
    create_collection(['2020-07-18', '2020-07-19'], cutoff, vector_dim, 17)

# story 19
# '2019-08-14'

for vector_dim in dimension_values:
    create_collection(['2019-08-14'], cutoff, vector_dim, 19)