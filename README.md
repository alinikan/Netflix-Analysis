# Netflix Data Analyzer

Netflix Data Analyzer is a Python script that loads, analyzes, and visualizes your Netflix usage data. It generates a detailed report including different text-based outputs and charts based on the analysis of your data. 

### Prerequisites

Ensure you have the following installed on your machine:
- Python 3.6 or later
- Pandas library
- Matplotlib library
- OS library

You can install the needed Python libraries with pip:

**pip install pandas matplotlib** or **pip3 install pandas matplotlib**

### Getting Your Netflix Data

To get your Netflix data:

1- Visit this [link](https://www.netflix.com/account/getmyinfo)

2- Click on **Submit Request** at the bottom of the page

3- Wait for an email from Netflix (this may take up to 30 days) and download the data provided

4- Open the folder named **CONTENT_INTERACTION**

4- Place these files **(MyList.csv, ViewingActivity.csv, SearchHistory.csv, Ratings.csv)** in a folder named **DATA** within the same directory as the script

## Running the Script

To run the script, simply run the code in your IDE, or navigate to the directory containing the script in a terminal and enter the following command: 

**python script_name.py** or **python3 script_name.py**

(Replace "script_name.py" with the actual name of your script.)

## Functionality

Here is a brief description of what each function in the script does:

- `load_data()`: Loads data from the CSV files obtained from Netflix

- `create_outputs_folder()`: Creates a folder named 'Outputs' for storing the generated plots

- `save_plot()`: Saves a given plot to the 'Outputs' folder

- `analyze_my_list()`: Analyzes the user's Netflix list and prints a summary

- `analyze_viewing_activity()`: Analyzes the user's viewing activity, prints a summary, and generates a plot

- `analyze_search_history()`: Analyzes the user's search history and prints a summary

- `analyze_ratings()`: Analyzes the user's rating data and prints a summary

- `analyze_viewing_behavior()`: Analyzes the user's viewing behavior and generates a plot

- `analyze_device_type()`: Analyzes the user's device usage data, prints a summary, and generates a plot

- `total_watch_time()`: Calculates and prints the total watch time

- `main()`: The main function that calls all the other functions

## Outputs

The script will generate text-based summaries in the console as well as plots saved in the 'Outputs' folder.

## Author

Ali Nikan
