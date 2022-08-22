import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# plot_array: plot from 1 to n array


def plot_array_n(files, title, xlabel, ylabel, save_path):

    # read inputs
    file_array = []
    for i in range(len(files)):
        # read text file content
        file = open(files[i], 'r')
        content = file.read()
        file.close()
        # remove all character that aren't digits or space from file content
        content = ''.join(
            [i for i in content if i.isdigit() or i == ' ' or i == '.'])
        # save content into a file
        file = open('temp.txt', 'w')
        file.write(content)
        file.close()
        file_array.append(np.loadtxt('temp.txt'))

    plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    # assign different colors
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    # remove all character that aren't digits or space from file content
    # read text file content
    for i in range(len(file_array)):
        plt.plot(file_array[i], colors[i], label=str(files[i]))
    plt.legend()
    plt.savefig(save_path)
    plt.show()
    #delete temp file
    os.remove('temp.txt')
    plt.close()


# main function
if __name__ == '__main__':
    # check inputs
    if len(sys.argv) < 6:
        print("Usage: python plot_array.py <file_array_1>...<file_array_n> <title> <xlabel> <ylabel> <save_path>")
        sys.exit(1)

    files = [] #names of the files
    for i in range(1, len(sys.argv) - 4):
        files.append(sys.argv[i])
    title = sys.argv[len(sys.argv)-4]
    xlabel = sys.argv[len(sys.argv)-3]
    ylabel = sys.argv[len(sys.argv)-2]
    save_path = sys.argv[len(sys.argv)-1]
    # plot
    plot_array_n(files, title, xlabel, ylabel, save_path)
    sys.exit(0)
# end of main function
