import os
from pathlib import Path

from borb.pdf import Image, Page
from borb.pdf.canvas.geometry.rectangle import Rectangle

from tools.data_tools import check_json_for_key
from tools.paragraph_style import *

root_dir = os.path.dirname(__file__)


def page_head_bottom(pdf):
    number_of_pages = int(pdf.get_document_info().get_number_of_pages())

    for index in range(0, number_of_pages):
        page: Page = pdf.get_page(index)

        Image(
            Path(f"{root_dir}/../source/logo.jpg"),
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
            vertical_alignment=Alignment.BOTTOM).paint(page, Rectangle(Decimal(27),
                                                                       Decimal(9),
                                                                       Decimal(100),
                                                                       Decimal(20)
                                                                       ))

        Paragraph(
            f"Page {index + 1} of {number_of_pages}",
            font_size=Decimal(8),
            font="Helvetica-Bold",
            horizontal_alignment=Alignment.RIGHT,
            vertical_alignment=Alignment.BOTTOM).paint(page, Rectangle(page.get_page_info().get_width() - Decimal(127),
                                                                       Decimal(9),
                                                                       Decimal(100),
                                                                       Decimal(20)
                                                                       ))


def table_front_gen(table, j):
    table.add(get_table_cell_title_def("1. Filer Code/Entry Number", "Helvetica", 2, 1))
    table.add(get_table_cell_title_def("2. Entry Type", "Helvetica", 3, 1))
    table.add(get_table_cell_title_def("3. Summary Date", "Helvetica", 3, 1))
    table.add(get_table_cell_title_def("4. Surety Number", "Helvetica", 2, 1))
    table.add(get_table_cell_title_def("5. Bond Type", "Helvetica", 2, 1))
    table.add(get_table_cell_title_def("6. Port Code", "Helvetica", 2, 1))
    table.add(get_table_cell_title_def("7. Entry Date", "Helvetica", 2, 1))
    table.add(get_table_cell_content_def(f"{j['num1']}", "Helvetica", 2, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("01   ABI/A", "Helvetica", 3, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(f"{j['num3']}", "Helvetica", 3, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(" 036", "Helvetica", 2, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(" 8", "Helvetica", 2, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(" 2704", "Helvetica", 2, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(f"{j['num7']}", "Helvetica", 2, 1, Alignment.LEFT))


def table_middle1_gen(table, j):
    table.add(get_table_cell_title_def("8. Importing Carrier", "Helvetica", 4, 1))
    table.add(get_table_cell_title_def("9. Mode of Transport", "Helvetica", 5, 1))
    table.add(get_table_cell_title_def("10. Country of Origin", "Helvetica", 5, 1))
    table.add(get_table_cell_title_def("11. Import Date", "Helvetica", 2, 1))
    table.add(get_table_cell_content_def(f"{j['num8']}", "Helvetica", 4, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(" 11", "Helvetica", 5, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("CN", "Helvetica", 5, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(f"{j['num11']}", "Helvetica", 2, 1, Alignment.LEFT))

    table.add(get_table_cell_title_def("12. B/L or AWB Number", "Helvetica", 4, 1))
    table.add(get_table_cell_title_def("13. Manufacturer ID", "Helvetica", 5, 1))
    table.add(get_table_cell_title_def("14. Exporting Country", "Helvetica", 5, 1))
    table.add(get_table_cell_title_def("15. Export Date", "Helvetica", 2, 1))
    table.add(get_table_cell_content_def(f"{j['num12']}", "Helvetica", 4, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(f"{j['num13']}", "Helvetica", 5, 1, Alignment.RIGHT))
    table.add(get_table_cell_content_def("CN", "Helvetica", 5, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(f"{j['num15']}", "Helvetica", 2, 1, Alignment.LEFT))


def table_middle2_gen(table, j):
    table.add(get_table_cell_title_def("16. I.T. Number", "Helvetica", 2, 1))
    table.add(get_table_cell_title_def("17. I.T. Date", "Helvetica", 4, 1))
    table.add(get_table_cell_title_def("18. Missing Docs", "Helvetica", 3, 1))
    table.add(get_table_cell_title_def("19. Foreign Port of Lading", "Helvetica", 4, 1))
    table.add(get_table_cell_title_def("20. U.S. Port of Unloading", "Helvetica", 3, 1))

    table.add(get_table_cell_content_def("", "Helvetica", 2, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("", "Helvetica", 4, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("", "Helvetica", 3, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(f"{j['num19']}", "Helvetica", 4, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("2709", "Helvetica", 3, 1, Alignment.LEFT))


def table_middle3_gen(table, j):
    table.add(get_table_cell_title_def("21. Location of Goods/G.O. Number", "Helvetica", 3, 1))
    table.add(get_table_cell_title_def("22. Consignee Number", "Helvetica", 6, 1))
    table.add(get_table_cell_title_def("23. Importer Number", "Helvetica", 4, 1))
    table.add(get_table_cell_title_def("24. Reference Number", "Helvetica", 3, 1))
    table.add(get_table_cell_content_def("Z666 Voyage: 0399", "Helvetica", 3, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("87-432023400", "Helvetica", 6, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("87-432023400", "Helvetica", 4, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def("", "Helvetica", 3, 1, Alignment.LEFT))

    table.add(get_table_cell_title_def("25. Ultimate Consignee Name (Last, First, M.I.) and Address",
                                       "Helvetica", 9, 1))
    table.add(get_table_cell_title_def("26. Importer of Record Name(Last, First, M.I.) and Address",
                                       "Helvetica", 7, 1))
    table.add(get_table_cell_content_def(
        f"{j['num25']}" +
        f"\nStreet: {j['num25street']}" +
        f"\n{j['num25st']}\n" +
        f"\nDestination: CA\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" +
        (f"CustomerReference # {j['num25customerReference']}" if check_json_for_key(j, 'num25customerReference')
         else "") +
        f"\nCity: {j['num25city']}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" +
        f"State: {j['num25state']}   Zip: {j['num25zip']}",
        "Helvetica", 9, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(
        f"{j['num26']}" +
        f"\nStreet: {j['num26street']}" +
        f"\n{j['num26st']}\n\n" +
        f"\nCity: {j['num26city']}\t\t\t\t" +
        f"State: {j['num26state']}   Zip: {j['num26zip']}",
        "Helvetica", 7, 1, Alignment.LEFT))


def table_middle4_gen(table):
    table.add(get_table_cell_center("27.  Line No.", "Helvetica", 9, 1, 2, Alignment.MIDDLE))
    table.add(get_table_cell_center("28. Description of Merchandise", "Helvetica", 9, 8, 1, Alignment.MIDDLE))
    table.add(get_table_cell_center(
        "32. " +
        "\nA.	Entered Value" +
        "\nB.	CHGS" +
        "\nC.	Relationship", "Helvetica", 9, 2, 2, Alignment.MIDDLE))
    table.add(get_table_cell_center(
        "33. " +
        "\nA.	HTSUS Rate" +
        "\nB.	ADA/CVD Rate" +
        "\nC.	IRC Rate" +
        "\nD.  Visa No.", "Helvetica", 9, 3, 2, Alignment.MIDDLE))
    table.add(get_table_cell_center(
        "34. " +
        "\nDuty and IR Tax",
        "Helvetica", 9, 2, 1, Alignment.MIDDLE))
    table.add(get_table_cell_center(
        "29. " +
        "\nA.	HTSUS No." +
        "\nB.	AD/CVD No.",
        "Helvetica", 9, 1, 1, Alignment.MIDDLE))
    table.add(get_table_cell_center(
        "30. " +
        "\nA.	Gross Weight" +
        "\nB.	Manifest Qty.",
        "Helvetica", 9, 4, 1, Alignment.MIDDLE))
    table.add(get_table_cell_center(
        "31. " +
        "\nNet Quantity in" +
        "\nHTSUS Units",
        "Helvetica", 9, 3, 1, Alignment.MIDDLE))
    table.add(get_table_cell_center(
        "Dollar     Cents",
        "Helvetica", 9, 2, 1, Alignment.TOP))


def table_bottom_gen(table, j, page):
    Image(
        Path(f"{root_dir}/../source/image1.jpg"),
        width=Decimal(14),
        height=Decimal(14),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP
    ).paint(page, Rectangle(Decimal(109),
                            page.get_page_info().get_height() - Decimal(596.5),
                            Decimal(21),
                            Decimal(21)
                            ))

    Image(
        Path(f"{root_dir}/../source/image2.jpg"),
        width=Decimal(14),
        height=Decimal(14),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP
    ).paint(page, Rectangle(Decimal(266.5),
                            page.get_page_info().get_height() - Decimal(611),
                            Decimal(21),
                            Decimal(21)
                            ))

    Image(
        Path(f"{root_dir}/../source/image2.jpg"),
        width=Decimal(14),
        height=Decimal(14),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP
    ).paint(page, Rectangle(Decimal(275),
                            page.get_page_info().get_height() - Decimal(628),
                            Decimal(21),
                            Decimal(21)
                            ))

    Image(
        Path(f"{root_dir}/../source/image1.jpg"),
        width=Decimal(14),
        height=Decimal(14),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP
    ).paint(page, Rectangle(Decimal(186),
                            page.get_page_info().get_height() - Decimal(644),
                            Decimal(21),
                            Decimal(21)
                            ))

    table.add(get_table_cell_def("Other Fee Summary(for Block 39)", "Helvetica", 9, 3, 4))
    table.add(get_table_cell_title_def("35. Total Entered Value", "Helvetica", 6, 1))
    table.add(get_table_cell_def("   CBP USE ONLY", "Helvetica-Bold", 12, 5, 1))
    table.add(get_table_cell_def("   TOTALS", "Helvetica", 12, 2, 1))
    table.add(get_table_cell_content_def("$ 11,397", "Helvetica", 6, 1, Alignment.LEFT))
    table.add(get_table_cell_def("A. LIQ CODE", "Helvetica", 9, 2, 2))
    table.add(get_table_cell_def("B. Ascertained Duty", "Helvetica", 9, 3, 2))
    table.add(get_table_cell_title_def("37. Duty", "Helvetica", 2, 1))
    table.add(get_table_cell_title_def("Total Other Fees", "Helvetica", 6, 1))
    table.add(get_table_cell_content_def(f"$ {j['num37Duty']}", "Helvetica", 2, 1, Alignment.RIGHT))
    table.add(get_table_cell_content_def(f"$ {j['totalOtherFees']}", "Helvetica", 6, 1, Alignment.LEFT))
    table.add(get_table_cell_def("REASON CODE", "Helvetica", 9, 2, 6))
    table.add(get_table_cell_def("C. Ascertained Tax", "Helvetica", 9, 3, 2))
    table.add(get_table_cell_title_def("38. Tax", "Helvetica", 2, 1))
    table.add(get_table_cell_def(
        "36. Declaration of Importer of Record (Owner or Purchaser) or Authorized Agent",
        "Helvetica", 10, 9, 2))
    table.add(get_table_cell_content_def("", "Helvetica", 2, 1, Alignment.RIGHT))
    table.add(get_table_cell_def("D. Ascertained Other", "Helvetica", 9, 3, 2))
    table.add(get_table_cell_title_def("39. Other", "Helvetica", 2, 1))
    table.add(get_table_cell_att(
        "I declare that I am the         Importer of record and that the actual owner, " +
        "purchaser, or consignee for CBP purposes is as shown above, OR         owner",
        "Helvetica", 8, 9, 3, True, False))
    table.add(get_table_cell_content_def(f"$ {j['num39Other']}", "Helvetica", 2, 1, Alignment.RIGHT))
    table.add(get_table_cell_def("D. Ascertained Total", "Helvetica", 9, 3, 2))
    table.add(get_table_cell_title_def("40. Total", "Helvetica", 2, 1))
    table.add(get_table_cell_content_def(f"$ {j['num40Total']}", "Helvetica", 2, 1, Alignment.RIGHT))
    table.add(get_table_cell_att(
        "or purchaser or agent thereof.  I further declare that the merchandise         was " +
        "obtained pursuant to a purchase or agreement to purchase and that the" +
        "\n prices set forth in the invoices are true, OR         " +
        "was not obtained pursuant to a purchase or agreement to purchase and the statements in the invoices as" +
        "\n to value or price are true to the best of my knowledge and belief.  " +
        "I also declare that the statements in the documents herein filed fully disclose to the best of my " +
        "knowledge and belief the true prices, values, quantities, rebates, drawbacks, fees, commissions, " +
        "and royalties and are true and correct, and that all goods or services provided to the seller of the" +
        " merchandise either free or at reduced cost are fully disclosed. \n I will immediately furnish to the " +
        "appropriate CBP officer any information showing a different statement of facts.",
        "Helvetica", 2, 16, 1, False, True))
    table.add(get_table_cell_def(
        "41. Declarant Name (Last, First, M.I.)       Title" +
        "                                                 " +
        "Signature                                                   " +
        "Date\nAMY LEE DBA GUARDIAN CUSTOMS" +
        "                                                              " +
        "                                                               " +
        "12/30/22",
        "Helvetica", 9, 16, 1))
    table.add(get_table_cell_title_def("42. Broker/Filer Information Name(Last, First, M.I.) and Phone Number",
                                       "Helvetica", 9, 1))
    table.add(get_table_cell_title_def("43. Broker/Importer File Number",
                                       "Helvetica", 7, 1))
    table.add(get_table_cell_content_def(
        "AMY YICHIN LEE DBA GUARDIAN CUSTOMS" +
        "\n454 ARCADIA DR" +
        "\nSAN PEDRO, CA 90731   6265525626",
        "Helvetica", 9, 1, Alignment.LEFT))
    table.add(get_table_cell_content_def(
        "0132257 / EITU1593922",
        "Helvetica", 7, 1, Alignment.LEFT))
