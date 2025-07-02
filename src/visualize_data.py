

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re
import itertools
import unicodedata
from janome.tokenizer import Tokenizer
import networkx as nx
from scipy.spatial import distance

import pandas as pd

header = []
rows = []
words = {}
allwords = {}
def category(word):
    vowels =  ['a','e','i','o','u', 'æ', 'ö', 'ø', 'j', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'y', 'œ']
    letter = word[0]
    if letter in vowels:
        return 'vowel'
    elif letter == 's':
        if word[1] == 'k':
            return 'sk'
        elif word[1] == 'p':
            return 'sp'
        elif word[1] == 't':
            return 'st'
        else:
            return 's'
    else:
        return letter

with open('full_p_vals.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            header = row
        else:
            rows.append(row)
            letter = row[0][0]
            cat = category(row[0])
            if cat not in words:
                words[cat] = []
            if row[0] not in words[cat]:
                words[cat].append(row[0])
            if row[1] not in words[cat]:
                words[cat].append(row[1])
            if row[0] not in allwords:
                allwords[row[0]] = 0
            if row[1] not in allwords:
                allwords[row[1]] = 0
            allwords[row[0]] += 1
            allwords[row[1]] += 1


        line_count ++ 1

co_occurency_tables = {}

for row in rows:
    cat = category(row[0])
    if cat not in co_occurrency_tables:
        co_occurency_tables[cat] = np.zeros((len(words[cat]), len(words[cat])))
    co_occurency_tables[cat][words[cat].index(row[0]), words[cat].index(row[1])] = int(row[2])
    co_occurency_tables[cat][words[cat].index(row[1]), words[cat].index(row[0])] += int(row[2])

df_tables = {}
wordlist = []

for table in co_occurency_tables:
    df = pd.DataFrame(co_occurency_tables[table], columns = words[table], index = words[table])
    df = df.loc[(df.sum(axis=1) > 100), (df.sum(axis=0) > 100)]
    df


jaccard_tables = {}
for table in co_occurency_tables:
    jaccard_tables[table] = 1 - distance.cdist(co_occurency_tables[table], co_occurency_tables[table], 'jaccard')

    nodes = []

    for i in range(len(words[table])):
        for j in range(i+1, len(words[table])):
            jaccard = jaccard_tables[table][i, j]
            if jaccard > 0:
                nodes.append([words[table][i], words[table][j], allwords[words[table][i]] allwords[words[table][j]], jaccard])

    len(nodes)

    G = nx.Graph()
    G.nodes(data=True)

    for pair in nodes:
        node_x, node_y, node_x_cnt, node_y_cnt, jaccard = pair[0], pair[1], pair[2], pair[3], pair[4]
        if not G.has_node(node_x):
            G.add_node(node_x, count=node_x_cnt)
        if not G.has_node(node_y):
            G.add_node(node_y, count=node_y_cnt)
        if not G.has_edge(node_x, node_y):
            G.add_edge(node_x, node_y, weight=jaccard)

    plt.figure(figsize=(15,15))
    pos = nx.spring_layout(G, k=0.1)

    node_size = [d['count']*100 for (n,d) in G.nodes(data=True)]
    nx.draw_networkx_nodes(G, pos, node_color='cyan', alpha=1.0, node_size=node_size)
    nx.draw_networkx_labels(G, pos, fontsize=14, font_family='Droid Sans Japanese')

    edge_width = [d['weight']*10 for (u,v,d) in G.edges(data=True)]
    nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='black', width=edge_width)

    plt.axis('off')
    plt.show()


#
#
# co_occur_array = co_occur.to_numpy()
#
# co_occur_array.shape
#
# #1b
#
# M = np.log(1+co_occur_array)
#
# u,s,vt = np.linalg.svd(M, full_matrices=True)
# smat = np.diag(s)
# k = 100
# vkt = vt[:k,:]
# uk = u[:,:k]
# sk = smat[:k,:k]
# M_rank_100 = uk.dot(sk).dot(vkt)
#
# y_vals = s[:100]
# x_vals = np.arange(100)
#
# plt.figure(figsize=(15,10))
# plt.scatter(x_vals, y_vals)
# plt.xlabel('Singular Value Number')
# plt.ylabel('Value')
# plt.show()
#
# # 1c
#
#
# dictionary_lines = []
# with open('/dictionary.txt') as filename:
#   for line in filename:
#     line = line.strip()
#     dictionary_lines.append(line)
#
# dictionary_array = np.array(dictionary_lines)
#
#
# for i in range(20):
#   singular_vector = u[:,i]
#
#   indices_biggest = (-singular_vector).argsort()[:10]
#   indices_smallest = (singular_vector).argsort()[:10]
#
#   positive_words = dictionary_array[indices_biggest]
#   negative_words = dictionary_array[indices_smallest]
#
#   print("For singular value ", i+1)
#   print("Words with Largest Positive Value: ", positive_words)
#   print("Words with Largest Negative Value: ", negative_words)
#   print("")
#
# #1d
#
# U = u[:,:100]
# norms = np.linalg.norm(U, axis=1)
# U = U/norms.reshape(norms.shape[0],1)
# woman_index = dictionary_lines.index("woman")
# man_index = dictionary_lines.index("man")
#
# woman_embedding = U[woman_index,:]
# man_embedding = U[man_index,:]
#
# v = woman_embedding - man_embedding
#
#
#
# projection_values = []
#
#
# for word in word_list:
#   word_embedding = U[dictionary_lines.index(word),:]
#   projection_value = np.dot(word_embedding, v) / np.linalg.norm(v)
#   print(word, projection_value)
#   projection_values.append(projection_value)
# plt.figure(figsize=(20,5))
#
# y_vals = np.zeros(12)
# #ar = np.arange(12) # just as an example array
# #plt.plot(ar, np.zeros_like(ar) + projection_values, 'x')
# plt.scatter(projection_values, y_vals)
# plt.plot([-0.4,0.5], [0,0],color="green")
# plt.yticks([])  # Command for hiding y-axis
#
# for i, label in enumerate(word_list):
#     plt.annotate(label, (projection_values[i], y_vals[i]))
# #plt.plot(projection_values)
# plt.show()
#
# word_list_2 = ["math", "matrix", "history", "nurse", "doctor", "pilot", "teacher", "engineer", "science", "arts", "literature", "bob", "alice"]
#
# projection_values = []
# for word in word_list_2:
#   word_embedding = U[dictionary_lines.index(word),:]
#   projection_value = np.dot(word_embedding, v) / np.linalg.norm(v)
#   print(word, projection_value)
#   projection_values.append(projection_value)
# plt.figure(figsize=(5,15))
#
# y_vals = np.zeros(13)
# #ar = np.arange(12) # just as an example array
# #plt.plot(ar, np.zeros_like(ar) + projection_values, 'x')
# plt.scatter(y_vals, projection_values)
# plt.plot([0, 0], [-0.5,0.5],color="green")
# plt.xticks([])  # Command for hiding y-axis
#
# for i, label in enumerate(word_list_2):
#     plt.annotate(label, (y_vals[i],projection_values[i]))
# #plt.plot(projection_values)
# plt.show()
