import flask,json   #引入flask和json数据格式化模块
from flask_cors import CORS #引入跨域模块
import py.connectsql
import datetime

def query():
    ID = 0
    project_name = 0
    project_type = 0
    contractor_name = 0
    contract_code = 0
    report_code = 0
    report_time1 = 0
    report_time2 = 0
    contract_money1 = 0
    contract_money2 = 0
    pay_1st_money1 = 0
    pay_1st_money2 = 0
    pay_1st_time1 = 0
    pay_1st_time2 = 0
    pay_2nd_money1 = 0
    pay_2nd_money2 = 0
    pay_2nd_time1 = 0
    pay_2nd_time2 = 0
    pay_3rd_money1 = 0
    pay_3rd_money2 = 0
    pay_3rd_time1 = 0
    pay_3rd_time2 = 0
    accounts_rece1 = 0
    accounts_rece2 = 0
    paper_char = 0
    paper_code = 0
    eva_write_name = 0
    sales_name = 0
    #每一个字段需要提前声明
    ID = flask.request.values.get('ID')
    project_name = flask.request.values.get('project_name')#获取前端参数
    project_type = flask.request.values.get('project_type')
    contractor_name = flask.request.values.get('contractor_name')
    contract_code = flask.request.values.get('contract_code')
    report_code = flask.request.values.get('report_code')
    report_time1 = flask.request.values.get('report_time1')
    report_time2 = flask.request.values.get('report_time2')
    contract_money1 = flask.request.values.get('contract_money1')
    contract_money2 = flask.request.values.get('contract_money2')
    pay_1st_money1 = flask.request.values.get('pay_1st_money1')
    pay_1st_money2 = flask.request.values.get('pay_1st_money2')
    pay_1st_time1 = flask.request.values.get('pay_1st_time1')
    pay_1st_time1 = flask.request.values.get('pay_1st_time1')
    pay_2nd_money1 = flask.request.values.get('pay_2nd_money1')
    pay_2nd_money2 = flask.request.values.get('pay_2nd_money2')
    pay_2nd_time1 = flask.request.values.get('pay_2nd_time1')
    pay_2nd_time2 = flask.request.values.get('pay_2nd_time2')
    pay_3rd_money1 = flask.request.values.get('pay_3rd_money1')
    pay_3rd_money2 = flask.request.values.get('pay_3rd_money2')
    pay_3rd_time1 = flask.request.values.get('pay_3rd_time1')
    pay_3rd_time2 = flask.request.values.get('pay_3rd_time2')
    accounts_rece1 = flask.request.values.get('accounts_rece1')
    accounts_rece2 = flask.request.values.get('accounts_rece2')
    paper_char = flask.request.values.get('paper_char')
    paper_code = flask.request.values.get('paper_code')
    eva_write_name = flask.request.values.get('eva_write_name')
    sales_name = flask.request.values.get('sales_name')
    def query():
        connect = py.connectsql.connect('financial_system')
        cursor = connect.cursor()
        sql = "select * from t_main WHERE isvaild=1"
        if ID:  # ID
            sql = sql + ' AND ID=' + str(ID)
        if project_name:  #1.		project_name
            sql = sql + " AND project_name LIKE '%" + project_name + "%'"
        if project_type: #2.		project_type
            sql = sql + " AND project_type LIKE '%" + project_type + "%'"
        if contractor_name: #3.		contractor_name
            sql = sql + " AND contractor_name LIKE '%" + contractor_name + "%'"
        if contract_code: #4.		contractor_name
            sql = sql + " AND contract_code LIKE '%" + contract_code + "%'"
        if report_code: #5.		report_code
            sql = sql + " AND report_code LIKE '%" + report_code + "%'"
        if report_time1 and report_time2: #6.		report_time
            sql = sql + " AND report_time BETWEEN '" + str(report_time1) + "' AND '" + str(report_time2) + "'"
        if contract_money1 and contract_money2: #7.		contract_money
            sql = sql + " AND contract_money BETWEEN " + str(contract_money1) + " AND " + str(contract_money2)
        if pay_1st_money1 and pay_1st_money2: #8.		pay_1st_money
            sql = sql + " AND pay_1st_money BETWEEN " + str(pay_1st_money1) + " AND " + str(pay_1st_money2)
        if pay_1st_time1 and pay_1st_time2: #9.		pay_1st_time
            sql = sql + " AND pay_1st_time BETWEEN '" + str(pay_1st_time1) + "' AND '" + str(pay_1st_time2) + "'"
        if pay_2nd_money1 and pay_2nd_money2: #10.		pay_2nd_money
            sql = sql + " AND pay_2nd_money BETWEEN " + str(pay_2nd_money1) + " AND " + str(pay_2nd_money1)
        if pay_2nd_time1 and pay_2nd_time2: #11.		pay_2nd_time
            sql = sql + " AND pay_2nd_time BETWEEN '" + str(pay_2nd_time1) + "' AND '" + str(pay_2nd_time) + "'"
        if pay_3rd_money1 and pay_3rd_money2: #12.		pay_3rd_money
            sql = sql + " AND pay_3rd_money BETWEEN " + str(pay_3rd_money1) + " AND " + str(pay_3rd_money2)
        if pay_3rd_time1 and pay_3rd_time2: #13.		pay_3rd_time
            sql = sql + " AND pay_3rd_time BETWEEN '" + str(pay_3rd_time1) + "' AND '" + str(pay_3rd_time2) + "'"
        if accounts_rece1 and accounts_rece2: #14.		accounts_rece
            sql = sql + " AND accounts_rece BETWEEN " + str(accounts_rece1) + " AND " + str(accounts_rece2)
        if paper_char: #15.		paper_char
            sql = sql + " AND paper_char LIKE '%" + paper_char + "%'"
        if paper_code: #16.		paper_code
            sql = sql + " AND paper_code LIKE '%" + paper_code + "%'"
        if eva_write_name: #17.		eva_write_name
            sql = sql + " AND eva_write_name LIKE '%" + eva_write_name + "%'"
        if sales_name: #18.		sales_name
            sql = sql + " AND sales_name LIKE '%" + sales_name + "%'"
        
        
    
        cursor.execute(sql)
        print('sql执行完成')   
        list1 = []
        row = cursor.fetchall()  #读取查询结果
        for i in range(0,len(row)):
            value = list(row[i])
            for j in range(0,len(value)):
                if type(value[j]) ==  datetime.date:
                    value[j] = value[j].strftime('%Y-%m-%d')
            key = ['ID','project_name','project_type','contractor_name','contract_code','report_code','report_time','contract_money','pay_1st_money','pay_1st_time','pay_1st_note','pay_2nd_money','pay_2nd_time','pay_2nd_note','pay_3rd_money','pay_3rd_time','pay_3rd_note','accounts_rece','paper_char','paper_code','eva_write_name','sales_name','sales_commission','tech_commission','tech_1st_money','tech_1st_time','tech_2nd_money','tech_2nd_time','review_fee','dete_commission','lab_commission','business_fee','other','agency_fee','include_review','business_class','eva_class','note','job_number','region_coefficient','industry_type_num','industry_type_tech','dete_num','industry_type_dete']
            dict1 = dict(zip(key,value))
            list1.append(dict1)
                

        cursor.close()   
        connect.close()
        
        return list1

    result = query()
    
    res = result
    #res数据
    print('query finish')
    return json.dumps(res,ensure_ascii=False)