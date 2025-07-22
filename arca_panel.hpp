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


			// Updates based on parameters in /etc/Arca/panel.conf
			update();

			// Sets the proper panel width
			setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
			setGeometry(0, 0, 
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
			vector<string> split_string = StrSplit(mMain_monitor, 'x');

	
};
