import pandas as pd
import googlemaps as gmaps
import matplotlib.pyplot as plt
import numpy as np
import pearsonr
import math

def addCommuteToDataFrame():
    # Initialize OpenRouteService client with your API key
    API_KEY = 'AIzaSyBGxmBxWKzk5l61JirnnpHFA9dakZD0cjI'
    cli = gmaps.Client(key=API_KEY)

    #Coventry City’s stadium location (latitude, longitude)
    coventry_stadium_coords = (52.4481, -1.4944)


    # Sample data - replace this with your actual fixture data
    opponent_stadium_data = {
        'Opponent_Stadium_Coordinates': [
            (52.0098, -0.7335),    # Stadium MK, MK Dons
            (51.4390, -2.6209),   # Ashton Gate, Bristol
            (51.38468167414515, 0.5617073688951303), #Gillingham
            (53.55244175289766, -1.467708650287881), #Barnsley
            (51.49094806427966, -0.2888447288699287), #Brentford
            (54.57829568503369, -1.2168904442113437), #Middlesborough
            (52.939937009912484, -1.1328459712165433), #Nottingham Forrest
            (51.650120437239465, -0.40159779285842023), #Watford
            (52.62218834093488, 1.3091125096855423), #Norwich
            (52.92058941762811, -1.4469649772043025), #Derby
            (51.63136151120107, -0.8003533423807407), #Wycombe Wanderers
            (53.411564190680394, -1.5006868344794106), #Sheff Wed
            (53.772563782819255, -2.6884375622640664), #PNE
            (52.62218834093488, 1.3091125096855423), #Norwich
            (51.4870229876299, -0.05084635802115084), #Millwall
            (51.42257470503287, -0.9826389072904965), #Reading
            (52.47583788238037, -1.8680828286532856), #Birmingham City
            (51.47296417372802, -3.2030128423589277), #Cardiff
            (51.642956098962756, -3.93455699513681), #Swansea
            (53.728889832697206, -2.4891047981981433), #Blackburn Rovers
            (51.88445521216652, -0.43175535579731544), #Luton
            (51.5094888169521, -0.2321485562912954), #QPR
            (50.73502386073819, -1.8391337556946), #Bournemouth
            (53.42715265450986, -1.3630106712208971), #Rotherham
            (52.988275303354676, -2.176215994824261), #Stoke
            (53.65441572847847, -1.7682946153763444), #Huddersfield
            (53.55244175289766, -1.467708650287881), #Barnsley
            (53.805576443544375, -3.0493753965801154), #Blackpool
            (51.5094888169521, -0.2321485562912954), #QPR
            (51.4870229876299, -0.05084635802115084), #Millwall
            (51.88445521216652, -0.43175535579731544), #Luton
            (53.728889832697206, -2.4891047981981433), #Blackburn Rovers
            (53.772563782819255, -2.6884375622640664), #PNE
            (53.746143815707526, -0.3680872151387129), #Hull
            (53.411564190680394, -1.5006868344794106), #Sheff Wed
            (50.73502386073819, -1.8391337556946), #Bournemouth
            (53.65441572847847, -1.7682946153763444), #Huddersfield
            (52.5665929188481, -0.2402491780917818), #Peterborough
            (54.57829568503369, -1.2168904442113437), #Middlesborough
            (51.42257470503287, -0.9826389072904965), #Reading
            (51.47296417372802, -3.2030128423589277), #Cardiff
            (51.44037240446043, -2.6203341002093734), #Bristol City
            (51.642956098962756, -3.93455699513681), #Swansea
            (52.92058941762811, -1.4469649772043025), #Derby
            (52.939937009912484, -1.1328459712165433), #Nottingham Forrest
            (51.47939074246434, -0.22229444716638527), #Fulham
            (52.47583788238037, -1.8680828286532856), #Birmingham City
            (52.509540719195165, -1.9638315955415677), #West Brom
            (50.90603309912257, -1.3902261745269902), #Southampton
            (52.988275303354676, -2.176215994824261), #Stoke
            (54.91470900546442, -1.3883066270216171), #Sunderland
            (51.4870229876299, -0.05084635802115084), #Millwall
            (53.746143815707526, -0.3680872151387129), #Hull
            (52.62218834093488, 1.3091125096855423), #Norwich
            (51.88445521216652, -0.43175535579731544), #Luton
            (52.47583788238037, -1.8680828286532856), #Birmingham City
            (51.44037240446043, -2.6203341002093734), #Bristol City
            (51.47296417372802, -3.2030128423589277), #Cardiff
            (52.988275303354676, -2.176215994824261), #Stoke
            (51.650120437239465, -0.40159779285842023), #Watford
            (51.42257470503287, -0.9826389072904965), #Reading
            (53.370723563651154, -1.470971886533067), #Sheffield United
            (53.7893039075538, -2.2303050172369403), #Burnley
            (52.509540719195165, -1.9638315955415677), #West Brom
            (53.42715265450986, -1.3630106712208971), #Rotherham
            (53.772563782819255, -2.6884375622640664), #PNE
            (53.65441572847847, -1.7682946153763444), #Huddersfield
            (53.5478180452599, -2.654100508758006), #Wigan
            (53.805576443544375, -3.0493753965801154), #Blackpool
            (51.642956098962756, -3.93455699513681), #Swansea
            (51.5094888169521, -0.2321485562912954), #QPR
            (53.728889832697206, -2.4891047981981433), #Blackburn Rovers
            (54.57829568503369, -1.2168904442113437), #Middlesborough
            (54.57829568503369, -1.2168904442113437), #Middlesborough
            (52.62051600806496, -1.142232415497442), #Leicester
            (51.43164003315739, -0.18668710010931702), #Wimbledon
            (51.642956098962756, -3.93455699513681), #Swansea
            (53.746143815707526, -0.3680872151387129), #Hull
            (51.47296417372802, -3.2030128423589277), #Cardiff
            (51.5094888169521, -0.2321485562912954), #QPR
            (51.44037240446043, -2.6203341002093734), #Bristol City
            (53.42715265450986, -1.3630106712208971), #Rotherham
            (53.772563782819255, -2.6884375622640664), #PNE
            (51.4870229876299, -0.05084635802115084), #Millwall
            (52.05568594015561, 1.1460875189382713), #Ipswich
            (53.77814724006821, -1.5721733411413423), #Leeds
            (54.91470900546442, -1.3883066270216171), #Sunderland
            (54.57829568503369, -1.2168904442113437), #Middlesborough
            (53.411564190680394, -1.5006868344794106), #Sheff Wed
            (53.411564190680394, -1.5006868344794106), #Sheff Wed
            (52.62218834093488, 1.3091125096855423), #Norwich
            (50.38848096615988, -4.151935238139904), #Plymouth
            (52.988275303354676, -2.176215994824261), #Stoke
            (52.509540719195165, -1.9638315955415677), #West Brom
            (51.650120437239465, -0.40159779285842023), #Watford
            (52.59038681463103, -2.1304546320468467), #Wolves
            (53.65441572847847, -1.7682946153763444), #Huddersfield
            (50.90603309912257, -1.3902261745269902), #Southampton
            (52.47583788238037, -1.8680828286532856), #Birmingham City
            (53.46351738535478, -2.2915410881057534), #Manchester United
            (53.728889832697206, -2.4891047981981433), #Blackburn Rovers
        ]
    }

    # Convert data to DataFrame
    opponent_stadium_data_df = pd.DataFrame(opponent_stadium_data)

    # Function to calculate distances from the origin to a list of destinations
    def calculate_distances(origin, destinations):
        results = []
        # Batch the destinations into groups of 10 to get around the 10 origins - 10 destinatons request dimension limit
        for i in range(0, len(destinations), 10):
            batch = destinations[i : i + 10]
            # Perform the Distance Matrix API request
            result = cli.distance_matrix(origins=origin, destinations=batch, mode="driving")
            results.extend(result['rows'][0]['elements'])
        
        return results
        
    # Getting the distances calculated by the google maps distance matrix API
    distances = calculate_distances(coventry_stadium_coords, opponent_stadium_data_df['Opponent_Stadium_Coordinates'])
    distances_df = pd.DataFrame(distances)

    # The distance matrix API returned a field containing a dictionary so the lambda function only keeps
    # the values that I'm interested in out of that field
    distancesAlone_df = (distances_df['distance'].apply(lambda x: x['value']))

    #Make a dataframe out of the data in the supplied csv file
    csv_file_path = './CCFC_match_lineups_data.csv'
    overall_df = pd.dataframe = pd.read_csv(csv_file_path)

    #Only keep the data on away matches
    awayMatches_df = overall_df[overall_df.location == "away"]

    #Adds the distances to the main dataframe as a new column
    awayMatches_df['Commute'] = distancesAlone_df.values

    #print(awayMatches_df['Commute'].sum()) - for the climate change calculations
    return awayMatches_df

