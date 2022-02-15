[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6685294&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 

## Technical information
### Repository URL
[Repository](https://github.com/ucl-comp0035/comp0034-cw1-g-group-12.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.


## Explaination and evaluation of visulisation designs
Currently, we have included datasets of PM2.5 and PM10 in four locations (London, Manchester, Cardiff and Edinburgh) from 01/01/2020 to 31/12/2020. Therefore, the visualization includes the comparison of air quality in different locations, the comparison of air quality in different time period, and the comparison between different pollutants.

Recall the personas listed in COMP0035. Coursework1 for better explanation of why each visualization is designed and how it satisfied the user requirements.

### Target audience
We have imitated 5 possible personas that are likely to use the ‘open air quality app’ according to the age, occupation, education, etc. The difference in these aspects can lead to the different result of motivation to download the app, goals or objectives to use the app, preferred ways to receive the information from the app, and what’s more, even the challenges the software engineers may face when designing the app. The personas are: commuter, tourist, environmentalist, air forecaster and air quality specialist.

#### Persona 1 --- commuter
<p align="center">
<img width="800" alt="image" src="https://user-images.githubusercontent.com/92019801/138783909-1f019f38-eb66-48b8-8219-dff07ba3bc83.png">

The first broadest user group is commuters, because they have to get to work and get off work every day. For long-term commuting lifestyles, air quality will directly influence people's physical health. At the same time, poor air conditions can also bring a negative impact on mental health. The first persona has shown a commuter at a middle age and with low educational level, who will be interested in the daily matters change. He’s information demonstrated that he may not be able to use and explore software flexibly and is not good at reading complex information, and maybe even need auxiliary information to help his understanding. Therefore, the app page should be made as concise and easy to understand as possible, reduce the provision of complicated information, and describe abstract concepts or diagrams in text to meet the requirements of potential large-scale users with low to secondary education level.

#### Persona 2 --- tourist
<p align="center">
<img width="800" alt="persona2" src="https://user-images.githubusercontent.com/92019801/138785817-34fb9739-3cc7-4eb5-9d1f-d4cc0f6ebf56.png">

The second user group that might be interested in the app are tourists, especially the new generation who are proficient in using software to quickly obtain information they want. Those people are usually university students and young workers who have received higher level education and will have a better understanding to data and graphs. Also, as a tourist, he would like to compare air quality in different cities (even different countries if the app is developed more advanced). The challenge is that he will have more requirements on the app, such as more beautiful color matching, faster information acquisition and higher data accuracy. He likes to use apps such as facebook, ins and twitter, so we can try to place ads on these software to increase exposure to the user group and age period.

#### Persona 3 --- environmentalist
<p align="center">
<img width="800" alt="persona3" src="https://user-images.githubusercontent.com/92019801/138783128-a817141a-8409-4fff-a288-079163b4f3b1.png">

 The third user group is environmentalists like Jennifer. She will have a higher frequency of data updates, in order to take immediate action when air quality declines to get the public's attention. Therefore, for the app design, we need to have a stable and continuous data source, and charts of various pollutant types to make comparison to meet her needs for data diversification.

#### Persona 4 --- air forecaster
<p align="center">
<img width="800" alt="persona4" src="https://user-images.githubusercontent.com/92019801/138784023-0398897c-f4a6-47d0-a716-fcf9343d31f2.png">

 The air forecasters are also considered as a user group. Due to her profession, she has very high standards of data reliability to maintain authority and gain public trust. Therefore, the app design still needs to pay attention to the data update frequency and data accuracy.

#### Persona 5 --- air quality specialist
<p align="center">
<img width="800" alt="persona5" src="https://user-images.githubusercontent.com/92019801/138786087-eb66eb5c-2d83-4a24-b260-8a301f0906de.png">

 The last user group is the air quality specialists. They will use the app when they need data to support their research because our software contains very large databases. They may want to find the trend of air quality in a certain place from historical data, so it will be very helpful for them if the software can produce a graph that shows the change of air quality over a certain period of time. Similarly, due to the needs of scientific research, the accuracy and reliability of the data are very important, and charts should be concise and clear, follows 'less ink' format for report reference.

### Visualization explanation
In this visualization, we have use 3 types of charts to illustrate the data, which are maps (include two types of maps, a scatter mapbox and a density heatmap), gauge charts and a line chart.


#### 1.	Maps
A map is a representation of a complete area or a portion of an area in visual form. A map's work is most commonly used to illustrate geography. Here, we have created two maps for different purposes.

##### Scatter mapbox
<img align="left" width="416" alt="scattermap" src="https://user-images.githubusercontent.com/92019801/154086509-46036151-a88a-4587-ad38-19a15ba9e929.png">

- Target audience:
This graph is prepared for users who are not familiar for with UK geography, the persona that match this situation might be tourists. 

- Questions can be answered from this visualization:
What is the geographic location of each city for the air quality data?   
                                              
- Data needed from the [data set](https://github.com/ucl-comp0035/comp0034-cw1-g-group-12/blob/e068b1540aebd942c2573d84f9d8e117d5b470ef/data/min-max-avg.csv) (***text inside ' ' are the column required from the dataset***):                 
The ’longitude’ and ’altitude’ from the dataset of each city has been used to locate the scatter on the mapbox. Besides, the city name from the ’location’ column in the dataframe is used to input as text above the scatter.

- Type of chart and appropriateness:
The first type of map we created is a scatter map, in this map, each location will be marked as a scatter. It shows the accurate geographic location of cities clearly by with their names labelled in larger font. The available types of maps include choropleth map, bubble map, filled area map, scatter map, density heatmap, etc. Among them, scatter map can be used for only showing the location point without showing the ‘frequency’ of each point. Therefore, it is more suitable than other maps to simply demonstrate the location of cities.

- Visualization evaluation:
The map shows the city locations available under the studied dataset, providing a more direct presentation of the geography to users. But there are many similarities with the density heatmap, the map and density heatmap can be merged further to improve the direct visualization to users and save the time for users to read multiple visualizations.

##### Density heatmap
<img align="right" width="450" alt="density heatmap" src="https://user-images.githubusercontent.com/92019801/154085781-ae85407d-40ab-4f86-a35c-0e53484186c5.png">

- Target audience:   
The graph is prepared for users who are interested and want to compare air quality in multiple locations, including tourists (they may decide their travel destination based on which city has better air quality) and environmentalists (they may launch calls and campaigns to reduce pollution in heavily polluted areas).

- Questions can be answered from this visualization:  
Which location has the most serious air pollution and which location has the least in a certain day? Does this location always have higher/lower air pollution than other cities or their rankings change everyday? 
(further research 1: Are there any potential relationship between the air quality and regional development? e.g. more developed areas have higher air quality index) (further research 2: Are there any potential relationship between the air quality and the geographical location? e.g. areas in higher altitude or near the coast will have better air quality)

- Data needed from the [data set](https://github.com/ucl-comp0035/comp0034-cw1-g-group-12/blob/e068b1540aebd942c2573d84f9d8e117d5b470ef/data/min-max-avg.csv) (***text inside ' ' are the column required from the dataset***):              
As it is also a form of map, the ’longitude’ and ’altitude’ from the dataset has been used to locate the cities. Besides, there is a time selection box on the top of the graph for users to select the day they want to check the air quality, so the ‘utc’ in the dataset is used as input to the date picker. Furthermore, it is a density map to demonstrate the pollution severity of different areas, where the severity is represented by the colour of the circle. So the values of PM2.5 and PM10 from the dataset is required. Mathematical operation has been done to sum and average the daily PM2.5 and PM10 pollutants amount as ‘total (avg)’ to show the general air pollution degree of the area. For example, on this graph, Edinburgh on the day of 01/01/2020 has the least total pollutants amount and has better air quality than other cities.

- Type of chart and appropriateness:   
This map is a density heatmap, in this case, it is a map used to find the density of air pollution across cities. The available types of maps that can describe the ‘density’ of objects also include choropleth map, bubble map and hexbin map. After comparison, it is found that the choropleth map is only very detailed and accurate to the division of each state area when displaying the ‘usa’ map. However, there is no ‘uk’ option in the map display, you can only choose either 'europe' or 'world' to find the location of UK. Nevertheless, in that way the scope of the map will be very large and not detailed, and it cannot be accurate to the division of each district of the UK, so it is not suitable for the current situation that we have only included UK local air quality data. For the bubble map, it has the same problem of regional inaccuracies as the choropleth map, and the bubbles will clutter the map and make it harder to get useful information. As for the hexbin map, it can show the "density" of an area through hexagons. It is a rarely seen chart style, which may be difficult to be understood by the public and does not achieve a more intuitive data visualization. Therefore, leaving the density heatmap as the most appropriate and acceptable map format.

- Visualization evaluation:   
The map shows the city locations available under the studied dataset as well as the air pollution information. Though there are many similarities with the scatter map. As mentioned before, these two maps can be merged further to improve the quality of the visualization. Furthermore, the total number of PM2.5 and PM10 cannot sufficiently illustrate the air quality. For improvements, the Air Quality Index (AQI) can be introduced in the density heatmap when more pollutant options are added to the dataset and visualizations in the future.

#### 2.	Gauge chart
<p align="center">
<img width="800" alt="gauge chart" src="https://user-images.githubusercontent.com/92019801/154086186-ca935ca4-bfe7-4655-93d7-32dfbfabb7e7.png">

- Target audience:   
This graph is designed for users who want to check the daily maximum/minimum/average air quality and relevant suggestions. Therefore, the commuters will be most interested in this graph (they may consider whether to wear some protective measures based on the daily pollution situation).

- Questions can be answered from this visualization:     
What is the daily maximum, minimum and average values of each pollutant? Which takes a larger portion and contribute more to the air pollution? What is the daily air quality condition, is it good or poor? How much air quality index is considered as good air quality and how much is poor? Are there any relevant comment and suggestions can be provided to users based on the air quality index?

- Data needed from the [data set](https://github.com/ucl-comp0035/comp0034-cw1-g-group-12/blob/8220cb9641edaf484c9e7ef0a607e49d5e3326c2/data/all.csv) (***text inside ' ' are the column required from the dataset***):     
To answer the above questions we all need ‘utc’ from the dataset as input to the date picker to select a specific day, ‘location’ to input into the area selection box to select a specific city, and parameter values of 'PM2.5' and 'PM10' to plot the gauge graph. coding has also been done to search and calculate maximum, minimum and mean values of the daily PM2.5 and PM10 amount.

- Type of chart and appropriateness:   
To answer the first questions, both bar chart or line chart can achieve the purpose. However, since both bar chart and line chart will require user to find the max/min value by themself from reading the peak/valley of the chart, it is not time efficient and does not fulfill the aim of the visualization to get useful information quickly. Therefore, as a substitute, a gauge chart is used to directly display the average daily pollutant amount. What’s more, a gauge chart can divide its range into different sections with different colors to demonstrate the level of pollutant amount. For example, in the chart above, the PM2.5 indicator is pointed at 19 which located in the yellow region, means ‘moderate’ amounts of PM2.5 and will not cause serious harm to human body. The division of colors in the gauge chart allows users to directly obtain the degree of air quality today as an answer to the second question, without the need to add additional descriptions like in bar chart or line chart to describe the quality of the air. Besides, since the gauge chart will only point the average value, a card with stated maximum and minimum values is also added under each gauge chart. We have also considered users who may not receive high education, comments and recommendations to every corresponding air quality condition are given near the charts as feedback.

<br />
- Visualization evaluation:  
The gauge chart shows the degree of the air pollution using different colors. Users can directly know the level of air pollution and the average pollution value from the chart, but the exact real-time value is not displayed on the gauge chart. Additional information such as minimum, maximum, and average values are given below the graph. The chart can be improved to update the current data in real time in the future, to give the user the most accurate and useful travel advice.

#### 3.	Scatter chart
<p align="center">
<img width="800" alt="scatter chart" src="https://user-images.githubusercontent.com/92019801/154085826-47eb9bc4-46b5-4089-a6b1-04b62987b223.png">
 
- Target audience:  
The graph is designed for users who want to know the variation of air quality, such as air quality specialists (they may want to investigate and summarize the rule of variation), air forecaster (they may want to predict the future air quality from the past years’ variation trend) and tourists (they may want to find the time period with best air quality at their destination and plan their travel time).

- Questions can be answered from this visualization:  
What time of a day is the air pollution most serious in each location? Do they have a similar daily variation trend or different? (further research: Are there any potential relationship between the air quality and daily life? e.g. air quality index is higher during the factories operating time)What is the long-term/annual air quality trend? (further research: Are there any potential relationship between the air quality and the season and climate?)

- Data needed from the [data set](https://github.com/ucl-comp0035/comp0034-cw1-g-group-12/blob/8220cb9641edaf484c9e7ef0a607e49d5e3326c2/data/all.csv) (***text inside ' ' are the column required from the dataset***):
The questions are about the air quality variation on the time scale in different area. Hence, ‘utc’ is required as input to the date picker to select the start and end dates, ‘location’ is required as input to the area selection box to select the city, names and valuess of parameter ‘PM2.5’ and ‘PM10’ are required as input to the pollutant selection box and to plot the chart.

- Type of chart and appropriateness:  
To generate a graph that can demonstrate the variation of data, usually a bar chart or a line chart will be used. But because the range of the independent variable could be hundreds of data if a long-term time scale variation is selected, the bar chart would be not suitable to view the trend because hundreds of bars will mess up the chart. In that case, line chart may be more appropriate to show the overall trend of air quality variation, both in the short and long term. Nevertheless, the dataset we downloaded from the database website is not continuous, there may contain missing values on a certain day, but the line chart will automatically connect two adjacent data which means the missing values cannot be correctly shown (for example, we have data on Jan.1st and Jan.3rd but no data for Jan.2nd, line chart will connect the data on Jan.1st and Jan.3rd, then the chart will look like there is data on Jan.2nd instead of indicating it is empty). Therefore, in order to correctly represent days without numerical values on the chart, scatter chart is used as a substitute to the line chart. The scatter chart can also demonstrate the trend of data and leave empty space if the data is not available, which fits our expectation.

- Visualization evaluation:  
This visualization shows the changes in PM2.5 and PM10 for cities within the selected period in the dataset, and users can read its trends from it. The downside of this chart is the variety of options available when comparing trends across different cities, and the chart can be improved by adding comparisons for any number of cities rather than just one selected city with London.

### Visual Aspects of the Design
Regarding the overall layout of the dash app, the `MINTY` stylesheet was chosen. Its main color and styles are in line with the aesthetics of contemporary users of all ages, focusing on the simplicity for users to obtain their desired information more efficiently and more easily. The use of tabs to separate different visualizations ease the user operations and allows users to find the specific information they need faster. For the scatter map, the chart is generated by the scatter mapbox in ‘plotly.graph_objects’, different marker colours with labelled city names are included. The density heatmap is created by the px.density_mapbox in `plotly.express`, the mapbox style is selected to be `stamen-watercolor`, because after comparison, this map style is more tidy than other styles, it will not appear cluttered when displaying density circles, and the color matching is brighter, which is easier to attract the user's attention. The gauge chart used is the default Gauge in `dash_daq` with the different color illustrating the degree of the air pollution. The scatter chart is implemented using the scatter diagram in `plotly.graph_objects` with different color to differ the cities.





## Creation of the Ploty Dash app containing the visulisations
[dash app](dash_app.py)

 
 
## Evidence of the appropriate use of software engineering and data science tools
[Linter](https://github.com/ucl-comp0035/comp0034-cw1-g-group-12/blob/master/.github/workflows/pylint.yml) 

### Requirements
Install [required python packages](https://github.com/ucl-comp0035/comp0034-cw1-g-group-12/blob/f4db97fba13e5b1f6140233a5bae3a69e160e02f/requirements.txt) from the library before running the code.
 
#### Users stories
The user stories that have been met in this visulization are listed below:
| No. | Persona | User Stories | Priority |
| :---: | :---: | --- | :---: |
| 1 | Commutor | As a website user, I want to see the air quality change throughout the day. | Must have | 
| 2 | Commutor | As a website user, I want to be provided some suggested measures based on the data, so as to reduce the thinking time I need to spend when looking at the data. | Could have |  
| 3 | Commutor | As a website user, I want to be able to see the maximum and minimum values of daily data so that I can make a rough assessment of the range of changes in air quality each day. | Could have |    
| 4 | Environmentalist | As a website user, I want to see the data of different pollutants so that I can find which contributed most to the air pollution. | Must have |    
| 5 | Air quality specialist | As a website user, I want to compare the data throughout months or years so that I can find the law of change. | Should have |  
| 6 | Developer | As a developer, I want to use a web browser as its user interface. | Must have |   
| 7 | Developer | As a developer, I want the web design program shall be written using standard python to run on different operation system. | Must have |



## Instructions for using the starter code

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
   or [Cloning a repository in VS Code](https://code.visualstudio.com/docs/editor/github#_cloning-a-repository)
2. Add a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [use python in your shell.](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. PyCharm, VisualStudio Code, Xcode and NetBeans have
   already been added.
5. Copy the prepared data set from COMP0035 coursework to this repository. You may need to use 'git add' to add the file
   to be tracked by git.
6. Commit and push the data set to GitHub. This is your first commit for coursework 1. Remember to use source code
   control throughout the coursework.
7. `dash_app.py` has been included to allow you to test that your project set up is sufficient to run Dash. Once you are
   happy that you have set up the project then you should delete the contents of app.py and replace with your coursework
   code.
    - To run the dash app from the terminal or shell make sure you are in directory of your repository and type and
      run `python dash_app.py`
    - To run the dash app from PyCharm, right click on the file name `dash_app.py` in the Project pane and
      select `Run dash_app`. Or open `dash_app.py` and click on the green run arrow near line 29.
    - To run the dash app from VS Code, use the Run option from the left pane.
8. By default, the dash app should launch on port 8050 of your localhost with the IP
   address [127.0.0.1:8050](http://127.0.0.1:8050/). Open the URL in a browser. Note: If you get an error like
   this: `OSError: [Errno 48] Address already in use` then another application is already using the default port (this
   will also happen if you forget to stop a previous Dash app and try to start another!). You can try another port by
   modifying the line of code that runs the Dash app to specify a different port number
   e.g. `app.run_server(debug=True, port=1337)`
