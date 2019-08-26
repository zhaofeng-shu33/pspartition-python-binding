'''load pickle data to plot
'''
import os
from datetime import datetime
import json
import argparse
import pdb

import matplotlib.pyplot as plt
color_list = ['red', 'green', 'blue', 'green']
marker_list = ['o', '+', 'x', 'o']
linestyle_list = ['-','-', '-', '--']

def plot_time(filename, format):
    '''combine different algorithms
    '''
    f = open(os.path.join('build', filename), 'r')
    data = json.loads(f.read())
    x_data = [int(i) for i in data.keys()]
    one_key = str(x_data[0])
    alg_data = {}
    for i in data[one_key].keys():
        alg_data[i] = []
    for i in data.values():
        for k,v in i.items():
            alg_data[k].append(v)
    index = 0
    for k,v in alg_data.items():
        if(k == 'num_edge'):
            continue
        plt.plot(x_data, v, label=k, linewidth=3, color=color_list[index],
            marker=marker_list[index], markersize=12, linestyle=linestyle_list[index])
        index += 1
    plt.ylabel('time(s)', fontsize=18)
    plt.xlabel('node num', fontsize=18)
    plt.title('Gaussian blob clustering', fontsize=18)
    plt.legend(fontsize='x-large')
    plt.savefig(os.path.join('build', filename.replace('json', format)), bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    current_time_str = datetime.now().strftime('%Y-%m-%d')    
    parser.add_argument('--date', help='which date to load', default=current_time_str)
    parser.add_argument('--format', default='eps', choices=['eps', 'png'])
    parser.add_argument('--debug', default=False, type=bool, nargs='?', const=True, help='whether to enter debug mode') 
    args = parser.parse_args()
    if(args.debug):
        pdb.set_trace()
    plot_time(current_time_str + '-' + 'gaussian.json', args.format)    