def distanceCommuteScatterGraph(dframe): 
    #Using the fact that NaN != Nan to filter out rows that have NULL Distance values
    am = dframe.query('Distance == Distance')[['opposition_team', 'Distance', 'Commute']]

    #A Scatter Plot of Commute vs The distance that players ran during games
    plt.figure()
    plt.scatter(am['Distance'], am['Commute'], label = 'Data Points', alpha = 0.8)

    # Calculate, and plot the regression line
    m, b = np.polyfit(am['Distance'], am['Commute'], 1)
    reg = f"y = {m : .1f}x + {b : .1f}"
    plt.plot(am['Distance'], m * am['Distance'] + b, color = 'red', label = 'Regression Line', alpha = 1)

    # Calculate the PMCC and p value
    pmcc, p = pearsonr.pearsonr(am['Distance'], am['Commute'])

    # Adding a title, labels, the regression line, pmcc and p value, and a legend/key to the graph
    plt.title('Scatter Plot to show the effect that the commute to a football ground has on the distance traveled by the players during the match'.title())
    plt.xlabel('Distance')
    plt.ylabel('Commute')
    plt.text(x = 0.05, y = 0.90, s = reg, fontsize = 12, ha = 'left', va = 'top', transform = plt.gca().transAxes)
    plt.text(x = 0.05, y = 0.85, s = f"PMCC = {pmcc : .2f}", fontsize = 12, ha = 'left', va = 'top', transform = plt.gca().transAxes)
    plt.text(x = 0.05, y = 0.80, s = f"p = {p : .2f}", fontsize = 12, ha = 'left', va = 'top', transform = plt.gca().transAxes)
    plt.legend()

    #Storing the graph inside of a file
    plt.savefig("distance-commute-scatter.png", dpi=300, bbox_inches='tight')
    # Showing the graph
    #plt.show()

