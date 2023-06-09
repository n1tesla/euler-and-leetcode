def counting_days():
    mod_of_days = {6: 'monday', 0: 'thuesday', 1: 'wednesday', 2: 'thursday', 3: 'friday', 4: 'saturday', 5: 'sunday'}
    total_days=0
    count_sunday=0
    non_leap_year_days=[31,28,31,30,31,30,31,31,30,31,30,31]

    for i in range(1901,2001):
        for index,total_day_in_month in enumerate(non_leap_year_days):
            if i%4==0 and index==1:
                total_days=total_day_in_month+1
                if total_days%7==5:
                    count_sunday+=1

            else:
                total_days+=total_day_in_month
                if total_days%7==5:
                    count_sunday+=1

    return count_sunday


if __name__=='__main__':
    print(counting_days())