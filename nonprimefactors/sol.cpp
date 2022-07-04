#include <iostream>
#include <vector>
#include <tuple>
#include <utility>

using namespace std;

void fast() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
}

int num_factors(int n, vector<int> primes) {
	int res = 1;
	for(int i = 0; n != 1 && primes[i] < 2000; i += 1) {
		int pow = 0;
		while(n % primes[i] == 0){
			pow += 1;
			n /= primes[i];
		}
		res *= (pow + 1);
	}	
	if(n != 1) 
		return 2 * res;
	return res;
}

int main() {
	//fast();

	int tcs;
	int n;
	cin >> tcs;

	const int MAXN = 2000001;
	int sieve[MAXN];		
	vector<int> primes;

	for(int i = 2; i < MAXN; i += 1) {
		if(sieve[i] == 0) {
			primes.push_back(i);
			for(int j = i; j < MAXN; j += i) {
				sieve[j] += 1;				
			}
		}
	}
		
	//cout << primes.size() << endl;
	//for(int i = 0; i < 20; i += 1) {
	//	cout << primes[i] << endl;
	//}

	while(tcs--) {
		cin >> n; 
		int res = num_factors(n, primes);
		cout << res - sieve[n] << endl;
	}
}
