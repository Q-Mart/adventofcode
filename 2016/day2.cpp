#include <iostream>
#include <string>
#include <string>


class keypadTraverser {
  int x;
  int y;
  std::string keycode;
  const static int KEYPAD[3][3];

  keypadTraverser();
  void processInstruction(char);
  std::string processInstructionSet(char*);
};

keypadTraverser::keypadTraverser() {
  x = 1;
  y = 1;
  keycode = "";
  const static int KEYPAD[3][3] = { {1,2,3},
                                    {4,5,6},
                                    {7,8,9} };
}

void keypadTraverser::processInstruction(char c) {
  switch (c) {
    case 'U' : --y;
               break;
    case 'D' : ++y;
               break;
    case 'L' : --x;
               break;
    case 'R' : ++x;
               break;
    case '\n' : keycode += KEYPAD[y][x];
                break;
  }

  int* vars[] = {&x,&y};
  for (auto i : vars) {
    if (i < 0) {
      i = 0;
    }

    if (i > 2) {
      i = 2;
    }
  }
}

std::string keypadTraverser::processInstructionSet(char* c) {
  return "Hello";
}

int main() {
  return 0;
}
