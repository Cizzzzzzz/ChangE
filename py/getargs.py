def eva_class_arg(t37):
    if t37 == 1:
        eva_class_arg = 1
    elif t37 == 2:
        eva_class_arg = 1.3
    elif t37 == 3:
        eva_class_arg = 1.2
    elif t37 == 4:
        eva_class_arg = 1.5
    return eva_class_arg
# eva_class_arg评价类别系数由37评价类别决定

def job_number_arg(t39):
    if 1 <= t39 < 10:
        job_number_arg = 0
    elif 11 < t39 < 15:
        job_number_arg = 0.1
    elif 16 < t39 < 20:
        job_number_arg = 0.2
    elif 21 < t39 < 25:
        job_number_arg = 0.3
    elif 26 < t39 < 30:
        job_number_arg = 0.4
    elif 31 < t39 < 35:
        job_number_arg = 0.5
    elif t39 > 36:
        job_number_arg = 0.6
    return job_number_arg
# job_number_arg工作量系数由39接害岗位数量决定

def region_coefficient_arg(t40):
    if t40 == 0:
        region_coefficient_arg = 0
    elif t40 == 1:
        region_coefficient_arg = 0.1
    return region_coefficient_arg
# region_coefficient_arg地区系数由40地区系数决定

def type_num_arg(t41):
    if t41 == 1:
        type_num_arg = 0
    elif t41 == 2:
        type_num_arg = 0.3
    elif t41 == 3:
        type_num_arg = 0.5
    elif t41 == 4:
        type_num_arg = 0.6
    return type_num_arg
# type_num_arg多行业系数由41涉及行业类型决定

def tech_base_arg(t42):
    if t42 == 1:
        tech_base_arg = 700
    elif t42 == 2:
        tech_base_arg = 1100
    elif t42 == 3:
        tech_base_arg = 1200
    elif t42 == 4:
        tech_base_arg = 1300
    elif t42 == 5:
        tech_base_arg = 1500
    elif t42 == 6:
        tech_base_arg = 1700
    elif t42 == 7:
        tech_base_arg = 1800
    elif t42 == 8:
        tech_base_arg = 2000
    return tech_base_arg
# tech_base_arg提成基数由42行业类型（技术）决定

def dete_num_arg(t36,t43):
    if t36 == 1:
        if t43 < 20:
            dete_num_arg = 0.75
        elif  20<= t43 <= 60:
            dete_num_arg = 1
        elif t43 > 60:
            dete_num_arg = t43/60
    if t36 == 2:
        if t43 < 60:
            dete_num_arg = 0.75
        elif 60 <= t43 <= 200:
            dete_num_arg = 1
        elif t43 > 200:
            dete_num_arg = t43/200
    return dete_num_arg
# dete_num_arg样品系数由36业务分类和43检测样品数决定

def industry_arg(t44):
    if t44 == 1:
        industry_arg = 1
    elif t44 == 2:
        industry_arg = 2
    return industry_arg
# industry_arg行业系数由行业系数决定(实验室行业系数默认为1）

def dete_base_arg(t36):
    if t36 == 1:
        dete_base_arg = 3500
    if t36 == 2:
        dete_base_arg = 15000
    return dete_base_arg
# dete_base_arg提成基数由36业务分类决定

def dete_commission_percentage(t36):
    if t36 == 1:
        dete_commission_percentage = 0.05
    if t36 == 2:
        dete_commission_percentage = 0.025
    return dete_commission_percentage
# dete_commission_percentage由36业务分类决定

def lab_commission_percentage(t36):
    if t36 == 1:
        lab_commission_percentage = 0.035
    if t36 == 2:
        lab_commission_percentage = 0.018
    return lab_commission_percentage
# lab_commission_percentage由36业务分类决定
