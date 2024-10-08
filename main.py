import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# Custom canvas class to integrate Matplotlib with PyQt
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Path Input and Switching Views")

        # Call the method to load the initial input view
        self.load_path_input_view()

    def load_path_input_view(self):
        # Create input fields for paths
        self.path_input_1 = QLineEdit()
        self.path_input_1.setPlaceholderText("Enter the first path")

        self.path_input_2 = QLineEdit()
        self.path_input_2.setPlaceholderText("Enter the second path")

        # Create a button to submit paths and switch view
        submit_button = QPushButton("Submit Paths")
        submit_button.clicked.connect(self.load_second_view)

        # Create layout for the input view
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Please enter two paths:"))
        layout.addWidget(self.path_input_1)
        layout.addWidget(self.path_input_2)
        layout.addWidget(submit_button)

        # Set the central widget for this view
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_second_view(self):
        # Retrieve paths from input fields
        path1 = self.path_input_1.text()
        path2 = self.path_input_2.text()

        # Create a pie chart in the second view
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Sample data for pie chart
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]  # Example data for the pie chart
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        explode = (0.1, 0, 0, 0)  # 'explode' the 1st slice

        # Plot pie chart
        self.canvas.axes.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                             shadow=True, startangle=90)
        self.canvas.axes.axis('equal')  # Equal aspect ratio to ensure pie is drawn as a circle.

        # Create a button to return to the input view
        return_button = QPushButton("Return to Path Input")
        return_button.clicked.connect(self.load_path_input_view)

        # Create layout for the second view
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Paths Entered:\nPath 1: {path1}\nPath 2: {path2}"))
        layout.addWidget(self.canvas)
        layout.addWidget(return_button)

        # Set the central widget for this view
        new_widget = QWidget()
        new_widget.setLayout(layout)
        self.setCentralWidget(new_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
