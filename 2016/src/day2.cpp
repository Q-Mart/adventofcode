#include <iostream>
#include <string>
#include <fstream>

int x = 1;
int y = 1;
std::string keycode = "";
const int KEYPAD[3][3] = { {1,2,3},
                           {4,5,6},
                           {7,8,9} };

void processInstruction(char);
std::string processInstructionSet(char*);

void processInstruction(char c) {
  switch (c) {
    case 'U' : --y;
               break;
    case 'D' : ++y;
               break;
    case 'L' : --x;
               break;
    case 'R' : ++x;
               break;
    case '\n' : keycode += std::to_string(KEYPAD[y][x]);
                break;
    default: break;
  }

  int* vars[] = {&x,&y};
  for (auto i : vars) {
    if (*i < 0) {
      *i = 0;
    }

    if (*i > 2) {
      *i = 2;
    }
  }
}

int main() {
  std::ifstream input("inputs/day2.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  char c;
  while (input.get(c)) {
    processInstruction(c);
  }

  input.close();

  std::cout << keycode;
  return 0;
}
