length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume_in_cub_cm = length * width * height
volume_in_cub_dm = volume_in_cub_cm / 1000
real_volume = volume_in_cub_dm - volume_in_cub_dm * percent / 100
print(real_volume)
