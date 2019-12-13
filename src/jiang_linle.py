#!/usr/bin/env python
# coding: utf-8

# ### INF 510 Fall 2019 Final Project Submission

# 1.	**The names of team member(s)**:
# 
#     Linle Jiang

# 2.	**How to run your code (what command-line switches they are, what happens when you invoke the code, etc.)**
# 
#     This project requires the following packages:
#     - requests, BeautifulSoup, pandas, json, csv, argparse and bokeh
#     
#     To use the Bokeh package, please make sure you activate the environment file.
#     
#     To run this project, make sure the above packages are installed, and then simply clone the repo at https://github.com/linlejiang/inf550_project and execute this notebook. Or, you can access the python file using command line. The -source=remote will scrape the place data from Google and TripAdvisor, and then access Google Place API to obtain the geolocation of the places. On the other hand, the -source=local will just used the processed data generated from the -source=remote code. With the data prepared, both will then proceed to the analysis section. 
#     
#     Note: please copy the Google API_key from the DEN Dropbox submission and insert it into the API_key variable below.
# 

# 3.	**Any major “gotchas” to the code (i.e. things that don’t work, go slowly, could be improved, etc.)**
#     
#     The code takes about 10 minutes to scrap the data from Google and TripAdvisor.  And the generated interative plots will all in the same row, I couldn't make them display in two rows.

# 4.  **Anything else you feel is relevant to the grading of your project your project.**
# 
#     If you don't run the remote mode before the local mode, you may find that the two mode generates slightly different hotel data. Specifically, the number of hotels may differ. For more details and explanations, please refer to the comments under the 'Hotel data criteria' in the trip_data() function.

# 5. **What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.)**
# 
#     Consistent with my Milestone 1 assignment, my motivation to select this project is to plan a trip to Hawaii. From my experience, there isn’t any interactive maps with both top sights and hotels plotted simultaneously or without substantial manual efforts. Therefore, the ultimate goals of this project are: 1) to create three interactive maps of Hawaii automatically, which will enable users to interact with the maps (e.g., the size of maps can be changed within the visualization, and when the mouse cursor is at a hotel datapoint, the name of the hotel will show up); and 2) to compare visually how different the distributions would be for hotels plotted by different popularity metrics.
# 
#     However, there are some minor changes: 
# 
#       1. the hotel address data was planned to be scraped from TripAdvisor initially, in order to use Google API to get geometry results. However, this plan was dropped due to the following reasons:     
#           1) some hotel addresses obtained from TripAdvisor were not correct, after check the website;  
#           2) Google API allows for hotel names as inputs to request hotel geometry, and using this approach substantially decrease the number of missing data than scraping from TripAdvisor;          
#           3) this increases the data acquiring time significantly, and lower the probability of being banned by the website, as the number of requests drop substantially.
# 
#       2. I plot 20 sights instead of 10.
# 
#       3. Instead of collecting all hotel listings from TripAdvisor, I specified certain criteria to determine what kinds of hotels should be included in this dataset. This is to resemble real-life hotel selection processes, and to limit the number of request queries when the code scrapes data from TripAdvisor.
# 
#       4. The three metrics used to describe the hotels are price, popularity (i.e., number of reviews), and recommendation (i.e., computed by the product of the ratings and the standardized number of reviews). The recommendation metric is also used to select the sights in the plot.

# 6. **What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?)**
# 
#     I generate three interative plots in a html file, if you run the code, they will automatically show up in your browser. The plot enables users to interact with the maps (1. the size of maps can be changed; 2. when the mouse cursor is at a sight, the name of the sight will show up; 3. when the mouse cursor is at a hotel, the name and lowest price of the hotel will show up; 4. when click on the hotel circle, the browser will open a new tab directing the user to the hotel webpage in TripAdvisor; 5. the map can zoom in/out if you launch the wheelZoom tool; 6. you can drag the map to view different areas within the map).
#     
#     Overall, in this project, I found that the most recommended sights (i.e., the metric based on reviews and ratings) are concentrated in the urban area, only a few of them are natural sights. Also, although all the islands have at least one most recommended sight, most of them are in Honolulu. This makes sense, considering that Honolulu is the most developed area in Hawaii islands. 
#     
#     For the hotels included in the dataset, first, most of them are located near the sea. This is consistent with the idea that the general public enjoys the beach and hotels with a view of the sea. Additionally, it appears that the cheaper hotels tend to cluster together, likely due to the high demand and competitive nature, while the more expensive hotels are more spread out. Also, only about half of the sights have hotels closeby, this is especially the case in the Island of Hawaii and the urban area of Honolulu. Moreover, these hotels closer to the sights tend to have lower prices. Finally, it appears that there are positive correlations between hotel price, popularity (i.e., number of reviews), and recommendation. Consider the higher expenses in Hawaii, it is possible that visitors of Hawaii tend to have higher income level. And thus they also tend to stay at hotels with higher quality, and are able to afford such expenses.

