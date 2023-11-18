from pathlib import Path

from borb.pdf import Image, FixedColumnWidthTable, TableCell
from borb.pdf.canvas.geometry.rectangle import Rectangle

from tools.paragraph_style import *


def page_head_bottom(page):
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


def table_front_gen(page, json):
    # tableFront info setting
    table_front: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=1,
        number_of_columns=7,
        margin_top=Decimal(12),
        column_widths=[Decimal(4.6), Decimal(2.5), Decimal(2.9), Decimal(2.8), Decimal(2.2), Decimal(2.2),
                       Decimal(2.8)],
    )

    # set properties on all table cells
    table_front.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))

    table_front.add(get_paragraph_def("1. Filer Code/Entry Number" + "\n" + json['num1'], "Helvetica"))
    table_front.add(get_paragraph_def("2. Entry Type", "Helvetica"))
    table_front.add(get_paragraph_def("3. Summary Date" + "\n" + json['num3'], "Helvetica"))
    table_front.add(get_paragraph_def("4. Surety Number", "Helvetica"))
    table_front.add(get_paragraph_def("5. Bond Type", "Helvetica"))
    table_front.add(get_paragraph_def("6. Port Code", "Helvetica"))
    table_front.add(get_paragraph_def("7. Entry Date" + "\n" + json['num7'], "Helvetica"))

    table_front.paint(page, Rectangle(Decimal(20),
                                      page.get_page_info().get_height() - Decimal(100),
                                      page.get_page_info().get_width() - Decimal(40),
                                      Decimal(20)
                                      ))


def table_middle1_gen(page, json):
    # table_middle1 info setting
    table_middle1: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=2,
        number_of_columns=4,
        column_widths=[Decimal(5), Decimal(3), Decimal(5), Decimal(2)],
    )

    table_middle1.add(get_paragraph_def("8. Importing Carrier" + "\n" + json['num8'], "Helvetica"))
    table_middle1.add(get_paragraph_def("9. Mode of Transport", "Helvetica"))
    table_middle1.add(get_paragraph_def("10. Country of Origin", "Helvetica"))
    table_middle1.add(get_paragraph_def("11. Import Date" + "\n" + json['num11'], "Helvetica"))
    table_middle1.add(get_paragraph_def("12. B/L or AWB Number" + "\n" + json['num12'], "Helvetica"))
    table_middle1.add(get_paragraph_def("13. Manufacturer ID" + "\n" + json['num13'], "Helvetica"))
    table_middle1.add(get_paragraph_def("14. Exporting Country", "Helvetica"))
    table_middle1.add(get_paragraph_def("15. Export Date" + "\n" + json['num15'], "Helvetica"))

    table_middle1.paint(page, Rectangle(Decimal(20),
                                        page.get_page_info().get_height() - Decimal(129),
                                        page.get_page_info().get_width() - Decimal(40),
                                        Decimal(20)
                                        ))


def table_middle2_gen(page, json):
    # table_middle2 info setting
    table_middle2: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=1,
        number_of_columns=5,
        column_widths=[Decimal(2.88), Decimal(2), Decimal(2), Decimal(3), Decimal(3)],
    )

    table_middle2.add(get_paragraph_def("16. I.T. Number", "Helvetica"))
    table_middle2.add(get_paragraph_def("17. I.T. Date", "Helvetica"))
    table_middle2.add(get_paragraph_def("18. Missing Docs", "Helvetica"))
    table_middle2.add(get_paragraph_def("19. Foreign Port of Lading" + "\n" + json['num19'], "Helvetica"))
    table_middle2.add(get_paragraph_def("20. U.S. Port of Unloading", "Helvetica"))

    table_middle2.paint(page, Rectangle(Decimal(20),
                                        page.get_page_info().get_height() - Decimal(186),
                                        page.get_page_info().get_width() - Decimal(40),
                                        Decimal(20)
                                        ))


