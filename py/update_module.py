import flask,json   #引入flask和json数据格式化模块
from flask_cors import CORS #引入跨域模块
import py.connectsql
import py.calculate

def update():
    connect = py.connectsql.connect('financial_system')
    cursor = connect.cursor()

    ID = 1
    project_name = 0
    project_type = 0
    contractor_name = 0
    contract_code = 0
    report_code = 0
    report_time = 0
    contract_money = 0
    pay_1st_money = 0
    pay_1st_time = 0
    pay_1st_note = 0
    pay_2nd_money = 0
    pay_2nd_time = 0
    pay_2nd_note = 0
    pay_3rd_money = 0
    pay_3rd_time = 0
    pay_3rd_note = 0
    accounts_rece = 0
    paper_char = 0
    paper_code = 0
    eva_write_name = 0
    sales_name = 0
    sales_commission = 0
    tech_commission = 0
    tech_1st_money = 0
    tech_1st_time = 0
    tech_2nd_money = 0
    tech_2nd_time = 0
    review_fee = 0
    dete_commission = 0
    lab_commission = 0
    business_fee = 0
    other = 0
    agency_fee = 0
    include_review = 0
    business_class = 0
    eva_class = 0
    note = 0
    job_number = 0
    region_coefficient = 0
    industry_type_num = 0
    industry_type_tech = 0
    dete_num = 0
    industry_type_dete = 0

    ID = flask.request.values.get('ID')
    project_name = flask.request.values.get('project_name')
    project_type = flask.request.values.get('project_type')
    contractor_name = flask.request.values.get('contractor_name')
    contract_code = flask.request.values.get('contract_code')
    report_code = flask.request.values.get('report_code')
    report_time = flask.request.values.get('report_time')
    contract_money = flask.request.values.get('contract_money')
    pay_1st_money = flask.request.values.get('pay_1st_money')
    pay_1st_time = flask.request.values.get('pay_1st_time')
    pay_1st_note = flask.request.values.get('pay_1st_note')
    pay_2nd_money = flask.request.values.get('pay_2nd_money')
    pay_2nd_time = flask.request.values.get('pay_2nd_time')
    pay_2nd_note = flask.request.values.get('pay_2nd_note')
    pay_3rd_money = flask.request.values.get('pay_3rd_money')
    pay_3rd_time = flask.request.values.get('pay_3rd_time')
    pay_3rd_note = flask.request.values.get('pay_3rd_note')
    accounts_rece = flask.request.values.get('accounts_rece')
    paper_char = flask.request.values.get('paper_char')
    paper_code = flask.request.values.get('paper_code')
    eva_write_name = flask.request.values.get('eva_write_name')
    sales_name = flask.request.values.get('sales_name')
    sales_commission = flask.request.values.get('sales_commission')
    tech_commission = flask.request.values.get('tech_commission')
    tech_1st_money = flask.request.values.get('tech_1st_money')
    tech_1st_time = flask.request.values.get('tech_1st_time')
    tech_2nd_money = flask.request.values.get('tech_2nd_money')
    tech_2nd_time = flask.request.values.get('tech_2nd_time')
    review_fee = flask.request.values.get('review_fee')
    dete_commission = flask.request.values.get('dete_commission')
    lab_commission = flask.request.values.get('lab_commission')
    business_fee = flask.request.values.get('business_fee')
    other = flask.request.values.get('other')
    agency_fee = flask.request.values.get('agency_fee')
    include_review = flask.request.values.get('include_review')
    business_class = flask.request.values.get('business_class')
    eva_class = flask.request.values.get('eva_class')
    note = flask.request.values.get('note')
    job_number = flask.request.values.get('job_number')
    region_coefficient = flask.request.values.get('region_coefficient')
    industry_type_num = flask.request.values.get('industry_type_num')
    industry_type_tech = flask.request.values.get('industry_type_tech')
    dete_num = flask.request.values.get('dete_num')
    industry_type_dete = flask.request.values.get('industry_type_dete')


    print('数据已接收')
    if business_class:
        t36 = int(business_class)
    else:
        t36 = 0
    if eva_class:
        t37 = int(eva_class)
    else:
        t37 = 0
    if job_number:
        t39 = int(job_number)
    else:
        t39 = 0
    if region_coefficient:
        t40 = int(region_coefficient)
    else:
        t40 = 0
    if industry_type_num:
        t41 = int(industry_type_num)
    else:
        t41 = 0
    if industry_type_tech:
        t42 = int(industry_type_tech)
    else:
        t42 = 0
    if dete_num:
        t43 = int(dete_num)
    else:
        t43 = 0
    if industry_type_dete:
        t44 = int(industry_type_dete)
    else:
        t44 = 0
    if contract_money:
        contract_money = int(contract_money)
    else:
        contract_money = 0
    if pay_1st_money:
        pay_1st_money = int(pay_1st_money)
    else:
        pay_1st_money = 0
    if pay_2nd_money:
        pay_2nd_money = int(pay_2nd_money)
    else:
        pay_2nd_money = 0
    if pay_3rd_money:
        pay_3rd_money = int(pay_3rd_money)
    else:
        pay_3rd_money = 0
    print('数据已转换')
    accounts_rece = contract_money - pay_1st_money - pay_2nd_money - pay_3rd_money
    
    if t37 and t39 and t41 and t42:
        tech_commission = py.calculate.tech_commission(t37,t39,t40,t41,t42)
    else:
        tech_commission = 0
    # eva_class_arg评价类别系数由37评价类别决定
    # job_number_arg工作量系数由39接害岗位数量决定
    # region_coefficient_arg地区系数由40地区系数决定
    # type_num_arg多行业系数由41涉及行业类型决定
    # tech_base_arg提成基数由42行业类型（技术）决定
    
    if report_time:  #第一次提成金额
        tech_1st_money = 0.8 * tech_commission #存在出具时间
    else:
        tech_1st_money = 0

    if accounts_rece == 0: #第二次提成金额
        tech_2nd_money = 0.2 * tech_commission #应收账款为0
    else:
        tech_2nd_money = 0

    # sales_commission = sales_commission - 底价
    
    if t36 and t43 and t44:
        dete_commission = py.calculate.dete_commission(t36,t43,t44)
    else:
        dete_commission = 0
    # 检测部提成=样品系数*行业系数*提成基数*检测部提成比例
    
    if t36 and t43 and t44:
        lab_commission = py.calculate.lab_commission(t36,t43,t44)
    else:
        lab_commission = 0
    # 实验室提成=样品系数*行业系数*提成基数*实验室提成比例
    print('计算完成')
    sql = "UPDATE t_main SET " 

    if project_name:
        sql = sql + "project_name='" + project_name + "',"
    if project_type:
        sql = sql + "project_type='" + project_type + "',"
    if contractor_name:
        sql = sql + "contractor_name='" + contractor_name + "',"
    if contract_code:
        sql = sql + "contract_code='" + contract_code + "',"
    if report_code:
        sql = sql + "report_code='" + report_code + "',"
    if report_time: #datetime
        sql = sql + "report_time='" + report_time + "',"
    if contract_money: #int
        sql = sql + "contract_money='" + str(contract_money) + "',"
    if pay_1st_money:
        sql = sql + "pay_1st_money='" + str(pay_1st_money) + "',"
    if pay_1st_time:
        sql = sql + "pay_1st_time='" + pay_1st_time + "',"
    if pay_1st_note:
        sql = sql + "pay_1st_note='" + pay_1st_note + "',"
    if pay_2nd_money:
        sql = sql + "pay_2nd_money='" + str(pay_2nd_money) + "',"
    if pay_2nd_time:
        sql = sql + "pay_2nd_time='" + pay_2nd_time + "',"
    if pay_2nd_note:
        sql = sql + "pay_2nd_note='" + pay_2nd_note + "',"
    if pay_3rd_money:
        sql = sql + "pay_3rd_money='" + str(pay_3rd_money) + "',"
    if pay_3rd_time:
        sql = sql + "pay_3rd_time='" + pay_3rd_time + "',"
    if pay_3rd_note:
        sql = sql + "pay_3rd_note='" + pay_3rd_note + "',"
    sql = sql + "accounts_rece='" + str(accounts_rece) + "',"
    if paper_char:
        sql = sql + "paper_char='" + paper_char + "',"
    if paper_code:
        sql = sql + "paper_code='" + paper_code + "',"
    if eva_write_name:
        sql = sql + "eva_write_name='" + eva_write_name + "',"
    if sales_commission:
        sql = sql + "sales_commission='" + str(sales_commission) + "',"
    if tech_commission:
        sql = sql + "tech_commission='" + str(tech_commission) + "',"
    if tech_1st_money:
        sql = sql + "tech_1st_money='" + str(tech_1st_money) + "',"
    if tech_1st_time:
        sql = sql + "tech_1st_time='" + tech_1st_time + "',"
    if tech_2nd_money:
        sql = sql + "tech_2nd_money='" + str(tech_2nd_money) + "',"
    if tech_2nd_time:
        sql = sql + "tech_2nd_time='" + tech_2nd_time + "',"
    if review_fee:
        sql = sql + "review_fee='" + str(review_fee) + "',"
    if dete_commission:
        sql = sql + "dete_commission='" + str(dete_commission) + "',"
    if lab_commission:
        sql = sql + "lab_commission='" + str(lab_commission) + "',"
    if business_fee:
        sql = sql + "business_fee='" + str(business_fee) + "',"
    if other:
        sql = sql + "other='" + other + "',"
    if agency_fee:
        sql = sql + "agency_fee='" + str(agency_fee) + "',"
    if include_review:
        sql = sql + "include_review='" + str(include_review) + "',"
    if business_class:
        sql = sql + "business_class='" + str(business_class) + "',"
    if eva_class:
        sql = sql + "eva_class='" + str(eva_class) + "',"
    if note:
        sql = sql + "note='" + note + "',"
    if job_number:
        sql = sql + "job_number='" + str(job_number) + "',"
    if region_coefficient:
        sql = sql + "region_coefficient='" + str(region_coefficient) + "',"
    if industry_type_num:
        sql = sql + "industry_type_num='" + str(industry_type_num) + "',"
    if industry_type_tech:
        sql = sql + "industry_type_tech='" + str(industry_type_tech) + "',"
    if dete_num:
        sql = sql + "dete_num='" + str(dete_num) + "',"
    if industry_type_dete:
        sql = sql + "industry_type_dete='" + str(industry_type_dete) + "',"


    sql = sql.rstrip(',') + ' WHERE ID'  + '=' + str(ID)
    print(sql)
    cursor.execute(sql)
    print('sql执行完成')
    connect.commit()
    cursor.close()   
    connect.close()
    print('finish')
    if connect.close:
        res = {'success':'true','msg': '修改成功'}
    else:
        res = {'success':'false','msg': '修改失败'}
    
    return json.dumps(res,ensure_ascii=False)