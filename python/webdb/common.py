#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict
from optparse import OptionParser
from sys import stdin, exit
from re import match

class Dic:
    def __init__(self, filename):
        self.ht = defaultdict(list)
        for line in open(filename):
            read, word, pos = line.strip().split("\t")[:3]
            self.add(read, word, pos)

    def add(self, read, word, pos):
        if not word in self.ht[read]:
            self.ht[read] += [(word, pos)]

    def lookup(self, string, maximum):
        result = defaultdict(list)

        for i in range(len(string)-1):
            for j in range(i+1, min(len(string)+1, i+maximum)):
                read = string[i:j]
                for word, pos in self.find(read):
                    node = Node(word, read, pos, j)
                    result[j] += [node]

        return result

    def find(self, string):
        return self.ht.get(string, [])

class Node:
    def __init__(self, word, read, pos, end):
        self.word = word
        self.read = read
        self.pos = pos
        self.end = end
        self.score = 0.0
        self.prev = None

    def is_bos(self):
        return self.pos == "BOS"

    def is_eos(self):
        return self.pos == "EOS"

    def __repr__(self):
        return "(%s, %s, %s, %s)" % (self.word, self.read, self.pos, self.score)

class Graph:
    def __init__(self, dic, string):
        self.nodes = defaultdict(list)

        # lookup dictionary
        self.nodes = dic.lookup(string, 16)

        # push BOS
        bos = Node("", "", "BOS", 0)
        self.nodes[0] = [bos]

        # push EOS
        self.eos = Node("", "", "EOS", len(string)+1)
        self.nodes[len(string)+1] = [self.eos]


    def get_prevs(self, node):
        if node.is_eos():
            # eosは長さが0なので特殊な処理が必要
            startpos = node.end - 1
            return self.nodes[startpos]
        elif node.is_bos():
            # bosはそれより前のノードがないので特殊な処理が必要
            return []
        else:
            startpos = node.end - len(node.read)
            return self.nodes[startpos]

class FeatureFuncs:
    def __init__(self, extend=False): 
        self.node_features = []
        self.edge_features = []

        # surface
        node_feature_surface = lambda node: "S" + node.word
        self.node_features += [node_feature_surface]

        # (surface, pronunciation)
        node_feature_surface_read = lambda node: "S" + node.word + "\tR" + node.read
        self.node_features += [node_feature_surface_read]

        # (sufrace_left, surface_right)
        edge_feature_surface = lambda prev_node, node: "S" + prev_node.word + "\tS" + node.word
        self.edge_features += [edge_feature_surface]

        if extend:
            # bias term
            #self.node_features += [lambda node: "BIAS"]

            # length term
            #self.node_features += [lambda node: "LENGTH_" + str(len(node.read))]

            # hiragana term
            #self.node_features += [lambda node: "IS_HIRAGANA" if match("^[ぁ-ん]+$", node.word) else "NOT_HIRAGANA"]

            # katakana term
            #self.node_features += [lambda node: "IS_KATAKANA" if match("^[ァ-ン]+$", node.word) else "NOT_KATAKANA"]

            # character type
            #self.node_features += [lambda node: "C_HIRA" if match("^[ぁ-んー]+$", node.word) else "CE_KATA" if match("^[ァ-ンー]+$", node.word) else "C_OTHER"]

            # part-of-speech
            self.node_features += [lambda node: "P" + node.pos]
            self.edge_features += [lambda node1, node2: "P" + node1.pos + "\tP" + node2.pos]

class Decoder:
    def __init__(self, feature_funcs):
        self.feature_funcs = feature_funcs

    def get_node_score(self, node, w):
        score = 0.0
        for func in self.feature_funcs.node_features:
            feature = func(node)
            score += w[feature]
        return score

    def get_edge_score(self, prev_node, node, w):
        score = 0.0
        for func in self.feature_funcs.edge_features:
            feature = func(prev_node, node)
            score += w[feature]
        return score

    def viterbi(self, graph, w):
        for i in sorted(graph.nodes.keys()):
            for node in graph.nodes[i]:
                if node.is_bos():
                    continue
                node.score = -1000000.0
                node_score_cache = self.get_node_score(node, w)

                for prev_node in graph.get_prevs(node):
                    tmp_score = prev_node.score \
                            + self.get_edge_score(prev_node, node, w) \
                            + node_score_cache
                    if tmp_score >= node.score:
                        node.score = tmp_score
                        node.prev = prev_node

        result = []
        node = graph.eos.prev

        while node and not node.is_bos():
            result += [(node.word, node.read)]
            node = node.prev

        result.reverse()
        return result

def read_weight_map(filename, dic):
    w = defaultdict(float)

    for line in open(filename):
        key, value = line.strip().split("\t\t")
        w[key] = float(value)
        keys = key.split("\t")
        if len(keys) == 2 and keys[0][0] == "S" and keys[1][0] == "R":
            word = keys[0][1:]
            read = keys[1][1:]
            dic.add(read, word, "UNK")
    return w

if __name__ == '__main__':
    dic = Dic("test-data/dictionary.txt")
    feature_funcs = FeatureFuncs()
    decoder = Decoder(feature_funcs)
    w = read_weight_map("test-data/model.txt", dic)

    graph = Graph(dic, "くるまでまつ")
    result = decoder.viterbi(graph, w)
    print graph.nodes
    print " ".join(word[0] for word in result)

