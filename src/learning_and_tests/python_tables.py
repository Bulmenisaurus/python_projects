class Table:
    def __init__(self, table_header, rows):
        """
        Initializes variables and stuffs

        self.columns generates a list of columns
        >>> #[['karate kid', 'nemo'], ['1 hour', '15 min']]

        :param table_header: The header of the table (always on the first row)
        For example: ['Movies', 'length', 'rating']
        :param rows: All the data of a table.
        For example: [['karate kid', '1 hour', '9/10'], ['nemo', '15 min', '0/10']]
        """
        self.table_header = table_header
        self.rows = rows
        self.columns = [[x[i] for x in rows] for i in range(len(rows[0]))]  # magic to het a list of colums
        self.dimensions = (len(self.table_header), len(self.rows))  # x, y dimensions of table

    def _row_widths(self, padding=2):
        """
        This is the most confusing piece of code I have EVER written
        This function gives you the max length of each column, so that you can center each column the same amount

        :padding: adds the padding to every value at the end, so the items aren't hugging the walls
        :return: returns the width of every column. For example: [2, 4, 10]
        """
        initial_widths = [len(item) for item in self.table_header]
        for column_num, column in enumerate(self.columns):
            for column_item in column:
                if len(column_item) > initial_widths[column_num]:
                    initial_widths[column_num] = len(column_item)
        return [pad+padding for pad in initial_widths]

    def _format_header(self, header, header_separator="│"):
        return header_separator.join(header)

    def table(self):
        paddings = self._row_widths()
        headers = '|'.join([d.center(paddings[index]) for index, d in enumerate(self.table_header)])
        print(headers)
        print('-' * len(''.join(headers)))
        data = '|'.join([d.center(paddings[index]) for index, d in enumerate(self.rows[0])])
        print(data)


myTable = Table(['Movies', 'length', 'rating'], [['karate kid 10', '1 hour', '9/10'], ['nemo', '15 min', '15.091%']])
myTable.table()



