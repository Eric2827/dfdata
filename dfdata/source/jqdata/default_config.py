#dfdata/source/tushare/default_config.py

postfix = '_jq'    #后缀，用于数据库名称
strftime_format = '%Y-%m-%d'   #时间转日期格式
start_date = '20050101'    #开始时间

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
    'XZCE':'郑州商品交易所',
    'XSGE':'上海期货交易所',
    'XDCE':'大连商品交易所',
    'CCFX':'中国金融期货交易所',
}