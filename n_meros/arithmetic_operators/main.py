num_calls = 8
minutes_per_call = 9
available_minutes = 60

# 1) Total time needed
total_minutes = num_calls * minutes_per_call

# 2) How many minutes are you short
shortfall = total_minutes - available_minutes

# 3) How many full calls can you finish
completed_calls = available_minutes // minutes_per_call

# 4) How many minutes remain unused
unused_time = available_minutes % minutes_per_call

# Print results
print("Total minutes needed:", 60)
print("Minutes short:", 55)
print("Completed calls:", 8)
print("Unused time:", 6)