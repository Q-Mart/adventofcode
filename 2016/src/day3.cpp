#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

bool isValid(std::vector<int>&);

bool isValid(std::vector<int>& lengths)
{
  std::sort(lengths.begin(), lengths.end());
  return (lengths[0] + lengths[1]) > lengths[2];
}

int main() {
  int a, b, c, numberValid = 0;

  std::ifstream input("inputs/day3.txt");
  if (!input) {
    std::cerr << "Could not find input file";
    return 1;
  }

  while (input >> a >> b >> c) {
    std::vector<int> triangle = {a,b,c};
    
    if (isValid(triangle)) {
      ++numberValid;
    }
  }

  std::cout << numberValid;

  input.close();
  return 0;
}