# 7. **What difficulties did you have in completing the project?**  
# 
#     *What didn't work?  What was hard to do?  What stumbling blocks did you run into?*
#     
#     The most difficult part for me is to scrape a large amount of data from TripAdvisor. According to my initial plan, I would have to make thousands of request to the website in order to get all the hotel data. To avoid being banned by the website, I tried to rotate proxies and user agents. However, that was not practical because the free public IP significantly slowed down the scraping processes, which is likely due to the extended time making requests via different proxies. Therefore, I had to step back and figure out what were the data that might not be necessary. Fortunately, I was able to increase the number of hotels to be included in this dataset by removing one unecessary attribute (i.e., hotel address, note that each address needs one individual request when scraping).
#     
#     Another difficulty I had was to optimize my code to shorten the time spent on scraping the hotel data. However, my hand is tied given the website structure, which requires a large amount of requests to be made.

# 8. **What skills did you wish you had while you were doing the project?**
# 
#     *Was there something that you wish you'd have known better while you were doing the project?  If you learned that skill while doing the project, note it here, but even if not, what would have helped?*
# 
#     As I mentioned in question 7, first, I wished I had learned how to optimize my code to collect data at a faster rate, but I wasn't sure if there are ways to make my code more efficient. Second, I wished I had learned how to perform proxy rotation and user agent rotation to prevent being banned by the website. I did learn some techniques and applied, but they weren't successful attempts. Third, I wished I had known how to create interative visualizations, which, through this project, I learned about how to use the bokeh package to create interactive maps. I was able to include all features as planned. Still, there are a lot more useful and interesting features to be learned. Finally, I wished I had learned some NLP techniques, so that I could collect the reviews for each hotel, and extract keywords from the review to provide some qualitative descriptions for the each hotel. 

# 9. **What would you do “next” to expand or augment the project?**
# 
#     *If you had to continue this project, what would you add to it?  If you had the skills you mentioned in question 8, what could you do to enhance things?*
#     
#     First, I would extend the program so that whenever people searches for a location, the program will automatically scrape data for that location and generate the interactive maps. Second, if I had known how to optimize my code and perform efficient proxies and user agent rotations, my program would scale better and be able to collect more data and operate faster. Third, if I had learned some NLP keyword extraction technique, I could include some extra attributes in this dataset.

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv
import argparse
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions, LinearColorMapper, ColorBar, HoverTool, TapTool, OpenURL
from bokeh.plotting import gmap
from bokeh.transform import transform
from bokeh.layouts import row

API_key = input('Google API Key: ')


# In[2]:


