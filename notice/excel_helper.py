import xlsxwriter
import os
from io import BytesIO
from .models import First_Notice, Periodical_Notice
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse
from django.utils.translation import ugettext

def create_periodical_notice(notice_id):
    notice = Periodical_Notice.objects.get(id=notice_id)
    nid = get_value(notice, notice_id, "notice_id")
    pnum = get_value(notice, notice_id, "period_num")
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet('缴款单')
    worksheet_s.set_column('A:E', 20)
    #TODO: insert image
    # print(str(os.path.isfile(static('logos/huahai_periodical.png'))))
    # worksheet_s.insert_image('A2', static('logos/huahai_periodical.png'))
    title = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 16,
        #'align': 'center',
        'valign': 'vcenter'
    })
    normal_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'valign': 'vcenter',
        'align': 'left',
    })
    border_round = workbook.add_format({
        'border':1
    })
    worksheet_s.merge_range(get_range('B', 2, 'E', 2), "华海电脑数码通讯广场连锁股份有限公司缴款通知单", title)
    worksheet_s.write(get_cell('B',3), "通知日期：", normal_text)
    worksheet_s.write(get_cell('D',3), "单据编号：", normal_text)

    worksheet_s.write(get_cell('A',5), "商家名称：", normal_text)
    worksheet_s.write(get_cell('C',5), "席位号：", normal_text)
    worksheet_s.write(get_cell('A',6), "缴款内容： ", normal_text)
    worksheet_s.write(get_cell('A',7), "缴款项目： ", normal_text)
    worksheet_s.write(get_cell('A',8), "结算起止日期： ", normal_text)
    worksheet_s.write(get_cell('A',9), "缴款金额（小写）： ", normal_text)
    worksheet_s.write(get_cell('A',10), "（大写）：", normal_text)
    worksheet_s.write(get_cell('A',12), "本期截止缴款时间：", normal_text)

    worksheet_s.merge_range(get_range('A', 13, 'E', 13), "逾期未缴滞纳金计算公式如下：租金金额*天数*千分之一＝滞纳金", normal_text)
    worksheet_s.merge_range(get_range('A', 14, 'E', 14), "收件人盖章：", normal_text)
    worksheet_s.merge_range(get_range('A', 15, 'E', 15), "签字：", normal_text)

    date_obj = get_value(notice, notice_id, "date_released")
    date_released_text = str(date_obj.year) + "年" + str(date_obj.month) + "月" +  str(date_obj.day) + "日"
    worksheet_s.write(get_cell('C',3), date_released_text, normal_text)
    worksheet_s.write(get_cell('E',3), nid, normal_text)

    worksheet_s.write(get_cell('B',5), get_value(notice, notice_id, "cname"), normal_text)
    worksheet_s.merge_range(get_range('D', 5, 'E', 5), get_value(notice, notice_id, "loc_code"), normal_text)
    worksheet_s.merge_range(get_range('B', 6, 'E', 6), "租金", normal_text)
    worksheet_s.merge_range(get_range('B', 7, 'E', 7), "第 " + str(get_value(notice, notice_id, "period_num")) + " 期", normal_text)
    sdate_obj = get_value(notice, notice_id, "payment_start_date")
    edate_obj = get_value(notice, notice_id, "payment_end_date")
    worksheet_s.merge_range(get_range('B', 8, 'E', 8), sdate_obj.strftime('%Y-%m-%d') + " - " + edate_obj.strftime('%Y-%m-%d'), normal_text)
    worksheet_s.merge_range(get_range('B', 9, 'E', 9), "¥" + str(get_value(notice, notice_id, "total_amount")), normal_text)
    worksheet_s.merge_range(get_range('B', 10, 'E', 10), "", normal_text)
    worksheet_s.merge_range(get_range('B', 12, 'E', 12), get_value(notice, notice_id, "deadline").strftime('%Y-%m-%d'), normal_text)

    worksheet_s.conditional_format(get_range('A', 5, 'E', 5), { 'type' : 'no_blanks' , 'format' : border_round} )
   #worksheet_s.conditional_format(get_range('A', 6, 'E', 10), { 'type' : 'no_blanks' , 'format' : border_round} )

    #box(workbook, worksheet_s, 4, 0, 9, 4)
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data, nid, pnum

