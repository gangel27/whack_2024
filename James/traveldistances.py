import pandas as pd
import openrouteservice as ors

API_Key = "5b3ce3597851110001cf6248bcf2b097e78944ab8ed10b34463e040f"

# Initialize OpenRouteService client with your API key
API_KEY = 'YOUR_OPENROUTESERVICE_API_KEY'
cli = openrouteservice.Client(key=API_KEY)

#Coventry City’s stadium location (latitude, longitude)
coventry_stadium_coords = (52.4481, -1.4944)


# Sample data - replace this with your actual fixture data
data = {
    'Season': ['2020/2021', '2020/2021', '2021/2022'],
    'Match Date': ['2020-09-12', '2020-09-19', '2021-08-14'],
    'Opponent': ['Bristol City', 'Barnsley', 'Nottingham Forest'],
    'Opponent Stadium': [
        'Ashton Gate Stadium, Bristol, UK',
        'Oakwell Stadium, Barnsley, UK',
        'City Ground, Nottingham, UK'
    ],
    'Opponent Coordinates': [
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
fixtures_df = pd.DataFrame(data)

# Function to calculate distance and duration using ORS
def calculate_distance_duration(origin_coords, destination_coords):
    try:
        route = client.directions(
            coordinates=[origin_coords, destination_coords],
            profile='driving-car',
            format='json'
        )
        distance_meters = route['routes'][0]['summary']['distance']  # in meters
        duration_seconds = route['routes'][0]['summary']['duration']  # in seconds
        return distance_meters, duration_seconds / 60  # duration in minutes
    except Exception as e:
        print(f"Error calculating route: {e}")
        return None, None

# Add distance and travel time columns to DataFrame
distances = []
durations = []

for index, row in fixtures_df.iterrows():
    opponent_coords = row['Opponent Coordinates']
    distance, duration = calculate_distance_duration(coventry_stadium_coords, opponent_coords)
    distances.append(distance)
    durations.append(duration)

# Append calculated data to the DataFrame
fixtures_df['Distance from Coventry (meters)'] = distances
fixtures_df['Travel Time (minutes)'] = durations

# Save to CSV
fixtures_df.to_csv('coventry_travel_distances_ors.csv', index=False)

print("Dataset created and saved as 'coventry_travel_distances_ors.csv'")