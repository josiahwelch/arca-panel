// Josiah Welch July 8th, 2025
//
// Arca v0.2 - Alpha 2
// Arca Panel v0.2
// C++ rewrite
#include <iostream>
#include <QApplication>
#include <QWidget>
#include <QPushButton>
#include <QMainWindow>
#include <QToolBar>
#include <QHBoxLayout>
#include <vector>

using namespace std;

class ArcaPanel : public QWidget {
	Q_OBJECT
	public:
		ArcaPanel(vector<string> monitors, QWidget *parent = nullptr) : QWidget(parent) {
			// Sets/gets monitor information
			mMonitors = monitors;
			mGetDimensions();

			// Updates based on parameters in /etc/Arca/panel.conf
			mUpdate();

			// Sets the proper panel width
			setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint);
			setGeometry(0, 0, mWidth, mHeight * 0.05); // Sets the dimensions of the menu to be the width of the screen and 5% of the height

			// Sets the dimensions of the M.A.T. button
			mMat_button.setFixedWidth(static_cast<int>(mWidth * 0.1));
			mMat_button.setFixedHeight(static_cast<int>(mHeight * 0.5));

			// Sets the dimensions of the Misc button
			mMisc_button.setFixedWidth(static_cast<int>(mWidth * 0.1));
			mMisc_button.setFixedHeight(static_cast<int>(mHeight * 0.5));
			
			// Sets the dimensions of the Time widget
			mTime_widget.setFixedWidth(static_cast<int>(mWidth * 0.1));
			mTime_widget.setFixedHeight(static_cast<int>(mHeight * 0.5));

		}
	
	private:
		// Initializes monitor information
		vector<string> mMonitors;
		string mMain_monitor;
		int mWidth;
		int mHeight;

		// Initializes the variables
		QHBoxLayout mLayout = QHBoxLayout();
		MATButton mMat_button = MATButton();
		MiscButton mMisc_button = MiscButton("Logout");
		TimeWidget mTime_widget = TimeWidget();

		// Private methods
		void mGetDimensions() {
			vector<string> split_string = StrSplit(mMain_monitor, 'x'); // Splits "1080x1920" into {"1080", "1920"}
			mWidth = split_string[0];
			mHeight = split_string[1];
		}
};
