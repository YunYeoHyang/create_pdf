from decimal import Decimal

from borb.pdf import Paragraph, Alignment


def get_paragraph_def(value, font) -> Paragraph:
    return Paragraph(
        value,
        font=font,
        respect_newlines_in_text=True,
        respect_spaces_in_text=True,
        font_size=Decimal(9),
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_bottom=Decimal(2),
        padding_right=Decimal(2)
    )


def get_paragraph_mid(value, font) -> Paragraph:
    return Paragraph(
        value,
        font=font,
        respect_newlines_in_text=True,
        respect_spaces_in_text=True,
        text_alignment=Alignment.CENTERED,
        horizontal_alignment=Alignment.CENTERED,
        font_size=Decimal(9),
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_bottom=Decimal(3),
        padding_right=Decimal(2)
    )


def get_paragraph_order_index(value, font) -> Paragraph:
    return Paragraph(
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
        padding_right=Decimal(2)
    )


def get_paragraph_order_info(value, font) -> Paragraph:
    return Paragraph(
        value,
        font=font,
        respect_newlines_in_text=True,
        respect_spaces_in_text=True,
        font_size=Decimal(10),
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_bottom=Decimal(3),
        padding_right=Decimal(2)
    )


def get_paragraph_att(value, font) -> Paragraph:
    return Paragraph(
        value,
        font=font,
        respect_newlines_in_text=True,
        respect_spaces_in_text=True,
        font_size=Decimal(8),
        padding_top=Decimal(2),
        padding_left=Decimal(2),
        padding_right=Decimal(2),
        margin_top=Decimal(2),
        margin_left=Decimal(5),
        margin_right=Decimal(5),
        fixed_leading=Decimal(8)
    )