def hsrAndSprintsCommitScatterGraph(dframe):

    #Filtering out rows that have NULL HSR values
    am = dframe[['opposition_team', 'HSR', 'Sprint', 'Commute']]

    #A Scatter Plot of Commute vs The distance that players ran during games between HSR and Sprints
    fig = plt.figure()
    sfig1 = fig.add_subplot(2, 1, 2)
    sfig2 = fig.add_subplot(2, 1, 1)
    sfig1.scatter(am['Commute'], am['HSR'], label = 'Data Points', alpha = 0.8)
    sfig2.scatter(am['Commute'], am['Sprint'], label = 'Data Points', alpha = 0.8)

    # Calculate, and plot the regression lines for the two graphs
    m1, b1 = np.polyfit(am['Commute'], am['HSR'], 1)
    reg1 = f"y = {m1 : .1f}x + {b1 : .1f}"
    sfig1.plot(am['Commute'], m1 * am['Commute'] + b1, color = 'red', label = 'Regression Line', alpha = 1)

    m2, b2 = np.polyfit(am['Commute'], am['Sprint'], 1)
    reg2 = f"y = {m2 : .1f}x + {b2 : .1f}"
    sfig2.plot(am['Commute'], m2 * am['Commute'] + b2, color = 'red', label = 'Regression Line', alpha = 1)

    # Calculate the PMCC and p values for the two graphs
    pmcc1, p1 = pearsonr.pearsonr(am['Commute'], am['HSR'])
    pmcc2, p2 = pearsonr.pearsonr(am['Commute'], am['Sprint'])

    fsize = 12 #setting the font size

    # Adding a title, labels, the regression line, pmcc and p value, and a legend/key to the two graphs
    sfig1.set_title('Commute Vs HSR'.title())
    sfig1.set_xlabel('Commute(m)')
    sfig1.set_ylabel('HSR Distance(m)')
    #sfig1.text(x = 0.01, y = 0.95, s = reg1, fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    sfig1.text(x = 0.01, y = 0.95, s = f"PMCC = {pmcc1 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    sfig1.text(x = 0.01, y = 0.85, s = f"p = {p1 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    sfig1.legend()

    sfig2.set_title('Commute Vs Sprints'.title())
    sfig2.set_xlabel('Commute(m)')
    sfig2.set_ylabel('Sprint Distance(m)')
    #sfig2.text(x = 0.01, y = 0.95, s = reg2, fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.text(x = 0.01, y = 0.95, s = f"PMCC = {pmcc2 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.text(x = 0.01, y = 0.85, s = f"p = {p2 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    # sfig2.legend()

    #Setting the super-title of the two-graph figure
    fig.suptitle("Graphs showing the effect that commuting to a stadium has on movement speed".title())
    
    fig.tight_layout() #automatically spreads the graphs apart so that they don't overlap

    #Storing the graph inside of a file
    fig.savefig("hsr-sprint-commute-scatter.png", dpi=300, bbox_inches='tight')

    # Showing the graph
    #fig.show()