def table_middle3_gen(page, json):
    # table_middle3 info setting
    table_middle3: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=2,
        number_of_columns=4,
        column_widths=[Decimal(2.87), Decimal(2.47), Decimal(2.33), Decimal(2.33)],
    )

    table_middle3.add(get_paragraph_def("21. Location of Goods/G.O. Number" + "\n", "Helvetica"))
    table_middle3.add(get_paragraph_def("22. Consignee Number", "Helvetica"))
    table_middle3.add(get_paragraph_def("23. Importer Number", "Helvetica"))
    table_middle3.add(get_paragraph_def("24. Reference Number", "Helvetica"))
    table_middle3.add(
        TableCell(
            get_paragraph_def(
                "25. Ultimate Consignee Name (Last, First, M.I.) and Address" +
                "\n" + json['num25'] +
                "\n" + "Street: " + json['num25street'] +
                "\n" + json['num25st'] +
                "\n" +
                "\n" + "CustomerReference # " + json['num25customerReference'] +
                "\n" + "City: " + json['num25city'] + "State: " + json['num25state'] + "Zip: " + json['num25zip'],
                "Helvetica"),
            column_span=2))
    table_middle3.add(
        TableCell(
            get_paragraph_def(
                "26. Importer of Record Name(Last, First, M.I.) and Address" +
                "\n" + json['num26'] +
                "\n" + "Street: " + json['num26street'] +
                "\n" + json['num26st'] +
                "\n\n" +
                "\n" + "City: " + json['num26city'] + "State: " + json['num26state'] + "Zip: " + json['num26zip'],
                "Helvetica"),
            column_span=2))

    table_middle3.paint(page, Rectangle(Decimal(20),
                                        page.get_page_info().get_height() - Decimal(215),
                                        page.get_page_info().get_width() - Decimal(40),
                                        Decimal(20)
                                        ))


def table_middle4_gen(page):
    # table_middle4 info setting
    table_middle4: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=2,
        number_of_columns=7,
        column_widths=[Decimal(1), Decimal(2.5), Decimal(2.5), Decimal(2.5), Decimal(2.5), Decimal(2.5), Decimal(2.45)],
    )

    table_middle4.add(TableCell(
        get_paragraph_mid("27. Line No.", "Helvetica"),
        row_span=2
    ))
    table_middle4.add(TableCell(
        get_paragraph_mid("28. Description of Merchandise", "Helvetica"),
        column_span=3
    ))

    table_middle4.add(TableCell(
        get_paragraph_mid(
            "32. " +
            "\n A.	Entered Value" +
            "\n B.	CHGS" +
            "\n C.	Relationship", "Helvetica"),
        row_span=2
    ))
    table_middle4.add(TableCell(
        get_paragraph_mid(
            "33. " +
            "\n A.	HTSUS Rate" +
            "\n B.	ADA/CVD Rate" +
            "\n C.	IRC Rate" +
            "\n D.  Visa No.", "Helvetica"),
        row_span=2
    ))
    table_middle4.add(get_paragraph_mid(
        "34. " +
        "\n Duty and IR Tax",
        "Helvetica"
    ))
    table_middle4.add(get_paragraph_mid(
        "29. " +
        "\n A.	HTSUS No." +
        "\n B.	AD/CVD No.",
        "Helvetica"
    ))
    table_middle4.add(get_paragraph_mid(
        "30. " +
        "\n A.	Gross Weight" +
        "\n B.	Manifest Qty.",
        "Helvetica"
    ))
    table_middle4.add(get_paragraph_mid(
        "31. " +
        "\n Net Quantity in" +
        "\n HTSUS Units",
        "Helvetica"
    ))
    table_middle4.add(get_paragraph_mid(
        "Dollar     Cents",
        "Helvetica"
    ))

    table_middle4.paint(page, Rectangle(Decimal(20),
                                        page.get_page_info().get_height() - Decimal(326),
                                        page.get_page_info().get_width() - Decimal(40),
                                        Decimal(20)
                                        ))