def create_first_notice(notice_id):
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet('缴款单')
    worksheet_s.set_column('A:B', 20)
    worksheet_s.set_column('O:O', 25)
    title = workbook.add_format({
        'font_name':'Cambria',
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'valign': 'vcenter'
    })
    bold_header = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'bold': True,
        'valign': 'vcenter'
    })
    red_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'color' : 'red',
        'valign': 'vcenter',
        'align' : 'left',
    })
    num_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'color' : 'red',
        'valign': 'vcenter',
        'align' : 'left',
        'num_format': '0.00',
    })
    bold_red_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'bold': True,
        'color' : 'red',
        'valign': 'vcenter',
        'align' : 'left',
        'num_format': '0.00'
    })
    normal_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'align': 'center',
        'valign': 'vcenter'
    })
    right_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'align': 'right',
        'valign': 'vcenter'
    })
    bold_right_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 10,
        'align': 'right',
        'valign': 'vcenter',
        'bold': True,
    })
    border_format = workbook.add_format({
        'bottom':1
    })
    right_border_format = workbook.add_format({
        'right':1
    })
    vertical_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 9,
        'align': 'center',
        'valign': 'vcenter'
    })
    #vertical_text.set_rotation(90)
    vertical_bold_text = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 9,
        'align': 'center',
        'valign': 'vcenter',
        'bold': True,
        'text_wrap':True,
    })
    dash_border = workbook.add_format({
        'border': 3,
        'bottom': 1,
    })

    nid = write_notice(notice_id, worksheet_s, 0, title, header, bold_header, red_text, num_text, bold_red_text, normal_text, right_text, bold_right_text, border_format,right_border_format)
    # worksheet_s.conditional_format(get_range('A', 18, 'S', 18), { 'type' : 'no_blanks' , 'format' : dash_border} )
    # worksheet_s.conditional_format(get_range('A', 37, 'S', 37), { 'type' : 'no_blanks' , 'format' : dash_border} )

    write_notice(notice_id, worksheet_s, 19, title, header, bold_header, red_text, num_text, bold_red_text, normal_text, right_text, bold_right_text, border_format,right_border_format)
    write_notice(notice_id, worksheet_s, 38, title, header, bold_header, red_text, num_text, bold_red_text, normal_text, right_text, bold_right_text, border_format,right_border_format)
    
    worksheet_s.merge_range(get_range('O', 3, 'O', 17), "第一联：客户联", vertical_text)
    worksheet_s.merge_range(get_range('P', 3, 'Q', 6), "友情提醒：", vertical_bold_text)
    worksheet_s.merge_range(get_range('P', 7, 'Q', 17), "缴款时请附带此单至我广场财务部，谢谢配合！", vertical_bold_text)
    worksheet_s.merge_range(get_range('O', 22, 'O', 36), "第二联：财务联", vertical_text)
    worksheet_s.merge_range(get_range('O', 41, 'O', 55), "第三联：存根联", vertical_text)

    #财务回执联
    bold_normal = workbook.add_format({
        'font_name':'Cambria',
        'font_size': 12,
        'bold': True,
        'align': 'center',
        'valign': 'vcenter'
    })
    border_round = workbook.add_format({
        'border':1
    })
    worksheet_s.merge_range(get_range('Q', 20, 'S', 20), "财务回执联", bold_normal)
    worksheet_s.conditional_format(get_range('Q', 20, 'S', 36), { 'type' : 'no_blanks' , 'format' : border_round} )
    worksheet_s.merge_range(get_range('Q', 21, 'R', 22), "席位号", normal_text)
    worksheet_s.merge_range(get_range('S', 21, 'S', 22), " ", normal_text)
    worksheet_s.merge_range(get_range('Q', 23, 'R', 24), "实际收款日", normal_text)
    worksheet_s.merge_range(get_range('S', 23, 'S', 24), " ", normal_text)
    worksheet_s.merge_range(get_range('Q', 25, 'R', 26), "收款单编号", normal_text)
    worksheet_s.merge_range(get_range('S', 25, 'S', 26), " ", normal_text)
    worksheet_s.merge_range(get_range('Q', 27, 'R', 32), "收款方式", normal_text)
    worksheet_s.merge_range(get_range('S', 27, 'S', 28), "□支 票", normal_text)
    worksheet_s.merge_range(get_range('S', 29, 'S', 30), "□现 金", normal_text)
    worksheet_s.merge_range(get_range('S', 31, 'S', 32), "□充 抵", normal_text)
    worksheet_s.merge_range(get_range('Q', 33, 'R', 34), "收款金额", normal_text)
    worksheet_s.merge_range(get_range('S', 33, 'S', 34), " ", normal_text)
    worksheet_s.merge_range(get_range('Q', 35, 'R', 36), "收款人", normal_text)
    worksheet_s.merge_range(get_range('S', 35, 'S', 36), " ", normal_text)

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data, nid

