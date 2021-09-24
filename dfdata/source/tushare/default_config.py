#dfdata/source/tushare/default_config.py

postfix = '_ts'    #后缀，用于数据库名称
strftime_format = '%Y%m%d'   #时间转日期格式
start_date = '19900101'    #开始时间

#-------------------------------------------------------------------------------
### 函数参数配置  
#-------------------------------------------------------------------------------

futures_daily = {
    'start_date' : '19960101',
}



################################################################################
### 定义字典 
################################################################################
futures_exchange = {  
    'CZCE':'郑州商品交易所',
    'SHFE':'上海期货交易所',
    'DCE':'大连商品交易所',
    'CFFEX':'中国金融期货交易所',
    'INE':'上海国际能源交易所'    
    
}

stock_exchange = {
     "SSE" : '上海证券交易所',
    "SZSE" : '深圳证券交易所',
}