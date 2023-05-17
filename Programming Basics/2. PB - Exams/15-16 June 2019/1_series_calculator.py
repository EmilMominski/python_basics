import math
series_title = input()
season_count = int(input())
episode_count = int(input())
episode_duration = float(input())

normal_episode_duration = episode_duration + episode_duration * 20 / 100
all_normal_episodes = normal_episode_duration * (episode_count - 1) * (season_count)
all_special_episodes = (normal_episode_duration + 10) * season_count
all_episodes_duration = all_normal_episodes + all_special_episodes

print(f"Total time needed to watch the {series_title} series is {math.floor(all_episodes_duration)} minutes.")
