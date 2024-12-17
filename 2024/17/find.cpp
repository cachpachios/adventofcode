#include <cstdint>
#include <iostream>
#include <vector>

bool exe(std::vector<int> &prog, int64_t A) {
  for (int i = 0; i < prog.size(); i++) {
    int64_t B = (A % 8) ^ 3;
    B = B ^ (A / (1 << B)) ^ 5;
    A = A / 8;
    if (prog[i] != B) {
      return false;
    }
  }
  return true;
}

int main() {
  std::vector<int> prog{2, 4, 1, 3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0};

  for (uint64_t A = 0; A < (uint64_t{1} << 49); A++) {
    if (A % (uint64_t{1} << 28) == 0) {
      std::cout << "Progress: " << A << " ("
                << (double)A / (double)(uint64_t{1} << 48) << ")" << std::endl;
    }
    if (exe(prog, A)) {
      std::cout << "SOLUTION: " << A << std::endl;
      break;
    }
  }
}
