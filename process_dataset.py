# Average patient data of a specific medical dataset

import pandas as pd
import argparse
import sys


# Extend the default ArgumentParser and display the help message when a parse error occurs
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


parser = MyParser(description='Process a medical dataset.')
parser.add_argument('filename', metavar='f', type=str,
                    help='the filename of the input dataset (.csv)')


def read_input(filename):
    print('Reading input csv file...', end='')
    df = pd.read_csv(filename)

    old_rowcount = df.shape[0]
    print('\tread ' + str(old_rowcount) + ' rows')

    print('Dropping rows with missing values...', end='')
    df.dropna(inplace=True)

    new_rowcount = df.shape[0]
    print('\tdropped ' + str(old_rowcount - new_rowcount) + ' rows')

    return df


def process_data(dataframe):
    print('Processing dataset...', end='')
    res = dataframe.groupby(['PatientID', 'Route', 'ParameterName']) \
        .agg({'TotaalGegevenDosis': 'sum'})
    print('\tprocessed ' + str(dataframe.shape[0]) + ' rows')

    return res


def write_output(result, filename):
    print('Saving result as ' + filename + '...', end='')
    result.to_csv(filename)
    print('\tsaved ' + str(result.shape[0]) + ' rows')


if __name__ == '__main__':

    args = parser.parse_args()

    print('\nPROCESSING MEDICAL DATASET\n')

    df = read_input(args.filename)
    res = process_data(df)
    write_output(res, 'result.csv')

    print('\nDONE')

