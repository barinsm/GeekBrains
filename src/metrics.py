#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np



def hit_rate(recommended_list, bought_list):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    flags = np.isin(bought_list, recommended_list)
    
    hit_rate = (flags.sum() > 0) * 1
    
    return hit_rate


def hit_rate_at_k(recommended_list, bought_list, k=5):
    
    # your_code
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    
    flags = np.isin(bought_list, recommended_list)
    
    hit_rate_at_k = (flags.sum() > 0) * 1
    
    return hit_rate_at_k



def precision(recommended_list, bought_list):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    flags = np.isin(bought_list, recommended_list)
    
    precision = flags.sum() / len(recommended_list)
    
    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    bought_list = bought_list  # Тут нет [:k] !!
    if k < len(recommended_list): recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
        
    # your_code
    # Лучше считать через скалярное произведение, а не цикл
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    
    bought_list = bought_list
    if k < len(recommended_list): recommended_list = recommended_list[:k]
    if k < len(prices_recommended): prices_recommended = prices_recommended[:k]
    
    flags = np.isin(recommended_list, bought_list)
    # переставлены местами аргументы, чтобы получить правильный вектор флагов на купленные из рекоменедованных товаров
    # , а именно порядок как в листе рекомендованных товаров и в листе цен на них и их правильное количесвто k в Топ.
        
    precision = np.dot(flags, prices_recommended) / prices_recommended.sum()
    
    return precision



def recall(recommended_list, bought_list):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    flags = np.isin(bought_list, recommended_list)
    
    recall = flags.sum() / len(bought_list)
    
    return recall


def recall_at_k(recommended_list, bought_list, k=5):
    
    # your_code
        
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    bought_list = bought_list  # Тут нет [:k] !!
    if k < len(recommended_list): recommended_list = recommended_list[:k]
    
    flags = np.isin(bought_list, recommended_list)
    
    recall = flags.sum() / len(bought_list)
    
    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    
    # your_code
    
    bought_list = np.array(bought_list)
    prices_bought = np.array(prices_bought)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    
    bought_list = bought_list
    prices_bought = prices_bought
    if k < len(recommended_list): recommended_list = recommended_list[:k]
    if k < len(prices_recommended): prices_recommended = prices_recommended[:k]
    
    flags = np.isin(recommended_list, bought_list)
    # переставлены местами аргументы, чтобы получить правильный вектор флагов на купленные из рекоменедованных товаров
    # , а именно порядок как в листе рекомендованных товаров и в листе цен на них и их правильное количесвто k в Топ.
        
    recall = np.dot(flags, prices_recommended) / prices_bought.sum()    
    return recall