def xgToCommuteScatterGraph(dframe):

    #Filtering out rows that have NULL values
    am = dframe[['opposition_team', 'np_xg', 'np_xg_conceded', 'Commute']]

    #A Scatter Plot of Commute vs win condition performance
    fig = plt.figure()
    sfig1 = fig.add_subplot(2, 1, 1)
    sfig2 = fig.add_subplot(2, 1, 2)
    sfig1.scatter(am['Commute'], am['np_xg'], label = 'Data Points', alpha = 0.8)
    sfig2.scatter(am['Commute'], am['np_xg_conceded'], label = 'Data Points', alpha = 0.8)

    # Calculate, and plot the regression lines for the two graphs
    m1, b1 = np.polyfit(am['Commute'], am['np_xg'], 1)
    reg1 = f"y = {m1 : .1f}x + {b1 : .1f}"
    sfig1.plot(am['Commute'], m1 * am['Commute'] + b1, color = 'red', label = 'Regression Line', alpha = 1)

    m2, b2 = np.polyfit(am['Commute'], am['np_xg_conceded'], 1)
    reg2 = f"y = {m2 : .1f}x + {b2 : .1f}"
    sfig2.plot(am['Commute'], m2 * am['Commute'] + b2, color = 'red', label = 'Regression Line', alpha = 1)

    # Calculate the PMCC and p values for the two graphs
    pmcc1, p1 = pearsonr.pearsonr(am['Commute'], am['np_xg'])
    pmcc2, p2 = pearsonr.pearsonr(am['Commute'], am['np_xg_conceded'])

    fsize = 12 #setting the font size

    # Adding a title, labels, the regression line, pmcc and p value, and a legend/key to the two graphs
    sfig1.set_title('Commute Vs xG')
    sfig1.set_xlabel('Commute(m)')
    sfig1.set_ylabel('xG')
    #sfig1.text(x = 0.01, y = 0.95, s = reg1, fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    sfig1.text(x = 0.01, y = 0.95, s = f"PMCC = {pmcc1 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    sfig1.text(x = 0.01, y = 0.85, s = f"p = {p1 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    #sfig1.legend()

    sfig2.set_title('Commute Vs xG Against')
    sfig2.set_xlabel('Commute(m)')
    sfig2.set_ylabel('xG Against')
    #sfig2.text(x = 0.01, y = 0.95, s = reg2, fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.text(x = 0.01, y = 0.95, s = f"PMCC = {pmcc2 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.text(x = 0.01, y = 0.85, s = f"p = {p2 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.legend()

    #Setting the super-title of the two-graph figure
    fig.suptitle("Graphs showing the effect that commuting to a stadium has on the win condition performance".title())
    
    fig.tight_layout() #automatically spreads the graphs apart so that they don't overlap

    #Storing the graph inside of a file
    fig.savefig("xG-commute-scatter.png", dpi=300, bbox_inches='tight')

    # Showing the graph
    #fig.show()

