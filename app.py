import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    folder_path = os.path.join(os.getcwd(), "DATA")
    my_list = pd.read_csv(os.path.join(folder_path, 'MyList.csv'))
    viewing_activity = pd.read_csv(os.path.join(folder_path, 'ViewingActivity.csv'))
    search_history = pd.read_csv(os.path.join(folder_path, 'SearchHistory.csv'))
    ratings = pd.read_csv(os.path.join(folder_path, 'Ratings.csv'))
    return my_list, viewing_activity, search_history, ratings


def create_outputs_folder():
    folder_path = os.path.join(os.getcwd(), "Outputs")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def save_plot(plt, file_name, folder):
    plt.savefig(os.path.join(folder, file_name))


def analyze_my_list(my_list, folder):
    unique_titles = my_list['Title Name'].nunique()
    unique_profiles = my_list['Profile Name'].nunique()
    title_distribution = my_list['Title Name'].value_counts()
    profile_distribution = my_list['Profile Name'].value_counts()

    print(f"In the MyList data, there are {unique_titles} unique titles.")
    print(f"There are {unique_profiles} profile(s):")
    for profile, count in profile_distribution.items():
        print(f"- {profile} has added {count} title(s) to their list.")

    if len(title_distribution) == len(my_list):
        print("All titles are unique. Cannot print the 10 most common titles.")
    else:
        print("The 10 most common titles are:")
        for title, count in title_distribution.head(10).items():
            print(f"- {title}: {count}")


def analyze_viewing_activity(viewing_activity, folder):
    viewing_activity['Start Time'] = pd.to_datetime(viewing_activity['Start Time'])
    viewing_activity['Duration'] = pd.to_timedelta(viewing_activity['Duration'])
    viewing_activity.set_index('Start Time', inplace=True)
    viewing_duration_distribution = viewing_activity['Duration'].describe()

    print("\nThe distribution of viewing durations is as follows:")
    print(f"- Average (mean) viewing duration: {viewing_duration_distribution['mean']}")
    print(f"- Standard deviation: {viewing_duration_distribution['std']}")
    print(f"- Minimum viewing duration: {viewing_duration_distribution['min']}")
    print(
        f"- 25th percentile (25% of viewing sessions are shorter than this duration): {viewing_duration_distribution['25%']}")
    print(f"- Median (50% of viewing sessions are shorter than this duration): {viewing_duration_distribution['50%']}")
    print(
        f"- 75th percentile (75% of viewing sessions are shorter than this duration): {viewing_duration_distribution['75%']}")
    print(f"- Maximum viewing duration: {viewing_duration_distribution['max']}")

    # Analyze popular titles based on viewing activity
    popular_titles = viewing_activity['Title'].value_counts().head(10)

    print("\nTop 10 Popular Titles:")
    for title, count in popular_titles.items():
        print(f"- {title}: {count} viewing sessions")

    # Calculate total watch time on Netflix
    total_watch_time = viewing_activity['Duration'].sum()

    print(f"\nTotal Watch Time on Netflix: {total_watch_time}")

    # Time series plot of viewing activity
    plt.figure(figsize=(10, 6))
    viewing_activity.resample('D')['Profile Name'].count().plot()
    plt.title('Viewing Activity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Viewing Sessions')
    plt.tight_layout()
    save_plot(plt, 'viewing_activity_plot.png', folder)


def analyze_search_history(search_history, folder):
    unique_queries = search_history['Query Typed'].nunique()
    unique_actions = search_history['Action'].nunique()
    action_distribution = search_history['Action'].value_counts()

    print(f"\nIn the SearchHistory data, there are {unique_queries} unique queries.")
    print(f"There are {unique_actions} unique actions.")

    print("\nThe distribution of actions is as follows:")
    for action, count in action_distribution.items():
        print(f"- {action}: {count}")


def analyze_ratings(ratings, folder):
    unique_titles = ratings['Title Name'].nunique()
    unique_profiles = ratings['Profile Name'].nunique()
    unique_rating_types = ratings['Rating Type'].nunique()
    rating_type_distribution = ratings['Rating Type'].value_counts()

    thumbs_value_distribution = ratings['Thumbs Value'].value_counts()
    thumbs_value_labels = {
        0: 'not rated',
        1: 'thumbs down',
        2: 'thumbs up',
        3: 'two thumbs up'
    }

    print(f"\nIn the Ratings data, there are {unique_titles} unique titles.")
    print(f"There are {unique_profiles} profile(s): {', '.join(ratings['Profile Name'].unique())}.")
    print(f"There are {unique_rating_types} unique rating types.")

    print("\nThe distribution of rating types is as follows:")
    for rating_type, count in rating_type_distribution.items():
        print(f"- {rating_type}: {count}")

    print("\nThe distribution of thumbs values is as follows:")
    for thumbs_value, count in thumbs_value_distribution.items():
        thumbs_label = thumbs_value_labels.get(thumbs_value, 'Unknown')
        print(f"- {thumbs_value} ({thumbs_label}): {count}")


def analyze_viewing_behavior(viewing_activity, folder):
    viewing_activity['Day of Week'] = viewing_activity.index.dayofweek
    viewing_activity['Weekend'] = viewing_activity['Day of Week'].apply(lambda x: 1 if x >= 5 else 0)
    weekday_viewing_count = viewing_activity[viewing_activity['Weekend'] == 0]['Profile Name'].count()
    weekend_viewing_count = viewing_activity[viewing_activity['Weekend'] == 1]['Profile Name'].count()

    print(f"\nViewing activity on weekdays: {weekday_viewing_count} sessions")
    print(f"Viewing activity on weekends: {weekend_viewing_count} sessions")

    viewing_activity['Hour'] = viewing_activity.index.hour

    plt.figure(figsize=(10, 6))
    viewing_activity['Hour'].value_counts().sort_index().plot(kind='bar')
    plt.title('Distribution of Viewing Sessions by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Viewing Sessions')
    plt.xticks(rotation=0)
    plt.tight_layout()
    save_plot(plt, 'viewing_sessions_by_hour.png', folder)


def analyze_device_type(viewing_activity, folder):
    device_viewing_count = viewing_activity['Device Type'].value_counts()
    device_viewing_duration = viewing_activity.groupby('Device Type')['Duration'].sum()

    print("\nViewing activity by device type:")
    for device, count in device_viewing_count.items():
        print(f"- {device}: {count} sessions")

    print("\nTotal viewing duration by device type:")
    for device, duration in device_viewing_duration.items():
        print(f"- {device}: {duration}")

    plt.figure(figsize=(27, 14))
    device_viewing_count.plot(kind='bar')
    plt.title('Viewing Sessions by Device Type')
    plt.xlabel('Device Type')
    plt.ylabel('Number of Viewing Sessions')
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    save_plot(plt, 'viewing_sessions_by_device.png', folder)


def total_watch_time(viewing_activity):
    total_watch_time = viewing_activity['Duration'].sum()
    print(f"\nTotal Watch Time on Netflix: {total_watch_time}")


def main():
    my_list, viewing_activity, search_history, ratings = load_data()
    folder_path = create_outputs_folder()

    analyze_my_list(my_list, folder_path)

    analyze_viewing_activity(viewing_activity, folder_path)

    analyze_search_history(search_history, folder_path)

    analyze_ratings(ratings, folder_path)

    analyze_viewing_behavior(viewing_activity, folder_path)

    analyze_device_type(viewing_activity, folder_path)

    total_watch_time(viewing_activity)


if __name__ == '__main__':
    main()
