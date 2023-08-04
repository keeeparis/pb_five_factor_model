import pandas as pd
import numpy as np
import pickle as pkl
from typing import Dict
import math
from src.utils.utils import *

def model(user_values: list[int]) -> dict[str, list[str] or list[int]]:
  model_file_name = 'test.pickle'
  df = pkl.load(open(model_file_name, 'rb'))
  
  extraversion = pd.Series(df['extraversion'])
  neuroticism = pd.Series(df['neuroticism'])
  agreeableness = pd.Series(df['agreeableness'])
  conscientiousness = pd.Series(df['conscientiousness'])
  openness = pd.Series(df['openness'])

  extraversion_quantile = math.ceil((((extraversion < user_values[0]).sum())/extraversion.count()) * 100)
  neuroticism_quantile = math.ceil((((neuroticism < user_values[1]).sum())/neuroticism.count()) * 100)
  agreeableness_quantile = math.ceil((((agreeableness < user_values[2]).sum())/agreeableness.count()) * 100)
  conscientiousness_quantile = math.ceil((((conscientiousness < user_values[3]).sum())/conscientiousness.count()) * 100)
  openness_quantile = math.ceil((((openness < user_values[4]).sum())/openness.count()) * 100)
  
  results_for_plot = dict(
    trait = [TRAITS_TRANSLATION['extraversion'], TRAITS_TRANSLATION['neuroticism'], TRAITS_TRANSLATION['agreeableness'], TRAITS_TRANSLATION['conscientiousness'], TRAITS_TRANSLATION['openness']],
    value = [extraversion_quantile, neuroticism_quantile, agreeableness_quantile, conscientiousness_quantile, openness_quantile]
  )
  
  results_for_text = {
    'extraversion': extraversion_quantile,
    'neuroticism': neuroticism_quantile,
    'agreeableness': agreeableness_quantile,
    'conscientiousness': conscientiousness_quantile,
    'openness': openness_quantile,
  }
  
  return [results_for_text, results_for_plot]
  
  

def traverse_results(user_data: Dict) -> Dict:
  user_data['EXT2'] = 6 - user_data['EXT2']
  user_data['EXT4'] = 6 - user_data['EXT4']
  user_data['EXT6'] = 6 - user_data['EXT6']
  user_data['EXT8'] = 6 - user_data['EXT8']
  user_data['EXT10'] = 6 - user_data['EXT10']
  user_data['EST2'] = 6 - user_data['EST2']
  user_data['EST4'] = 6 - user_data['EST4']
  user_data['AGR1'] = 6 - user_data['AGR1']
  user_data['AGR3'] = 6 - user_data['AGR3']
  user_data['AGR5'] = 6 - user_data['AGR5']
  user_data['AGR7'] = 6 - user_data['AGR7']
  user_data['CSN2'] = 6 - user_data['CSN2']
  user_data['CSN4'] = 6 - user_data['CSN4']
  user_data['CSN6'] = 6 - user_data['CSN6']
  user_data['CSN8'] = 6 - user_data['CSN8']
  user_data['OPN2'] = 6 - user_data['OPN2']
  user_data['OPN4'] = 6 - user_data['OPN4']
  user_data['OPN6'] = 6 - user_data['OPN6']
  
  return user_data
