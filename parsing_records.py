# %%
import pandas as pd


def create_head_to_head_matrix(records_data):
    """
    Create a head-to-head record matrix from the provided records data.

    Args:
    records_data (dict): A dictionary where each key is a team, and each value is another dictionary
                         detailing win ('W') and loss ('L') counts against other teams.

    Returns:
    pandas.DataFrame: A DataFrame representing the head-to-head record matrix.
    """

    # Extract the team names from the keys of the input dictionary
    teams = list(records_data.keys())

    # Initialize a pandas DataFrame with team names as both row and column indices
    matrix_df = pd.DataFrame(index=teams, columns=teams, dtype=str)

    # Loop through each team
    for team in teams:
        # Loop through each opponent team
        for opponent in teams:
            # Check if the team and opponent are the same
            if team == opponent:
                # Set the diagonal values to '--' to indicate self
                matrix_df.at[team, opponent] = "--"
            else:
                # Extract the number of wins against the opponent from the data
                wins = records_data[team][opponent]["W"]
                # Set the cell value to the number of wins
                matrix_df.at[team, opponent] = str(wins)

    # Rename the index label to 'Tm' (short for Team)
    matrix_df.index.name = "Tm"

    # Add a new row at the bottom with team names to align with column headers
    matrix_df.loc["Tm"] = matrix_df.columns

    # Remove the index name to match the formatting requirement
    matrix_df.index.name = None

    # Set the column headers to be the same as the last row for consistent formatting
    matrix_df.columns = matrix_df.loc["Tm"]

    # Return the formatted DataFrame
    return matrix_df


# load the data
records_data = {
    "BRO": {
        "BSN": {"W": 10, "L": 12},
        "CHC": {"W": 15, "L": 7},
        "CIN": {"W": 15, "L": 7},
        "NYG": {"W": 14, "L": 8},
        "PHI": {"W": 14, "L": 8},
        "PIT": {"W": 15, "L": 7},
        "STL": {"W": 11, "L": 11},
    },
    "BSN": {
        "BRO": {"W": 12, "L": 10},
        "CHC": {"W": 13, "L": 9},
        "CIN": {"W": 13, "L": 9},
        "NYG": {"W": 13, "L": 9},
        "PHI": {"W": 14, "L": 8},
        "PIT": {"W": 12, "L": 10},
        "STL": {"W": 9, "L": 13},
    },
    "CHC": {
        "BRO": {"W": 7, "L": 15},
        "BSN": {"W": 9, "L": 13},
        "CIN": {"W": 12, "L": 10},
        "NYG": {"W": 7, "L": 15},
        "PHI": {"W": 16, "L": 6},
        "PIT": {"W": 8, "L": 14},
        "STL": {"W": 10, "L": 12},
    },
    "CIN": {
        "BRO": {"W": 7, "L": 15},
        "BSN": {"W": 9, "L": 13},
        "CHC": {"W": 10, "L": 12},
        "NYG": {"W": 13, "L": 9},
        "PHI": {"W": 13, "L": 9},
        "PIT": {"W": 13, "L": 9},
        "STL": {"W": 8, "L": 14},
    },
    "NYG": {
        "BRO": {"W": 8, "L": 14},
        "BSN": {"W": 9, "L": 13},
        "CHC": {"W": 15, "L": 7},
        "CIN": {"W": 9, "L": 13},
        "PHI": {"W": 12, "L": 10},
        "PIT": {"W": 15, "L": 7},
        "STL": {"W": 13, "L": 9},
    },
    "PHI": {
        "BRO": {"W": 8, "L": 14},
        "BSN": {"W": 8, "L": 14},
        "CHC": {"W": 6, "L": 16},
        "CIN": {"W": 9, "L": 13},
        "NYG": {"W": 10, "L": 12},
        "PIT": {"W": 13, "L": 9},
        "STL": {"W": 8, "L": 14},
    },
    "PIT": {
        "BRO": {"W": 7, "L": 15},
        "BSN": {"W": 10, "L": 12},
        "CHC": {"W": 14, "L": 8},
        "CIN": {"W": 9, "L": 13},
        "NYG": {"W": 7, "L": 15},
        "PHI": {"W": 9, "L": 13},
        "STL": {"W": 6, "L": 16},
    },
    "STL": {
        "BRO": {"W": 11, "L": 11},
        "BSN": {"W": 13, "L": 9},
        "CHC": {"W": 12, "L": 10},
        "CIN": {"W": 14, "L": 8},
        "NYG": {"W": 9, "L": 13},
        "PHI": {"W": 14, "L": 8},
        "PIT": {"W": 16, "L": 6},
    },
}


# Generate the matrix
matrix_df = create_head_to_head_matrix(records_data)

# Display or process the matrix as needed
print(matrix_df)
