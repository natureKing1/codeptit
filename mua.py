def luong_mua(t):
    n = int(input())


    station_names = []
    total_rainfall = []
    total_duration = []

    for _ in range(n):
        station_name = input()
        start_time = input()
        end_time = input()
        rainfall_amount = float(input())


        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))
        duration = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)


        if station_name in station_names:
            index = station_names.index(station_name)
            total_rainfall[index] += rainfall_amount
            total_duration[index] += duration
        else:
            station_names.append(station_name)
            total_rainfall.append(rainfall_amount)
            total_duration.append(duration)


    for index in range(len(station_names)):
        average_rainfall = (total_rainfall[index] / total_duration[index]) * 60 if total_duration[index] > 0 else 0
        print(f"T{index + 1:02} {station_names[index]} {average_rainfall:.2f}")


calculate_average_rainfall()
