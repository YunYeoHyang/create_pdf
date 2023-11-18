import typing
from decimal import Decimal

from borb.pdf import MultiColumnLayout


class Layout(MultiColumnLayout):
    def __init__(self, page):
        w: typing.Optional[Decimal] = page.get_page_info().get_width()
        h: typing.Optional[Decimal] = page.get_page_info().get_height()
        assert w is not None
        assert h is not None
        super().__init__(
            page=page,
            column_widths=[w * Decimal(0.93)],
            footer_paint_method=None,
            header_paint_method=None,
            inter_column_margins=[],
            margin_bottom=h * Decimal(0.02),
            margin_left=w * Decimal(0.04),
            margin_right=w * Decimal(0.04),
            margin_top=h * Decimal(0.02),
        )