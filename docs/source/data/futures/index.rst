期货
============

期货数据保存在如下数据表中：

.. csv-table:: 期货数据表
    :header: "数据表", "名称", "保存函数", "读取函数"
    :widths: 40, 60, 60, 60
    :delim: ; 

    futures_product; 期货品种表; save_futures_product; read_futures_product
    futures_basic; 期货合约表; save_futures_basic; read_futures_basic
    futures_date; 期货日历表; save_futures_date; read_futures_date
    futures_daily; 期货日线表; save_futures_daily; read_futures_daily
    futures_min; 期货分钟表; save_futures_daily; read_futures_daily


期货数据保存时，默认的数据库名称为：

.. csv-table:: 期货数据库名称
    :header: "数据源", "数据库默认名称"
    :widths: 30, 60
    :delim: ;

    tushare ; futures_ts.db
    jqdata;  futures_jq.db

      

.. toctree::
    :maxdepth: 2

    futures_basic
    futures_product
    futures_exchange
    futures_date
    futures_daily