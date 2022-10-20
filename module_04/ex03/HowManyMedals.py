## Sort elem by year 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html 
## Unique Year in dict form df 
# https://stackoverflow.com/questions/66642744/create-a-dictionary-of-unique-values-of-a-column-in-a-dataframe-in-pandas 
# https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping 
## Find Occurence with mutliple conditions 
# https://stackoverflow.com/questions/60029500/how-to-count-occurrences-based-on-multiple-criteria-in-a-dataframe
from FileLoader import FileLoader 

def how_many_medals(df, name) :
    good_people = df[df['Name'] == name]
    good_people.sort_values(by=['Year'])
    # Create simple dict with Year 
    ret_dict = dict(enumerate(good_people.Year.unique()))
    ret_dict = {v: k for k, v in ret_dict.items()}
    # Insert Type Of Medals 
    for key, value  in ret_dict.items() :
        ret_dict[key] = {
        'G' : sum((good_people.Year == key) & (good_people.Medal == 'Gold')),
        'S':  sum((good_people.Year == key) & (good_people.Medal == 'Silver')),
        'B':  sum((good_people.Year == key) & (good_people.Medal == 'Bronze'))}

if __name__ == "__main__":

    f = FileLoader()
    df = f.load('../athlete_events.csv')
    how_many_medals(df, 'Gary Abraham')
    how_many_medals(df, 'Yekaterina Konstantinovna Abramova')
    how_many_medals(df, 'Kristin Otto')





