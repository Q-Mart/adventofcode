#include <iostream>
#include <string>
#include <fstream>

int x = 1;
int y = 1;
std::string keycode = "";

const int KEYPAD1[3][3] = { {1,2,3},
                            {4,5,6},
                            {7,8,9} };

const int KEYPAD2[5][5] = { {0,0,1,0,0},
                            {0,2,3,4,0},
                            {5,6,7,8,9},
                            {0,0xA,0xB,0xC,0},
                            {0,0,0xD,0,0} };

void processInstruction(char, int, int**);
std::string toString(int);

std::string toString(int a) {
  if (a < 0xA) {
    return std::to_string(a);
  }

  switch (a) {
    case 0xA : return "A";
    case 0xB : return "B";
    case 0xC : return "C";
    case 0xD : return "D";
  }
  
  return "";
}


void processInstruction(char c, int size) {
  switch (c) {
    case 'U' : --y;
               break;
    case 'D' : ++y;
               break;
    case 'L' : --x;
               break;
    case 'R' : ++x;
               break;
    default: break;
  }

  int* vars[] = {&x,&y};
  for (auto i : vars) {
    if (*i < 0) {
      *i = 0;
    }

    if (*i > size) {
      *i = size;
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
    processInstruction(c, 5);

    if (KEYPAD2[y][x] == 0)
    {
      switch (c) {
        case 'U': ++y;
                  break;
        case 'D': --y;
                  break;
        case 'L': ++x;
                 break;
        case 'R': --x;
                  break;
      }
    }


    if (c == '\n') {
      keycode += toString(KEYPAD2[y][x]);
    }
  }

  input.close();

  std::cout << keycode;
  return 0;
}
