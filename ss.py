# coding: utf8
import spacy
import collections
from operator import itemgetter
import sys
import os
nlp = spacy.load('en')

def ss(texts):
	dic = {}

	for te in texts:
		ts = texts
		ts.remove(te)

		for sent in te.sents: ## Sentences in the main text

			Sum_high = []
			for text in ts: ## for all texts
				a = sorted(text.sents, key = lambda x: sent.similarity(x), reverse = True)

				Sum_high.append(sent.similarity(a[0])) ## Add the Highest Sim

			dic[sent] = (sum(Sum_high) / len(Sum_high))

	sorted_list = sorted(dic.items(), key = lambda kv: kv[1]) ## sort from high to low
	sorted_dic = collections.OrderedDict(sorted_list) ## convert to dic

	lis = []
	
	for k, v in sorted_dic.items(): ## filtering all the bad
		if v > 0.86:
			lis.append(k)

	lis.reverse()

	for v in lis: ## taking just the highest sims
		for v2 in lis:
			if v.similarity(v2) > 0.85 and lis.index(v) < lis.index(v2):
				lis.remove(v2)

	return lis ## return list of the importent sen

def summary(texts):
	texts = [nlp(text) for text in texts]
	most_importent_sents = ss(texts)

	lis = []
	for text in most_importent_sents:
		tok = [token.text for token in text if not token.is_stop and token.is_alpha] ## remove all but the good stuff
		lis.extend(tok)

	dic = {}

	for word in lis:
		count = lis.count(word)
		dic[word] = count

	max_key = max(dic, key=dic.get)
	max_value = dic[max_key]

	for word in dic:
		dic[word] = dic[word] / max_value


	dic_sen = {}
	value = 0
	for sen in most_importent_sents:
		for k,v in dic.items():
			value =  value + (v * str(sen).count(k))

		dic_sen[sen] = value
		value = 0


	sorted_list = sorted(dic_sen.items(), key = lambda kv: kv[1]) ## sort from low to high
	sorted_dic = collections.OrderedDict(sorted_list) ## convert to dic
	sorted_list = list(sorted_dic.keys())
	sorted_list.reverse()


	string = ''
	for s in sorted_list:
		string = string + str(s)

	print(string)