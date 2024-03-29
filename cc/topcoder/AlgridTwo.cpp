#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

class AlgridTwo {
public:
  int makeProgram(vector <string> output) {
    return solve(output, output.size()-2, output[0].size()-2);
  }
  int solve(vector <string> output, int i, int j) {
    vector<string> temp(output);
    if (i == 0 && j == 0)
      return 1;
    int result = 0;
    int next_j = (j==0) ? output[0].size()-2 : j-1;
    int next_i = (j==0) ? i-1 : i;
    if (output[i][j] == 'W' && output[i][j+1] == 'W') {
      return solve(output, next_i, next_j);
    } else if (output[i][j] == 'B' && output[i][j+1] == 'W') {
      if (output[i+1][j] != 'B' || output[i+1][j+1] != 'B')
        return 0;
      temp[i+1][j] = 'W'; temp[i+1][j+1] = 'W'; result += solve(temp, next_i, next_j);
      temp[i+1][j] = 'W'; temp[i+1][j+1] = 'B'; result += solve(temp, next_i, next_j);
      temp[i+1][j] = 'B'; temp[i+1][j+1] = 'W'; result += solve(temp, next_i, next_j);
      temp[i+1][j] = 'B'; temp[i+1][j+1] = 'B'; result += solve(temp, next_i, next_j);
    } else if (output[i][j] == 'W' && output[i][j+1] == 'B') {
      if (output[i+1][j] != 'W' || output[i+1][j+1] != 'W')
        return 0;
      temp[i+1][j] = 'W'; temp[i+1][j+1] = 'W'; result += solve(temp, next_i, next_j);
      temp[i+1][j] = 'W'; temp[i+1][j+1] = 'B'; result += solve(temp, next_i, next_j);
      temp[i+1][j] = 'B'; temp[i+1][j+1] = 'W'; result += solve(temp, next_i, next_j);
      temp[i+1][j] = 'B'; temp[i+1][j+1] = 'B'; result += solve(temp, next_i, next_j);
    } else if (output[i][j] == 'B' && output[i][j+1] == 'B') {
      char c = temp[i+1][j];
      temp[i+1][j] = temp[i+1][j+1];
      temp[i+1][j+1] = c;
      result += solve(temp, next_i, next_j);
    }
    return result;
  }

  
// BEGIN CUT HERE
	public:
	void run_test(int Case) { if ((Case == -1) || (Case == 0)) test_case_0(); if ((Case == -1) || (Case == 1)) test_case_1(); if ((Case == -1) || (Case == 2)) test_case_2(); if ((Case == -1) || (Case == 3)) test_case_3(); }
	private:
	template <typename T> string print_array(const vector<T> &V) { ostringstream os; os << "{ "; for (typename vector<T>::const_iterator iter = V.begin(); iter != V.end(); ++iter) os << '\"' << *iter << "\","; os << " }"; return os.str(); }
	void verify_case(int Case, const int &Expected, const int &Received) { cerr << "Test Case #" << Case << "..."; if (Expected == Received) cerr << "PASSED" << endl; else { cerr << "FAILED" << endl; cerr << "\tExpected: \"" << Expected << '\"' << endl; cerr << "\tReceived: \"" << Received << '\"' << endl; } }
	void test_case_0() { string Arr0[] = {"BB",
 "WB"}; vector <string> Arg0(Arr0, Arr0 + (sizeof(Arr0) / sizeof(Arr0[0]))); int Arg1 = 1; verify_case(0, Arg1, makeProgram(Arg0)); }
	void test_case_1() { string Arr0[] = {"BBWBBB",
 "WBWBBW"}; vector <string> Arg0(Arr0, Arr0 + (sizeof(Arr0) / sizeof(Arr0[0]))); int Arg1 = 8; verify_case(1, Arg1, makeProgram(Arg0)); }
	void test_case_2() { string Arr0[] = {"BWBWBW",
 "WWWWWW",
 "WBBWBW"}; vector <string> Arg0(Arr0, Arr0 + (sizeof(Arr0) / sizeof(Arr0[0]))); int Arg1 = 0; verify_case(2, Arg1, makeProgram(Arg0)); }
	void test_case_3() { string Arr0[] = {"WWBWBWBWBWBWBWBW",
 "BWBWBWBWBWBWBWBB",
 "BWBWBWBWBWBWBWBW"}; vector <string> Arg0(Arr0, Arr0 + (sizeof(Arr0) / sizeof(Arr0[0]))); int Arg1 = 73741817; verify_case(3, Arg1, makeProgram(Arg0)); }

// END CUT HERE

};

// BEGIN CUT HERE
int main() {
  AlgridTwo ___test;
  ___test.run_test(-1);
}
// END CUT HERE
