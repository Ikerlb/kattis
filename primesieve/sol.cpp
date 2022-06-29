#include <cmath>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
	int n;
	int q;
	int i;
	int count = 0;

	cin >> n;
	cin >> q;

    vector<bool> primes(n+1, true);
    primes[0] = false;
    primes[1] = false;
    int m = sqrt(n);

	for(int i = 2; i <= n; i++) {
		if(primes[i]) {
			count += 1;
			for(int j = 2 * i; j <= n; j += i) {
				primes[j] = false;
			}
		}
	}

	cout << count << endl;
	while(q--){
		cin >> i;
		cout << primes[i] << endl;
	}

}
