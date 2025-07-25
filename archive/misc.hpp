using namespace std;

string GetStdoutFromCommand(string cmd) {

  string data;
  FILE * stream;
  const int max_buffer = 256;
  char buffer[max_buffer];
  cmd.append(" 2>&1");

  stream = popen(cmd.c_str(), "r");
  if (stream) {
    while (!feof(stream))
      if (fgets(buffer, max_buffer, stream) != NULL) data.append(buffer);
    pclose(stream);
  }
  return data;
}

vector<string> strSplit(string str, char delim) {
	stringstream ss(str);
	string buffer;
	vector<string> split_string;
	while(getline(ss, buffer, delim)) {
		split_string.push_back(buffer);
	return split_string;