def goalsToCommuteScatterGraph(dframe):
    #Filtering out rows that have NULL values
    am = dframe[['opposition_team', 'goals_scored', 'goals_conceded', 'Commute']]

    # A Scatter Plot of Commute vs actual win condition performance
    fig = plt.figure()
    sfig1 = fig.add_subplot(2, 1, 1)
    sfig2 = fig.add_subplot(2, 1, 2)
    sfig1.scatter(am['Commute'], am['goals_scored'], label = 'Data Points', alpha = 0.8)
    sfig2.scatter(am['Commute'], am['goals_conceded'], label = 'Data Points', alpha = 0.8)

    # Calculate, and plot the regression lines for the two graphs
    m1, b1 = np.polyfit(am['Commute'], am['goals_scored'], 1)
    reg1 = f"y = {m1 : .1f}x + {b1 : .1f}"
    sfig1.plot(am['Commute'], m1 * am['Commute'] + b1, color = 'red', label = 'Regression Line', alpha = 1)

    m2, b2 = np.polyfit(am['Commute'], am['goals_conceded'], 1)
    reg2 = f"y = {m2 : .1f}x + {b2 : .1f}"
    sfig2.plot(am['Commute'], m2 * am['Commute'] + b2, color = 'red', label = 'Regression Line', alpha = 1)

    # Calculate the PMCC and p values for the two graphs
    pmcc1, p1 = pearsonr.pearsonr(am['Commute'], am['goals_scored'])
    pmcc2, p2 = pearsonr.pearsonr(am['Commute'], am['goals_conceded'])

    fsize = 12 #setting the font size

    # Adding a title, labels, the regression line, pmcc and p value, and a legend/key to the two graphs
    sfig1.set_title('Commute Vs Goals Scored')
    sfig1.set_xlabel('Commute(m)')
    sfig1.set_ylabel('Goals Scored')
    #sfig1.text(x = 0.01, y = 0.95, s = reg1, fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    sfig1.text(x = 0.01, y = 0.95, s = f"PMCC = {pmcc1 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    sfig1.text(x = 0.01, y = 0.85, s = f"p = {p1 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig1.transAxes)
    #sfig1.legend()

    sfig2.set_title('Commute Vs Goals Against')
    sfig2.set_xlabel('Commute(m)')
    sfig2.set_ylabel('Goals Against')
    #sfig2.text(x = 0.01, y = 0.95, s = reg2, fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.text(x = 0.01, y = 0.95, s = f"PMCC = {pmcc2 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.text(x = 0.01, y = 0.85, s = f"p = {p2 : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = sfig2.transAxes)
    sfig2.legend()

    #Setting the super-title of the two-graph figure
    fig.suptitle("Graphs showing the effect that commuting to a stadium has on the actual win condition performance".title())
    
    fig.tight_layout() #automatically spreads the graphs apart so that they don't overlap

    #Storing the graph inside of a file
    fig.savefig("goals-commute-scatter.png", dpi=300, bbox_inches='tight')

    # Showing the graph
    #fig.show()

def commuteAvgPoints(dframe):

    # Only selecting the columns that I need for performance reasons
    am = dframe[['opposition_team','Commute','match_outcome']]
    

    # Using a lambda function to add a points column according to the outcome of matches
    am['Points'] = am['match_outcome'].apply(lambda x : 3 \
                                   if x == 'won' else (1 \
                                                  if x == 'draw' else 0))
    
    #Makes a dictionary where the keys are a commute distance range and the values are
    #the corresponding points per game
    dic = {}
    dic1 = {}
    for i in range(0, am['Commute'].max(), 20000):
        amState = am.query('@i <= Commute and @i + 20000 > Commute')
        j = round(i / 1000)
        dic[f"{j} - {j + 20}"] = amState['Points'].sum() / amState['Points'].count()
        dic1[j + 10] = ""

    #Then makes a dataframe out of it
    amProcessed = pd.DataFrame({'Commute_Range' : dic.keys(), 'Commute_Avg' : dic1.keys(), 'PPG' : dic.values()})
    
    # #With dic1 had to do something different to make a regression line for the bar chart
    # amProcessedRegLine = pd.DataFrame({Commute_avg : dic1.keys(), 'PPG'})
    amProcessed_clean = amProcessed.dropna()

    plt.figure()
    plt.bar(amProcessed_clean['Commute_Range'], amProcessed_clean['PPG'], color = 'skyblue', width = 0.3)

    # m, b = np.polyfit(amProcessed_clean['Commute_Avg'], amProcessed_clean['PPG'], 1)
    # plt.plot(amProcessed_clean['Commute_Avg'], m * amProcessed_clean['Commute_Avg'] + b, color = 'red', label = 'Regression Line', alpha = 1)

    pmcc, p = pearsonr.pearsonr(am['Commute'], amProcessed_clean['PPG'])
    fsize = 12

    plt.xticks(rotation = 45)
    plt.xlabel('Commute Distance(km)')
    plt.ylabel('Points Per Game')
    plt.text(x = 0.01, y = 0.95, s = f"PMCC = {pmcc : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = plt.gca().transAxes)
    plt.text(x = 0.01, y = 0.90, s = f"p = {p : .2f}", fontsize = fsize, ha = 'left', va = 'top', transform = plt.gca().transAxes)
    plt.title('Bar Chart of Commute distance vs points per game'.title())
    plt.legend()
    plt.savefig("commute-ppg-bar2.png", dpi=300, bbox_inches='tight')
    plt.show




awayMatches_df = addCommuteToDataFrame()
awayMatches_df_clean = awayMatches_df.dropna()
#distanceCommuteScatterGraph(awayMatches_df_clean)
#hsrAndSprintsCommitScatterGraph(awayMatches_df_clean)
#xgToCommuteScatterGraph(awayMatches_df_clean)
#goalsToCommuteScatterGraph(awayMatches_df_clean)
commuteAvgPoints(awayMatches_df_clean)