def write_notice(notice_id, worksheet_s, offset, title, header, bold_header, red_text, num_text, 
bold_red_text, normal_text, right_text, bold_right_text, border_format,right_border_format):
    notice = First_Notice.objects.get(id=notice_id)
    title_text = u"{0} {1}".format(ugettext(""), "缴 款 通 知 单")
    worksheet_s.merge_range(get_range('A', 1+offset, 'N', 1+offset), title_text, title)

    date_obj = get_value(notice, notice_id, "date_released")
    date_released_text = str(date_obj.year) + "年" + str(date_obj.month) + "月" +  str(date_obj.day) + "日"
    worksheet_s.merge_range(get_range('A', 2+offset, 'J', 2+offset), "下单日期：" + date_released_text, normal_text)

    worksheet_s.merge_range(get_range('K', 2+offset, 'L', 2+offset), "单据编号：", normal_text)
    worksheet_s.merge_range(get_range('M', 2+offset, 'N', 2+offset), get_value(notice,notice_id, "notice_id"), red_text)

    #adding headers...
    worksheet_s.write(get_cell('A',3+offset), "经销商名称：", header)
    worksheet_s.write(get_cell('A',4+offset), "1、缴款时段：", header)
    worksheet_s.merge_range(get_range('A', 5+offset, 'N', 5+offset), "2、合同缴款内容：", header)
    worksheet_s.merge_range(get_range('A', 6+offset, 'A', 7+offset), "  ①租赁费：      ", header)
    worksheet_s.write(get_cell('A',8+offset), "  ②统一推广费：        ", header)
    worksheet_s.write(get_cell('A',9+offset), "3、履约保证金差额： ", header)
    worksheet_s.merge_range(get_range('A', 10+offset, 'F', 10+offset), "", header)
    worksheet_s.write(get_cell('A',11+offset), "     以上费用总计：", header)
    worksheet_s.merge_range(get_range('A', 12+offset, 'F', 12+offset), "4、经销商另需支付：", header)
    worksheet_s.write(get_cell('A',13+offset), " ①上网费：", header)
    worksheet_s.write(get_cell('A',14+offset), " ②超用电费：", header)
    worksheet_s.write(get_cell('A',15+offset), "本次缴款总金额：  ", bold_header)
    worksheet_s.write(get_cell('A',16+offset), "5、经销商请于", header)
    worksheet_s.merge_range(get_range('A', 17+offset, 'N', 17+offset), "滞纳金计算公式如下：总金额*天数*千分之一＝滞纳金", header)
    worksheet_s.merge_range(get_range('E', 16+offset, 'N', 16+offset), "前全额支付上述款项。逾期需按以下公式支付滞纳金。", header)

    worksheet_s.merge_range(get_range('I', 3+offset, 'J', 3+offset), "席位号：", header)
    worksheet_s.write(get_cell('C',4+offset), "年", header)
    worksheet_s.write(get_cell('E',4+offset), "月", header)
    worksheet_s.merge_range(get_range('G', 4+offset, 'H', 4+offset), "日至", header)
    worksheet_s.write(get_cell('J',4+offset), "年", header)
    worksheet_s.write(get_cell('L',4+offset), "月", header)
    worksheet_s.write(get_cell('N',4+offset), "日", header)
    worksheet_s.merge_range(get_range('F', 6+offset, 'N', 7+offset), "元/" + str(get_value(notice,notice_id, "payment_cycle")) + "个月", header)
    worksheet_s.merge_range(get_range('F', 8+offset, 'N', 8+offset), "元/年", header)
    worksheet_s.write(get_cell('F',9+offset), "元", header)
    worksheet_s.write(get_cell('N',9+offset), "元", header)
    worksheet_s.write(get_cell('N',10+offset), "元", header)
    worksheet_s.merge_range(get_range('G', 9+offset, 'J', 9+offset), "应退18年度保证金：", header)
    worksheet_s.merge_range(get_range('G', 10+offset, 'J', 10+offset), "应退18年度保证金：", header)
    worksheet_s.merge_range(get_range('F', 11+offset, 'N', 11+offset), "元", header)
    worksheet_s.merge_range(get_range('F', 13+offset, 'N', 13+offset), "元/年  ", header)
    worksheet_s.merge_range(get_range('F', 14+offset, 'N', 14+offset), "元/年  ", header)
    worksheet_s.merge_range(get_range('F', 15+offset, 'N', 15+offset), "元", bold_header)

    worksheet_s.merge_range(get_range('B', 6+offset, 'B', 7+offset), "¥", right_text)
    worksheet_s.write(get_cell('B',8+offset), "¥", right_text)
    worksheet_s.write(get_cell('B',9+offset), "¥", right_text)
    worksheet_s.write(get_cell('B',11+offset), "¥", right_text)
    worksheet_s.write(get_cell('B',13+offset), "¥", right_text)
    worksheet_s.write(get_cell('B',14+offset), "¥", right_text)
    worksheet_s.write(get_cell('K',9+offset), "¥", right_text)
    worksheet_s.write(get_cell('K',10+offset), "¥", right_text)
    worksheet_s.write(get_cell('B',15+offset), "¥", right_text)
    #adding data...
    worksheet_s.merge_range(get_range('B', 3+offset, 'H', 3+offset), get_value(notice,notice_id, "cname"), red_text)
    worksheet_s.merge_range(get_range('K', 3+offset, 'N', 3+offset), get_value(notice,notice_id, "loc_code"), red_text)

    sdate_obj = get_value(notice, notice_id, "payment_start_date")
    worksheet_s.write(get_cell('B',4+offset), sdate_obj.year, red_text)
    worksheet_s.write(get_cell('D',4+offset), sdate_obj.month, red_text)
    worksheet_s.write(get_cell('F',4+offset), sdate_obj.day, red_text)

    edate_obj = get_value(notice,notice_id, "payment_start_date")
    worksheet_s.write(get_cell('I',4+offset), edate_obj.year, red_text)
    worksheet_s.write(get_cell('K',4+offset), edate_obj.month, red_text)
    worksheet_s.write(get_cell('M',4+offset), edate_obj.day, red_text)
    
    worksheet_s.merge_range(get_range('C', 6+offset, 'E', 7+offset), get_value(notice,notice_id, "total_rent"), num_text)
    worksheet_s.merge_range(get_range('C', 8+offset, 'E', 8+offset), get_value(notice,notice_id, "promotion_fee"), num_text)
    #TODO: 履约保证金水电网

    worksheet_s.merge_range(get_range('C', 11+offset, 'E', 11+offset), get_value(notice,notice_id, "total_amount"), num_text)
    worksheet_s.merge_range(get_range('C', 15+offset, 'E', 15+offset), get_value(notice,notice_id, "total_amount"), bold_red_text)

    ddl_obj = get_value(notice, notice_id, "deadline")
    worksheet_s.merge_range(get_range('B', 16+offset, 'D', 16+offset), ddl_obj.strftime('%Y-%m-%d'), normal_text)

    worksheet_s.conditional_format(get_range('A', 2+offset, 'N', 2+offset), { 'type' : 'no_blanks' , 'format' : border_format} )
    worksheet_s.conditional_format(get_range('A', 3+offset, 'N', 3+offset), { 'type' : 'no_blanks' , 'format' : border_format} )
    worksheet_s.conditional_format(get_range('A', 4+offset, 'N', 4+offset), { 'type' : 'no_blanks' , 'format' : border_format} )
    worksheet_s.conditional_format(get_range('A', 11+offset, 'N', 11+offset), { 'type' : 'no_blanks' , 'format' : border_format} )
    worksheet_s.conditional_format(get_range('A', 14+offset, 'N', 14+offset), { 'type' : 'no_blanks' , 'format' : border_format} )
    worksheet_s.conditional_format(get_range('A', 15+offset, 'N', 15+offset), { 'type' : 'no_blanks' , 'format' : border_format} )
    worksheet_s.conditional_format(get_range('A', 17+offset, 'N', 17+offset), { 'type' : 'no_blanks' , 'format' : border_format} )
   # worksheet_s.conditional_format(get_range('N', 3+offset, 'N', 17+offset), { 'type' : 'no_blanks' , 'format' : right_border_format} )
    return get_value(notice, notice_id, "notice_id")

