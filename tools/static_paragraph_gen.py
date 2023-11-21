from pathlib import Path

from borb.pdf import Image, FixedColumnWidthTable, Page
from borb.pdf.canvas.geometry.rectangle import Rectangle

from tools.paragraph_style import *


def page_head_bottom(pdf):
    number_of_pages = int(pdf.get_document_info().get_number_of_pages())

    for index in range(0, number_of_pages):
        page: Page = pdf.get_page(index)

        Image(
            Path("../source/logo.jpg"),
            width=Decimal(33.7),
            height=Decimal(33.7),
            horizontal_alignment=Alignment.LEFT,
            vertical_alignment=Alignment.TOP
        ).paint(page, Rectangle(Decimal(20),
                                page.get_page_info().get_height() - Decimal(52),
                                Decimal(100),
                                Decimal(33.7)
                                ))

        if index < 1:
            Paragraph(
                "DEPARTMENT OF HOMELAND SECURITY U.S. Customs and Border Protection",
                font="Helvetica",
                text_alignment=Alignment.CENTERED,
                horizontal_alignment=Alignment.CENTERED,
                vertical_alignment=Alignment.TOP,
                fixed_leading=Decimal(0.75),
                font_size=Decimal(10)).paint(page, Rectangle(page.get_page_info().get_width() / 2 - Decimal(92),
                                                             page.get_page_info().get_height() - Decimal(40),
                                                             Decimal(200),
                                                             Decimal(24)
                                                             ))
            Paragraph(
                "ENTRY SUMMARY",
                font="Helvetica-Bold",
                text_alignment=Alignment.CENTERED,
                horizontal_alignment=Alignment.CENTERED,
                vertical_alignment=Alignment.TOP,
                font_size=Decimal(12)).paint(page, Rectangle(page.get_page_info().get_width() / 2 - Decimal(52),
                                                             page.get_page_info().get_height() - Decimal(69),
                                                             Decimal(120),
                                                             Decimal(24)
                                                             ))

            Paragraph(
                "OMB APPROVAL NO. 1651-0022 EXPIRATION DATE 01/31/2021",
                font="Helvetica-Bold",
                horizontal_alignment=Alignment.RIGHT,
                vertical_alignment=Alignment.TOP,
                fixed_leading=Decimal(0.7),
                font_size=Decimal(6)).paint(page, Rectangle(page.get_page_info().get_width() - Decimal(135),
                                                            page.get_page_info().get_height() - Decimal(35),
                                                            Decimal(100),
                                                            Decimal(20)
                                                            ))
        else:
            Paragraph(
                "ENTRY SUMMARY CONTINUATION SHEET",
                font="Helvetica-bold",
                text_alignment=Alignment.CENTERED,
                horizontal_alignment=Alignment.CENTERED,
                vertical_alignment=Alignment.TOP,
                font_size=Decimal(9)).paint(page, Rectangle(page.get_page_info().get_width() / 2 - Decimal(92),
                                                            page.get_page_info().get_height() - Decimal(55),
                                                            Decimal(200),
                                                            Decimal(24)
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
            f"Page {index + 1} of {number_of_pages}",
            font_size=Decimal(8),
            font="Helvetica-Bold",
            horizontal_alignment=Alignment.RIGHT,
            vertical_alignment=Alignment.BOTTOM).paint(page, Rectangle(page.get_page_info().get_width() - Decimal(120),
                                                                       Decimal(10),
                                                                       Decimal(100),
                                                                       Decimal(20)
                                                                       ))


def table_front_gen(json, layout):
    # tableFront info setting
    table_front: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=2,
        number_of_columns=7,
        column_widths=[Decimal(4.6), Decimal(2.5), Decimal(2.9), Decimal(2.8), Decimal(2.2), Decimal(2.2),
                       Decimal(2.8)]
    )

    table_front.add(get_table_cell_title_def("1. Filer Code/Entry Number", "Helvetica", 1, 1))
    table_front.add(get_table_cell_title_def("2. Entry Type", "Helvetica", 1, 1))
    table_front.add(get_table_cell_title_def("3. Summary Date", "Helvetica", 1, 1))
    table_front.add(get_table_cell_title_def("4. Surety Number", "Helvetica", 1, 1))
    table_front.add(get_table_cell_title_def("5. Bond Type", "Helvetica", 1, 1))
    table_front.add(get_table_cell_title_def("6. Port Code", "Helvetica", 1, 1))
    table_front.add(get_table_cell_title_def("7. Entry Date", "Helvetica", 1, 1))
    table_front.add(get_table_cell_content_def(f"{json['num1']}", "Helvetica", 1, 1, Alignment.LEFT))
    table_front.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_front.add(get_table_cell_content_def(f"{json['num3']}", "Helvetica", 1, 1, Alignment.LEFT))
    table_front.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_front.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_front.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_front.add(get_table_cell_content_def(f"{json['num7']}", "Helvetica", 1, 1, Alignment.LEFT))

    layout.add(table_front)


