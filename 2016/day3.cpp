#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>

bool isValid(std::vector<int>&);

bool isValid(std::vector<int>& lengths)
{
  std::sort(lengths.begin(), lengths.end());
  return (lengths[0] + lengths[1]) > lengths[2];
}

int main() {
  /* Method: */
  /*   Use a 3x3 matrix as a sliding window. */
  /*   Get 3 lines of values and put in matrix */
  /*   Transpose matrix and then do isValid on every row */

  std::string line;
  int numberValid = 0;

  std::ifstream input("inputs/day3.txt");
  if (!input) {
    std::cerr << "Could not find input file";
    return 1;
  }

  while (!input.eof()) {

    int window[3][3];
    for (int i=0; i<3; ++i)
    {
      std::getline(input, line);
      std::stringstream(line) >> window[i][0] >> window[i][1] >> window[i][2];
    }

    if (line.empty())
    {
      std::cout << "Empty line, exiting...\n";
      break;
    }

    for (int i=0; i<3; ++i) {
      std::vector<int> triangle = {window[0][i], window[1][i], window[2][i]};

      if (isValid(triangle)) {
        ++numberValid;
      }
    
    }

  }

  std::cout << numberValid;

  input.close();
  return 0;
}
