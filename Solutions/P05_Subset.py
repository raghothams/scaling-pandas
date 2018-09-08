trips_data.sort_values(['duration'], inplace = True) # Sorting from top to bottom 
trips_data.iloc[-5:] # Longest 5 trips
trips_data.iloc[:5] # Shortest 5 trips
