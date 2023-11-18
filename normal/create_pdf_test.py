import json

from borb.pdf import Document
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.pdf import PDF

from tools.dynamic_paragraph_gen import table_order_paragraph
from tools.layout import Layout
from tools.static_paragraph_gen import *

if __name__ == '__main__':
    # testInfo form json
    with open("../source/response.json", "r", encoding="utf-8") as f:
        json = json.load(f)

    pdf = Document()
    page = Page()
    pdf.add_page(page)
    layout: PageLayout = Layout(page)

    table_front_gen(json, layout)

    table_middle1_gen(json, layout)

    table_middle2_gen(json, layout)

    table_middle3_gen(json, layout)

    table_middle4_gen(layout)

    table_order_paragraph(json, layout)

    table_bottom_gen(json, layout)

    table_middle4_gen(layout)

    table_order_paragraph(json, layout)

    page_head_bottom(pdf)

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)
