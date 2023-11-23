from decimal import Decimal

from borb.pdf import Paragraph, Alignment, TableCell


def get_table_cell_title_def(value, font, column_span, row_span) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            font_size=Decimal(9),
            padding_top=Decimal(1.3),
            padding_left=Decimal(1),
            padding_right=Decimal(2),
        ),
        border_bottom=False,
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span
    )


def get_table_cell_content_def(value, font, column_span, row_span, horizontal_alignment) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            horizontal_alignment=horizontal_alignment,
            font_size=Decimal(10),
            padding_left=Decimal(3),
            padding_bottom=Decimal(1.6),
            padding_right=Decimal(2),
            fixed_leading=Decimal(0.9)
        ),
        border_top=False,
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span
    )


def get_table_cell_def(value, font, font_size, column_span, row_span) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            font_size=Decimal(font_size),
            padding_top=Decimal(0.8),
            padding_left=Decimal(2),
            fixed_leading=Decimal(0.9)
        ),
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span
    )


def get_table_cell_center(value, font, font_size, column_span, row_span, vertical_alignment) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.CENTERED,
            horizontal_alignment=Alignment.CENTERED,
            vertical_alignment=vertical_alignment,
            font_size=Decimal(font_size),
            padding_top=Decimal(0.8),
            padding_left=Decimal(2),
            fixed_leading=Decimal(0.9)
        ),
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span
    )


def get_table_cell_att(value, font, padding_top, column_span, row_span, border_top, border_bottom) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            font_size=Decimal(8),
            padding_top=Decimal(padding_top),
            padding_left=Decimal(2),
            padding_right=Decimal(2),
            margin_top=Decimal(2),
            margin_left=Decimal(5),
            margin_right=Decimal(5),
            fixed_leading=Decimal(7)
        ),
        border_top=border_top,
        border_bottom=border_bottom,
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span
    )


def get_table_cell_order_index(value, font, column_span, row_span, border_top, border_bottom) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            text_alignment=Alignment.RIGHT,
            horizontal_alignment=Alignment.RIGHT,
            font_size=Decimal(10),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_bottom=Decimal(3),
            padding_right=Decimal(2),
        ),
        border_top=border_top,
        border_bottom=border_bottom,
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span,
    )


def get_table_cell_order_info(value, font, column_span, row_span, border_top, border_bottom, border_right, border_left,
                              horizontal_alignment) -> TableCell:
    return TableCell(
        Paragraph(
            value,
            font=font,
            respect_newlines_in_text=True,
            respect_spaces_in_text=True,
            horizontal_alignment=horizontal_alignment,
            font_size=Decimal(10),
            padding_top=Decimal(2),
            padding_left=Decimal(2),
            padding_bottom=Decimal(3),
            padding_right=Decimal(2),
            fixed_leading=Decimal(0.9)
        ),
        border_top=border_top,
        border_bottom=border_bottom,
        border_right=border_right,
        border_left=border_left,
        border_width=Decimal(0.5),
        column_span=column_span,
        row_span=row_span,
    )
