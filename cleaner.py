def filter_nondigits(list_of_heart_rates: list) -> list:
   new_list_of_rates = []
   for heart_rate in list_of_heart_rates:
       heart_rate = heart_rate.strip('\n')
       if heart_rate.isdigit():
           new_list_of_rates.append(int(heart_rate))
   print(new_list_of_rates)
   return new_list_of_rates


""" Remove data that's less than 30 (<30)
   OR greater than 250 (>250) """


def filter_outliers(new_list_of_rates: list) -> list:
   newer_list_of_rates = []
   for heart_rate in new_list_of_rates:
       if 30 < heart_rate < 250:
           newer_list_of_rates.append(heart_rate)
   print(newer_list_of_rates)  
   return newer_list_of_rates 