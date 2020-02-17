#!/usr/bin/env python3

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='superdata76 NLP/ML disaster tweet detection. Builds ML model from TRAIN_DATA and runs against TEST_DATA, creates CSV RESULT_SET for submission.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--train-data', '-tr', help='CSV for training data',
        default='./slalombuilddatacontest/train.csv')
    parser.add_argument('--test-data', '-te', help='CSV for test data',
        default='./slalombuilddatacontest/test.csv')
    parser.add_argument('--result-set', '-rs', help='CSV result for submission',
        default='./slalombuilddatacontest/test_result.csv')
    return parser.parse_args()


def main():
    args = parse_args()
    # invoke NLP/ML on training data to create model
    # invoke trained model on test data, save result set CSV

if __name__ == '__main__':
    main()
