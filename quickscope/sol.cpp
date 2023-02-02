#include <unordered_map>
#include <vector>
#include <iostream>
#include <ios>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

	int n;
	string t, iden, typ;
	cin >> n;


	vector<unordered_map<string, string> > context;
	unordered_map<string, string> global;
	context.push_back(global);

	for(int i = 0; i < n; i += 1) {
		cin >> t;
		if(t == "{") {
			unordered_map<string, string> nm;
			context.push_back(nm);
		} else if (t == "}") 
			context.pop_back();
		else if(t == "DECLARE") {
			cin >> iden;
			cin >> typ;
			unordered_map<string, string> last_scope = context[context.size() - 1];
			if(last_scope.find(iden) == last_scope.end()) {
				context.back()[iden] = typ;
			}
			else {
				cout << "MULTIPLE DECLARATION" << endl;
				break;
			}
		} else if (t == "TYPEOF") {
			cin >> iden;
			bool found = false;
			for(int j = context.size() - 1; j >= 0; j -= 1) {
				unordered_map<string, string> d = context[j];
				if(d.find(iden) == d.end()) {
					continue;
				} else {
					cout << d[iden] << endl;
					found = true;
					break;
				}
			}
			if(!found)
				cout << "UNDECLARED" << endl;
		}
	}
}
