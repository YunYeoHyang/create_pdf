from borb.pdf import FixedColumnWidthTable

from tools.paragraph_style import *
from tools.static_paragraph_gen import table_bottom_gen, table_middle4_gen


def table_order_paragraph(table, json, layout, page):
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
            "Helvetica", 8, 1, True, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 2, 1, True, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 3, 1, True, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info(
            "001",
            "Helvetica", 2, 1, True, False, True, True, Alignment.LEFT))

        table.add(get_table_cell_order_index("", "Helvetica", 1, 1, False, True))
        table.add(get_table_cell_order_info(
            "Totals for Invoice" +
            "\n" + f"14920770213612302" +
            "\n" +
            "\n" +
            "\n" +
            "\n" +
            "\n",
            "Helvetica", 3, 1, False, True, False, True, Alignment.LEFT))
        table.add(get_table_cell_order_info(
            "Invoice Value" +
            "\n" + f"11,397.00 USD" +
            "\n" +
            "\n" +
            "\n" +
            "\n" +
            "\n",
            "Helvetica", 5, 1, False, True, True, False, Alignment.RIGHT))
        table.add(get_table_cell_order_info(
            "+/- MMV",
            "Helvetica", 2, 1, False, True, True, True, Alignment.RIGHT))
        table.add(get_table_cell_order_info(
            "Exchange" +
            "\n  1.00000",
            "Helvetica", 3, 1, False, True, True, True, Alignment.CENTERED))
        table.add(get_table_cell_order_info(
            "Entered Value " +
            "\n11,397.00  USD ",
            "Helvetica", 2, 1, False, True, True, True, Alignment.RIGHT))

        table_bottom_gen(table, json, page)

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
                    "Helvetica", 8, 1, True, False, True, True, Alignment.LEFT))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, True, False, True, True, Alignment.LEFT))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 3, 1, True, False, True, True, Alignment.LEFT))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, True, False, True, True, Alignment.LEFT))
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
                    "Helvetica", 8, 1, False, True, True, True, Alignment.LEFT))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, False, True, True, True, Alignment.LEFT))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 3, 1, False, True, True, True, Alignment.LEFT))
                table.add(get_table_cell_order_info(
                    "001",
                    "Helvetica", 2, 1, False, True, True, True, Alignment.LEFT))

        table_bottom_gen(table, json, page)

        layout.add(table)

        table_more_orders_paragraph(json, layout)


def table_more_orders_paragraph(json, layout):
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

    t.add(get_table_cell_title_def("1. Filer Code/Entry Number", "Helvetica", 16, 1))
    t.add(get_table_cell_content_def(f"{json['num1']}", "Helvetica", 16, 1, Alignment.LEFT))

    table_middle4_gen(t)

    t.add(get_table_cell_order_index("", "Helvetica", 1, 1, False, True))
    t.add(get_table_cell_order_info(
        "Totals for Invoice" +
        "\n" + f"14920770213612302" +
        "\n" +
        "\n" +
        "\n" +
        "\n" +
        "\n",
        "Helvetica", 3, 1, False, True, False, True, Alignment.LEFT))
    t.add(get_table_cell_order_info(
        "Invoice Value" +
        "\n" + f"11,397.00 USD" +
        "\n" +
        "\n" +
        "\n" +
        "\n" +
        "\n",
        "Helvetica", 5, 1, False, True, True, False, Alignment.RIGHT))
    t.add(get_table_cell_order_info(
        "+/- MMV",
        "Helvetica", 2, 1, False, True, True, True, Alignment.RIGHT))
    t.add(get_table_cell_order_info(
        "Exchange" +
        "\n  1.00000",
        "Helvetica", 3, 1, False, True, True, True, Alignment.CENTERED))
    t.add(get_table_cell_order_info(
        "Entered Value " +
        "\n11,397.00  USD ",
        "Helvetica", 2, 1, False, True, True, True, Alignment.RIGHT))

    layout.add(t)
