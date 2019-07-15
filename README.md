# Ogma

We present Ogma, the first approach, which provides a systematic test framework for machine-learning systems that accepts grammar-based inputs.
See the paper [Grammar Based Directed Testing of Machine Learning Systems](https://arxiv.org/pdf/1902.10027) for more details

## Prerequisites

* Python 2.7.15
* numpy 1.14.5
* scipy 1.1.0
* scikit-learn 1.19.0

The authors used Pycharm CE 2017.2.3 as the development IDE.

## Background

The Ogma approach is encapsulated in GramFuzz*.py. 
To run these files, you'll need a Context Free Grammar, a Jaccard Threshold and an API for your NLP service. 
You can look at the sample APIs in aylien_API.py, rosette_API.py and uclassify_API.py. 
Please run these with an example to see the type of inputs required of the output. 

## Demo
`python <filename>`

eg. `python GramFuzz_Rosette_uClassify.py`

## Contact
* Please contact sakshi_udeshi@mymail.sutd.edu.sg for any comments/questions
