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
			cout<<monitors[0]<<endl;
		}
	
	private:
		
};
