// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int writetofile()
{
    string input = "";
    // How to get a string/sentence with spaces
    cout << "Please enter a valid sentence (with spaces):\n>";
    getline(cin, input);
    ofstream myfile;
    myfile.open ("example.txt");
    myfile << input, "\n";
    myfile.close();
    return 0;
}

int readfromfile()
{
    string line;
    ifstream myfile ("example.txt");
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            cout << "file says " << line << '\n';
        }
    myfile.close();
  }

  else cout << "Unable to open file";

  return 0;
}
int main () {
    writetofile();
    readfromfile();
    return 0;
}
