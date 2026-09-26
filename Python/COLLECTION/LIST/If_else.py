age_list = [34,52,41,2,6,9,78]

filter_list = [(age,"Eligible") if age > 18 else(age,"not Eligible") for age in age_list]

print(age_list)
print(filter_list)