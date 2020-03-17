import openpyxl
from scripts.handle_os import EXCEL_PATH

class obj:
    pass


class HandleExcel:
    def __init__(self, sheetname, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = EXCEL_PATH
        self.sheetname = sheetname

    def open_excel(self):
        self.wb = openpyxl.load_workbook(self.filepath)
        self.sheet = self.wb[self.sheetname]

    def operate_excel(self):
        self.open_excel()
        excel_values = list(self.sheet.rows)
        head_value = [hv.value for hv in excel_values[0]]
        object_list = []
        for arg_value in excel_values[1:]:
            ob = obj()
            values = [av.value for av in arg_value]
            hv_zip = zip(head_value, values)
            for hz in hv_zip:
                setattr(ob, hz[0], hz[1])
            object_list.append(ob)
        self.wb.close()
        return object_list

    def write_excel(self, rowid, colid, sheet_value):
        self.open_excel()
        self.sheet.cell(row=rowid, column=colid, value=sheet_value)
        self.wb.save(self.filepath)
        self.wb.close()


if __name__ == '__main__':
    he = HandleExcel('register')
    list_obj = he.operate_excel()
    for obj in list_obj:
        print(obj.data)