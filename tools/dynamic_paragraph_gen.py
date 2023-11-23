from pathlib import Path

from borb.pdf import FixedColumnWidthTable, Image, Page, PageLayout
from borb.pdf.canvas.geometry.rectangle import Rectangle

from tools.data_tools import *
from tools.layout import Layout
from tools.paragraph_style import *
from tools.static_paragraph_gen import table_bottom_gen, table_middle4_gen, check_json_for_key


def table_order_paragraph(table, j, layout, page, pdf):
    order_list: [] = j['productList']

    if len(order_list) == 1:
        table_total_paragraph_gen(table, j, table_order_paragraph_gen(order_list[0], table, j, page, True), True)
        table_bottom_gen(table, j, page)
        layout.add(table)
    else:
        table_total_paragraph_gen(table, j, table_order_paragraph_gen(order_list[0], table, j, page, True), False)
        table_bottom_gen(table, j, page)
        layout.add(table)

        table_more_orders_paragraph(order_list, j, pdf)


def table_order_paragraph_gen(data, table, j, page, is_first) -> int:
    info_list: [] = data['pd1']['info']
    row_number = 4 + len(info_list) * 2
    if is_first:
        row_number += 1
    if check_json_for_key(data['pd3'], 'valuedOverUnit'):
        row_number += 1

    if is_first:
        table.add(get_table_cell_order_index("", "Helvetica", 1, 1, True, False))
        table.add(get_table_cell_order_info1(
            f"{j['pkgs']} PKGS", "Helvetica", 8, 1, True, False, True, True, Alignment.RIGHT))
        table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, True, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1("", "Helvetica", 3, 1, True, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, True, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_index("001", "Helvetica", 1, row_number - 1, False, False))
    else:
        table.add(get_table_cell_order_index("001", "Helvetica", 1, row_number, False, False))

    table.add(get_table_cell_order_info1(
        f"{info_list[0]['adacvdRate']}", "Helvetica", 8, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1("", "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))

    table.add(get_table_cell_order_info1(
        f"{info_list[0]['adcvdNo']}", "Helvetica", 1, 1, False, False, False, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1(
        f"{add_commas(trans_json_for_key(info_list[0], 'kg1'))} KG" if trans_json_for_key(info_list[0], 'kg1') != "" else "",
        "Helvetica", 4, 1, False, False, False, False, Alignment.RIGHT))

    if len(info_list) == 1:
        table.add(get_table_cell_order_info1(
            f"{data['pd1']['manifestQty']} NO" if data['pd1']['manifestQtyShow'] else "",
            "Helvetica", 3, 1, False, False, True, False, Alignment.RIGHT))
        table.add(get_table_cell_order_info1(f"${data['pd2']['totalValue']}",
                                             "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
        table.add(get_table_cell_order_info1(
            f"{trans_json_for_key(data['pd3'], 'htsusRate')}" if trans_json_for_key(data['pd3'], 'htsusRate') else "",
            "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1(
            f"${data['pd4']['dutyAndIrTax']}"
            , "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
    else:
        table.add(get_table_cell_order_info1(
            "",
            "Helvetica", 3, 1, False, False, True, False, Alignment.RIGHT))
        table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1(
            f"{trans_json_for_key(data['pd3'], 'htsusRate')}" if trans_json_for_key(data['pd3'], 'htsusRate') else "",
            "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1(
            f"${data['pd4']['dutyAndIrTax']}"
            , "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))

        table.add(get_table_cell_order_info1(
            f"{info_list[1]['htsusDepict']}", "Helvetica", 8, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1("", "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))

        table.add(get_table_cell_order_info1(
            f"{info_list[1]['htsusNo']}", "Helvetica", 1, 1, False, False, False, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1(
            f"{add_commas(trans_json_for_key(info_list[1], 'kg2'))} KG" if trans_json_for_key(info_list[1], 'kg2') != "" else "",
            "Helvetica", 4, 1, False, False, False, False, Alignment.RIGHT))

        table.add(get_table_cell_order_info1(
            f"{data['pd1']['manifestQty']} NO" if data['pd1']['manifestQtyShow'] else "",
            "Helvetica", 3, 1, False, False, True, False, Alignment.RIGHT))
        table.add(get_table_cell_order_info1(f"${data['pd2']['totalValue']}",
                                             "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
        string = f"{trans_json_for_key(data['pd3'], 'htsusRate2')}" if trans_json_for_key(data['pd3'], 'htsusRate2') \
            else ""
        if check_json_for_key(data['pd3'], 'valuedOverUnit'):
            string = (f"${data['pd3']['valuedOver']}\t" +
                      f"{data['pd3']['valuedOverUnit']}\t+\t" +
                      f"{trans_json_for_key(data['pd3'], 'htsusRate2')}")
        table.add(get_table_cell_order_info1(
            string,
            "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1(f"${data['pd4']['dutyAndIrTax2']}",
                                             "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))

    table.add(get_table_cell_order_info1(
        f"{data['pd1']['netQuantityIn']} KG" if data['pd1']['netQuantityInShow'] else "",
        "Helvetica", 8, 1, False, False, True, True, Alignment.RIGHT))
    table.add(get_table_cell_order_info1(f"C ${data['pd2']['moneyC']}",
                                         "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
    table.add(get_table_cell_order_info1("", "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))

    table.add(get_table_cell_order_info1("", "Helvetica", 8, 1, False, False, True, True, Alignment.RIGHT))
    table.add(get_table_cell_order_info1("N", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
    table.add(get_table_cell_order_info1("", "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))

    if check_json_for_key(data['pd3'], 'valuedOverUnit'):
        table.add(get_table_cell_order_info1("056 - CottonFee                              ",
                                             "Helvetica", 8, 1, False, False, True, True, Alignment.RIGHT))
        table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
        table.add(get_table_cell_order_info1(f"${data['pd3']['cottonFee']} {data['pd3']['cottonFeeUnit']}",
                                             "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
        table.add(get_table_cell_order_info1(f"${data['pd4']['cottonFeeResult']}",
                                             "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))

    table.add(get_table_cell_order_info1(
        "499 - Merchandise Processing Fee", "Helvetica", 8, 1, False, False, True, True, Alignment.RIGHT))
    table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1("0.3464%", "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1(f"${data['pd4']['merchandiseProcessingFee']}",
                                         "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))

    table.add(get_table_cell_order_info1(
        "501 - Harbor Maintenance Fee       ", "Helvetica", 8, 1, False, False, True, True, Alignment.RIGHT))
    table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1("0.1250%", "Helvetica", 3, 1, False, False, True, True, Alignment.LEFT))
    table.add(get_table_cell_order_info1(f"${data['pd4']['harborMaintenanceFee']}",
                                         "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))

    Image(
        Path("../source/line.jpg"),
        width=Decimal(560),
        height=Decimal(2),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP
    ).paint(page, Rectangle(Decimal(25.704),
                            page.get_page_info().get_height() - Decimal(337) - Decimal(row_number * 11.25),
                            Decimal(560),
                            Decimal(2)
                            ))

    return 14 - row_number


def table_more_orders_paragraph(order_list, j, pdf):
    page = Page(width=Decimal(612), height=Decimal(792))
    pdf.add_page(page)
    layout: PageLayout = Layout(page)

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
    table_order_paragraph_gen(order_list[0], t, j, page, False)

    layout.add(t)


def table_total_paragraph_gen(table, j, row_number, is_draw):
    if is_draw and row_number > 3:
        table.add(get_table_cell_order_index("", "Helvetica", 1, row_number, False, True))

        title_list = [
            ['Totals for Invoice', 'Invoice Value', '+/- MMV', 'Exchange', 'Entered Value'],
            [f'{trans_json_for_key(j, 'totalsForInvoice')}', f'{add_commas(j['invoiceValue'])} USD',
             '', '1.00000', f'{add_commas(j['enteredValue'])} USD'],
        ]
        title_list_index = 0

        is_empty = round((row_number - 2) / 2)

        for index in range(row_number):
            if index < is_empty or index >= is_empty + 2 and index != row_number - 1:
                table.add(get_table_cell_order_info1("", "Helvetica", 3, 1, False, False, False, True, Alignment.LEFT))
                table.add(get_table_cell_order_info1("", "Helvetica", 5, 1, False, False, True, False, Alignment.RIGHT))
                table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
                table.add(
                    get_table_cell_order_info1("", "Helvetica", 3, 1, False, False, True, True, Alignment.CENTERED))
                table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
            elif index == row_number - 1:
                table.add(get_table_cell_order_info1("", "Helvetica", 3, 1, False, True, False, True, Alignment.LEFT))
                table.add(get_table_cell_order_info1("", "Helvetica", 5, 1, False, True, True, False, Alignment.RIGHT))
                table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, True, True, True, Alignment.RIGHT))
                table.add(
                    get_table_cell_order_info1("", "Helvetica", 3, 1, False, True, True, True, Alignment.CENTERED))
                table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, True, True, True, Alignment.RIGHT))
            else:
                table.add(get_table_cell_order_info1(
                    f"{title_list[title_list_index][0]}", "Helvetica", 4, 1, False, False, False, True, Alignment.LEFT))
                table.add(get_table_cell_order_info1(
                    f"{title_list[title_list_index][1]}", "Helvetica", 4, 1, False, False, True, False,
                    Alignment.RIGHT))
                table.add(get_table_cell_order_info1(
                    f"{title_list[title_list_index][2]}", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
                table.add(get_table_cell_order_info1(
                    f"{title_list[title_list_index][3]}", "Helvetica", 3, 1, False, False, True, True,
                    Alignment.CENTERED))
                table.add(get_table_cell_order_info1(
                    f"{title_list[title_list_index][4]}", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
                title_list_index += 1
    else:
        table.add(get_table_cell_order_index("", "Helvetica", 1, row_number, False, True))

        for index in range(row_number):
            table.add(get_table_cell_order_info1("", "Helvetica", 4, 1, False, False, False, True, Alignment.LEFT))
            table.add(get_table_cell_order_info1("", "Helvetica", 4, 1, False, False, True, False, Alignment.RIGHT))
            table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))
            table.add(
                get_table_cell_order_info1("", "Helvetica", 3, 1, False, False, True, True, Alignment.CENTERED))
            table.add(get_table_cell_order_info1("", "Helvetica", 2, 1, False, False, True, True, Alignment.RIGHT))


def get_table_cell_order_info1(value, font, column_span, row_span, border_top, border_bottom, border_right, border_left,
                               horizontal_alignment) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            horizontal_alignment=horizontal_alignment,
            font_size=Decimal(10),
            padding_top=Decimal(1),
            padding_left=Decimal(3),
            padding_right=Decimal(2),
            fixed_leading=Decimal(0.7),
        ),
        border_top=border_top,
        border_bottom=border_bottom,
        border_right=border_right,
        border_left=border_left,
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span,
    )


def draw_line_for_self_style(page):
    Image(
        Path("../source/line.jpg"),
        width=Decimal(560),
        height=Decimal(2),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP
    ).paint(page, Rectangle(Decimal(25.704),
                            page.get_page_info().get_height() - Decimal(332) - Decimal(8 * 11.25),
                            Decimal(560),
                            Decimal(2)
                            ))
