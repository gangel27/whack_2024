import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
import pandas as pd



class SpiderDiagrams():

    def __init__():
        df = pd.read_csv('CCFC_match_lineups_data.csv')
        df = df.dropna(how='any')
        pass

    def radar_factory(num_vars, frame='Circle'):
    
        theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

        class RadarTransform(PolarAxes.PolarTransform):
            def transform_path_non_affine(self, path):
                if path._interpolation_steps > 1:
                    path = path.interpolated(num_vars)
                return Path(self.transform(path.vertices), path.codes)

        class RadarAxes(PolarAxes):
            name = 'radar'
            PolarTransform = RadarTransform

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.set_theta_zero_location('N')
            
            def fill(self, *args, closed=True, **kwargs):
                return super().fill(closed=closed, *args, **kwargs)
            
            def plot(self, *args, **kwargs):
                lines = super().plot(*args, **kwargs)
                for line in lines:
                    self._close_line(line)

            def _close_line(self, line):
                x, y = line.get_data()

                if x[0] != x[-1]:
                    x = np.append(x, x[0])
                    y = np.append(y, y[0])
                    line.set_data(x, y)
            
            def set_varlabels(self, labels):
                self.set_thetagrids(np.degrees(theta), labels)
            
            def _gen_axes_patch(self):
                if frame == 'circle':
                    return Circle((0.5, 0.5), 0.5)
                elif frame == 'polygon':
                    return RegularPolygon((0.5, 0.5), num_vars, radius = 0.5, edgecolor="k")
                else:
                    raise ValueError("Unknown value for 'frame': %s" % frame)
                
            def _gen_axes_spines(self):
                if frame == 'circle':
                    return super()._gen_axes_spines()
                elif frame == 'polygon':
                    spine = Spine(axes=self, spine_type = 'circle', path = Path.unit_regular_polygon(num_vars))
                    spine.set_transform(Affine2D().scale(0.5).translate(0.5, 0.5) + self.transAxes)
                    return {'polar': spine}
                else:
                    raise ValueError("Unknown value for 'frame': %s" % frame)
                
        register_projection(RadarAxes)
        return theta
    
    def normalize_data(data):
        """ Normalize the data to the range [0, 1] """
        return (data - data.min()) / (data.max() - data.min())

    def plot_average_radar(teams, selected_stats):
        # Filter the DataFrame for the specified teams
        filtered_df = df[df['Opposition'].isin(teams)]

        for stat in selected_stats:
            filtered_df[stat] = normalize_data(filtered_df[stat])

        # Calculate the average for the specified statistics
        averages = filtered_df.groupby('Opposition')[selected_stats].mean().reset_index()

        # Create radar chart
        N = len(selected_stats)
        theta = radar_factory(N, frame='polygon')

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='radar'))

        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        
        # Iterate through the averaged values
        for i, (index, row) in enumerate(averages.iterrows()):
            team_name = row['Opposition']
            r = row[selected_stats].values

            ax.plot(theta, r, color=colors[i % len(colors)], label=team_name)
            ax.fill(theta, r, color=colors[i % len(colors)], alpha=0.25)

        # Set variable labels using your custom set_varlabels method
        ax.set_varlabels(selected_stats)

        ax.set_rlim(0, 1)  # Adjust limits as needed
        ax.set_title('Radar Plot for Selected Teams')

        # Add legend
        ax.legend(loc='upper left', fontsize='small')

        return plt

    # # Example usage
    # teams = ['Reading', 'Millwall', 'Brentford']  # Replace with your teams
    # selected_stats = ['possession', 'np_xg', 'shots', 'pressures', 'tackles', 'goals_conceded']  # Replace with your stats
    # plot_average_radar(teams, selected_stats)