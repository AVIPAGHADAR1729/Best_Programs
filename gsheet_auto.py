import itertools
from dataclasses import dataclass

import gspread
from gspread.exceptions import (
    IncorrectCellLabel,
    SpreadsheetNotFound,
    WorksheetNotFound,
)


@dataclass
class Gsheet:
    spreadsheet: str
    cred_file: str


@dataclass
class AutoGsheet:
    gsheet: Gsheet

    def __post_init__(self):
        self.client = self.connect()

    def connect(self) -> gspread.Spreadsheet:
        try:
            gc = gspread.service_account(filename=self.gsheet.cred_file)
            sh = gc.open(self.gsheet.spreadsheet)
            return sh
        except SpreadsheetNotFound:
            print("Spreadsheet is Not Found")
        except FileNotFoundError as fne:
            print(fne)

    def get_all_worksheets(self) -> list[gspread.Worksheet]:
        return self.client.worksheets()

    def change_worksheet(self, title: str):
        try:
            return self.client.worksheet(title)
        except WorksheetNotFound:
            print(f"Worksheet {title} in not Found in {self.gsheet.spreadsheet}")

    def show(self, title="Sheet1", /, range_name=None):
        try:
            return self.change_worksheet(title).get_values(range_name)
        except Exception as e:
            print(e)

    def update_cell(self, worksheet: str, cell: tuple[int, int] | str, value: str):
        wh = self.change_worksheet(worksheet)
        if isinstance(cell, tuple):
            wh.update_cell(cell[0], cell[1], value)
        elif isinstance(cell, str):
            try:
                wh.update_acell(cell, value)
            except IncorrectCellLabel:
                print("Invalid cell Label")
        else:
            raise IncorrectCellLabel("Invalid cell Label")

    def update_cells(
        self, worksheet: str, cells: list[tuple[int, int] | str], values: list[str]
    ):
        try:
            for cell, value in itertools.zip_longest(cells, values, fillvalue="None"):
                self.update_cell(worksheet, cell, value)
        except Exception as e:
            print(e)

    def get_cell_value(self, worksheet: str, label: str):
        try:
            return self.change_worksheet(worksheet).get(label)
        except IncorrectCellLabel:
            print("Invalid cell Label")

    def get_cells_value(self, worksheet: str, labels: list[str]):
        try:
            for label in labels:
                yield self.get_cell_value(worksheet, label)
        except Exception as e:
            print(e)

    def get_column_value(self, worksheet: str, indexes: list[int]):
        wh = self.change_worksheet(worksheet)
        if isinstance(indexes, list):
            try:
                for index in indexes:
                    yield f"Col:{index},{wh.col_values(index)}"
            except Exception as e:
                print(e)
        else:
            raise TypeError("indexes must be iterables")

    def get_row_value(self, worksheet: str, indexes: list[int]):
        wh = self.change_worksheet(worksheet)
        if isinstance(indexes, list):
            try:
                for index in indexes:
                    yield f"Row:{index},{wh.row_values(index)}"
            except Exception as e:
                print(e)
        else:
            raise TypeError("indexes must be iterables")

    def add_column(
        self,
        worksheet: str,
        *,
        col: int,
        row_limit: int | list[int],
        value: str = "None",
        offset: int = 1,
    ):

        if isinstance(row_limit, list):
            cells = [(row, col) for row in row_limit]
        elif isinstance(row_limit, int):
            cells = [(row, col) for row in range(1, row_limit + 1, offset)]
        for cell in cells:
            self.update_cell(worksheet, cell, value)


if __name__ == "__main__":
    sheet = Gsheet("gsheet", "creds.json")
    print(sheet)

    auto = AutoGsheet(gsheet=sheet)
    print(auto)

    # print(auto.get_all_worksheets())

    # print(auto.print("q"))

    # auto.update_cell("Sheet1", "B1", "JSONX")
    # print(auto.show("Sheet2", range_name="A:B"))

    # cells = [(1, 1), (1, 2), "A2", "B2", "C1"]
    # values = ("Language", "Year", "JavaScript", "1991")
    # auto.update_cells("Sheet1", cells, values)

    # print(auto.show())
    # print(auto.get_cell_value("Sheet1", "A1"))

    # for v in auto.get_row_value("Sheet1", [1, 4, 5]):
    #     print(v)

    # for v in auto.get_column_value("Sheet1", [1, 2]):
    #     print(v)

    auto.add_column(
        "Sheet1", col=4, row_limit=[1, 2, 11, 20, 50], value="OKOKOK", offset=3
    )
