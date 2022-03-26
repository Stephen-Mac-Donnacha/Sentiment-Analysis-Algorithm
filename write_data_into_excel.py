import openpyxl
from openpyxl.chart import PieChart
from openpyxl.chart.series import DataPoint
from main import capture_profile_and_analyse

# Workbook saved here as a global variable
wb = openpyxl.Workbook()


def get_profile_data():
    data_arr = capture_profile_and_analyse()

    for i in range(len(data_arr)):
        data1 = data_arr[0]
        data2 = data_arr[1]

    return data1, data2


sentiment_data = get_profile_data()[0]


def write_sentiment_data_to_excel():
    # Create worksheet for sentiment data
    sheet = wb.active

    # One can change the name of the title
    sheet.title = "Sentiment Data"

    # print("Printing data to worksheet :", sheet.title)

    sheet['A1'] = "Date"
    sheet['B1'] = "Sentiment"

    for row, (Date, Sentiment) in enumerate(sentiment_data.items(), start=2):
        sheet[f"A{row}"] = Date
        sheet[f"B{row}"] = Sentiment

    wb.save("C:\\Users\\Stephen Mac Donnacha\\PycharmProjects\\Final Year Project\\excel-worksheets\\fyp-data.xlsx")


def create_workbook():
    # Call a Workbook() function of openpyxl
    # to create a new blank Workbook object

    # Get workbook active sheet
    # from the active attribute
    sheet = wb.active

    # One can change the name of the title
    sheet.title = "sheet1"

    print("sheet name is titled as: " + sheet.title)


def main():
    # create_workbook()
    # get_profile_data()
    write_sentiment_data_to_excel()


if __name__ == "__main__":
    main()
