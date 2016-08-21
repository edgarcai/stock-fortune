import tushare as ts
import sys
from sqlalchemy import create_engine

ENGINE = create_engine('mysql+pymysql://root:123456@localhost/stockdb?charset=utf8')

#行业分类信息
def industrytodb():
	#获取sina行业分类信息
	industry_sina = ts.get_industry_classified("sina")
	print(industry_sina, sep=' ', end='\n', file=sys.stdout, flush=False)
	#获取申万行业分类信息
	industry_sw = ts.get_industry_classified("sw")
	print(industry_sw, sep=' ', end='\n', file=sys.stdout, flush=False)
	print("连接数据库", sep=' ', end='\n', file=sys.stdout, flush=False)
	print(engine, sep=' ', end='\n', file=sys.stdout, flush=False)
	industry_sina.to_sql('industry_sina_data',ENGINE)
	industry_sw.to_sql('industry_sw_data',ENGINE)

#概念分类信息
def conceptdb():
	concept_sina = ts.get_concept_classified()
	print(concept_sina, sep=' ', end='\n', file=sys.stdout, flush=False)
	concept_sina.to_sql('concept_sina_data',ENGINE)

#区域信息
def areadb():
	area_sina = ts.get_area_classified()
	print(area_sina, sep=' ', end='\n', file=sys.stdout, flush=False)
	area_sina.to_sql('area_sina_data',ENGINE)

#中小板信息
def smedb():
	sme = ts.get_sme_classified()
	print(sme, sep=' ', end='\n', file=sys.stdout, flush=False)
	sme.to_sql('sme_data',ENGINE)

#创业板信息
def gmedb():
	gme = ts.get_gem_classified()
	print(gme)
	gme.to_sql('gme_data',ENGINE)

#风险警示板：
def stdb():
	st = ts.get_st_classified()
	print(st)
	st.to_sql('st_data',ENGINE)

#沪深300成分及权重
def hs300db():
	hs300 = ts.get_hs300s()
	print(hs300)
	hs300.to_sql('hs300_data',ENGINE)

#上证50成分股
def sz50db():
	sz50 = ts.get_sz50s()
	print(sz50, sep=' ', end='\n', file=sys.stdout, flush=False)
	sz50.to_sql('sz50_data',ENGINE)

#中证500成分股
def zz500db():
	zz500 = ts.get_zz500s()
	print(zz500, sep=' ', end='\n', file=sys.stdout, flush=False)
	zz500.to_sql('zz500_data',ENGINE)

#终止上市股票
def terminateddb():
	terminated = ts.get_terminated()
	print(terminated, sep=' ', end='\n', file=sys.stdout, flush=False)
	terminated.to_sql('terminated_data',ENGINE)

#暂停上市股票列表
def suspendeddb():
	suspended = ts.get_suspended()
	print(suspended)
	suspended.to_sql('suspended_data',ENGINE)

#股票分类信息，收盘后更新
if __name__ == '__main__':
	# 获取sina和申万行业分类信息，每日一更
	industrytodb()
	#获取概念分类，每日一更
	conceptdb()
	#获取区域信息,每日一更
	areadb()
	#中小板信息
	smedb()
	#创业板信息
	gmedb()
	#风险警示板
	stdb()
	#沪深300成分及权重
	hs300db()
	#上证50成分股
	sz50db()
	#中证500成分股
	zz500db()
	#终止上市股票列表
	terminateddb()
	#暂停上市股票列表
	suspendeddb()
	#todo:日志系统、监测重启功能、定时任务功能
