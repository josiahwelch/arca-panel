#include <iostream>
#include <QApplication>
#include <QWidget>
#include <QPushButton>
#include <QMainWindow>
#include <QToolBar>
#include <QHBoxLayout>
#include <vector>
#include "arca_panel.hpp"
#include "misc.hpp"

using namespace std;

int main(int argc, char* argv[]) {
	vector<string> monitors;

	QApplication app(argc, argv);
	monitors.push_back(GetStdoutFromCommand("xdpyinfo | awk \'/dimensions:/ { print $2 }\'"));
	monitors.push_back("test");
	ArcaPanel arca_panel(monitors);
	arca_panel.show();
	return app.exec();
}
