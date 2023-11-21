from borb.pdf import FixedColumnWidthTable

from tools.paragraph_style import *
from tools.static_paragraph_gen import table_bottom_gen, table_middle4_gen


def table_order_paragraph(table, json, layout):
    order_list: [] = json['productList']

    if len(order_list) < 2:
        table.add(get_table_cell_order_index(f"001", "Helvetica", 1, 1, True, False))
        table.add(get_table_cell_order_info(
            f"{order_list[0]['adacvdRate']}" +
            "\n" + f"{order_list[0]['adcvdNo']}" +
            "\n" + f"{order_list[0]['htsusDepict']}" +
            "\n" + f"{order_list[0]['htsusNo']}" +
            "\n" +
            "\n" +
            "\n",
            "Helvetica", 8, 1, True, False))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 2, 1, True, False))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 3, 1, True, False))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 2, 1, True, False))

        table.add(get_table_cell_order_index("", "Helvetica", 1, 1, False, True))
        table.add(get_table_cell_order_info(
            f"{order_list[0]['adacvdRate']}" +
            "\n" + f"{order_list[0]['adcvdNo']}" +
            "\n" + f"{order_list[0]['htsusDepict']}" +
            "\n" + f"{order_list[0]['htsusNo']}" +
            "\n" +
            "\n" +
            "\n",
            "Helvetica", 8, 1, False, True))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 2, 1, False, True))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 3, 1, False, True))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 2, 1, False, True))

        table_bottom_gen(table, json)

        layout.add(table)
    else:
        for index in range(len(order_list)):
            if index == 2:
                break
            if index == 0:
                table.add(get_table_cell_order_index(f"00{index + 1}", "Helvetica", 1, 1, True, False))
                table.add(get_table_cell_order_info(
                    f"{order_list[index]['adacvdRate']}" +
                    "\n" + f"{order_list[index]['adcvdNo']}" +
                    "\n" + f"{order_list[index]['htsusDepict']}" +
                    "\n" + f"{order_list[index]['htsusNo']}" +
                    "\n" +
                    "\n" +
                    "\n",
                    "Helvetica", 8, 1, True, False))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, True, False))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 3, 1, True, False))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, True, False))
            else:
                table.add(get_table_cell_order_index(f"00{index + 1}", "Helvetica", 1, 1, False, True))
                table.add(get_table_cell_order_info(
                    f"{order_list[index]['adacvdRate']}" +
                    "\n" + f"{order_list[index]['adcvdNo']}" +
                    "\n" + f"{order_list[index]['htsusDepict']}" +
                    "\n" + f"{order_list[index]['htsusNo']}" +
                    "\n" +
                    "\n" +
                    "\n",
                    "Helvetica", 8, 1, False, True))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, False, True))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 3, 1, False, True))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, False, True))

        table_bottom_gen(table, json)

        layout.add(table)

        t: FixedColumnWidthTable = FixedColumnWidthTable(
            number_of_rows=29,
            number_of_columns=16,
            column_widths=[
                Decimal(0.75), Decimal(1.8), Decimal(0.6),
                Decimal(0.5), Decimal(0.5), Decimal(0.35),
                Decimal(0.35), Decimal(0.9), Decimal(0.6),
                Decimal(1), Decimal(0.8), Decimal(0.6),
                Decimal(0.7), Decimal(0.6),
                Decimal(0.9), Decimal(0.9)]
        )

        table_middle4_gen(t)

        layout.add(t)