def table_bottom_gen(page, json):
    # table_bottom info setting
    table_bottom: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=13,
        number_of_columns=5,
        column_widths=[Decimal(4.3), Decimal(4.2), Decimal(2.4), Decimal(2.7), Decimal(2.35)],
    )

    table_bottom.add(TableCell(
        get_paragraph_def("Other Fee Summary(for Block 39)" + "\n", "Helvetica"),
        row_span=4
    ))
    table_bottom.add(TableCell(
        get_paragraph_def(
            "35. Total Entered Value" +
            "\n" +
            "\n $ 11,397", "Helvetica"),
        row_span=2
    ))

    table_bottom.add(TableCell(Paragraph(
        "   CBP USE ONLY",
        font_size=Decimal(12),
        font="Helvetica-Bold",
        respect_spaces_in_text=True,
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_bottom=Decimal(3),
        padding_right=Decimal(2)
    ), column_span=2))
    table_bottom.add(Paragraph(
        "   TOTALS",
        font_size=Decimal(12),
        font="Helvetica",
        respect_spaces_in_text=True,
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_bottom=Decimal(3),
        padding_right=Decimal(2)))
    table_bottom.add(TableCell(
        get_paragraph_def("A. LIQ CODE", font="Helvetica"),
        row_span=2
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("B. Ascertained Duty", font="Helvetica"),
        row_span=2
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("37. Duty", font="Helvetica"),
        border_bottom=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_def(
            "Total Other Fees" +
            "\n" +
            f"\n $ {json['totalOtherFees']}", "Helvetica"),
        row_span=2
    ))
    table_bottom.add(TableCell(
        Paragraph(
            str(json['num37Duty']),
            font_size=Decimal(9),
            font="Helvetica",
            horizontal_alignment=Alignment.RIGHT),
        border_top=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("REASON CODE", font="Helvetica"),
        row_span=6
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("C. Ascertained Tax", font="Helvetica"),
        row_span=2
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("38. Tax", font="Helvetica"),
        border_bottom=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_order_info(
            "36. Declaration of Importer of Record (Owner or Purchaser) or Authorized Agent",
            font="Helvetica"),
        column_span=2,
        row_span=2
    ))
    table_bottom.add(TableCell(
        Paragraph(
            "",
            font_size=Decimal(9),
            font="Helvetica",
            horizontal_alignment=Alignment.RIGHT),
        border_top=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("D. Ascertained Other", font="Helvetica"),
        row_span=2
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("39. Other", font="Helvetica"),
        border_bottom=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_att(
            "I declare that I am the Importer of record and that the actual owner," +
            "purchaser, or consignee for CBP purposes is as shown above, OR owner",
            font="Helvetica"),
        column_span=2,
        row_span=3,
        border_bottom=False
    ))

    table_bottom.add(TableCell(
        Paragraph(
            str(json['num39Other']),
            font_size=Decimal(9),
            font="Helvetica",
            horizontal_alignment=Alignment.RIGHT),
        border_top=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("D. Ascertained Total", font="Helvetica"),
        row_span=2
    ))
    table_bottom.add(TableCell(
        get_paragraph_def("40. Total", font="Helvetica"),
        border_bottom=False
    ))
    table_bottom.add(TableCell(
        Paragraph(
            str(json['num40Total']),
            font_size=Decimal(9),
            font="Helvetica",
            horizontal_alignment=Alignment.RIGHT),
        border_top=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_att(
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
            font="Helvetica"),
        column_span=5,
        border_top=False
    ))

    table_bottom.add(TableCell(
        get_paragraph_def(
            "41. Declarant Name (Last, First, M.I.)       Title" +
            "                                                 " +
            "Signature                                                   " +
            "Date\nAMY LEE DBA GUARDIAN CUSTOMS" +
            "                                                              " +
            "                                                               " +
            "12/30/22",
            font="Helvetica"),
        column_span=5
    ))
    table_bottom.add(TableCell(
        get_paragraph_def(
            "42. Broker/Filer Information Name(Last, First, M.I.) and Phone Number",
            font="Helvetica"),
        column_span=2,
        border_bottom=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_def(
            "43. Broker/Importer File Number",
            font="Helvetica"),
        column_span=3,
        border_bottom=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_order_info(
            "AMY YICHIN LEE DBA GUARDIAN CUSTOMS" +
            "\n454 ARCADIA DR" +
            "\nSAN PEDRO, CA 90731   6265525626",
            font="Helvetica"),
        column_span=2,
        border_top=False
    ))
    table_bottom.add(TableCell(
        get_paragraph_order_info(
            "0132257 / EITU1593922",
            font="Helvetica"),
        column_span=3,
        border_top=False
    ))

    table_bottom.paint(page, Rectangle(Decimal(20),
                                       page.get_page_info().get_height() - Decimal(764),
                                       page.get_page_info().get_width() - Decimal(40),
                                       Decimal(280)
                                       ))
