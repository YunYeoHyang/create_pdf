from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout

# New import(s)
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.forms.text_field import TextField
from borb.pdf.canvas.color.color import HexColor
from decimal import Decimal
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.forms.drop_down_list import DropDownList

# New import(s)
from borb.pdf.canvas.layout.forms.country_drop_down_list import CountryDropDownList

# New import(s)
import typing
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.page.page_size import PageSize
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory
# from borb.pdf.canvas.layout.image.shape import Shape
#
# ps: typing.Tuple[Decimal, Decimal] = PageSize.A4_PORTRAIT.value
# r: Rectangle = Rectangle(Decimal(0), Decimal(32), ps[0], Decimal(8))
# Shape(points=LineArtFactory.rectangle(r), stroke_color=HexColor("56cbf9"), fill_color=HexColor("56cbf9")).layout(page,
#                                                                                                                  r)

# New import(s)
from borb.pdf.pdf import PDF


def main():
    # 创建空文件
    pdf = Document()

    # 创建空页
    page = Page()

    # 添加页面到文档
    pdf.append_page(page)

    # 创建页面布局
    layout: PageLayout = SingleColumnLayout(page)

    # 让我们从添加一个标题开始
    layout.add(Paragraph("Patient Information:", font="Helvetica-Bold"))

    # 使用一个表格来布置表格
    table: FixedColumnWidthTable = FixedColumnWidthTable(number_of_rows=5, number_of_columns=2)

    # 姓名
    table.add(Paragraph("Name : ", horizontal_alignment=Alignment.RIGHT, font_color=HexColor("56cbf9")))
    table.add(TextField(value="Doe", font_color=HexColor("56cbf9"), font_size=Decimal(20)))

    # 姓氏
    table.add(Paragraph("Surname : ", horizontal_alignment=Alignment.RIGHT, font_color=HexColor("56cbf9")))
    table.add(TextField(value="John", font_color=HexColor("56cbf9"), font_size=Decimal(20)))

    # 性别
    table.add(Paragraph("Gender : ", horizontal_alignment=Alignment.RIGHT))
    table.add(DropDownList(
        possible_values=[
            "女性",
            "男性",
            "其他",
            "保密",
        ]
    ))

    # 居住地
    table.add(Paragraph("Country of Residence : ", horizontal_alignment=Alignment.RIGHT))
    table.add(CountryDropDownList(value="Belgium"))

    # 国籍
    table.add(Paragraph("Nationality : ", horizontal_alignment=Alignment.RIGHT))
    table.add(CountryDropDownList(value="Belgium"))

    # 在表格上设置一些属性以使布局更漂亮
    table.set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    table.no_borders()

    # 在PageLayout中添加表格
    layout.add(table)

    # 数据保护政策
    layout.add(Paragraph("Data Protection Policy",
                         font="Helvetica-Bold"))

    # Dummy 文本
    layout.add(Paragraph(
        """
        ** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """,
        font="Helvetica-Oblique"
    ))