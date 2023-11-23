import json

from borb.pdf import Document, FixedColumnWidthTable
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.pdf import PDF

from tools.dynamic_paragraph_gen import table_order_paragraph
from tools.layout import Layout
from tools.static_paragraph_gen import *

if __name__ == '__main__':
    # testInfo form json
    with open("../source/response1.json", "r", encoding="utf-8") as f:
        json = json.load(f)

    pdf = Document()
    page = Page(width=Decimal(612), height=Decimal(792))
    pdf.add_page(page)
    layout: PageLayout = Layout(page)

    table: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=41,
        number_of_columns=16,
        column_widths=[
            Decimal(0.75), Decimal(1.8), Decimal(0.6),
            Decimal(0.5), Decimal(0.5), Decimal(0.35),
            Decimal(0.35), Decimal(0.9), Decimal(0.6),
            Decimal(1), Decimal(0.8), Decimal(0.6),
            Decimal(0.7), Decimal(0.6),
            Decimal(0.9), Decimal(0.9)]
    )

    table_front_gen(table, json)

    table_middle1_gen(table, json)

    table_middle2_gen(table, json)

    table_middle3_gen(table, json)

    table_middle4_gen(table)

    table_order_paragraph(table, json, layout, page, pdf)

    page_head_bottom(pdf)

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)
