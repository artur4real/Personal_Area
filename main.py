import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from queries import insert_schedule_data

class ScheduleApp(QDialog):
    def __init__(self):
        super(ScheduleApp, self).__init__()
        loadUi("ui/window.ui", self)

        self.pushButton.clicked.connect(self.add_schedule)

    def add_schedule(self):
        day_of_week = self.tableWidget.item(0, 0).text()
        start_time = self.tableWidget.item(0, 1).text()
        end_time = self.tableWidget.item(0, 2).text()
        break_start_time = self.tableWidget.item(0, 3).text()
        break_end_time = self.tableWidget.item(0, 4).text()

        if not all([day_of_week, start_time, end_time, break_start_time, break_end_time]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")
            return

        try:
            # Пример: int_value = int(start_time)
            # Повторите для других значений, если они должны быть целыми числами
            pass
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Некорректный формат числа.")
            return

        schedule_data = (day_of_week, start_time, end_time, break_start_time, break_end_time)

        try:
            insert_schedule_data(schedule_data)
            QMessageBox.information(self, "Успех", "Данные расписания добавлены успешно!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при добавлении данных: {str(e)}")

        self.clear_input_fields()

    def clear_input_fields(self):
        for col in range(self.tableWidget.columnCount()):
            item = QTableWidgetItem("")
            self.tableWidget.setItem(0, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScheduleApp()
    window.show()
    sys.exit(app.exec_())
