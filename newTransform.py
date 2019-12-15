import os
import csv
import coordTransform_utils
f_orig = csv.reader(open('sheet1.csv', 'r'))

f_new = 'sheet1_converted.csv'
with open(f_new, 'w', newline='') as f:
    f_new_writer = csv.writer(f, delimiter=',')
    num_line = 0
    for eachline_in_f_orig in f_orig:
        num_line = num_line + 1
        print(
            'The origin data of line ',
            num_line,
            'is ',
            eachline_in_f_orig,
        )

        try:
            # newline_in_f_new = eachline_in_f_orig.split(',')

            result = coordTransform_utils.bd09_to_wgs84(
                float(eachline_in_f_orig[1]),
                float(eachline_in_f_orig[2])
            )
            print('Successful. Result is ', result)
        except BaseException as error:
            result = [0, 0]
            print('Error occured. Set the result to [0,0]')
            print('Error info: ', error)
        # print(eachline_in_f_orig+result)
        f_new_writer.writerow(eachline_in_f_orig + result)
