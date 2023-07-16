from sg_story_vects import cluster_stories_for_dates
import json

def create_collection(dates, cutoff, cutoff_integer, story_id):
    
    # generate the clusters using the new algorithm function

    story_vectors = cluster_stories_for_dates(dates, min_cosine_sim=cutoff, story_vect_dim=1000, cmp_only_event_con_comps=False)

    # create the JSON file
    story_json = json.dumps(story_vectors)

    # save the json file
    with open(f"data/story_{story_id}/{cutoff_integer}/story_{story_id}_cutoff_{cutoff_integer}.json", "w") as outfile:
        outfile.write(story_json)


# list of cutoff values to test in order to find the best performing
cutoff_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# below each story is the dates the story appears in

# story 0
# '2018-06-11'
# '2018-06-12'
# '2018-06-13'


for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2018-06-11', '2018-06-12', '2018-06-13'], cutoff, integer_cutoff, 0)

#story 1
# '2018-02-07'
# '2018-02-08'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2018-02-07', '2018-02-08'], cutoff, integer_cutoff, 1)

#story 2
# '2018-07-05'
# '2018-07-06'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2018-07-05', '2018-07-06'], cutoff, integer_cutoff, 2)

# story 3
# '2018-10-27'
# '2018-10-28'
# '2018-10-29'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2018-10-27', '2018-10-28', '2018-10-29'], cutoff, integer_cutoff, 3)

#story 4
# '2018-12-13'
# '2018-12-14'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2018-12-13', '2018-12-14'], cutoff, integer_cutoff, 4)

#story 5
# '2018-12-01'
# '2018-12-02'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2018-12-01', '2018-12-02'], cutoff, integer_cutoff, 5)

# story 6

# story 7

# story 8
# '2019-02-16'
# '2019-02-17'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2019-02-16', '2019-02-17'], cutoff, integer_cutoff, 8)

# story 9
# '2019-03-30'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2019-03-30'], cutoff, integer_cutoff, 9)

# story 10

# story 11
# '2019-12-29'
# '2019-12-30'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2019-12-29', '2019-12-30'], cutoff, integer_cutoff, 11)

# story 12

# story 13

# story 14

# story 15

# story 16
# '2020-12-28'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2020-12-28'], cutoff, integer_cutoff, 16)


# story 17
# '2020-07-18'
# '2020-07-19'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2020-07-18', '2020-07-19'], cutoff, integer_cutoff, 17)

# story 18

# story 19
# '2019-08-14'

for cutoff in cutoff_values:
    integer_cutoff = int(cutoff*100)
    create_collection(['2019-08-14'], cutoff, integer_cutoff, 19)
