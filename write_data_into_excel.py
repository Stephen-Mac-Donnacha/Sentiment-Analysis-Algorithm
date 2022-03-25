import openpyxl
from main import capture_profile_and_analyse

# Workbook saved here as a global variable
wb = openpyxl.Workbook()

def get_profile_data():
    data1 = capture_profile_and_analyse()
    return data1


def write_sentiment_data_to_excel():
    sentiment_data = get_profile_data()

    # Create worksheet for sentiment data
    sheet = wb.active

    # One can change the name of the title
    sheet.title = "Sentiment Data "

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
