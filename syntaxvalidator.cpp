#include <iostream>
#include <fstream>
#include <stack>
#include <string>
using namespace std;

struct Bracket {
    char ch;
    int line;
    int col;
};

bool validateSyntax(const string &fileName) {
    ifstream in(fileName);
    if (!in.is_open()) {
        cout << "Error: Cannot open file -> " << fileName << endl;
        return false;
    }

    stack<Bracket> st;
    char ch;
    int line = 1, col = 0;
    bool valid = true;

    while (in.get(ch)) {
        col++;
        if (ch == '\n') {
            line++;
            col = 0;
        }

        if (ch == '(' || ch == '{' || ch == '[') {
            st.push({ch, line, col});
        } else if (ch == ')' || ch == '}' || ch == ']') {
            if (st.empty()) {
                cout << "❌ Error: Unmatched closing '" << ch
                     << "' at line " << line << ", col " << col << endl;
                valid = false;
            } else {
                Bracket top = st.top();
                if ((ch == ')' && top.ch != '(') ||
                    (ch == '}' && top.ch != '{') ||
                    (ch == ']' && top.ch != '[')) {
                    cout << "❌ Error: Mismatched '" << top.ch
                         << "' (opened at line " << top.line << ", col " << top.col
                         << ") with closing '" << ch
                         << "' at line " << line << ", col " << col << endl;
                    valid = false;
                }
                st.pop();
            }
        }
    }

    while (!st.empty()) {
        Bracket top = st.top();
        cout << "❌ Error: Unmatched opening '" << top.ch
             << "' at line " << top.line << ", col " << top.col << endl;
        st.pop();
        valid = false;
    }

    in.close();
    return valid;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " <source-file>" << endl;
        return 1;
    }

    string fileName = argv[1];

    if (validateSyntax(fileName)) {
        cout << "✅ Syntax check passed" << endl;
    } else {
        cout << "❌ Syntax check failed" << endl;
    }

    return 0;
}
