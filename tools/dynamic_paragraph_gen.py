from borb.pdf import FixedColumnWidthTable
from borb.pdf.canvas.geometry.rectangle import Rectangle

from tools.paragraph_style import *


def table_order_paragraph(page, json):
    order_list: [] = json['productList']

    if len(order_list) < 3:
        print(3)
    else:
        table_order: FixedColumnWidthTable = FixedColumnWidthTable(
            number_of_rows=2,
            number_of_columns=5,
            column_widths=[Decimal(1), Decimal(7.5), Decimal(2.5), Decimal(2.5), Decimal(2.45)],
        )

        for index in range(len(order_list)):
            if index == 2:
                break
            table_order.add(get_paragraph_order_index(f"00{index + 1}", "Helvetica"))
            table_order.add(get_paragraph_order_info(
                f"{order_list[index]['adacvdRate']}" +
                "\n" + f"{order_list[index]['adcvdNo']}" +
                "\n" + f"{order_list[index]['htsusDepict']}" +
                "\n" + f"{order_list[index]['htsusNo']}",
                "Helvetica"))
            table_order.add(get_paragraph_order_info(
                "001",
                "Helvetica"))
            table_order.add(get_paragraph_order_info(
                "001",
                "Helvetica"))
            table_order.add(get_paragraph_order_info(
                "001",
                "Helvetica"))

        table_order.paint(page, Rectangle(Decimal(20),
                                          page.get_page_info().get_height() - Decimal(394),
                                          page.get_page_info().get_width() - Decimal(40),
                                          Decimal(20)
                                          ))
