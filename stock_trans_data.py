import tushare as ts
import sys
from sqlalchemy import create_engine

ENGINE = create_engine('mysql+pymysql://root:123456@localhost/stockdb?charset=utf8')

if __name__ == '__main__':
	