def table_middle1_gen(json, layout):
    # table_middle1 info setting
    table_middle1: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=4,
        number_of_columns=4,
        column_widths=[Decimal(5), Decimal(3), Decimal(5), Decimal(2)],
    )

    table_middle1.add(get_table_cell_title_def("8. Importing Carrier", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_title_def("9. Mode of Transport", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_title_def("10. Country of Origin", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_title_def("11. Import Date", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_content_def(f"{json['num8']}", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle1.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle1.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle1.add(get_table_cell_content_def(f"{json['num11']}", "Helvetica", 1, 1, Alignment.LEFT))

    table_middle1.add(get_table_cell_title_def("12. B/L or AWB Number", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_title_def("13. Manufacturer ID", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_title_def("14. Exporting Country", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_title_def("15. Export Date", "Helvetica", 1, 1))
    table_middle1.add(get_table_cell_content_def(f"{json['num12']}", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle1.add(get_table_cell_content_def(f"{json['num13']}", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle1.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle1.add(get_table_cell_content_def(f"{json['num15']}", "Helvetica", 1, 1, Alignment.LEFT))

    layout.add(table_middle1)


def table_middle2_gen(json, layout):
    # table_middle2 info setting
    table_middle2: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=2,
        number_of_columns=5,
        column_widths=[Decimal(2.88), Decimal(2), Decimal(2), Decimal(3), Decimal(3)],
    )

    table_middle2.add(get_table_cell_title_def("16. I.T. Number", "Helvetica", 1, 1))
    table_middle2.add(get_table_cell_title_def("17. I.T. Date", "Helvetica", 1, 1))
    table_middle2.add(get_table_cell_title_def("18. Missing Docs", "Helvetica", 1, 1))
    table_middle2.add(get_table_cell_title_def("19. Foreign Port of Lading", "Helvetica", 1, 1))
    table_middle2.add(get_table_cell_title_def("20. U.S. Port of Unloading", "Helvetica", 1, 1))
    table_middle2.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle2.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle2.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle2.add(get_table_cell_content_def(f"{json['num19']}", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle2.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))

    layout.add(table_middle2)


def table_middle3_gen(json, layout):
    # table_middle3 info setting
    table_middle3: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=4,
        number_of_columns=4,
        column_widths=[Decimal(2.87), Decimal(2.47), Decimal(2.33), Decimal(2.33)],
    )

    table_middle3.add(get_table_cell_title_def("21. Location of Goods/G.O. Number", "Helvetica", 1, 1))
    table_middle3.add(get_table_cell_title_def("22. Consignee Number", "Helvetica", 1, 1))
    table_middle3.add(get_table_cell_title_def("23. Importer Number", "Helvetica", 1, 1))
    table_middle3.add(get_table_cell_title_def("24. Reference Number", "Helvetica", 1, 1))
    table_middle3.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle3.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle3.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))
    table_middle3.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.LEFT))

    table_middle3.add(get_table_cell_title_def("25. Ultimate Consignee Name (Last, First, M.I.) and Address",
                                               "Helvetica", 2, 1))
    table_middle3.add(get_table_cell_title_def("26. Importer of Record Name(Last, First, M.I.) and Address",
                                               "Helvetica", 2, 1))
    table_middle3.add(get_table_cell_content_def(
        f"{json['num25']}" +
        f"\nStreet: {json['num25street']}" +
        f"\n{json['num25st']}\n" +
        f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" +
        f"CustomerReference # {json['num25customerReference']}" +
        f"\nCity: {json['num25city']}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" +
        f"State: {json['num25state']}   Zip: {json['num25zip']}",
        "Helvetica", 2, 1, Alignment.LEFT))
    table_middle3.add(get_table_cell_content_def(
        f"{json['num26']}" +
        f"\nStreet: {json['num26street']}" +
        f"\n{json['num26st']}\n\n" +
        f"\nCity: {json['num26city']}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" +
        f"State: {json['num26state']}   Zip: {json['num26zip']}",
        "Helvetica", 2, 1, Alignment.LEFT))

    layout.add(table_middle3)


def table_middle4_gen(layout):
    # table_middle4 info setting
    table_middle4: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=2,
        number_of_columns=7,
        column_widths=[Decimal(1), Decimal(2.5), Decimal(2.5), Decimal(2.5),
                       Decimal(2.48), Decimal(2.49), Decimal(2.48)],
    )

    table_middle4.add(TableCell(
        Paragraph(
            "27. Line No.",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=2
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "28. Description of Merchandise",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            vertical_alignment=Alignment.MIDDLE,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=3,
        row_span=1
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "32. " +
            "\nA.	Entered Value" +
            "\nB.	CHGS" +
            "\nC.	Relationship",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=2
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "33. " +
            "\nA.	HTSUS Rate" +
            "\nB.	ADA/CVD Rate" +
            "\nC.	IRC Rate" +
            "\nD.  Visa No.",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=2
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "34. " +
            "\nDuty and IR Tax",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=1
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "29. " +
            "\nA.	HTSUS No." +
            "\nB.	AD/CVD No.",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            vertical_alignment=Alignment.MIDDLE,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=1
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "30. " +
            "\nA.	Gross Weight" +
            "\nB.	Manifest Qty.",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            vertical_alignment=Alignment.MIDDLE,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=1
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "31. " +
            "\nNet Quantity in" +
            "\nHTSUS Units",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            vertical_alignment=Alignment.MIDDLE,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=1
    ))
    table_middle4.add(TableCell(
        Paragraph(
            "Dollar     Cents\n",
            font="Helvetica",
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            font_size=Decimal(9),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            padding_bottom=Decimal(2),
            fixed_leading=Decimal(0.7)
        ),
        border_width=Decimal(0.45),
        column_span=1,
        row_span=1
    ))

    # table_middle4.add(get_table_cell_def("27. Line No.", "Helvetica", row_span=4, column_span=1))
    # table_middle4.add(get_table_cell_def("28. Description of Merchandise", "Helvetica", row_span=1, column_span=3))
    # table_middle4.add(get_table_cell_def(
    #         "32. " +
    #         "\nA.	Entered Value" +
    #         "\nB.	CHGS" +
    #         "\nC.	Relationship", "Helvetica", row_span=4, column_span=1))
    # table_middle4.add(get_table_cell_def(
    #         "33. " +
    #         "\nA.	HTSUS Rate" +
    #         "\nB.	ADA/CVD Rate" +
    #         "\nC.	IRC Rate" +
    #         "\nD.  Visa No.", "Helvetica", row_span=4, column_span=1))
    # table_middle4.add(get_table_cell_def(
    #     "34. " +
    #     "\nDuty and IR Tax",
    #     "Helvetica", row_span=2, column_span=1))
    # table_middle4.add(get_table_cell_def(
    #     "29. " +
    #     "\nA.	HTSUS No." +
    #     "\nB.	AD/CVD No.",
    #     "Helvetica", row_span=3, column_span=1))
    # table_middle4.add(get_table_cell_def(
    #     "30. " +
    #     "\nA.	Gross Weight" +
    #     "\nB.	Manifest Qty.",
    #     "Helvetica", row_span=3, column_span=1))
    # table_middle4.add(get_table_cell_def(
    #     "31. " +
    #     "\nNet Quantity in" +
    #     "\nHTSUS Units",
    #     "Helvetica", row_span=3, column_span=1))
    # table_middle4.add(get_table_cell_def(
    #     "Dollar     Cents",
    #     "Helvetica", row_span=1, column_span=1))

    layout.add(table_middle4)


def table_bottom_gen(json, layout):
    # table_bottom info setting
    table_bottom: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=13,
        number_of_columns=5,
        column_widths=[Decimal(4.3), Decimal(4.2), Decimal(2.4), Decimal(2.7), Decimal(2.35)],
    )

    table_bottom.add(get_table_cell_def("Other Fee Summary(for Block 39)", "Helvetica", 9, 1, 4))
    table_bottom.add(get_table_cell_title_def("35. Total Entered Value", "Helvetica", 1, 1))
    table_bottom.add(get_table_cell_def("   CBP USE ONLY", "Helvetica-Bold", 12, 2, 1))
    table_bottom.add(get_table_cell_def("   TOTALS", "Helvetica", 12, 1, 1))
    table_bottom.add(get_table_cell_content_def("$ 11,397", "Helvetica", 1, 1, Alignment.LEFT))
    table_bottom.add(get_table_cell_def("A. LIQ CODE", "Helvetica", 9, 1, 2))
    table_bottom.add(get_table_cell_def("B. Ascertained Duty", "Helvetica", 9, 1, 2))
    table_bottom.add(get_table_cell_title_def("37. Duty", "Helvetica", 1, 1))
    table_bottom.add(get_table_cell_title_def("Total Other Fees", "Helvetica", 1, 1))
    table_bottom.add(get_table_cell_content_def(f"$ {json['num37Duty']}", "Helvetica", 1, 1, Alignment.RIGHT))
    table_bottom.add(get_table_cell_content_def(f"$ {json['totalOtherFees']}", "Helvetica", 1, 1, Alignment.LEFT))
    table_bottom.add(get_table_cell_def("REASON CODE", "Helvetica", 9, 1, 6))
    table_bottom.add(get_table_cell_def("C. Ascertained Tax", "Helvetica", 9, 1, 2))
    table_bottom.add(get_table_cell_title_def("38. Tax", "Helvetica", 1, 1))
    table_bottom.add(get_table_cell_def(
        "36. Declaration of Importer of Record (Owner or Purchaser) or Authorized Agent",
        "Helvetica", 10, 2, 2))
    table_bottom.add(get_table_cell_content_def("", "Helvetica", 1, 1, Alignment.RIGHT))
    table_bottom.add(get_table_cell_def("D. Ascertained Other", "Helvetica", 9, 1, 2))
    table_bottom.add(get_table_cell_title_def("39. Other", "Helvetica", 1, 1))
    table_bottom.add(get_table_cell_att(
        "I declare that I am the Importer of record and that the actual owner," +
        "purchaser, or consignee for CBP purposes is as shown above, OR owner",
        "Helvetica", 8, 2, 3, True, False))
    table_bottom.add(get_table_cell_content_def(f"$ {json['num39Other']}", "Helvetica", 1, 1, Alignment.RIGHT))
    table_bottom.add(get_table_cell_def("D. Ascertained Total", "Helvetica", 9, 1, 2))
    table_bottom.add(get_table_cell_title_def("40. Total", "Helvetica", 1, 1))
    table_bottom.add(get_table_cell_content_def(f"$ {json['num40Total']}", "Helvetica", 1, 1, Alignment.RIGHT))
    table_bottom.add(get_table_cell_att(
        "or purchaser or agent thereof.  I further declare that the merchandise was " +
        "obtained pursuant to a purchase or agreement to purchase and that the" +
        "\n prices set forth in the invoices are true, OR " +
        "was not obtained pursuant to a purchase or agreement to purchase and the statements in the invoices as" +
        "\n to value or price are true to the best of my knowledge and belief.  " +
        "I also declare that the statements in the documents herein filed fully disclose to the best of my " +
        "knowledge and belief the true prices, values, quantities, rebates, drawbacks, fees, commissions, " +
        "and royalties and are true and correct, and that all goods or services provided to the seller of the" +
        " merchandise either free or at reduced cost are fully disclosed. \n I will immediately furnish to the " +
        "appropriate CBP officer any information showing a different statement of facts.",
        "Helvetica", 2, 5, 1, False, True))
    table_bottom.add(get_table_cell_def(
        "41. Declarant Name (Last, First, M.I.)       Title" +
        "                                                 " +
        "Signature                                                   " +
        "Date\nAMY LEE DBA GUARDIAN CUSTOMS" +
        "                                                              " +
        "                                                               " +
        "12/30/22",
        "Helvetica", 9, 5, 1))
    table_bottom.add(get_table_cell_title_def("42. Broker/Filer Information Name(Last, First, M.I.) and Phone Number",
                                              "Helvetica", 2, 1))
    table_bottom.add(get_table_cell_title_def("43. Broker/Importer File Number",
                                              "Helvetica", 3, 1))
    table_bottom.add(get_table_cell_content_def(
        "AMY YICHIN LEE DBA GUARDIAN CUSTOMS" +
        "\n454 ARCADIA DR" +
        "\nSAN PEDRO, CA 90731   6265525626",
        "Helvetica", 2, 1, Alignment.LEFT))
    table_bottom.add(get_table_cell_content_def(
        "0132257 / EITU1593922",
        "Helvetica", 3, 1, Alignment.LEFT))

    layout.add(table_bottom)
