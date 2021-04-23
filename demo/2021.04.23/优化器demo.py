#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/1/17 14:09
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : 优化器demo.py

import rqdatac
import rqoptimizer2

rqdatac.init()


def generate_stock_pool(date, indicator_series, stock_number):
    order_book_ids = indicator_series.index.tolist()
    industry_classification = rqdatac.zx_instrument_industry(order_book_ids, date)['first_industry_name']
    index_weight = rqdatac.index_weights('000300.XSHG', date)

    # 优先选入沪深300成分股中权重大于3%的股票
    prioritized_stock_pool = index_weight[index_weight >= 0.03].index.tolist()
    prioritized_stock_industry = industry_classification.loc[prioritized_stock_pool]
    remaining_indicator_series = indicator_series.drop(prioritized_stock_pool)
    selected_stock = prioritized_stock_pool
    for i in list(industry_classification.unique()):
        # 除优先选入股票外，在每个行业选取指标得分最高的股票，使得每一个行业股票总数量为5
        industry_prioritized_stock = prioritized_stock_industry[prioritized_stock_industry == i].index.tolist()
        industry_stocks = industry_classification[industry_classification == i].drop(industry_prioritized_stock)
        industry_selected_stock = remaining_indicator_series.loc[industry_stocks.index].sort_values()[
                                  -(stock_number - len(industry_prioritized_stock)):].index.tolist()
        selected_stock = selected_stock + industry_selected_stock
    return selected_stock


bounds = {'*': (0, 0.05)}
date = '2014-07-16'  # 优化日期
# Wildcard的exclude列表为空，即对所有风格/行业设置相同的约束，其中使用中信行业分类
cons = [rqoptimizer2.WildcardIndustryConstraint(lower_limit=-0.01, upper_limit=0.01, relative=True, hard=False,
                                                classification=rqoptimizer2.IndustryClassification.ZX),
        rqoptimizer2.WildcardStyleConstraint(lower_limit=-0.3, upper_limit=0.3, relative=True, hard=False)]

# 获取前一交易日中证800成分股的净利润增长率（TTM）
previous_date = rqdatac.get_previous_trading_date(date)
index_component = rqdatac.index_components('000906.XSHG', previous_date)
indicator_series = rqdatac.get_factor(index_component, 'net_profit_growth_ratio_ttm', previous_date,
                                      previous_date).dropna()
selected_stock = generate_stock_pool(previous_date, indicator_series, stock_number=5)
# 个股指标得分范围调整至0.1-1.1，避免权重过分集中于部分指标得分较大的个股
adjusted_series = ((indicator_series.loc[selected_stock] - indicator_series.loc[selected_stock].min()) / (
        indicator_series.loc[selected_stock].max() - indicator_series.loc[selected_stock].min())) + 0.1
portfolio_weight = rqoptimizer2.portfolio_optimize(selected_stock, date, bnds=bounds, cons=cons,
                                                   benchmark='000300.XSHG', objective=rqoptimizer2.MaxIndicator(
        indicator_series=adjusted_series))
