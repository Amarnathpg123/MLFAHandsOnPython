# -*- coding: utf-8 -*-
"""unit4_Evaluator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKlb6b3HyOJTZRbSCh4bgULNFLKE5TCa
"""

import ast


def main(ans):
    res = {}
    res["status"] = 'Success'
    res["Comments"] = "Please make sure the Python script you are submitting is not having errors. Try running before submitting"
  
    try:
        res["Message"] = "Successfully submitted! Thanks for taking the exercise"
        return res

    except:
        return res,{'status': 'Failure'}



