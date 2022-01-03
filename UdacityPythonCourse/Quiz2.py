# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff

rainfall=((90/100)*rainfall)

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall 

# increase reservoir_volume by 5% to account for stormwater that flows
reservoir_volume=(105/100)*reservoir_volume

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume=(95/100)*reservoir_volume

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print (reservoir_volume)


carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits

rabbits = 12

print(crs_per_rab)    