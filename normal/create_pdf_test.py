import json

from borb.pdf import Document
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF

from tools.dynamic_paragraph_gen import table_order_paragraph
from tools.static_paragraph_gen import *

if __name__ == '__main__':
    # testInfo form json
    with open("../source/response.json", "r", encoding="utf-8") as f:
        json = json.load(f)

    pdf = Document()
    page = Page()
    pdf.add_page(page)
    layout: PageLayout = SingleColumnLayout(page)

    page_head_bottom(page)

    table_front_gen(page, json)

    table_middle1_gen(page, json)

    table_middle2_gen(page, json)

    table_middle3_gen(page, json)

    table_middle4_gen(page)

    table_order_paragraph(page, json)

    table_bottom_gen(page, json)

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)
