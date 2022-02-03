#!/usr/bin/env python
# coding: utf-8

import glob
import pandas as pd
import sys

def main():
    all_files = glob.glob("*.csv")

    lists_of_df = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df['filename'] = filename
        lists_of_df.append(df)

    df_all = pd.concat(lists_of_df, axis=0, ignore_index=True)

    df_all.to_csv('combined.csv')

if __name__ == '__main__':
   main()



