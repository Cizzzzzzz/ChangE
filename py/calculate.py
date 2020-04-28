import py.getargs

t37 = 3
t39 = 22
t40 = 1
t41 = 2
t42 = 3
t36 = 1
t43 = 50
t44 = 2
ID = 1

def tech_commission(t37,t39,t40,t41,t42):
    tech_commission = (py.getargs.eva_class_arg(t37) + py.getargs.job_number_arg(t39) + py.getargs.region_coefficient_arg(t40) + py.getargs.type_num_arg(t41)) * py.getargs.tech_base_arg(t42)
    return float('%.2f' %(tech_commission))
# 技术部提成（评价部提成）=（评价类别系数+工作量系数+地区系数+多行业系数）*提成基数
# eva_class_arg评价类别系数由37评价类别决定
# job_number_arg工作量系数由39接害岗位数量决定
# region_coefficient_arg地区系数由40地区系数决定
# type_num_arg多行业系数由41涉及行业类型决定
# tech_base_arg提成基数由42行业类型（技术）决定

# # sales_commission = sales_commission - 底价

def dete_commission(t36,t43,t44):
    dete_commission = py.getargs.dete_num_arg(t36,t43) * py.getargs.industry_arg(t44) * py.getargs.dete_base_arg(t36) * py.getargs.dete_commission_percentage(t36)
    return float('%.2f' %(dete_commission))
# 检测部提成=样品系数*行业系数*提成基数*检测部提成比例

def lab_commission(t36,t43,t44): 
    lab_commission = py.getargs.dete_num_arg(t36,t43) * py.getargs.industry_arg(t44) * py.getargs.dete_base_arg(t36) * py.getargs.lab_commission_percentage(t36)
    return float('%.2f' %(lab_commission))
# 实验室提成=样品系数*行业系数*提成基数*实验室提成比例

# print(tech_commission(t37,t40,t41,t42))
# print(tech_1st_money,tech_2nd_money)
# print(dete_commission(t36,t43,t44))
# print(lab_commission(t36,t43,t44))