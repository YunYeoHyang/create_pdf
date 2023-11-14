import json
from pathlib import Path
from borb.pdf import Document, Image, FixedColumnWidthTable, TableCell
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from decimal import Decimal
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.geometry.rectangle import Rectangle

if __name__ == '__main__':

    # testInfo form json
    with open("../source/response.json", "r", encoding="utf-8") as f:
        json = json.load(f)

    pdf = Document()
    page = Page()
    pdf.add_page(page)
    layout: PageLayout = SingleColumnLayout(page)

    Image(
        Path("../source/logo.jpg"),
        width=Decimal(32),
        height=Decimal(32),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP
    ).paint(page, Rectangle(Decimal(20),
                            page.get_page_info().get_height() - Decimal(50),
                            Decimal(100),
                            Decimal(20)
                            ))

    Paragraph(
        "DEPARTMENT OF HOMELAND SECURITY U.S. Customs and Border Protection",
        font="Helvetica",
        text_alignment=Alignment.CENTERED,
        horizontal_alignment=Alignment.CENTERED,
        vertical_alignment=Alignment.TOP,
        font_size=Decimal(10)).paint(page, Rectangle(page.get_page_info().get_width() / 2 - Decimal(100),
                                                     page.get_page_info().get_height() - Decimal(40),
                                                     Decimal(200),
                                                     Decimal(20)
                                                     ))
    Paragraph(
        "ENTRY SUMMARY",
        font="Helvetica-Bold",
        text_alignment=Alignment.CENTERED,
        horizontal_alignment=Alignment.CENTERED,
        vertical_alignment=Alignment.TOP,
        font_size=Decimal(12)).paint(page, Rectangle(page.get_page_info().get_width() / 2 - Decimal(60),
                                                     page.get_page_info().get_height() - Decimal(70),
                                                     Decimal(120),
                                                     Decimal(20)
                                                     ))

    Paragraph(
        "OMB APPROVAL NO. 1651 - 0022 EXPIRATION DATE 01 / 31 / 2021",
        font="Helvetica-Bold",
        horizontal_alignment=Alignment.RIGHT,
        vertical_alignment=Alignment.TOP,
        font_size=Decimal(6)).paint(page, Rectangle(page.get_page_info().get_width() - Decimal(120),
                                                    page.get_page_info().get_height() - Decimal(40),
                                                    Decimal(100),
                                                    Decimal(20)
                                                    ))

    Paragraph(
        "CBP Form 7501 (5/22)",
        font_size=Decimal(8),
        font="Helvetica-Bold",
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.BOTTOM).paint(page, Rectangle(Decimal(20),
                                                                   Decimal(10),
                                                                   Decimal(100),
                                                                   Decimal(20)
                                                                   ))

    Paragraph(
        "Page 1 of 2",
        font_size=Decimal(8),
        font="Helvetica-Bold",
        horizontal_alignment=Alignment.RIGHT,
        vertical_alignment=Alignment.BOTTOM).paint(page, Rectangle(page.get_page_info().get_width() - Decimal(120),
                                                                   Decimal(10),
                                                                   Decimal(100),
                                                                   Decimal(20)
                                                                   ))
    Paragraph(Paragraph("111"))

    # table info setting
    table: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=2,
        number_of_columns=7,
        margin_top=Decimal(12),
        column_widths=[Decimal(5), Decimal(2), Decimal(3), Decimal(3), Decimal(2), Decimal(2), Decimal(3)],
    )

    # set properties on all table cells
    table.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))

    table.add(Paragraph(
        "1. Filer Code/Entry Number" + "\n" + json['num1'],
        font="Helvetica",
        font_size=Decimal(9),
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_bottom=Decimal(3),
        padding_right=Decimal(2)
    ))
    table.add(Paragraph(
        "2. Entry Type" + "\n" + json['num2'],
        font="Helvetica",
        font_size=Decimal(9),
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_bottom=Decimal(3),
        padding_right=Decimal(2)
    ))
    table.add(Paragraph("3. Summary Date", font="Helvetica", font_size=Decimal(9)))
    table.add(Paragraph("4. Surety Number", font="Helvetica", font_size=Decimal(9)))
    table.add(Paragraph("5. Bond Type", font="Helvetica", font_size=Decimal(9)))
    table.add(Paragraph("6. Port Code", font="Helvetica", font_size=Decimal(9)))
    table.add(Paragraph("7. Entry Date", font="Helvetica", font_size=Decimal(9)))

    table.paint(page, Rectangle(Decimal(20),
                                page.get_page_info().get_height() - Decimal(100),
                                page.get_page_info().get_width() - Decimal(40),
                                Decimal(20)
                                ))

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)