def get_value(notice, notice_id, field_name):
    field_value = getattr(notice, field_name)
    return field_value

def get_range(l1, n1, l2, n2):
    return l1 + str(n1) + ':' + l2 + str(n2)

def get_cell(l, n):
    return l + str(n)

# def box(workbook, sheet_name, row_start, col_start, row_stop, col_stop):
#     """Makes an RxC box. Use integers, not the 'A1' format"""

#     rows = row_stop - row_start + 1
#     cols = col_stop - col_start + 1

#     for x in range((rows) * (cols)): # Total number of cells in the rectangle

#         box_form = workbook.add_format()   # The format resets each loop
#         row = row_start + (x // cols)
#         column = col_start + (x % cols)

#         if x < (cols):                     # If it's on the top row
#             box_form = add_to_format(box_form, {'top':1}, workbook)
#         if x >= ((rows * cols) - cols):    # If it's on the bottom row
#             box_form = add_to_format(box_form, {'bottom':1}, workbook)
#         if x % cols == 0:                  # If it's on the left column
#             box_form = add_to_format(box_form, {'left':1}, workbook)
#         if x % cols == (cols - 1):         # If it's on the right column
#             box_form = add_to_format(box_form, {'right':1}, workbook)

#         sheet_name.write(row, column, "", box_form)

# def add_to_format(existing_format, dict_of_properties, workbook):
#     """Give a format you want to extend and a dict of the properties you want to
#     extend it with, and you get them returned in a single format"""
#     new_dict={}
#     for key, value in existing_format.__dict__.items():
#         if (value != 0) and (value != {}) and (value != None):
#             new_dict[key]=value
#     del new_dict['escapes']
#     d = new_dict.copy()
#     d.update(dict_of_properties)
#     return(workbook.add_format(d)))