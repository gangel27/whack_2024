import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


p = [3061, 3299, 3317, 3355, 3386, 3743, 4179, 4365, 4576, 7537, 7847]
t = "Barnsley"

model_path = "../George/Models/first_model.pth"

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available() else "cpu"
)


class SimpleModel(nn.Module):
    def __init__(self, input_size=90, hidden_size=128, output_size=3):
        super(SimpleModel, self).__init__()

        # Define layers
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x


class Integration:
    def __init__(self, team, player_ids, home):
        self.players = [
            3061,
            3299,
            3317,
            3355,
            3386,
            3743,
            4179,
            4365,
            4576,
            7537,
            7847,
            8998,
            9276,
            9422,
            9709,
            10026,
            10028,
            10460,
            10781,
            13247,
            15304,
            15542,
            15811,
            19425,
            22008,
            22361,
            23399,
            29040,
            29363,
            29397,
            29405,
            29407,
            29659,
            29839,
            30077,
            31088,
            32261,
            32685,
            35241,
            35708,
            36075,
            38531,
            39092,
            41508,
            42693,
            42928,
            47879,
            48708,
            49458,
            56408,
            134012,
            137710,
        ]
        self.teams = [
            "AFC Bournemouth",
            "Barnsley",
            "Birmingham City",
            "Blackburn Rovers",
            "Blackpool",
            "Brentford",
            "Bristol City",
            "Burnley",
            "Cardiff City",
            "Derby County",
            "Fulham",
            "Huddersfield Town",
            "Hull City",
            "Ipswich Town",
            "Leeds United",
            "Leicester City",
            "Luton Town",
            "Middlesbrough",
            "Millwall",
            "Norwich City",
            "Nottingham Forest",
            "Peterborough United",
            "Plymouth Argyle",
            "Preston North End",
            "Queens Park Rangers",
            "Reading",
            "Rotherham United",
            "Sheffield United",
            "Sheffield Wednesday",
            "Southampton",
            "Stoke City",
            "Sunderland",
            "Swansea City",
            "Watford",
            "West Bromwich Albion",
            "Wigan Athletic",
            "Wycombe Wanderers",
        ]

        self.model = SimpleModel().to(device)
        self.model.eval()
        optimizer = optim.Adam(self.model.parameters(), lr=0.001)

        # Load the model and optimizer states
        checkpoint = torch.load(model_path)
        self.model.load_state_dict(checkpoint["model_state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

        test_x = self.return_full_array(team, player_ids, home)

        self.new_input_tensor = torch.tensor(test_x, dtype=torch.float32).to(device)

    def return_home_array(self, home):
        if home == "home":
            return np.array([1])
        return np.array([0])

    def return_player_array(self, player_ids):
        arr = np.zeros(len(self.players))
        for player_id in player_ids:
            i = self.players.index(player_id)
            arr[i] = 1
        return arr

    def return_oppo_array(self, team):
        i = self.teams.index(team)
        arr = np.zeros(len(self.teams))
        arr[i] = 1
        return arr

    def return_full_array(self, team, player_ids, home):
        # players, oppo, home
        x = np.concatenate(
            (
                self.return_player_array(player_ids),
                self.return_oppo_array(team),
                self.return_home_array(home),
            ),
            axis=0,
        )
        return x

    def predict(self):

        with torch.no_grad():
            raw_output = self.model(
                self.new_input_tensor
            )  # Get raw logits from the model
            probabilities = torch.softmax(
                raw_output, dim=-1
            )  # Apply softmax to get probabilities

        # Convert probabilities to a readable format
        probabilities = probabilities.cpu().numpy()  # Convert to numpy array if desired
        # print("Output values (summing to 1):", probabilities)
        return probabilities


X = Integration(t, p, "home")
print(X.predict())