# get soup data from website
def get_trip_soup(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException:
        print("There is a problem connecting you to the website.")
    else:
        soup = BeautifulSoup(r.content, 'lxml')
    return soup


# In[3]:


# Google sight data scraper
def google_data(soup):
    div_all_results = soup.findAll('div', {'class':'GwjAi'})
    sight_data = {}
    
    for sights in div_all_results:
        sight_name = sights.find('div', {'class':'skFvHc'}).contents[0]
        sight_data[sight_name] = []
        
        # some of the sights may not have ratings or reviews, so need to check if that data is available before adding it
        if sights.find('span', {'class':'KFi5wf'}) != None:
            sight_rating = float(sights.find('span', {'class':'KFi5wf'}).contents[0])  # ratings are float, convert from str
        else:
            sight_rating = 0.0
        
        review = []
        if sights.find('span', {'class':'jdzyld'}) != None:
            sight_review = sights.find('span', {'class':'jdzyld'}).contents[0]
        else:
            sight_review = '0'
        
        # sight_review is a Navigatestring object, this is to format it
        # using .lstrip() can convert it back to regular string
        review = list(sight_review.lstrip())
        for i in review:
            for j in ['(', ')', ',']:
                if j in review:
                    review.remove(j)
        review_str = ''.join(review)
        
        sight_data[sight_name] = [sight_rating, int(review_str)]  # review_str are int, convert from str

    return sight_data  # return a dict, each key represents a sight, and the value holds data for that sight


# In[4]:


# TripAdvisor hotel data scraper
def trip_data(trip_soup):

    """logic:

    1) The hotel data are organized by regions (i.e., cities), so the first step of this function is to get all the 
    links for the regions. The regions are scattered in three pages.

    Note that the format of the first page and the rest are different.

    2) Each region may have multiple pages of hotel data, so the second step is to, after request a region page, 
    collect hotel data from a page, and then iterate through all the pages. Iterate requesting the regions pages.

    Note that the hotel address data was planned to be scraped from TripAdvisor initially, in order to use Google
    API to get geometry results. However, this plan was dropped in this project due to the following reasons:
        1) some hotel addresses obtained from TripAdvisor were not correct, after check the website;
        2) Google API allows for hotel names as inputs to request hotel geometry, and using this approach substantially
        decrease the number of missing data than scraping from TripAdvisor;
        3) this increases the data acquiring time significantly, and lower the probability of being banned by the
        website, as the number of requests drop substantially.

    Hotel data criteria:

    Due to the huge amount of data, data is included only if it is with: 
        1) more than 100 reviews are included;
        2) available and qualified user rating (>= 3.0);
        3) available price listing.
    And the hotel listing is not sponsored (i.e., ad). With this criterion, it may lead to inconsistent number of
    hotel data. Because sponsored hotel will not be listed again in regular hotel listings, and there are different
    sponsored hotels, with different hotel criteria as listed aforementioned.
    """

    # 1st. get all regions (i.e., city) links for later access
    # since the regions links differ between the ones from the first page and from the rest pages, get them separately

    # for regions links in page 1
    regions_div = trip_soup.findAll('div', {'class': 'geo_wrap'})
    regions_list = []

    # get the region links
    for regions in regions_div:
        if regions.find('a', {'class': 'linkText'}) != None:
            region_sublink = regions.find('a').get('href')
            region_links = 'https://www.tripadvisor.com' + region_sublink
            regions_list.append(region_links)

    # for regions links in the following pages
    next_region_page_soup = trip_soup
    while True:
        region_page_sublink = next_region_page_soup.find('a', {'class': 'nav next taLnk ui_button primary'})

        if region_page_sublink == None:  # stop if no more next page available
            break

        else:
            next_regions_link = 'https://www.tripadvisor.com' + region_page_sublink.get('href')
            requests.packages.urllib3.disable_warnings()  # this is to prevent error causing by SSL verification
            next_region_page_soup = get_trip_soup(next_regions_link)

            next_regions_li = next_region_page_soup.findAll('li', {'class': 'ui_column is-12-mobile is-4-tablet is-3-desktop'})

            for next_regions in next_regions_li:
                if next_regions.find('a', {'class': 'city'}) != None:
                    next_regions_sublink = next_regions.find('a').get('href')
                    next_regions_links = 'https://www.tripadvisor.com' + next_regions_sublink
                    regions_list.append(next_regions_links)

    # 2nd. get all hotel pages link from each region link (each region link may contain multiple pages of hotel data)
    # when each page link is obtained, create new page soup to get hotel data at the same time

    hotel_data = {}  # hotel names are keys, all other data (including hotel_url, hotel_price, hotel_rating, 
                    # hotel_review) are stored in a list as values

    for regions in regions_list:
        page_soup = get_trip_soup(regions)

        while True:
            # hotel data on every following page
            div_all_results = page_soup.findAll('div', {'class':'ui_column is-8 main_col allowEllipsis'})

            for hotels in div_all_results:

                # get hotel name:
                try:
                    
                    if hotels.find('a', {'dir': 'ltr'}).contents[0] != None:
                        hotel_name = hotels.find('a', {'dir': 'ltr'}).contents[0]
                    
                except AttributeError:
                    break
                        
                except TypeError:
                    break
                    
                else:
                    # get number of reviews, definately has a value for each hotel (equal or greater than 0)
                    # format the reviews from NavigatableString to int
                    review = list(hotels.find('a', {'class': 'review_count'}).contents[0].split(' ')[0])
                    if ',' in review:
                        review.remove(',')
                    hotel_review = int(''.join(review))

                    # hotel criteria with number of reviews
                    if hotel_name not in hotel_data and hotel_review > 100:
                            
                        try:

                            # hotel criteria with ratings, if no ratings, the attribute will not occur, so need to catch that exception
                            if hotels.find('a', {'data-clicksource': 'BubbleRating'}).attrs['alt'].split(' ')[0] != None and float(hotels.find('a', {'data-clicksource': 'BubbleRating'}).attrs['alt'].split(' ')[0]) >= 3.0:
                                hotel_rating = float(hotels.find('a', {'data-clicksource': 'BubbleRating'}).attrs['alt'].split(' ')[0])
                                
                        except AttributeError:
                                break
                                
                        else:

                            try:

                                # hotel criteria with price listings, if not available, it will indicate TypeError, so need to catch that exception
                                if hotels.find('div', {'class': 'price autoResize'}) != None:
                                    price = hotels.find('div', {'class': 'price autoResize'}).contents[0]
                                    list_price = list(price.lstrip())
                                        
                            except TypeError:
                                break
                                        
                            else:        
                                
                                # formating price to float from NavigatableString
                                for i in ['$', ',']:
                                    if i in list_price:
                                        list_price.remove(i)
                                hotel_price = int(''.join(list_price))

                                # get hotel url
                                url = hotels.find('a').get('href')
                                hotel_url = 'https://www.tripadvisor.com' + url
    
                                # relevant hotel data are stored as lists
                                hotel_d = [hotel_url, hotel_price, hotel_rating, hotel_review]
                                hotel_data[hotel_name] = hotel_d
                    
            # find the next page in the current region
            page_sublink = page_soup.find('a', {'class':'nav next taLnk ui_button primary'})   

            if page_sublink == None:  # if no more next page available, break
                break

            else:  # get the link for next page in the current region
                page_link = 'https://www.tripadvisor.com' + page_sublink.get('href')
                page_soup = get_trip_soup(page_link)
                
    return hotel_data  # returns a dict of lists


# In[5]:


# Access Google API to get geometry data for sights and hotels, the results are in json format
def get_geometry(place):
    end_point = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    params = {
        'input': place,
        'inputtype': 'textquery',
        'key': API_key,
        'fields': 'geometry'
    }
    req = requests.get(end_point, params = params)
    results = req.json()
    return results


# In[6]:


# access Google Place API to obtain the geometry data of the sights and write all the attributes to a csv file
def request_sight_data():
    google_url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502405%2C2502548%2C4208993%2C4254308%2C4258168%2C4260007%2C4270442%2C4274032%2C4285990%2C4288513%2C4289525%2C4291318%2C4296668%2C4301054%2C4303479%2C4305595%2C4308216%2C4308226%2C4309597%2C4313006%2C4315873%2C4317816%2C4318264%2C4319577%2C4320537%2C4324289%2C4270859%2C4284970%2C4291517%2C4292955%2C4307997&hl=en&gl=us&un=1&otf=1&dest_mid=%2Fm%2F03gh4&dest_state_type=sattd#ttdm=20.321388_-157.381472_7&ttdmf=%252525252Fm%252525252F02lyz9'

    soup = get_trip_soup(google_url)  # get soup data
    sights_all_data = google_data(soup)  # launch the Google data scraper

    for i in sights_all_data:
        out = get_geometry(i)

        lat = out['candidates'][0]['geometry']['location']['lat']
        lng = out['candidates'][0]['geometry']['location']['lng']
        sights_all_data[i].append(lat)
        sights_all_data[i].append(lng)

    # write the dict to a csv file so that source -local can access
    with open("Sights.csv", "w", newline = '', encoding = 'utf-8') as f1:
        csv_output = csv.writer(f1)
        csv_output.writerow(['sight_name', 'sight_rating', 'sight_reviews', 'LAT', 'LNG'])  # attributes write to the csv file
        for key in sights_all_data.keys():
            csv_output.writerow([key] + sights_all_data[key])

    # data modeled as dataframe
    sight_df = pd.read_csv('Sights.csv')        
    return sight_df


# In[7]:


# access Google Place API to obtain the geometry data of the hotels and write all the attributes to a csv file
def request_hotel_data():
    tripadvisor_url = 'https://www.tripadvisor.com/Hotels-g28932-Hawaii-Hotels.html#LEAF_GEO_LIST'
    
    trip_soup = get_trip_soup(tripadvisor_url)  # get soup data
    data = trip_data(trip_soup)  # launch the TripAdvisor data scraper

    for i in data:

        try:
            out = get_geometry(i)
            lat = out['candidates'][0]['geometry']['location']['lat']
            lng = out['candidates'][0]['geometry']['location']['lng']

        # if Google cannot find geometry data for a specific hotel name, that hotel data will be excluded
        except:  
            print('Google cannot find the location info for', i)
            data[i].append(None)
            data[i].append(None)

        else:
            data[i].append(lat)
            data[i].append(lng)

    # write the dict to a csv file so that source -local can access
    with open("Hotels.csv", "w", newline = '', encoding = 'utf-8') as f2:
        csv_output = csv.writer(f2)
        csv_output.writerow(['hotel_name', 'hotel_url', 'hotel_price', 'hotel_rating', 'hotel_review', 'LAT', 'LNG'])  # attributes write to the csv file
        for key in data.keys():
            csv_output.writerow([key] + data[key])

    # data modeled as dataframe
    hotel_df = pd.read_csv('Hotels.csv')     
    return hotel_df


# In[8]:


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-source", choices = ["local", "remote"], help = "where data should be gotten from")
    args = parser.parse_args()
    
    location = args.source

    if location == "local":
        # local mode
        
        # since local doesn't get data from webpages or API, it obtains data from local
        # load local files and model data as dataframe
        sight_df = pd.read_csv('Sights.csv')
        hotel_df = pd.read_csv('Hotels.csv')
        
    else:
        # remote mode
        
        # this code will scrape data from Google and TripAdvisor, then access Google Place API to obtain 
        # geolocation of places, and eventually create two dataframes to hold the sight data and the hotel data. 
        # It will also write the data to two csv data files, so that the local mode can access.
        sight_df = request_sight_data()
        hotel_df = request_hotel_data()
        
    # Milestone 3
        
    # get the z score of the sight review variable
    sight_df['z_sight_review'] = (sight_df['sight_reviews'] - sight_df['sight_reviews'].mean())/sight_df['sight_reviews'].std()
        
    # generate the recommendation metric, taking the product of sight rating and the z score of sight review
    sight_df['rec_sights'] = sight_df['z_sight_review']*sight_df['sight_rating']
        
    # get the z score of the hotel review variable
    hotel_df['z_hotel_review'] = (hotel_df['hotel_review'] - hotel_df['hotel_review'].mean())/hotel_df['hotel_review'].std()
        
    # generate the recommendation metric, taking the product of hotel rating and the z score of hotel review
    hotel_df['rec_hotels'] = hotel_df['z_hotel_review']*hotel_df['hotel_rating']

    # create a html file to store the three interactive maps
    output_file("Hawaii Sights and Hotels.html")

    # set the map at Hawaii (with the geometry data provided), using Google terrain map as tile with a zoom level of 7
    map_options = GMapOptions(lat = 20.716179, lng = -158.214676, map_type = "terrain", zoom = 7)

    # this package takes in ColumnDataSource format, here converts our dataframe to the corresponding format to provide the data sources for plotting
    # sort the sight data by the recommendation metric, and select the 20 most recommended sights
    source1 = ColumnDataSource(sight_df.sort_values(by = ['rec_sights'], ascending = False)[:20])
    source2 = ColumnDataSource(hotel_df)

    # plot Recommended Sights with Hawaii Hotels by Price
        
    # generate a Hawaii base map by making a request to Google MAP API, and specify the title for the map
    p1 = gmap(API_key, map_options, title = "Recommended Sights with Hawaii Hotels by Price")

    # create triangle objects to represent the sights, specifying the geometry data as x- and y-axis,
    # set the color, size of the triangles, also provide a legend to the map
    o1 = p1.triangle(x = "LNG", y = "LAT", size = 9, legend = 'sight', fill_color = "blue", fill_alpha = 0.8, source = source1)
    # add the hovertool so that when the mouse cursor is at a sight, the sight name will be displayed
    p1.add_tools(HoverTool(renderers = [o1], tooltips = [('Sight', '@sight_name')]))

    # specify the color for the hotel circles
    color_mapper_price = LinearColorMapper(palette = 'BuPu9', low = hotel_df['hotel_price'].min(), high = hotel_df['hotel_price'].max())
        
    # create a color bar to indicate the relationship between color and price
    color_bar_price = ColorBar(color_mapper = color_mapper_price, label_standoff = 12, location = (0,0), title = 'Price')
        
    # create circle objects to represent the hotels, specifying the geometry data as x- and y-axis,
    # set the color, size of the circles, also provide a legend to the map
    o2 = p1.circle(x = "LNG", y = "LAT", size = 7, legend = 'hotel', color = transform('hotel_price', color_mapper_price), alpha = 0.8, source = source2)
    # add the hovertool so that when the mouse cursor is at a hotel, the hotel name and lowest price will be displayed
    p1.add_tools(HoverTool(renderers = [o2], tooltips = [('Hotel', '@hotel_name'),
                                                            ('Price', '@hotel_price')]))

    # add a taptool that enable user to click a hotel circle and jump to the hotel webpage in TripAdvisor
    url = '@hotel_url'  # specify the url source in our ColumnDataSource
    tap = TapTool(callback = OpenURL(url = url))  # specify the open link action for this taptool
        
    # avoid the hotel circles being grey out during any interations
    o2.selection_glyph = None
    o2.nonselection_glyph = None
        
    # add the taptool to the plot
    p1.add_tools(tap)

    # add the color bar next to the plot
    p1.add_layout(color_bar_price, 'right')

    # similar to the above, plot Recommended Sights with Hawaii Hotels by Popularity Metric       
    p2 = gmap(API_key, map_options, title = "Recommended Sights with Hawaii Hotels by Popularity Metric")
    o3 = p2.triangle(x = "LNG", y = "LAT", size = 9, legend = 'sight', fill_color = "blue", fill_alpha = 0.8, source = source1)
    p2.add_tools(HoverTool(renderers = [o3], tooltips = [('Sight', '@sight_name')]))
    color_mapper_pop = LinearColorMapper(palette = 'Viridis9', low = hotel_df['hotel_review'].min(), high = hotel_df['hotel_review'].max())
    color_bar_pop = ColorBar(color_mapper = color_mapper_pop, label_standoff = 12, location = (0,0), title = 'Popularity')
    o4 = p2.circle(x = "LNG", y = "LAT", size = 7, legend = 'hotel', color = transform('hotel_review', color_mapper_pop), alpha = 0.8, source = source2)
    p2.add_tools(HoverTool(renderers = [o4], tooltips = [('Hotel', '@hotel_name'),
                                                            ('Price', '@hotel_price')]))
    url = '@hotel_url'
    tap = TapTool(callback = OpenURL(url = url))
    o4.selection_glyph = None
    o4.nonselection_glyph = None
    p2.add_tools(tap)
    p2.add_layout(color_bar_pop, 'right')
        
    # similar to the above, plot Recommended Sights with Hawaii Hotels by Recommendation Metric
    p3 = gmap(API_key, map_options, title = "Recommended Sights with Hawaii Hotels by Recommendation Metric")
    o5 = p3.triangle(x = "LNG", y = "LAT", size = 9, legend = 'sight', fill_color = "blue", fill_alpha = 0.8, source = source1)
    p3.add_tools(HoverTool(renderers = [o5], tooltips = [('Sight', '@sight_name')]))
    color_mapper_pop = LinearColorMapper(palette = 'PiYG9', low = hotel_df['rec_hotels'].min(), high = hotel_df['rec_hotels'].max())
    color_bar_pop = ColorBar(color_mapper = color_mapper_pop, label_standoff = 12, location = (0,0), title = 'Recommendation')
    o6 = p3.circle(x = "LNG", y = "LAT", size = 7, legend = 'hotel', color = transform('rec_hotels', color_mapper_pop), alpha = 0.8, source = source2)
    p3.add_tools(HoverTool(renderers = [o6], tooltips = [('Hotel', '@hotel_name'),
                                                            ('Price', '@hotel_price')]))
    url = '@hotel_url'
    tap = TapTool(callback = OpenURL(url = url))
    o6.selection_glyph = None
    o6.nonselection_glyph = None
    p3.add_tools(tap)
    p3.add_layout(color_bar_pop, 'right')

    # automatically pop up the interactive plots in the browser, displayed in a row
    show(row(p1,p2,p3))
        
    # store all data to two csv files
    sight_df.to_csv("Google_sights_data_complete.csv", index=False)
    hotel_df.to_csv("Hotel_data_complete.csv", index=False)

if __name__ == "__main__":
    main()   


# In[ ]:




